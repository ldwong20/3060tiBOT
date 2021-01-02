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

from BotYuri.search import openPage, searchPageAmazon, searchPageNewegg, inStockAmazon

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
            body = "Please view the attachment below\n\n" + link + " is below " + "$" + str(amount)
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
            body = "Please view the attachment below\n\n" + link + " is below " + "$" + str(amount)
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


def inStock(link, site):
    data = openPage(link)

    if site.lower() == 'amazon' and inStockAmazon(data):
        # send notification

        sender_email = "mailingtester69@gmail.com"
        receiver_email = "lacwang1032@gmail.com"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Item is now in stock"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        
        your item is now in stock at:""" + link
        html = """\
        <html>
          <body>
            <p>Hi,<br>
               <br>
               <a href=""" + link + """">Link</a> 
               is where your item can be found.
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )


while True:
    """loop to calculate and graph prices"""

    """figure labels and dimensions"""
    fig = plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(211)
    ax1.set_ylabel('Price $')
    ax1.set_xlabel('Date/Time')
    ax1.set_title('Tracking prices by date')

    """add items to track for in stock"""
    inStock('https://www.amazon.com/MSI-MPG-B550-Motherboard-Processors/dp/B089CQFHHZ/ref=sr_1_1?dchild=1&keywords'
            '=b550+gaming+edge&qid=1609120972&sr=8-1', 'amazon')
    """add items to create a dictionary using checkPrice function"""
    a, b = zip(*sorted(checkPrice(
        'https://www.newegg.com/black-fractal-design-meshify-c-dark-tg-atx-mid-tower/p/N82E16811352072#',
        71.0, 'newegg').items()))
    item1[a] = b
    a, b = zip(*sorted(checkPrice(
        'https://www.amazon.com/Crucial-Ballistix-Desktop-Gaming-BL2K8G32C16U4B/dp/B083TRRT16',
        51.0, 'amazon').items()))
    item2[a] = b
    a, b = zip(*sorted(checkPrice(
        'https://www.newegg.com/corsair-16gb-288-pin-ddr4-sdram/p/N82E16820236551?Description=vengeance%20rgb%20pro'
        '&cm_re=vengeance_rgb%20pro-_-20-236-551-_-Product&quicklink=true',
        71.0, 'newegg').items()))
    item3[a] = b
    a, b = zip(*sorted(checkPrice(
        'https://www.amazon.com/NZXT-H510-Management-Water-Cooling-Construction/dp/B07TC76671/ref=sr_1_2?dchild=1'
        '&keywords=h510&qid=1609119370&sr=8-2&th=1',
        65.0, 'amazon').items()))
    item4[a] = b
    a, b = zip(*sorted(checkPrice(
        'https://www.newegg.com/msi-b550m-pro-vdh-wifi/p/N82E16813144331',
        106.0, 'newegg').items()))
    item5[a] = b
    a, b = zip(*sorted(checkPrice(
        'https://www.amazon.com/dp/B089DNM8LR?tag=pcpapi-20&linkCode=ogi&th=1&psc=1',
        86.0, 'amazon').items()))
    item6[a] = b
    a, b = zip(*sorted(checkPrice(
        'https://www.amazon.com/Vetroo-Cooler-Processor-Universal-Addressable/dp/B08F21X2VP/ref=sr_1_2?dchild=1'
        '&keywords=vetroo%2Bair%2Bcooler&qid=1609119624&s=electronics&sr=1-2&th=1',
        26.0, 'amazon').items()))
    item7[a] = b

    """plot dictionaries"""
    x, y = zip(*sorted(item1.items()))
    plt.plot(x, y, label="Meshify Case (~70)")

    x, y = zip(*sorted(item2.items()))
    plt.plot(x, y, label="Ballistics RAM (~50)")

    x, y = zip(*sorted(item3.items()))
    plt.plot(x, y, label="Corsair RAM (~70)")

    x, y = zip(*sorted(item4.items()))
    plt.plot(x, y, label="NZXT Case (~65)")

    x, y = zip(*sorted(item5.items()))
    plt.plot(x, y, label="MSI Motherboard (~105)")

    x, y = zip(*sorted(item6.items()))
    plt.plot(x, y, label="Crucial P2 SSD (~85)")

    x, y = zip(*sorted(item7.items()))
    plt.plot(x, y, label="Vetroo V5 Cooler(~25)")

    plt.legend(loc="lower left")
    plt.savefig('graph.pdf', bbox_inches='tight')
    plt.show()

    """sleep timer"""
    time.sleep(2)
