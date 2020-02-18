from bs4 import BeautifulSoup
import requests
import wget
import re

regex = re.compile(".*?\\((.*?)\\)")
"""
https://www.tumblr.com/tagged/hilarious-memes
https://www.tumblr.com/tagged/funny-memes
https://www.tumblr.com/tagged/funny-meme
"""
URL = 'https://www.tumblr.com/tagged/funny-meme'
page = requests.get(URL)

counter = 0

soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.findAll('div', {'class': 'photo_stage_img'}):
    counter += 1
    result = re.findall(regex, link['style'])
    url = result[0]
    wget.download(url, 'images/meme' + str(counter) + '.jpg')


print("\n\nCount: " + str(counter))
