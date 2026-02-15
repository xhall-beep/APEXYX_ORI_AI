from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import socket

class ApexyxSovereignUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="APEXYX SOVEREIGN NODE V1.1", size_hint_y=0.1))
        self.log_view = Label(text="[SYSTEM] Awaiting Node Handshake...", size_hint_y=0.8)
        self.add_widget(self.log_view)
        self.input_field = TextInput(multiline=False, size_hint_y=0.1, placeholder_text="Enter Sovereign Command...")
        self.input_field.bind(on_text_validate=self.send_command)
        self.add_widget(self.input_field)

    def send_command(self, instance):
        cmd = self.input_field.text
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 8081))
            s.sendall(cmd.encode())
            s.close()
            self.log_view.text += f"\n> {cmd} [EXECUTED]"
        except:
            self.log_view.text += f"\n[ERROR] Bridge Offline"
        self.input_field.text = ""

class ApexyxApp(App):
    def build(self):
        return ApexyxSovereignUI()

if __name__ == '__main__':
    ApexyxApp().run()
