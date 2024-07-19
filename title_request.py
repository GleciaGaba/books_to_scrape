from bs4 import BeautifulSoup
from pprint import pprint

with open("index.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
"""a_inside_h3 = soup.find_all("h3")

for link in a_inside_h3:

    references = link.find("a").get("title")
    print(references)
"""

title = [a['title'] for a in soup.find_all("a", title=True)]
pprint(title)

