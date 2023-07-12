import smtplib
from pydantic import BaseModel, EmailStr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader, TemplateNotFound, select_autoescape

from config.config import settings


MAIL_USERNAME = settings.MAIL_USERNAME
MAIL_PASSWORD = settings.MAIL_PASSWORD
MAIL_FROM = settings.MAIL_FROM
MAIL_PORT = settings.MAIL_PORT
MAIL_SERVER = settings.MAIL_SERVER
MAIL_FROM_NAME = settings.MAIL_FROM_NAME

class EmailSchema(BaseModel):
    email : EmailStr
    

def render_template(template: str, data: dict):
    try:
        templateLoader = FileSystemLoader(searchpath='templates')
        template_env = Environment(
            loader=templateLoader,
            autoescape=select_autoescape(['html', 'xml'])
        )
        templ = template_env.get_template(template)
        return templ.render(**data)
    except TemplateNotFound as e:
        raise Exception(f'No template found: {str(e)}')
    

def send_email(recipient, subject, body):
    try:
        
        message = MIMEMultipart()
        message['From'] = MAIL_FROM
        message['To'] = recipient
        message['Subject'] = subject

        # body_part =send_email_verification_email(template_name,template_variables)
        message.attach(MIMEText(body, "html"))
        message_body = message.as_string()
        server = smtplib.SMTP(MAIL_SERVER, int(MAIL_PORT))
        server.starttls()
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.sendmail(MAIL_FROM, recipient, message_body)
    except Exception as e:
        raise Exception(f'Error sending email: {str(e)}')
    finally:
        server.quit()



