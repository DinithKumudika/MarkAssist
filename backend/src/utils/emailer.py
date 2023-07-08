import smtplib
from pydantic import BaseModel, EmailStr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os

from config.config import settings

MAIL_USERNAME = settings.MAIL_USERNAME
MAIL_PASSWORD = settings.MAIL_PASSWORD
MAIL_FROM = settings.MAIL_FROM
MAIL_PORT = settings.MAIL_PORT
MAIL_SERVER = settings.MAIL_SERVER
MAIL_FROM_NAME = settings.MAIL_FROM_NAME



class EmailSchema(BaseModel):
    email : EmailStr


def send_email(recipient_email, subject, body):
    try:
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = MAIL_FROM
        message['To'] = recipient_email
        message.attach(MIMEText(body, "html"))
        msgBody = message.as_string()
        server = smtplib.SMTP(MAIL_SERVER, int(MAIL_PORT))
        server.starttls()
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.sendmail(MAIL_FROM, recipient_email, msgBody)
    except Exception as e:
        raise Exception(f'Error sending email: {str(e)}')
    finally:
        server.quit()



