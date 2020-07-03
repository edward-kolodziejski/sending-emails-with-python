import yagmail

receiver = 'patryyk96@gmail.com'
body = 'Hello from Yagmail'
filename = 'python.jpg'

yag = yagmail.SMTP('edward.p.kolodziejski@gmail.com')

yag.send(
    to=receiver,
    subject='Yagmail test witch attachment',
    contents=body,
    attachments=filename,
)