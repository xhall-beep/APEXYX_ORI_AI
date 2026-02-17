from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ApexyxCore(App):
    def build(self):
        # This layout is your canvas for future upgrades
        self.root = BoxLayout()
        self.label = Label(text="Apexyx Sovereign Core v1.0\nStatus: Online & Upgradable")
        self.root.add_widget(self.label)
        return self.root

if __name__ == "__main__":
    ApexyxCore().run()
