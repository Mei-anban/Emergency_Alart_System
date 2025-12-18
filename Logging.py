
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
import smtplib


conn= sqlite3.connect("Emergency_contect.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS alarts (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               contect_name TEXT,
               contect_email TEXT,
               alart_subjects TEXT,
               alart_message TEXT
               timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)""")

conn.commit()

#logging function

def log_alart(name,email,subject,message):
    cursor.execute(
        "INSERT INTO alarts (contect_name,contect_email,alart_subjects,alart_message) VALUES (?,?,?,?)",(name,email,subject,message)
    )

    conn.commit()

#update alart triger

def send_email(subject,message):
    sender_email = "meiyanban70@gmail.com"
    sender_pass="zdsb jrws ywxx xaqd"

    cursor.execute("SELECT name,email from contects")
    contects = cursor.fetchall()

    for name,email in contects :
        msg = MIMEMultipart()
        msg ["From"] = sender_email
        msg ["To"] = email
        msg ["Subject"] = subject
        msg.attach(MIMEText(message,"plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_pass)
            server.sendmail(sender_email, email, msg.as_string())
            server.quit()
            print(f"✅ Alert sent to {name} ({email})")

            #log the alart

            log_alart(name,email,subject,message)

        except Exception as e:
            print(f"Failed to send to {name}: {e}")

def view_alarts():
    cursor.execute("SELECT * FROM alarts")
    for i in cursor.fetchall():
        print(i)
