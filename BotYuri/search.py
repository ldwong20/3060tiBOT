# TODO: function opens page
# TODO: function that scrapes page
# TODO: function that notifies person
import urllib3
import requests
from bs4 import BeautifulSoup
import re


def openPage(link):
    # returns a string of the HTML of the page

    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
    page = requests.get(link, headers=HEADERS)
    return page.content


def searchPageAmazon(html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    # print(soup.prettify())

    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    return price


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
    url = "https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820232866?Description=trident%20z%20neo" \
          "&cm_re=trident_z%20neo-_-20-232-866-_-Product "
    data = openPage(url)
    # print(data)
    x = searchPageNewegg(data)
    print(x)
