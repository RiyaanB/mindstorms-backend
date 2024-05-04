from flask import Flask, request, jsonify, render_template
from engine.hive import Hive
from engine.task import Task

app = Flask(__name__)
hive = Hive()

@app.route('/register', methods=['POST'])
def register():
    user_data = request.json
    hive_mind.register_user(user_data)
    return jsonify({"status": "success", "message": "User registered successfully"})

@app.route('/task_completed', methods=['POST'])
def task_completed():
    task_data = request.json
    task = Task.get_task_by_id(task_data.id)
    task.set_result(task_data.result)
    hive.notify_completion(task)
    return jsonify({"status": "success", "message": "Task processed successfully"})

@app.route('/task_completed', methods=['GET'])
def request_task():
    task_data = request.json
    return jsonify({"status": "success", "message": "Task processed successfully"})

@app.route('/status')
def status():
    data = hive_mind.get_system_status()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)