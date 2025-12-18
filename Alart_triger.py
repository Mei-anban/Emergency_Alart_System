#alart triger

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3

#connect to db

conn=sqlite3.connect("Emergency_contect.db")
cursor= conn.cursor()

def send_alart(subject,message):

    sender_email = "meiyanban70@gmail.com"
    sender_pass = "zdsb jrws ywxx xaqd"

    cursor.execute("SELECT name,email FROM contects")
    contects = cursor.fetchall()

    for name,email in contects:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email
        msg["Subject"] = subject

        msg.attach(MIMEText(message,"plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls() # encrypt the connection
            server.login(sender_email,sender_pass)
            server.sendmail(sender_email,email,msg.as_string())
            server.quit()
            print(f"Alart sent to {name} ({email})")

        except Exception as e:
            print(f"❌ Failed to send to {name}: {e}")


