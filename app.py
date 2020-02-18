from bs4 import BeautifulSoup
import requests
import wget
import re

regex = re.compile(".*?\\((.*?)\\)")

URL = 'https://www.tumblr.com/tagged/memes'
page = requests.get(URL)

counter = 0

soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.findAll('div', {'class': 'photo_stage_img'}):
    counter += 1
    result = re.findall(regex, link['style'])
    url = result[0]
    wget.download(url, 'images/test' + str(counter) + '.jpg')


print("\n\nCount: " + str(counter))
