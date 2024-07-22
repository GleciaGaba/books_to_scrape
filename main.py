from bs4 import BeautifulSoup
import requests

"""url = "https://books.toscrape.com/"
response = requests.get(url)"""

with open("index.html", "r") as f:
    html = f.read()


soup = BeautifulSoup(html, "html.parser")


"""
soup = BeautifulSoup(response.text, "html.parser")

Desirable features of the parser to be used. This may be the name of a specific parser("lxml"
, "lxml-xml", "html.parser", or "html5lib". It's recommended that you name a specific parses, 
so that Beautiful Soup gives you the same results across platforms.
"""

#  print(soup.prettify())
# prettify organizes the html code, inserting the indentations.

aside = soup.find("div", class_="side_categories")
categories_div = aside.find("ul").find("li").find("ul")
categories = [child.text.strip() for child in categories_div.children if child.name]
#print(categories)

# print(category.text.strip()) we have some objects None or some line breaks
# to correct this problem with the objects None or the lines breakers we will check the category name

# print(category.name) # we're going to have None or li

# if we use find we will receive just a tag (target) with the landmark body

# if we use find_all it will return a list


images = soup.find("section").find_all("img")
print(images)
for image in images:
    print(image['src'])
