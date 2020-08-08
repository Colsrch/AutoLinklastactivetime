import requests
import random
import re
import datetime
from bs4 import BeautifulSoup
from urllib import error, request

header = [
    {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 '
                   '(KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}
]
f = open('link.txt', 'r')
# 读取友链链接
links = str(f.read())
links = links.replace('\n', '')
links = links.replace('\r', '')
print(links)
f.close()
if (len(links) >= 2):
    urls = links.split(',')
else:
    urls = ['https://colsrch.top']
file_name = 'time.txt'
utime = '+'
none = 'None'
with open(file_name, 'w') as file_obj:
    for i in range(0, len(urls)):
        link = urls[i] + '/atom.xml'
        try:
            response = request.urlopen(link)
            session = requests.session()
            html = session.get(link)
            content = BeautifulSoup(html.content, 'html.parser')
            time = BeautifulSoup(str(content), 'html.parser').find('updated')
            time = str(time)
            time = time.replace('<updated>', '')
            time = time.replace('</updated>', '')
            if utime in time:
                print(urls[i] + "不支持的时间格式（直接截取）")
                time = time.replace('-', '')
                time = time[0:4] + '年' + time[4:6] + '月' + time[6:8] + '日'
                print(urls[i] + '：' + time)
                file_obj.write(urls[i] + ': ' + time + '\n')
            elif none in time:
                # 如果网站返回错误，则写入url，code,错误原因
                print(urls[i] + ': 活跃时间未知')
                file_obj.write(urls[i] + ': 活跃时间未知' + '\n')
            else:
                UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
                utcTime = datetime.datetime.strptime(time, UTC_FORMAT)
                localtime = utcTime + datetime.timedelta(hours=8)
                time = str(localtime)
                time = time.replace('-', '')
                time = time[0:4] + '年' + time[4:6] + '月' + time[6:8] + '日'
                print(urls[i] + '：' + time)
                file_obj.write(urls[i] + ': ' + time + '\n')
        except error.URLError as e:
            try:
                # 如果网站返回错误，则写入url，code,错误原因
                print(urls[i] + ': 活跃时间未知')
                file_obj.write(urls[i] + ': 活跃时间未知' + '\n')
            except:
                # 如果服务器不存在则写入url,错误原因
                print(urls[i] + '：服务器不存在')
                file_obj.write(urls[i] + ': NOSERVER' + '\n')
    file_obj.close()
