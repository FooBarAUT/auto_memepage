from src import scrapeTumblr
from src import fileIO

urls = ['https://www.tumblr.com/tagged/funny-meme',
        'https://www.tumblr.com/tagged/funny-memes',
        'https://www.tumblr.com/tagged/hilarious-memes']
counter = 1

for url in urls:
    list = scrapeTumblr.get_stage_images_from_URL(url)

    for image in list:
        fileIO.download_image(image, "images/", "test" + str(counter))
        counter += 1
