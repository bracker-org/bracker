import argparse
import json

# Đọc file client.json
json_obj = json.load(open('client.json'))


def install(client, version=None, mc_version=None):
	if mc_version is None:
		mc_version = '1.8.9'
	version_object = {}

	for item in json_obj:
		if item['id'] == client:
			for j in item['mc_versions']:
				if j['name'] == mc_version:
					if version == None:
						version_object = j['client_versions'][0]
					else:
						for k in j['client_versions']:
							if k['name'] == version:
								version_object = k
								break
					break
			break
	print(version_object)

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
	args = parser.parse_args()
	return args


def main():
	# Parse args
	args = parse_argument()

	if args.action == 'install':
		# Thực hiện lệnh install
		install(args.client, version=args.version, mc_version=args.mc_version)



if __name__ == '__main__':
	main()