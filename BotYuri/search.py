# TODO: function opens page
# TODO: function that scrapes page
# TODO: function that notifies person
import urllib3
import requests
from bs4 import BeautifulSoup
import re


def openPage(link):
    # returns a string of the HTML of the page

    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/74.0.3729.169 Safari/537.36", 'referer': 'https://www.google.com/'}

    page = requests.get(link, headers=header)
    return page.content


def searchPageAmazon(html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    # print(soup.prettify())

    # title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    return price


def inStockAmazon(html_data):
    # returns boolean indicating in stock or not
    soup = BeautifulSoup(html_data, "html.parser")
    if soup.find(id='priceblock_ourprice') is None:
        return False
    else:
        return True


def searchPageNewegg(html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    x = str(soup.find_all('strong'))
    m = re.search(r"\d", x)
    start = m.start()
    end = 0
    for i in range(4):
        if x[start + i].isdigit():
            end += 1

    price = x[start:start + end]
    # print(x)
    # title = soup.find(id='monetate_selector').get_text().strip()
    # price = soup.find(class='price-current-label').get_text().strip()
    return price


if __name__ == "__main__":
    url = "https://www.amazon.com/MSI-MPG-B550-Motherboard-Processors/dp/B089CQFHHZ/ref=sr_1_1?dchild=1&keywords=b550" \
          "+gaming+edge&qid=1609120972&sr=8-1 "
    data = openPage(url)
    # print(data)
    x = inStockAmazon(data)
    print(x)
