# Python backend for to-do list Application
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from email_service import send_email
import time



app = Flask(__name__, template_folder='dist', static_url_path="/")  # Create a Flask app
tasks = []  # Stores data in a simple list

# CORS(app)  # Enable Cross-Origin Resource Sharing if neededCORS(app)  # Enable Cross-Origin Resource Sharing if needed

@app.route('/', methods=['GET'])
def home():
    print(app.static_folder, "index.html")
    # return index.html
    return send_from_directory(app.static_folder, "index.html")

# Handle React Router Paths
@app.route("/<path:path>")
def serve_static_files(path):
    try:
        print(path)
        return send_from_directory(app.static_folder, path)
    except:
        return send_from_directory(app.static_folder, "index.html")  # Serve React for unknown pathsç

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200  # Return the list of tasks with status code 200

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if 'task' not in data:
        return jsonify({"error": "Task description is missing"}), 400  # Handle missing task description
    tasks.append({"task": data['task'], "time": time.ctime()})
    send_email()
    return jsonify({"message": "Task added successfully"}), 201  # Return success message with status code 201

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode