"""
all the email template functions go here
"""
from jinja2 import Environment, FileSystemLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_password_recovery_email():
     """
     Send email for password recovery
     """
     pass

def send_registration_email():
     """
     Send email for registration
     """
     pass

def send_email_verification_email(template_name:str,template_variables:dict):
    
    """
    Send email for verification
    """
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    body = template.render(**template_variables)
    
    body_part = MIMEText(body, 'html')
        
    return body_part
