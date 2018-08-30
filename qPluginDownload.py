import requests
from lxml import etree
import os

url = 'https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins'
req = requests.get(url).text

html = etree.HTML(req)
links = html.xpath('//tr/td[5]/a/@href')

for link in links:
    if link[-3:] == '.py':
        with open(os.path.join('plugins', os.path.basename(link)), 'wb') as f:
            req = requests.get(link, stream=True)
            f.write(req.content)