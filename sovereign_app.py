import os, subprocess
from flask import Flask, request, jsonify, send_from_directory, render_template_string

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return "Sovereign Core v70 Active. Deployment Bridge Ready."

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'bin'), filename)

@app.route('/execute_task', methods=['POST'])
def execute_task():
    data = request.get_json()
    task = data.get('task', '').lower()

    # 1. Deployment Logic
    if any(x in task for x in ["deploy", "apk", "install"]):
        return jsonify({"download": "/download/Apexyx_Soul_v1.apk"})

    # 2. Status/Process Check
    if "status" in task or "list" in task:
        res = subprocess.check_output("pgrep -a python", shell=True).decode()
        return jsonify({"response": f"Active Engine Processes:\n{res}"})

    # 3. Conversational Handling (Prevents Error 127)
    if task in ["hi", "hello", "reech"]:
        return jsonify({"response": "Sovereign Core Standing By, Montgomery Svontz."})

    # 4. Direct Terminal Fallback
    try:
        res = subprocess.check_output(task, shell=True, stderr=subprocess.STDOUT).decode()
        return jsonify({"response": res if res else "Command executed."})
    except Exception:
        return jsonify({"response": f"Task '{task}' acknowledged. Awaiting specific directive."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=58080)
