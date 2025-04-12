from flask import Flask, jsonify
from flask_cors import CORS

import mysql.connector
import time
import uuid

app = Flask(__name__)
CORS(app) 
config = {
    'user': 'root',
    'password': 'mypassword',
    'host': 'mariadb',
    'database': 'todo_db'
}

def wait_for_db():
    while True:
        try:
            conn = mysql.connector.connect(
                user=config['user'],
                password=config['password'],
                host=config['host']
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS todo_db")
            conn.commit()
            cursor.close()
            conn.close()
            break
        except mysql.connector.Error:
            time.sleep(2)

def initialize_database():
    wait_for_db()
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id VARCHAR(36) PRIMARY KEY,
            title VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM todos")
    count = cursor.fetchone()[0]

    if count == 0:
        todos = [
            (str(uuid.uuid4()), "Buy groceries"),
            (str(uuid.uuid4()), "Learn Flask with Docker and K8s")
        ]
        cursor.executemany("INSERT INTO todos (id, title) VALUES (%s, %s)", todos)
        conn.commit()
    cursor.close()
    conn.close()

@app.route('/api/todos', methods=['GET'])
def get_todos():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(todos)

if __name__ == '__main__':
    initialize_database()
    app.run(host='0.0.0.0', port=5000)
