from selectolax.parser import HTMLParser
from loguru import logger
import sys
import requests
import re
from urllib.parse import urljoin

logger.remove()
logger.add(f"books1.log", level="WARNING", rotation="500kb")
logger.add(sys.stderr, level="INFO")

"""
## Fonctions à coder

# Fonction pour récuperer l'URL de la page suivante
- Récuperer à partir du HTML directement ou de l'URL?

# Fonction qui à partir de l'URL d'un livre, va calculer le prix.

- Fonction pour récuper le prix à partir du HTML

- Fonction pour récuperer la quantité disponible à partir du HTML

- Fonction pour récupererer les URLs de tous les livres de la bibliothèque

- Fonction pour récuperer les URLs sur une page spécifique

"""

"""
# Fonction pour récuperer l'URL de la page suivante
- Récuperer à partir du HTML directement ou de l'URL?

# Fonction pour récuperer les URLs sur une page spécifique

"""


# Fonction pour récupererer les URLs de tous les livres de la bibliothèque


def get_all_books_urls(url: str) -> list[str]:
    """
    Récuperer toutes mes URLs des livres sur toutrs les pages à partir d'une URL

    :param url: URL de départ
    :return: Liste des URLs de toutes les pages
    """
    pass


def get_next_page_url(tree: HTMLParser) -> str:
    """Récupère l'URL de la page suivante à partir du HTML d'une page donnée.

    :param tree: Objet HTMLParser de la page à chercher.
    :return: URL de la page suivante.
    """
    pass


def get_all_books_urls_on_page(tree: HTMLParser) -> list[str]:
    """
    Récuperer toutes les URLs des livres présent sur une page.

    :param tree: Objet HTMLParser de la page
    :return: Liste de URLs de tous les livres sur la page
    """
    books_links_nodes = tree.css("h3 > a")
    urls = [link for link in books_links_nodes]
    print(urls)


"""
# Fonction qui à partir de l'URL d'un livre, va calculer le prix.

- Fonction pour récuper le prix à partir du HTML

- Fonction pour récuperer la quantité disponible à partir du HTML


"""


def get_book_price(url: str) -> float:
    """
    Récupère le prix d'un livre à partir de son URL.

    :param url: URL de la page du livre.
    :return: Prix du livre multiplié par le nombre de livres en stock.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()
        tree = HTMLParser(response.text)
        price = extract_price_from_page(tree=tree)
        stock = extract_stock_quantity_from_page(tree=tree)
        return price * stock

    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de la requête HTTP: {e}")
        return 0.0


def extract_price_from_page(tree: HTMLParser) -> float:
    """
    Extrait le prix du livre depuis le code HTML de la page.

    :param tree: Objet HTMLParser de la page du livre.
    :return: Le prix unitaire du livre
    """
    price_node = tree.css_first("p.price_color")
    if price_node:
        price_string = price_node.text()
    else:
        logger.error("Aucun noeud contenant le prix n'a été trouvé.")
        return 0.0
    try:
        price = re.findall(r"[0-9.]+", price_string)[0]

    except IndexError as e:
        logger.error(f"Aucun nombre n'a été trouvé: {e}")
        return 0.0
    else:
        return float(price)






def extract_stock_quantity_from_page(tree: HTMLParser) -> int:
    """ Extrait la quantité de livres en stock depuis le code HTML de la page

    :param tree: Objet HTMLParser de la page du livre
    :return: Le nombre de livres en stock
    """
    try:
        stock_node = tree.css_first("p.instock.availability")

        return int(re.findall(f"\d+", stock_node.text())[0])

    except AttributeError as e:
        logger.error(f"Aucun noeud 'p.instock availability' n'a été trouvé sur la page {e}")
        return 0
    except IndexError as e:
        logger.error(f"Aucun noeud 'p.instock availability' n'a été trouvé sur la page {e}")
        return 0



def main():
    base_url = "https://books.toscrape.com/index.html"
    all_books_urls = get_all_books_urls(url=base_url)
    total_price = []
    for book_url in all_books_urls:
        price = get_book_price(url=book_url)
        total_price.append(price)

    return total_price


if __name__ == '__main__':
    url = "https://books.toscrape.com/index.html"
    r = requests.get(url)
    tree = HTMLParser(r.text)
    get_all_books_urls_on_page(tree=tree)
