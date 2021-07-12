import smtplib, ssl
import sys

a = sys.stdin.readline()
port = 25
smtp_server = "smtp.gmail.com"
sender_email = "informacion.pipelines@gmail.com"
receiver_email = a
password = "Sampo2020"
message = """\

Holaaa."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)