from loguru import logger
import sys
from selectolax.parser import HTMLParser
import requests
from bs4 import BeautifulSoup

logger.remove()
logger.add("books.log", rotation="500kb", level="WARNING")
logger.add(sys.stderr, level="INFO")

url = "https://books.toscrape.com/index.html"

response = requests.get(url)
tree = HTMLParser(response.text)
soup = BeautifulSoup(response.text, "html.parser")

all_links_soup = soup.select("a")
first_link_soup = soup.select("a")

all_links_tree = tree.css("a")
first_links_tree = tree.css_first("a")

print()

