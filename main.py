from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
import json

class ApexyxCockpit(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=5)
        
        # Header: Corrected to REECH
        self.status_bar = Button(text="[ SEARCHING FOR REECH... ]", size_hint_y=0.1, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.status_bar)

        self.scroll = ScrollView(size_hint_y=0.7)
        self.terminal_log = Label(
            text=">> REECH SOVEREIGN LINK INITIALIZED\n>> Awaiting Command...",
            size_hint_y=None, halign='left', valign='top', font_size='14sp'
        )
        self.terminal_log.bind(texture_size=self.terminal_log.setter('size'))
        self.scroll.add_widget(self.terminal_log)
        self.root.add_widget(self.scroll)

        self.cmd_input = TextInput(
            hint_text="Direct Terminal Input...", multiline=False,
            size_hint_y=0.1, background_color=(0.1, 0.1, 0.1, 1), foreground_color=(0, 1, 0, 1)
        )
        self.cmd_input.bind(on_text_validate=self.send_cmd)
        self.root.add_widget(self.cmd_input)

        self.update_status()
        return self.root

    def send_cmd(self, instance):
        cmd = self.cmd_input.text
        self.terminal_log.text += f"\n\n[USER]: {cmd}"
        UrlRequest(
            "http://10.0.0.203:58080/command",
            req_body=json.dumps({"command": cmd}),
            on_success=self.on_success,
            on_error=self.on_error,
            method='POST'
        )
        self.cmd_input.text = ""

    def on_success(self, req, res):
        out = res.get('stdout') or res.get('stderr')
        self.terminal_log.text += f"\n[REECH]:\n{out}"
        self.scroll.scroll_y = 0

    def on_error(self, req, err):
        self.terminal_log.text += f"\n[!] LINK SEVERED: {err}"

    def update_status(self, *args):
        UrlRequest("http://10.0.0.203:58080/", on_success=self.set_online)

    def set_online(self, req, res):
        self.status_bar.text = "● REECH ONLINE | PIXEL 8 PRO LINK ACTIVE"
        self.status_bar.background_color = (0, 0.5, 0, 1)

if __name__ == "__main__":
    ApexyxCockpit().run()
