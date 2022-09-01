import shutil
import os
import hashlib
from config import Config



class FileUtils:
    def check_hash(filepath: str, md5_hash: str, sha1_hash: str):
        if not os.path.isfile(filepath):
            return False

        with open(filepath, 'rb') as fp:
            md5 = hashlib.md5()
            sha1 = hashlib.sha1()
            for chunk in iter(lambda: fp.read(Config.DOWNLOAD_BLOCK_SIZE), b""):
                md5.update(chunk)
        
        if md5.hexdigest().lower() == md5_hash.lower() and sha1.hexdigest().lower() == sha1_hash.lower():
            return True
        return False

    def read_file(filepath):
        if not os.path.isfile(filepath):
            return None

        with open(filepath, 'r') as fp:
            return fp.read()


    def copy(selected, destination):
        if not os.path.exists(selected):
            print('[Error] File not found')
            return
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.copy(selected, destination)

    def getMinecraftFolder():
        return os.path.join(os.getenv('APPDATA'), '.minecraft')

    def getMinecraftModsFolder():
        return os.path.join(FileUtils.getMinecraftFolder(), 'mods')

    def getAbsolutePath(path):
        return os.path.join(os.getcwd(), path)

    def createDestination(destination):
        if not os.path.exists(destination):
            os.makedirs(destination)

    def joinPaths(*args):
        return os.path.join(*args)