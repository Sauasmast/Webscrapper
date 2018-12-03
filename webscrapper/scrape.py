import requests


class scrape():

    def __init__(self, url):
        self.url = url

    def initiatescrape(self):
        try:
            return requests.get(self.url)
        except:
            return ("Please make sure that the url is correct")
