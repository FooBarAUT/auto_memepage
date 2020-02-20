from instapy_cli import client
import random


def get_random_hashtags(input, number):
    """Gets a user-specified number of random hashtags from input

    Parameters:
    input (list): list of hashtags e.g. from fileIO.get_hashtags()
    number (int): number of random hashtags the we wanna get out

    Returns:
    Array of random hashtags
   """
    output = []

    for i in range(1, number + 1):
        hashtag = random.choice(input)
        output.append(hashtag)
    return output


def create_text(text, hashtags):
    """Returns a solid string containing the entire text of the posting

    Parameters:
    text (string): text of your posting
    hashtags (list): list of hashtags e.g. from get_random_hashtags()

    Returns:
    string that contains the posting
   """
    output = text + '\n.\n.\n.\n.\n' + ' '.join(map(str, hashtags))
    return output


def post(username, password, image, text):
    """Creates a posting on instagram

    Parameters:
    username (string): username
    password (string): password
    image (string): path to image e.g. 'images/test-1.png'
    text (string): text for the posting e.g. from create_text()

    Returns:
    Nothing, just posts to instagram
   """
    try:
        with client(username, password) as cli:
            cli.upload(image, text)
        return("Sucess!")
    except Exception as e:
        return e
