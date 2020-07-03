from getpass import getpass
import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465

sender = 'edward.p.kolodziejski@gmail.com'
password = getpass('Enter your password: ')

receiver = 'patryyk96@gmail.com'
message = """\
    From: {}
    To: {}
    Subject: Hello World!

    This is test message and it has been sent from Python.
""".format(sender, receiver)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)