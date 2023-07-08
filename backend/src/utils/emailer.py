import smtplib
from config.config import settings
from email.mime.multipart import MIMEMultipart


from utils.mailTemplates import send_email_verification_email


MAIL_USERNAME = settings.MAIL_USERNAME
MAIL_PASSWORD = settings.MAIL_PASSWORD
MAIL_FROM = settings.MAIL_FROM
MAIL_PORT = settings.MAIL_PORT
MAIL_SERVER = settings.MAIL_SERVER
MAIL_FROM_NAME = settings.MAIL_FROM_NAME

def send_email(recipient_email, subject, template_name, template_variables):
    try:
        
        message = MIMEMultipart()
        message['From'] = MAIL_FROM
        message['To'] = recipient_email
        message['Subject'] = subject

        body_part =send_email_verification_email(template_name,template_variables)
        
        message.attach(body_part)

        server = smtplib.SMTP(MAIL_SERVER, int(MAIL_PORT))
        server.starttls()
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.sendmail(MAIL_FROM, recipient_email, message.as_string())
        server.quit()
    except Exception as e:
        raise Exception(f'Error sending email: {str(e)}')



