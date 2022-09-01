import requests
import os
import re
from urllib.parse import urlparse
from utils.FileUtils import FileUtils
from config import Config


class Downloader:
    def __init__(self, url, destination=None, headers={}, filename=None):
        self.url = url
        self.destination = os.getcwd() if destination is None else FileUtils.getAbsolutePath(destination)
        self.headers = headers
        self.filename = filename
        self.filepath = None

    def download(self):
        resp = requests.get(self.url, headers=self.headers, stream=True)
        filename = self.parse_filename(resp) if self.filename is None else self.filename

        FileUtils.createDestination(self.destination)
        self.filepath = FileUtils.getAbsolutePath(self.destination, filename)

        with open(self.filepath, 'wb') as fp:
            for data in resp.iter_content(Config.DOWNLOAD_BLOCK_SIZE):
                fp.write(data)

    def check_hash(self, md5_hash, sha1_hash):
        if not FileUtils(self.filepath, md5_hash, sha1_hash):
            print("Error: File not match")

    def parse_filename(self, resp: requests.Response):
        headers = resp.headers
        if 'content-disposition' in headers.keys():
            return re.findall(r"filename=(.+)", headers['content-disposition'])[0]
        return os.path.basename(urlparse(self.url).path)


if __name__ == '__main__':
    url = 'https://download1532.mediafire.com/kjbvri1fqdjg/owqa5bc551w0qyy/hud.json'
    Downloader(url).test()
