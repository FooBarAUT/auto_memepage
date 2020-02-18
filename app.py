from src import scrapeTumblr
from src import fileIO

"""
https://www.tumblr.com/tagged/hilarious-memes
https://www.tumblr.com/tagged/funny-memes
https://www.tumblr.com/tagged/funny-meme
"""
URL = 'https://www.tumblr.com/tagged/funny-meme'

list = scrapeTumblr.get_stage_images_from_URL(URL)

counter = 1
for image in list:
    fileIO.download_image(image, "image/", "test" + str(counter))
    counter += 1
