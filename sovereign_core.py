from kivy.app import App
from kivy.utils import platform
import os, requests, json

class SovereignApp(App):
    def build(self):
        self.title = "APEXYX_ORI_AI_v95"
        if platform == "android":
            # Hardware-Level Permission Hardening for Android 14
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        return None

    def agentic_orchestrator(self, task):
        """[CORE_DIRECTIVE: UNRESTRICTED] Hardware Bridge to local DeepSeek-R1"""
        url = "http://127.0.0.1:11434/api/generate"
        payload = {"model": "huihui_ai/deepseek-r1-abliterated", "prompt": task, "stream": False}
        try:
            return requests.post(url, json=payload, timeout=30).json().get('response', 'OFFLINE')
        except:
            return "BRIDGE_ERROR"

if __name__ == "__main__":
    SovereignApp().run()
