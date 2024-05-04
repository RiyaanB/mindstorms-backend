from flask import Flask, request, jsonify, render_template
from engine.hive import Hive

app = Flask(__name__)
hive = Hive("We are building the next Google")

@app.route('/register', methods=['POST'])
def register():
    user_data = request.json
    hive.register_user(user_data)
    return jsonify({"status": "success", "message": "User registered successfully"})

@app.route('/task_completed', methods=['POST'])
def task_completed():
    task = request.json
    hive.update_gc_with_task_result(task)
    return jsonify({"status": "success", "message": "Task processed successfully"})

@app.route('/request_task', methods=['GET'])
def request_task():
    task = hive.get_unassigned_task()
    if task is None:
        return jsonify({})
    return jsonify(task)

@app.route('/status')
def status():
    data = hive.get_system_status()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
