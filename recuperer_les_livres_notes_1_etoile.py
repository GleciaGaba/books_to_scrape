import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"


def main():

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

if __name__ == '__main__':
    main()