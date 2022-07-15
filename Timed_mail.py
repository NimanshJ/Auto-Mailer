import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

delay = int(input("Enter the delay time(in mins) "))
sleep(delay*60)

sender = 'jainnimansh@gmail.com'
password = 'wntbeminnxmicvlq'
receiver = input("The mail ids to which u want to send(separated by a space): ").split(" ")

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender, password)

text = input("Enter the text you want to send: ")
for i in receiver:

    Body = MIMEMultipart()
    Body['From'] = sender
    Body['To'] = i
    Body['Subject'] = 'This is a python orientated msg'

    html_txt = f"""
        <html>
            <body>
                <h2>{text}</h2>
            </body>
        </html>  
        """
        
    html_at = MIMEText(html_txt, "html")
    Body.attach(html_at)

    text = Body.as_string()
    session.sendmail(sender, i, text)
    print(f'Mail Sent to {i}')

session.quit()