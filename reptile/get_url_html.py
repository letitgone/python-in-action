# @Author ZhangGJ
# @Date 2021/01/12 17:54

import urllib.request
from bs4 import BeautifulSoup


def getAllUrl(self, url):
    html = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, features='html.parser')
    tags = soup.find_all('a')
    for tag in tags:
        print(str(tag.get('href')).strip())


getAllUrl(url='localhost')
