from configparser import ConfigParser
from PIL import Image
import random
import wget
import io
import os


def download_image(URL, path, filename):
    """Downloads an image to the given path with given filename

    Parameters:
    URL (string): URL of image
    path (string): path to where the file should be saved e.g. 'images/'
    filename (string): desired name of file

    Returns:
    Nothing, just downloads a file
   """
    wget.download(URL, path + filename + '.png')


def make_square(imagePath, background_color):
    """Takes image from given path and makes it square

    Parameters:
    imagePath (string): path to image
    background_color (RGB): color that's background for non-square images e.g. (255,255,255)

    Returns:
    PIL image
   """
    image = Image.open(imagePath)
    width, height = image.size

    if width == height:
        return image
    elif width > height:
        result = Image.new(image.mode, (width, width), background_color)
        result.paste(image, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(image.mode, (height, height), background_color)
        result.paste(image, ((height - width) // 2, 0))
        return result


def save_image(image, path, filename):
    """Saves an image to the given path with given filename

    Parameters:
    image (PIL image): PIL image e.g. from make_square()
    path (string): path to where the file should be saved e.g. 'images/'
    filename (string): desired name of file

    Returns:
    Nothing, just saves the image
   """
    image.save(path + filename + '.png', dpi=(300, 300), compress_level=0)


def get_hashtags():
    """Reads the hashtags.txt

    Parameters:
    None

    Returns:
    List of hashtags
   """
    hashtags = [line.rstrip('\n') for line in open('hashtags.txt')]
    return hashtags


def remove_duplicates(hashtags):
    """Removes duplicates from given hashtag list

    Parameters:
    hashtags (list): list of hashtags

    Returns:
    List of hashtags without duplicate entries
   """
    result = list(dict.fromkeys(hashtags))
    return result


def save_hashtags(hashtags, filename):
    """Saves the hashtags to a given filename

    Parameters:
    hashtags (list): list of hashtags
    filename (string): desired file to open and append to

    Returns:
    Nothing, just saves the hashtags into the file
   """
    file = open(filename, 'a+')

    for entry in hashtags:
        file.write(entry + '\n')

    file.close()


def get_instagram_credentials():
    """Reads credentials for Instagram login

    Parameters:
    None

    Returns:
    Dictionary with username and password
   """
    config_parser = ConfigParser()

    if config_parser.read('src\\credentials.config'):
        username = config_parser.get('authentication_Instagram', 'username')
        password = config_parser.get('authentication_Instagram', 'password')
        credentials = {'username': username, 'password': password}

        return credentials
    else:
        pass


def delete_file(path):
    """Deletes file

    Parameters:
    path (string): path of file to be deleted

    Returns:
    Sucess or error-message
   """
    try:
        os.remove(path)
        return("Success!")
    except Exception as e:
        return(e)
