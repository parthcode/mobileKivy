from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import ButtonBehavior
from kivy.uix.image import AsyncImage


class ImageButton(ButtonBehavior, AsyncImage):
    pass


class MyGrid(GridLayout):
    def __init__(self,foo,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 2
        for i in range(len(foo)):
            self.image =foo['Image_url1']
            self.add_widget(ImageButton(source=self.image))
            self.text=foo['text1']
            self.add_widget(Label(text=self.text))


class MainApp(App):
    def build(self):
        foo = {'Image_url1': 'https://picsum.photos/200/300',
               'text1': 'some random text of few words',
               'Image_url2': 'https://picsum.photos/200/300',
               'text2': 'some random text of few words'
               }
        return MyGrid(foo)

if __name__ == '__main__':
    app = MainApp()
    app.run()