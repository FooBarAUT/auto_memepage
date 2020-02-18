from src import scrapeTumblr
from src import fileIO
import os

urls = ['https://www.tumblr.com/tagged/funny-meme',
        'https://www.tumblr.com/tagged/funny-memes',
        'https://www.tumblr.com/tagged/hilarious-memes']
counter = 1

for url in urls:
    list = scrapeTumblr.get_stage_images_from_URL(url)

    for image in list:
        fileIO.download_image(image, "images/", "test-" + str(counter))
        counter += 1

imagelist = os.listdir('images')
for filename in imagelist:
    square = fileIO.make_square("images/" + filename, (255, 255, 255))
    fileIO.save_image(square, "square/", filename[:-4])
