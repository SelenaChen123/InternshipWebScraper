# Imports libraries
import requests as req
from bs4 import BeautifulSoup as bs

# Sets base URL
baseURL = "https://www.levels.fyi/internships/"


def getPage():
    # Gets the page and parses it
    html = req.get(baseURL + str(id)).text
    page = bs(html, "html.parser")

    return page


def main():
    page = getPage()
    print(page.find("table", {"class": "internships-table"}))


print()
main()
print()
