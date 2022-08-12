import requests
from bs4 import BeautifulSoup
from utils.download import Download

class Mediafire:
    def __init__(self, url, headers={}, destination=None):
        self.url = url
        self.headers = headers
        self.destination = destination

    def download(self):
        resp = requests.get(self.url, headers=self.headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            link = soup.find('a', {'aria-label': 'Download file', 'id': 'downloadButton'})['href']
            Download(link, self.destination, self.headers).download()