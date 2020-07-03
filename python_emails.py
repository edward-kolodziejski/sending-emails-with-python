import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass


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

filename = 'python.jpg'

with open(filename, 'rb') as attachment:
    part_a = MIMEBase('application', 'octet-stream')
    part_a.set_payload(attachment.read())

encoders.encode_base64(part_a)

part_a.add_header(
    'Content-Disposition',
    f'attachment; filename={filename}'
)

message.attach(part1)
message.attach(part2) #last attach goes first
message.attach(part_a)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
