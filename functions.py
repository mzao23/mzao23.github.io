import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import db


def email_verification(email):

    def verification_code():
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"

        code = ""

        for i in range(8):

            char = random.randint(1, 3)

            if char == 1:
                code = f"{code}{alphabet[random.randint(0, 25)]}"
            
            if char == 2:
                code = f"{code}{alphabet[random.randint(0, 25)].upper()}"
            
            if char == 3:
                code = f"{code}{numbers[random.randint(0, 9)]}"
        
        return code

    code = verification_code()

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'nizaroxhxray@gmail.com'
    smtp_password = 'mxcr dioa opgj xjud'

    sender_email = 'nizaroxhxray@gmail.com'

    subject = 'Verification'
    body = f"Here is your verification code : {code}"
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        server.sendmail(sender_email, email, message.as_string())

        return [True, code]

    except Exception as e:
        return [e]

    finally:
        server.quit()

def add_user(email, password):
    db.cursor.execute("INSERT INTO users (email, password, name, last_name) VALUES (%s, %s, %s, %s)", (email, password, "", ""))
    db.connection.commit()

def verify_user(email, password):
    db.cursor.execute("SELECT email FROM users WHERE email = %s AND password = %s", (email, password))
    result = db.cursor.fetchone()
    return result
