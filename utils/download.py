import requests
import os
import threading
import time
from queue import Queue
from tqdm import tqdm



class Download:
    def __init__(self, url, destination=None, headers={}):
        self.url = url
        self.destination = destination
        self.headers = headers

    def download(self):
        filename = self.url.split('/')[-1]
        if self.destination is None:
            self.destination = os.getcwd()
        filepath = os.path.join(self.destination, filename)
        self.create_destination_directory()
        r = requests.get(self.url, headers=self.headers, stream=True)
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024
        t = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(filepath, 'wb') as f:
            for data in r.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()

    def get_absolute_path(self, path):
        return os.path.join(os.getcwd(), path)

    def create_destination_directory(self):
        if not os.path.exists(self.destination):
            os.makedirs(self.destination)



