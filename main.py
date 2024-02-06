import os
import ssl
from email.message import EmailMessage
import smtplib

email_sender = 'your_email@gmail.com'
email_password = 'your_password'
email_receiver='receiver_email@gmail.com'

subject = 'Check out'
body = '''Just posted a new video'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
