import random
import wget


def download_image(URL, path, filename):
    """Downloads an image to the given path with given filename

    Parameters:
    URL (string): URL of image
    path (string): path to where the file should be saved e.g. 'images/'
    filename (string): desired name of file

    Returns:
    Nothing, just downloads a file
   """
    wget.download(URL, path + filename + '.jpg')
