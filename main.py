import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
kivy.require('1.9.1')


class MyWindowApp(App):
        def __init__(self):
            super(MyWindowApp,self).__init__()
            for i in range(5):
                self.btn = Label(text="Read Me!")
                self.lbl = Label(text="Read Me!")

                self.layout = BoxLayout()
                self.layout.orientation = 'vertical'
                self.layout.add_widget(self.lbl)
                self.layout.add_widget(self.btn)



window = MyWindowApp()
window.run()