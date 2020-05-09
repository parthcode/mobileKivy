import requests
from constant import NEWSURL


class NewsData:
    def __init__(self):
        self.news_url = NEWSURL

    def get_news_data(self):
        meta_data = requests.get(self.news_url)
        data = meta_data.json()
        meta_data.close()
        return data
