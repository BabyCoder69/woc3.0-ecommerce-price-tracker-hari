import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(email_ID, user_name, product_name, website_name, price, product_URL):
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    #smtpObj.ehlo()

    #test_user_email_ID
    #email_ID = 'hc17760@gmail.com'

    #building the mail content 
    
    with open('credentials.json') as json_data:
        credentials = json.load(json_data)
    
    msg = MIMEMultipart()

    msg['From'] = credentials['user']
    msg['To'] = email_ID
    msg['Subject'] = "Desired Deal available!!!"

    body = "Dear " + user_name + ", <p>The Product: " + product_name + " is available on " + website_name + " at " + price + ".</p>" + "<P>Click <a href=" + product_URL +">here</a>" + " to proceed to the webpage of the product.</p>" 

    msg.attach(MIMEText(body, 'html'))
    
    #Sending the mail
    smtpObj.starttls()
    
    smtpObj.login(credentials['user'],credentials['password'])
    
    smtpObj.sendmail(credentials['user'],email_ID,msg.as_string())

    smtpObj.quit()