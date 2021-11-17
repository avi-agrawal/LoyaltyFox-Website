import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail_company(msg):
    sender_email = "testing0963@gmail.com"
    receiver_email = "aviagrawal212@gmail.com"
    # receiver_email_cc = "aviagrawal2121998@gmail.com"
    password = "test@12345"
    # msg = "Hello!\navi"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Loyalty Fox Website | Contact US Response"
    message["From"] = sender_email
    message["To"] = receiver_email
    # message["Cc"] = receiver_email_cc

    # Create the plain-text and HTML version of your message
    # text = msg
    # html = msg

    # Turn these into plain/html MIMEText objects
    part = MIMEText(msg, "plain")
    # part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part)
    # message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


#function to mail the the person whom want to be contacted
def mail_viwer(receiver_email, msg):
    sender_email = "testing0963@gmail.com"
    # receiver_email = "aviagrawal212@gmail.com"
    # receiver_email_cc = "aviagrawal2121998@gmail.com"
    password = "test@12345"
    msg = """
    Thank You for showing interest in our company, we'll contact to you soon.
    Here are the details that you filled:
    """ + str(msg)


    message = MIMEMultipart("alternative")
    message["Subject"] = "Loyalty Fox | Contact US"
    message["From"] = sender_email
    message["To"] = receiver_email
    # message["Cc"] = receiver_email_cc

    # Create the plain-text and HTML version of your message
    # text = msg
    # html = msg

    # Turn these into plain/html MIMEText objects
    part = MIMEText(msg, "plain")
    # part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part)
    # message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
