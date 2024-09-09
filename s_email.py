import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, recipient_email):
    # SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'adityajangitiaap@gmail.com'
    sender_password = 'ctia aicd uxqk nfgy'

    #email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(message)
    server.quit()

if __name__ == "__main__":
    # Email details
    subject = "Test Email"
    body = "This is a test email sent from a Python script."
    recipient_email = "rajeshchitti71@gmail.com"

    # Send the email
    send_email(subject, body, recipient_email)