from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text="Hello World", font_size=50)

if __name__ == "__main__":
    TestApp().run()