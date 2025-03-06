import smtplib

def send_email():
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient@example.com"
    password = "your_password"

    message = """
    Subject: Reminder Task
    This is an automated reminder from your Task Manager.
    """

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()


   