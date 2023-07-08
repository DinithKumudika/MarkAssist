# from config.config import settings
# from schemas.user import MailBody
# from ssl import create_default_context
# from email.mime.text import MIMEText
# from smtplib import SMTP


# def send_mail(data: dict | None = None):
#     msg = MailBody(**data)
#     message = MIMEText(msg.body, "html")
#     message["From"] = settings.USERNAME
#     message["To"] = ",".join(msg.to)
#     message["Subject"] = msg.subject

#     ctx = create_default_context()

#     try:
#         with SMTP(settings.HOST, settings.PORT) as server:
#             server.ehlo()
#             server.starttls(context=ctx)
#             server.ehlo()
#             server.login(settings.USERNAME, settings.PASSWORD)
#             server.send_message(message)
#             server.quit()
#         return {"status": 200, "errors": None}
#     except Exception as e:
#         return {"status": 500, "errors": e}