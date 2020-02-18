import re
import requests
from bs4 import BeautifulSoup

regex = re.compile(".*?\\((.*?)\\)")

URL = 'https://www.tumblr.com/tagged/memes'
page = requests.get(URL)

counter = 0

soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.findAll('div', {'class': 'photo_stage_img'}):
    result = re.findall(regex, link['style'])
    counter += 1
    print(result[0])


print("Count: " + str(counter))
