import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

"""gets all the prices with the names of the products as a dictionary on a newegg search page"""
def get(link):
    page = requests.get(link, headers=HEADERS).content
    soup = BeautifulSoup(page, features='lxml')
    item_data = soup.find_all('div', {'class': 'item-cell'})
    items = {}

    for item in item_data:
        price = item.find('li', {'class': 'price-current'})
        if price is not None:
            name = item.find('a', {'class': 'item-title'}).get_text(strip=True)
            price = price.get_text(strip=True)
            items[name] = price

    print(items)


if __name__ == "__main__":
    link = "https://www.newegg.com/p/pl?d=2060"
    get(link)
