from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Funksjon for å koble til databasen
def get_db_connection():
    return mysql.connector.connect(
        user="adriatik",
        password="Adriatik.123",
        database="restaurant",
        host="10.2.4.76",
        port=3306
    )

@app.route('/')
def index():
    return render_template('index.html')  # Skjemaet som skal vises i nettleseren

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']  # Bruker 'username' i stedet for 'name'
        password = request.form['password']  # Bruker 'password' i stedet for 'email'
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Sett inn data i users-tabellen
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return redirect(url_for('index'))  # Etter innsending, vis skjemaet igjen

if __name__ == '__main__':
    app.run(debug=True)
