from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import re

URL = "https://books.toscrape.com/"


def count_price():
    with requests.Session() as session:
        response = session.get(URL)

        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.select("article.product_pod h3 a")
        for article in articles:
            reference = article["href"]
            reference_urls = urljoin(URL, reference)

            response1 = session.get(reference_urls)
            soup1 = BeautifulSoup(response1.text, "html.parser")
            prices = soup1.select("p.price_color")
            for price in prices:
                all_prices = price.text.strip("Â£")
                new_price = float(all_prices)
                #print(new_price)

            stocks_node = soup1.css_first("p.instock.availability")
            stock = int(re.findall(f"\d+", stocks_node.text())[0])
            print(stock)






if __name__ == '__main__':
    count_price()
