import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def mail(email_ID, attachment_file):
    
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)

    #building the mail content 
    
    with open('credentials.json') as json_data:
        credentials = json.load(json_data)
    
    msg = MIMEMultipart()

    msg['From'] = credentials['user']
    msg['To'] = email_ID
    msg['Subject'] = "List of Companies that need your skills!!"
    # Email body
    body = "Hi,\nWe have attached a list of companies that are looking for your skills.\nRegards"
    msg.attach(MIMEText(body, 'plain'))
    # Email attachment
    payload = MIMEBase('application', 'octate-stream')
    with open(attachment_file, 'rb') as attach_file:
        payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) 
    payload.add_header("Content-Disposition",f"attachment; filename= {attachment_file}")
    msg.attach(payload)
    
    #Sending the mail
    smtpObj.starttls()
    
    smtpObj.login(credentials['user'],credentials['password'])
    
    smtpObj.sendmail(credentials['user'],email_ID,msg.as_string())

    smtpObj.quit()