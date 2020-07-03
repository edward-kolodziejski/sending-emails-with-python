from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465

sender = 'edward.p.kolodziejski@gmail.com'
password = getpass('Enter your password: ')
receiver = 'patryyk96@gmail.com'

message = MIMEMultipart('alternative')
message['Subject'] = 'Multipart Test'
message['From'] = sender
message['To'] = receiver

text = """\
    Hi,
    How are you?
    Real python has many great tutorials.
"""

html = """\
<html>
    <body>
        <p>Hi,<br>
            How are you?<br>
            <a href="https://realpython.com">Real Python</a>
            has many great tutorials.
        </p>
    </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

message.attach(part1)
message.attach(part2) #last attach goes first

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())