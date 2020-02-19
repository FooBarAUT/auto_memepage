from bs4 import BeautifulSoup
import requests
import re

# strips everything from the 'style'-tag in which the URL is hidden
regex = re.compile('.*?\\((.*?)\\)')


def get_stage_images_from_URL(URL):
    """Gets a list of image URL's from given Tumblr-URL

    Parameters:
    URL (string): URL of meme-tagged page

    Returns:
    Array of URL's
   """
    results = []

    page = requests.get(URL)
    imageList = BeautifulSoup(page.content, 'html.parser')

    for link in imageList.findAll('div', {'class': 'photo_stage_img'}):
        imageURL = re.findall(regex, link['style'])
        results.append(imageURL[0])

    return results


def get_hashtags_from_URL(URL):
    """Returns a list of hashtags from a given Tumblr-URL

    Parameters:
    URL (string): URL of meme-tagged page

    Returns:
    List of hashtags
   """
    results = []

    page = requests.get(URL)
    imageList = BeautifulSoup(page.content, 'html.parser')

    for link in imageList.findAll('a', {'class': 'post_tag'}):
        hashtag = link.text
        results.append(hashtag)

    return results
