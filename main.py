# Forge-ID: 16KB-SYNC-v1.0.1
from kivy.app import App
from kivy.uix.button import Button

class ApexyxApp(App):
    def build(self):
        return Button(
            text="Apexyx Core: Online\n[Version 1.0.1]",
            font_size='20sp',
            background_color=(0, 0.7, 0.9, 1)
        )

if __name__ == "__main__":
    ApexyxApp().run()
