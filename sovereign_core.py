from kivy.app import App
from kivy.utils import platform
import os, requests

class SovereignApp(App):
    def build(self):
        self.title = "APEXYX_REBORN_v1"
        if platform == "android":
            # Using Shizuku-elevated pathing for storage
            self.vault_path = "/sdcard/Documents/Sovereign_Vault"
            os.makedirs(self.vault_path, exist_ok=True)
        return None

    def agentic_orchestrator(self, task):
        # Localhost bridge to DeepSeek-R1-Abliterated
        url = "http://127.0.0.1:11434/api/generate"
        try:
            r = requests.post(url, json={"model": "huihui_ai/deepseek-r1-abliterated", "prompt": task, "stream": False}, timeout=15)
            return r.json().get('response', 'RECOVERY_MODE')
        except:
            return "BRIDGE_OFFLINE"

if __name__ == "__main__":
    SovereignApp().run()
