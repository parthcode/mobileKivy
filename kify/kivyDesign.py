from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button

from kify.newsdata import NewsData

class ImageButton(ButtonBehavior, AsyncImage):
    pass


# class MyGrid(GridLayout):
#     def __init__(self,news_data,**kwargs):
#         super(MyGrid,self).__init__(**kwargs)
#         self.cols = 2
#         for i in range(5):
#             image_key = 'image_url_'+str(i)
#             self.image =news_data[image_key]
#             self.add_widget(ImageButton(source=self.image))
#             title_key = 'title_'+str(i)
#             self.text=news_data[title_key]
#             self.add_widget(Label(text=self.text))

class MainApp(App):
    def __get_news(self):
        data = NewsData()
        news_data = data.get_news_data()
        return news_data

    def build(self):
        #return MyGrid(self.__get_news())
        VB = BoxLayout(orientation='vertical')
        data = self.__get_news()
        for i in range(11):
            title_key = 'title_' + str(i)
            btn3 = Button(text=data[title_key])
            VB.add_widget(btn3)

        return VB


if __name__ == '__main__':
    app = MainApp()
    app.run()