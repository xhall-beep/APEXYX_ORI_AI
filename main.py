from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.codeinput import CodeInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock

class ApexyxSovereignUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="APEXYX SOVEREIGN NODE V1", size_hint_y=0.1, color=(0, 1, 0, 1)))
        
        self.log_view = CodeInput(text="[SYSTEM] Awaiting Handshake...\n", readonly=True, size_hint_y=0.7)
        self.scroll = ScrollView(size_hint_y=0.7)
        self.scroll.add_widget(self.log_view)
        self.add_widget(self.scroll)
        
        self.input_field = TextInput(text="", placeholder_text="Enter Command to Sub-Agents...", multiline=False, size_hint_y=0.1)
        self.input_field.bind(on_text_validate=self.send_command)
        self.add_widget(self.input_field)

    def send_command(self, instance):
        cmd = self.input_field.text
        self.log_view.text += f"\n> {cmd}\n[RECON] Executing Sovereign Logic..."
        self.input_field.text = ""

class ApexyxApp(App):
    def build(self):
        return ApexyxSovereignUI()

if __name__ == '__main__':
    ApexyxApp().run()
