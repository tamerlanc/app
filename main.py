from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class FinanceApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Финансовое приложение", font_size=30))
        layout.add_widget(Button(text="Начать работу", size_hint=(1, 0.5)))
        return layout

if __name__ == "__main__":
    FinanceApp().run()