import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(emails, subject, text):

    context = ssl.create_default_context()
    message = f"""From: BEST Valladolid <valladolid@sendinblue.com>
Originally-From: valladolid@best.eu.org
Reply-To: valladolid@best.eu.org
Subject: {subject}
Content-Type: text/html

    {text}
    """

    with smtplib.SMTP("smtp-relay.sendinblue.com",587) as smtp:
        smtp.starttls(context=context)
        smtp.login("valladolid@best.eu.org","xjdwNaLv4Dt2rqpc")
        smtp.sendmail("valladolid@best.eu.org",emails,message)