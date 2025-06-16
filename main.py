from kivy.app import App
from kivy.uix.button import Button

class FinanceApp(App):
    def build(self):
        return Button(text="Финансовое приложение", font_size=30)

if __name__ == "__main__":
    FinanceApp().run()