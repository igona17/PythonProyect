import smtplib, ssl

port = 25
smtp_server = "smtp.gmail.com"
sender_email = "informacion.pipelines@gmail.com"
receiver_email = "grodriguez@novakorp.io"
receiver_email2 = "agiannoni@novakorp.io"
password = "Sampo2020"
message = """\


Success padreee"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.sendmail(sender_email, receiver_email2, message)