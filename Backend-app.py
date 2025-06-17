from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Simple in-memory task list
tasks = []

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        "id": str(uuid.uuid4()),
        "title": data.get("title", ""),
        "status": "pending"
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["status"] = data.get("status", task["status"])
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)
