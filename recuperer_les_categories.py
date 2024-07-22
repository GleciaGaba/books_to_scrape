from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

URL = "https://books.toscrape.com/"


def main(threshold: int = 5):
    with requests.Session() as session:

        response = session.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

        # aside = soup.find("ul", class_="nav nav-list").find_all("a")

        # Alternative
        categories = soup.select("ul.nav.nav-list a")
        categories_url = [category.get("href") for category in categories[1:]]
        for category_url in categories_url:
            absolute_url = urljoin(URL, category_url)
            response = session.get(absolute_url)
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.select("article.product_pod")
            number_of_books = len(books)
            category_title = soup.select_one("h1").text

            if number_of_books <= threshold:
                print(f"La catégorie '{category_title}' ne contient pas assez de livres ({number_of_books}).")
            else:
                print(f"La catégorie '{category_title}' contient assez de livres ({number_of_books})")


if __name__ == '__main__':
    main(threshold=1)
