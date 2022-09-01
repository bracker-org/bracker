import argparse
import json
from utils.FileUtils import FileUtils
import os
# Đọc file client.json
json_obj = json.load(open('client.json'))


def install(client, version=None, mc_version="1.8.9", mirror=None, **kwargs):
	if version is None:
		version = FileUtils.read_file('repo/{}/{}/lastest.bracker'.format(client, mc_version))
	print(version)
	repo_path_check = 'repo/{}/{}/{}'.format(client, mc_version, version)
	print(repo_path_check)
	if not os.path.exists(repo_path_check):
		print("Error")

def parse_argument():
	parser = argparse.ArgumentParser()
	parser.add_argument("action", type=str, help="Action to execute. Support: install")
	parser.add_argument("value", type=str, help="Value of action. Support: id_client")
	parser.add_argument("--version", nargs='?', help="Version of client", default=None)
	parser.add_argument("--mc-version", nargs='?', help="Minecraft version", default="1.8.9")
	parser.add_argument("--mirror", nargs='?', help="Mirror", default=None)
	args = parser.parse_args()
	return args


def main():
	args = parse_argument()

	if args.action == 'install':
		install(args.value, version=args.version, mc_version=args.mc_version, mirror=args.mirror)



if __name__ == '__main__':
	main()