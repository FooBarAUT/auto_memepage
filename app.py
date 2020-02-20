from src import scrapeTumblr
from src import fileIO
from src import instagram
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

"""hashtags = scrapeTumblr.get_hashtags_from_URL(
    "https://www.tumblr.com/tagged/hilarious-memes")
fileIO.save_hashtags(fileIO.remove_duplicates(hashtags), "hashtags.txt")"""

"""hashtags = fileIO.get_hashtags()
randomHashtags = instagram.get_random_hashtags(hashtags, 15)
text = instagram.create_text(
    "hahaha, funny meme", randomHashtags)

print(text)

username = fileIO.get_instagram_credentials()['username']
password = fileIO.get_instagram_credentials()['password']

image = "square/" + os.listdir("square")[0]

instagram.post(username, password, image, text)
print("Posted!\nNow deleting the file ...\n")
fileIO.delete_file(image)"""
