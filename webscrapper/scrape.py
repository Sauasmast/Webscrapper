import requests
import time


class scrape():

    def __init__(self, url):
        self.url = url

    def initiatescrape(self):
        # Wait for  5 seconds before scraping the website
        time.sleep(1)
        try:
            return requests.get(self.url).text
        except:
            return ("Please make sure that the url is correct")
