import argparse
import json
from utils.download import Download
from getlink.mediafire import Mediafire
# Đọc file client.json
json_obj = json.load(open('client.json'))


def install(client, version=None, mc_version=None, mirror=None):
	if mc_version is None:
		mc_version = '1.8.9'
	client_object = {}
	mc_version_object = {}
	version_object = {}
	mirror = ''
	link = ''

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
		Mediafire(link).download()
	else:
		Download(link).download()

def parse_argument():
	'''
		Trích xuất các tham số trong CLI
		Ex: python main.py install fdpclient --version 4.4.5
	'''

	parser = argparse.ArgumentParser()
	parser.add_argument("action", type=str)
	parser.add_argument("client", type=str)
	parser.add_argument("--version", nargs='?', help="Version of client", default=None)
	parser.add_argument("--mc-version", nargs='?', help="Minecraft version", default=None)
	parser.add_argument("--mirror", nargs='?', help="Mirror", default=None)
	args = parser.parse_args()
	return args


def main():
	# Parse args
	args = parse_argument()

	if args.action == 'install':
		# Thực hiện lệnh install
		install(args.client, version=args.version, mc_version=args.mc_version, mirror=args.mirror)



if __name__ == '__main__':
	main()