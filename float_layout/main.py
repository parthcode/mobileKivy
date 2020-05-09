# Sample Python application demonstrating the
# working of FloatLayout in Kivy

import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# module consist the floatlayout
# to work with FloatLayout first
# you have to import it
from kivy.uix.floatlayout import FloatLayout

# To change the kivy default settings
# we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)


# creating the App class
class MyApp(App):
    def build(self):
        Fl = FloatLayout()

        btn = Button(text='Hello world',
                     size_hint=(.3, .2),
                     pos=(200, 300))

        # adding widget i.e button
        Fl.add_widget(btn)

        return Fl


if __name__ == "__main__":
    MyApp().run()