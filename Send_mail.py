import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

delay = int(input("Enter the delay time(in mins) "))
sleep(delay*60)

sender = 'jainnimansh@gmail.com'
password = 'wntbeminnxmicvlq'
receiver = input("The mail id to which u want to send: ")

Body = MIMEMultipart()
Body['From'] = sender
Body['To'] = receiver
Body['Subject'] = 'This is a python orientated msg'

text = input("Enter the text you want to send: ")
html_txt = f"""
    <html>
        <body>
            <h2>{text}</h2>
        </body>
    </html>  
    """
    
html_at = MIMEText(html_txt, "html")
Body.attach(html_at)

session = smtplib.SMTP('smtp.gmail.com', 587)

session.starttls()

session.login(sender, password)

text = Body.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print('Mail Sent')