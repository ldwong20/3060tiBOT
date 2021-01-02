import time
import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from BotYuri.search import openPage, searchPageAmazon, searchPageNewegg

item1 = {}
item2 = {}
item3 = {}
item4 = {}
item5 = {}
item6 = {}
item7 = {}
item8 = {}
password = str(input("Type your password and press enter:"))


def checkPrice(link, amount, site):
    """given a link and an amount, the checkPrince function returns a dictionary with dates and their associated
    prices. The function also sends an email once the price has dipped below a certain threshold """
    prices = {}
    data = openPage(link)

    if site.lower() == 'amazon':
        x = searchPageAmazon(data)
        price_float = float(x[1:])
        if price_float < amount:
            # send notification

            subject = "New Price Drop"
            body = "Please view the attachment below"
            sender_email = "mailingtester69@gmail.com"
            receiver_email = "lacwang1032@gmail.com"
            # password = str(input("Type your password and press enter:"))

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            filename = "graph.pdf"  # In same directory as script

            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()

            # Log in to server using secure context and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
        prices[datetime.datetime.now()] = price_float
        # print(prices)
    elif site.lower() == 'newegg':
        x = searchPageNewegg(data)
        price_float = float(x)
        if price_float < amount:
            # send notification

            subject = "New Price Drop"
            body = "Please view the attachment below"
            sender_email = "mailingtester69@gmail.com"
            receiver_email = "lacwang1032@gmail.com"
            # password = str(input("Type your password and press enter:"))

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            filename = "graph.pdf"  # In same directory as script

            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()

            # Log in to server using secure context and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)

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
        300.0, 'newegg').items()))
    item1[a] = b
    a, b = zip(*sorted(checkPrice(
        'https://www.amazon.com/Crucial-Ballistix-Desktop-Gaming-BL2K8G32C16U4B/dp/B083TRRT16',
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

    plt.legend(loc="lower left")
    plt.savefig('graph.pdf', bbox_inches='tight')
    plt.show()

    """sleep timer"""
    time.sleep(2)
