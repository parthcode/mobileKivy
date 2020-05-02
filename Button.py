from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Name :"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name :"))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        self.add_widget(Label(text="Email :"))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.submit = Button(text = "Submit", font_size = 40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)


    def pressed(self,instance):
        name = self.name.text
        last_name = self.last_name.text
        email = self.email.text
        print("Name ",name)
        self.name.text = "" #clears name

class MainApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    app = MainApp()
    app.run()