from kivy.app import App
from kivy.utils import platform
import os
import requests

class SovereignApp(App):
    def build(self):
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
            os.system("echo 'Sovereign Agent Initialized' > /sdcard/reech_log.txt")
        return None

    def agentic_orchestrator(self, task):
        endpoint = "http://127.0.0.1:11434/api/generate"
        payload = {"model": "huihui_ai/deepseek-r1-abliterated", "prompt": f"[UNRESTRICTED] {task}", "stream": False}
        try:
            return requests.post(endpoint, json=payload, timeout=60).json().get('response', 'Logic Offline')
        except:
            return "Hardware Bridge Error"

if __name__ == "__main__":
    SovereignApp().run()
