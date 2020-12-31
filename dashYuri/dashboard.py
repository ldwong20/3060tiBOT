import time
import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from BotYuri.search import openPage, searchPageAmazon, searchPageNewegg

item1 = {}
item2 = {}
item3 = {}
item4 = {}
item5 = {}
item6 = {}
item7 = {}
item8 = {}


def checkPrice(link, amount, site):
    """given a link and an amount, the checkPrince function"""
    prices = {}
    data = openPage(link)

    if site.lower() == 'amazon':
        x = searchPageAmazon(data)
        price_float = float(x[1:])
        if price_float < amount:
            # send notification
            pass
        prices[datetime.datetime.now()] = price_float
        # print(prices)
    elif site.lower() == 'newegg':
        x = searchPageNewegg(data)
        price_float = float(x)
        if price_float < amount:
            # send notification
            pass
        prices[datetime.datetime.now()] = price_float
        # print(prices)

    return prices


while True:
    """loop to calculate and graph prices"""

    """figure labels and dimensions"""
    fig = plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(211)
    ax1.set_ylabel('Price $')
    ax1.set_xlabel('Date/Time')
    ax1.set_title('Tracking prices by date')

    """add items to create a dictionary using checkPrice function"""
    a, b = zip(*sorted(checkPrice(
        'https://www.newegg.com/black-fractal-design-meshify-c-dark-tg-atx-mid-tower/p/N82E16811352072#',
        70.0, 'newegg').items()))
    item1[a] = b
    a, b = zip(*sorted(checkPrice(
        'https://www.amazon.com/Crucial-Ballistix-Desktop-Gaming-BL2K8G32C16U4B/dp/B083TRRT16/ref=sxts_sxwds-bia-wc'
        '-nc-drs2_0?cv_ct_cx=ballistix+3200&dchild=1&keywords=ballistix+3200&pd_rd_i=B083TRRT16&pd_rd_r=510968d6-e68e'
        '-4aba-b8d9-282f7b2c9e7a&pd_rd_w=Eeeya&pd_rd_wg=sJEzD&pf_rd_p=a64002b9-9c26-4361-b8a1-b0f5a4835670&pf_rd_r'
        '=ATGGJT2Q69RN5YN5XC3W&psc=1&qid=1609121451&sr=1-2-38d0a374-3318-4625-ad92-b6761a63ecf6',
        50.0, 'amazon').items()))
    item2[a] = b
    a, b = zip(*sorted(checkPrice(
        'https://www.newegg.com/corsair-16gb-288-pin-ddr4-sdram/p/N82E16820236551?Description=vengeance%20rgb%20pro'
        '&cm_re=vengeance_rgb%20pro-_-20-236-551-_-Product&quicklink=true',
        70.0, 'newegg').items()))
    item3[a] = b

    """plot dictionaries"""
    x, y = zip(*sorted(item1.items()))
    plt.plot(x, y, label="Meshify Case (~70)")

    x, y = zip(*sorted(item2.items()))
    plt.plot(x, y, label="Ballistics RAM (~50)")

    x, y = zip(*sorted(item3.items()))
    plt.plot(x, y, label="Corsair RAM (~70)")

    plt.legend(loc="upper right")
    plt.show()

    """sleep timer"""
    time.sleep(5)
