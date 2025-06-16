from kivy.app import App
from kivy.uix.label import Label

class FinanceApp(App):
    def build(self):
        return Label(text="Приложение для учета финансов")

if __name__ == "__main__":
    FinanceApp().run()

