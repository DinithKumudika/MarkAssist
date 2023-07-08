from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="../templates")
"""
all the email template functions go here
"""

def send_password_recovery_email(to: str):
     """
     Send email for password recovery
     """
     pass

def send_registration_email(to : str, url: str):
     """
     Send email for registration
     """
     

def send_email_verification_email(to : str):
     """
     Send email for verification
     """
     pass