import smtplib
from email.mime.text import MIMEText


def send_email(subject,body):
    sender_email="mahajanhemangi219@gmail.com"
    receiver_email="mahajahemangi8767@gmail.com"
    password="ldzq pjyl tlim jvqf"

    msg = MIMEText(body)
    msg['subject'] = subject
    msg['from'] = sender_email
    msg['to'] = receiver_email
    
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.startttls() # encryption connection
        server.login(sender_email,password)
        server.send_message(msg)
        print("Message send successfully")


send_email("Test Email","checking my mail function")