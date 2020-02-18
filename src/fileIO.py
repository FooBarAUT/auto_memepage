from configparser import ConfigParser
from PIL import Image
import random
import wget
import io


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
    """Downloads an image to the given path with given filename

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
    image.save(path + filename + '.png', quality=95)


def get_hashtags():
    """Reads the hashtags.txt

    Parameters:
    None

    Returns:
    List of hashtags
   """
    hashtags = [line.rstrip('\n') for line in open("hashtags.txt")]
    return hashtags


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
