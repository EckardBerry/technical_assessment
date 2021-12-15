import requests
from bs4 import BeautifulSoup


def download_scrabble_words_to_a_file():

    url = "http://www.mieliestronk.com/corncob_lowercase.txt"
    page = requests.get(url)
    all_words = BeautifulSoup(page.content, "html.parser").children

    with open('list_of_words.txt', 'w') as f:
        for word in all_words:
            f.write(str(word))


if __name__ == '__main__':
    download_scrabble_words_to_a_file()