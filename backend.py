# Python backend for to-do list Application
from flask import Flask, jsonify, request
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing if needed
tasks = []  # Stores data in a simple list

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200  # Return the list of tasks with status code 200

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if 'task' not in data:
        return jsonify({"error": "Task description is missing"}), 400  # Handle missing task description
    tasks.append({"task": data['task'], "time": time.ctime()})
    return jsonify({"message": "Task added successfully"}), 201  # Return success message with status code 201

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode