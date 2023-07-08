import smtplib

from config.config import settings

MAIL_USERNAME = settings.MAIL_USERNAME
MAIL_PASSWORD = settings.MAIL_PASSWORD
MAIL_FROM = settings.MAIL_FROM
MAIL_PORT = settings.MAIL_PORT
MAIL_SERVER = settings.MAIL_SERVER
MAIL_FROM_NAME = settings.MAIL_FROM_NAME

def send_email(recipient_email, subject, body):
    try:
        server = smtplib.SMTP(MAIL_SERVER, int(MAIL_PORT))
        server.starttls()
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(MAIL_FROM, recipient_email, message)
        server.quit()
    except Exception as e:
        raise Exception(f'Error sending email: {str(e)}')



