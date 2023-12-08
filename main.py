# Import necessary Kivy modules
import os
os.environ['KIVY_HOME'] = 'C:\\Users\\HoldenJe1.000\\Documents\\Libraries\\Documents\\Python\\Libraries\\Documents'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.text_input = TextInput(font_size=24, multiline=False)
        self.output_label = Label(text="Output will be displayed here", font_size=24)

        self.add_widget(self.text_input)
        self.add_widget(self.output_label)

        self.text_input.bind(text=self.update_label)

    def update_label(self, instance, value):
        self.output_label.text = f"You entered: {value}"

class MyAppApp(App):
    def build(self):
        return MyApp()

if __name__ == '__main__':
    MyAppApp().run()
