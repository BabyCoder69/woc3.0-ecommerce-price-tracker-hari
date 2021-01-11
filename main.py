import schedule
import time
from datetime import datetime

import amazon_price
import flipkart_price
import ebay_price
import send_mail
import calc_time

def compare(req_price, current_price):
    if current_price <= req_price:
        return 1,current_price
    return 0,current_price


def compute():
    # take URL from user (temporary, later to be modified to able to work with a database)
    #ebay_URL 
    #amazon_URL
    #flipkart_URL

    with open('amazon.txt','r') as obj:
        amazon_URL = obj.readline()
        amazon_product_name = obj.readline()

    with open('flipkart.txt','r') as obj:
        flipkart_URL = obj.readline()
        flipkart_product_name = obj.readline()

    with open('ebay.txt','r') as obj:
        ebay_URL = obj.readline()
        ebay_product_name = obj.readline()


    # take user price requirement (temporary, later to be modified to able to work with a database)
    # user_price

    amazon_product_req_price = float(2900)
    flipkart_product_req_price = float(2100)
    ebay_product_req_price = float(700)


    ##-----------------------------------------------------------------------------------------------------
    # compare user price with scrapped price 
    # if condition is met "SEND EMAIL"

    amz = compare(amazon_product_req_price,amazon_price.amazon_price(amazon_URL))
    flp = compare(flipkart_product_req_price,flipkart_price.flipkart_price(flipkart_URL))
    eby = compare(ebay_product_req_price,ebay_price.ebay_price(ebay_URL))

    if amz[0]:
        send_mail.mail('hc17760@gmail.com','Hari',amazon_product_name,'Amazon','₹' + str(amz[1]),amazon_URL)
    if flp[0]:
        send_mail.mail('hc17760@gmail.com','Hari',flipkart_product_name,'Flipkart','₹' + str(flp[1]),flipkart_URL)
    if eby[0]:
        send_mail.mail('hc17760@gmail.com','Hari',ebay_product_name,'Ebay',str(eby[1]) + '$',ebay_URL)
    

    global duration

    #updates duration for next time 
    duration = calc_time.time_diff()

    #writes back the current time to keep track for next time 
    with open('time.txt','w') as obj:
        obj.write(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

##------------------------------------------------------------------------
# driver code

duration = calc_time.time_diff()
print(duration)
schedule.every(duration).minutes.do(compute)

while 1:
    schedule.run_pending()
    time.sleep(1)