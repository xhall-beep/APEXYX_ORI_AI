from kivy.app import App
from kivy.uix.button import Button

class ApexyxShell(App):
    def build(self):
        return Button(
            text="ApexyxShell v0.1\n[Awaiting Evolution]",
            font_size='22sp',
            background_color=(0, 0.5, 0.8, 1)
        )

if __name__ == "__main__":
    ApexyxShell().run()
