import csv
import scrape_tech
import send_mail

# Generate scrapped result 
data = scrape_tech.scrape()
# using hard coded data for testing purposes ; uncomment the above line before running the code and comment the below one  
#data = {'52° North GmbH': ['https://summerofcode.withgoogle.com/archive/2020/organizations/6309633414660096/', 'java', 'android', 'javascript', 'python', 'react'], 'AboutCode.org': ['https://summerofcode.withgoogle.com/archive/2020/organizations/6689005560659968/', 'python', 'c/c++', 'rust', 'javascript', 'postgresql'], 'Academy Software Foundation (ASWF)': ['https://summerofcode.withgoogle.com/archive/2020/organizations/6043464124334080/', 'c/c++', 'python']}

# Take user input for Technologies
user_tech_list = []
while 1:
    temp = input("Enter What you know from the above tech stack: ")
    if temp == "exit":
        break
    else:
        user_tech_list.append(temp.strip())
# Take user input for email ID
email_id = input("Enter your email ID: ")

# Making the csv file
with open('result_'+ str(email_id) +'.csv','w',newline='') as obj:
    thewriter = csv.writer(obj)
    for key in data:
        for tech in user_tech_list:
            if tech in data[key]:
                temp_list = [key,data[key][0],data[key][1:]]
                thewriter.writerow(temp_list)

# Sending the mail
send_mail.mail(email_id,'result_'+ str(email_id) +'.csv')