import os
import smtplib
import ssl
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv(dotenv_path='config.local')


def send_email(message_object, titre, texte):
    """Fonction d'envoie d'email

    Args:
        message_object (String): L'objet du mail
        titre (String): Le titre du mail
        texte (String): Le texte du mail
    """
    try:
        smtp_port = 465  # SSL
        smtp_address = os.getenv('STMP_ADRESS')
        email_address = os.getenv('EMAIL_ADRESS')
        email_password = os.getenv('EMAIL_PASSWORD')
        email_receiver = os.getenv('EMAIL_RECEIVER')

        # Create_mail
        message = MIMEMultipart('alternative')
        message['Subject'] = message_object
        message['From'] = email_address
        message['To'] = email_receiver

        html = f"""
        <html>
            <body>
                <h1>{titre}</h1>
                <p>{texte}</h1>
            <body>
        </html> 
        """

        html_mime = MIMEText(html, 'html')
        message.attach(html_mime)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
            server.login(email_address, email_password)
            server.sendmail(email_address, email_receiver, message.as_string())

    except Exception as e:
        print(f'Exception causée en essayant d\'envoyer un mail : {e}')


if __name__ == '__main__':
    pass
