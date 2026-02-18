from kivy.app import App
from kivy.uix.browser import WebView # Ensure this is mapped to the native provider
from kivy.core.window import Window

class ReechVessel(App):
    def build(self):
        # Direct link to your active Termux Brain
        # This gives you full terminal control immediately upon opening
        return WebView(url="http://10.0.0.203:58081/")

if __name__ == '__main__':
    ReechVessel().run()
