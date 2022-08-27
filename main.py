import argparse
import json
from utils.download import Download
from getlink.mediafire import Mediafire
from utils.filemanager import FileManager
import os
# Đọc file client.json
json_obj = json.load(open('client.json'))


def install(client, version=None, mc_version=None, mirror=None, **kwargs):
	global client_object, mc_version_object, version_object
	global link, downloader
	download_destination = 'files_downloaded'


	for key, value in kwargs.items():
		if key == 'download_destination':
			download_destination = value


	if mc_version is None:
		mc_version = '1.8.9'
	

	for item in json_obj:
		if item['id'] == client:
			client_object = item
			break

	if client_object == {}:
		print('[Error] Client not found')
		return

	for item in client_object['mc_versions']:
		if item['mc_version'] == mc_version:
			mc_version_object = item
			break
	
	if mc_version_object == {}:
		print('[Error] Minecraft version of client not found')
		return

	if version is None:
		version_object = mc_version_object['client_versions'][-1]
	else:
		for item in mc_version_object['client_versions']:
			if item['version'] == version:
				version_object = item
				break

	if version_object == {}:
		print('[Error] Version of client not found')
		return

	if mirror is None:
		link = version_object['mirrors'][-1]['link']
		mirror = version_object['mirrors'][-1]['mirror']
	else:
		for item in version_object['mirrors']:
			if item['mirror'] == mirror:
				link = item['link']
				mirror = item['mirror']
				break
	
	if link == '':
		print('[Error] Mirror of client not found. Using default mirror')
		link = version_object['mirrors'][-1]['link']
		mirror = version_object['mirrors'][-1]['mirror']

	if mirror == 'mediafire':
		downloader = Mediafire(link, destination=download_destination)
	else:
		downloader = Download(link, destination=download_destination)

	# Check file downloaded
	if not downloader.check_file_downloaded():
		downloader.download()
		print('[Info] Download complete')
	else: 
		print('[Info] File already downloaded')
	

	# Copy file to minecraft folder
	download_file_des = FileManager.get_absolute_path(os.path.join(download_destination, downloader.filename))
	FileManager.copy(download_file_des, FileManager.getMinecraftModsFolder())

	print('[Info] Install complete')

def parse_argument():
	parser = argparse.ArgumentParser()
	parser.add_argument("action", type=str, help="Action to execute. Support: install")
	parser.add_argument("value", type=str, help="Value of action. Support: id_client")
	parser.add_argument("--version", nargs='?', help="Version of client", default=None)
	parser.add_argument("--mc-version", nargs='?', help="Minecraft version", default=None)
	parser.add_argument("--mirror", nargs='?', help="Mirror", default=None)
	args = parser.parse_args()
	return args


def main():
	args = parse_argument()

	if args.action == 'install':
		install(args.value, version=args.version, mc_version=args.mc_version, mirror=args.mirror)



if __name__ == '__main__':
	main()