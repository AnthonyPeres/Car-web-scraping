import os
import smtplib, ssl
from dotenv import load_dotenv

load_dotenv(dotenv_path='config.local')

smtp_address = os.getenv('STMP_ADRESS')
smtp_port = 465
email_address = os.getenv('EMAIL_ADRESS')
email_password = os.getenv('EMAIL_PASSWORD')
email_receiver = os.getenv('EMAIL_RECEIVER')

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
    # connexion au compte
    server.login(email_address, email_password)
    # envoi du mail
    server.sendmail(email_address, email_receiver, 'le contenu de l\'e-mail')