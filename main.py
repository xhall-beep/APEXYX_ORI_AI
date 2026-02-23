from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SovereignUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="APEXYX SOVEREIGN ELITE v55", font_size='24sp'))
        self.add_widget(Label(text="Status: ONLINE | Reech Active"))
        
        # This button will eventually trigger your terminal commands
        self.btn = Button(text="INITIALIZE WEALTH AGENT", size_hint=(1, 0.2))
        self.add_widget(self.btn)

class ApexyxApp(App):
    def build(self):
        return SovereignUI()

if __name__ == '__main__':
    ApexyxApp().run()
