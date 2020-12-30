import time
import datetime
import matplotlib.pyplot as plt
from BotYuri.search import openPage, searchPage

prices = {}


def checkPrice(link, amount):
    # print("Doing stuff...")
    # do your stuff

    data = openPage(link)
    # print(data)
    x = searchPage(data)
    price_float = float(x[1:])
    if price_float < amount:
        # send notification
        pass
    prices[datetime.datetime.now()] = price_float
    print(prices)




while True:
    checkPrice('https://www.amazon.com/HIFIMAN-SUNDARA-Over-Ear-Full-Size-Headphones/dp/B077XDWT7X/ref=sr_1_3?crid'
               '=2XSA51A1WO3MU&dchild=1&keywords=hifiman+sundara&qid=1609353646&sprefix=hifiman%2Caps%2C462&sr=8-3',
               300.0)

    x, y = zip(*sorted(prices.items()))
    plt.plot(x, y)
    plt.show()


    time.sleep(5)
