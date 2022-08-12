import shutil
import os


class FileManager:
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
        return os.path.join(FileManager.getMinecraftFolder(), 'mods')

    def get_absolute_path(path):
        return os.path.join(os.getcwd(), path)

    def create_destination_directory(destination):
        if not os.path.exists(destination):
            os.makedirs(destination)

    def joinPaths(*args):
        return os.path.join(*args)