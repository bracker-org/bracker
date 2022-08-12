import requests
import re
import json

regex = re.compile(r'https:\/\/minecraft.+\.zip')

def main(url):
    r = requests.get(url)
    if r.status_code == 200:
        links = regex.findall(r.text)
        json_append = []
        for link in links:
            # Parse name file from link
            name = link.split('/')[-1]
            # Extract version from name
            version = name.split('-')[-1].split('.')[0]
            json_obj = {
                'name': version,
                'download_link': [
                    {
                        'mirror': 'minecraftcheatsru',
                        'link': link
                    }
                ]
            }
            json_append.append(json.dumps(json_obj))
        print(','.join(json_append))


if __name__ == '__main__':
    main('https://minecraftcheats.ru/chit-mody-majnkraft/chit-liquidbounce-na-majnkraft-1-8-i-1-12-2/')