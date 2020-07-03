from getpass import getpass
import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 587

sender = 'edward.p.kolodziejski@gmail.com'
password = getpass('Enter your password: ')

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() #extended hello version
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
    #send email
    print('It worked')
except Exception as e:
    print(e)
finally:
    server.quit()