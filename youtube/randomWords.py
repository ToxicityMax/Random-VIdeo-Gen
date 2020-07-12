import requests
words_url = "https://random-word-api.herokuapp.com/word?number=3&&swear=0"


def genWords():
    words = []
    words = requests.get(words_url).json()
    return words    