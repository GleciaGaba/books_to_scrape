import requests
import re
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"


def main() -> list[int]:
    book_ids = []
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Il y a eu un problème lors de m'accèes au site.")
        raise requests.exceptions.RequestException from e
    soup = BeautifulSoup(response.text, "html.parser")
    one_star_books = soup.select("p.star-rating.One")
    for book in one_star_books:
        try:
            book_link = book.find_next("h3").find("a")["href"]

        except AttributeError as e:
            print("Impossible de trouver la balise h3 ou la basile a.")
            raise AttributeError from e
        except TypeError as e:
            print("Impossible de trouver la balise 'a' à l'interieur de 'h3'.")
            raise TypeError from e
        except KeyError as e:
            print("Impossible de trouver la clé 'href' à l'interieur de 'a'.")
            raise KeyError from e

        try:
            book_id = re.findall(r'_\d+', book_link)[0][1:]

        except IndexError as e:
            print("Impossible de trouver l'ID du livre")
            raise IndexError from e
        else:
            book_ids.append(int(book_id))

    return book_ids


if __name__ == '__main__':
    print(main())
