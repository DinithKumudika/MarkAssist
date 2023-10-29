"""
all the email template functions go here
"""

from utils.emailer import render_template, send_email

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

def send_email_verification_email(to: str, name: str, url: str):

     """
     Send email for verification
     """
     template = 'auth/verification.html'
     subject = "MarkAssist - Email Verification"
     data = {
          "url": url, 
          "first_name": name,
          "subject": subject
     }
     html = render_template(template, data)
     send_email(to, subject, html)


def send_add_password_email(to: str, name: str, url: str):

     """
     Send email for teacher account create complete
     """
     template = 'auth/addPassword.html'
     subject = "MarkAssist - Account Create Complete"
     data = {
          "url": url, 
          "first_name": name,
          "subject": subject
     }
     html = render_template(template, data)
     send_email(to, subject, html)
