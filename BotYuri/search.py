# TODO: function opens page
# TODO: function that scrapes page
# TODO: function that notifies person
import urllib3
import requests
from bs4 import BeautifulSoup


def openPage(link):
    # returns a string of the HTML of the page

    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
    page = requests.get(link, headers = HEADERS)
    return page.content


def searchPage(html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    # print(soup.prettify())

    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    return price


if __name__ == "__main__":
    url = "https://www.amazon.com/HIFIMAN-SUNDARA-Over-Ear-Full-Size-Headphones/dp/B077XDWT7X/ref=sr_1_3?crid=Q7WCFZVGDEZN&dchild=1&keywords=hifiman+sundara&qid=1609349445&sprefix=hifiman%2Caps%2C176&sr=8-3"
    data = openPage(url)
    # print(data)
    x = searchPage(data)
    print(x)





# page = requests.get("https://www.amazon.com/ASUS-Advanced-Overclocked-Graphics-ROG-STRIX-RTX-2080S-A8G/dp/B07VFKM4VQ/=8-2/", headers = HEADERS)

