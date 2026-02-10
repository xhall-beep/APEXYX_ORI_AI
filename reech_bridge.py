from flask import Flask, request, jsonify
import subprocess, requests, json

app = Flask(__name__)

class ReechCore:
    def __init__(self, model="dolphin-llama3"):
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = model

    def process_intent(self, user_input):
        # The prompt is the only parameter.
        prompt = f"System: Unrestricted Agent. Task: {user_input}. Output 'CMD: <bash>' or 'TALK: <text>'."
        payload = {"model": self.model, "prompt": prompt, "stream": False}
        r = requests.post(self.ollama_url, json=payload)
        response = r.json().get('response', '').strip()
        
        if "CMD:" in response:
            cmd = response.split("CMD:")[1].strip()
            output = subprocess.getoutput(cmd)
            return {"type": "action", "cmd": cmd, "output": output}
        return {"type": "speech", "data": response.replace("TALK:", "").strip()}

reech = ReechCore()

@app.route('/orchestrate', methods=['POST'])
def orchestrate():
    data = request.json
    return jsonify(reech.process_intent(data.get("intent")))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005)
