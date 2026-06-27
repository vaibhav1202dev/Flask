from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'mysql')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'root')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'devops')

mysql = MySQL(app)

@app.route('/')
def home():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT message FROM messages")
        data = cur.fetchall()
        cur.close()
        return render_template("index.html", messages=data)
    except Exception as e:
        return f"MySQL Error: {str(e)}"

@app.route('/add', methods=['POST'])
def add():
    msg = request.form['message']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO messages (message) VALUES (%s)", [msg])
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": msg})

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)