from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)


class ImageButton(ButtonBehavior, AsyncImage):
    pass


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.cols = 1
        icon = 'https://cdn2.iconfinder.com/data/icons/flat-ui-icons-24-px/24/eye-24-256.png'
        self.add_widget(ImageButton(source=icon))


class Test(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    Test().run()