from msilib.schema import File
import requests
import os
from tqdm import tqdm
from utils.filemanager import FileManager



class Download:
    def __init__(self, url, destination=None, headers={}):
        self.url = url
        self.destination = FileManager.get_absolute_path(destination) if destination else os.getcwd()
        self.headers = headers
        self.filename = self.url.split('/')[-1]

    def download(self):
        FileManager.create_destination_directory(self.destination)
        filepath = os.path.join(self.destination, self.filename)
        r = requests.get(self.url, headers=self.headers, stream=True)
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024
        t = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(filepath, 'wb') as f:
            for data in r.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()

    def check_file_downloaded(self):
        return os.path.exists(os.path.join(self.destination, self.filename))



