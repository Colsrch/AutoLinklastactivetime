import requests
import sys
import random
import re
import datetime
from bs4 import BeautifulSoup

header = [
    {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 '
                   '(KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}
]

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    urls = ['https://colsrch.top/']
file_name = 'friends.txt'
with open(file_name, 'w') as file_obj:
    for i in range(0, len(urls)):
        link = urls[i] + '/atom.xml'
        session = requests.session()
        html = session.get(link)
        content = BeautifulSoup(html.content, 'html.parser')
        time = BeautifulSoup(str(content), 'html.parser').find('updated')
        time = str(time)
        time = time.replace('<updated>', '')
        time = time.replace('</updated>', '')
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
        utcTime = datetime.datetime.strptime(time, UTC_FORMAT)
        localtime = utcTime + datetime.timedelta(hours=8)
        localtime = str(localtime)
        print(item + '：' + localtime)
        file_obj.write(item + '：' + localtime + '\n')
