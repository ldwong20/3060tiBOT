import smtplib
import ssl

sender_email = "mailingtester69@gmail.com"
receiver_email = "lacwang1032@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""


# Send email here
port = 465  # For SSL
password = str(input("Type your password and press enter: "))

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("mailingtester69@gmail.com", password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)
