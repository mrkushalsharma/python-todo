from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

todos = [
    {'id': str(uuid.uuid4()), 'title': 'Buy groceries'},
    {'id': str(uuid.uuid4()), 'title': 'Learn Flask'},
    {'id': str(uuid.uuid4()), 'title': 'Deploy app using Docker'}
]

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)