import requests

class PageRequester:
    def __init__(self, url: str):
       self.url = url

    def get(self):
        return requests.get(self.url).content
