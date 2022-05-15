import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

kivy.require('2.1.0')
class EpicApp(App):
    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    EpicApp().run()