import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

def send_email(subject, body):
    sender_email = "mahajanhemangi219@gmail.com"
    receiver_email = "mahajahemangi8767@gmail.com"
    password = "ldzqpjyltlimjvqf"   # remove spaces

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # attach message
    msg.attach(MIMEText("<h1>" + body + "</h1>", 'html'))

    filename = "app.log"

    with open(filename, "rb") as attachment:
        mime_base = MIMEBase("application", "octet-stream")
        mime_base.set_payload(attachment.read())

    encoders.encode_base64(mime_base)
    mime_base.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(mime_base)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

    print("Message sent successfully")

send_email("Test Email", "checking my mail function")