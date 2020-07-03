from getpass import getpass
import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465

sender = 'edward.p.kolodziejski@gmail.com'
password = getpass('Enter your password: ')

context = ssl.create_default_context()


with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print('It worked!')