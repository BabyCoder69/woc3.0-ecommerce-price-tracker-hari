
# Returns flipkart product price for the given FLIPKART URL
from selenium import webdriver

def flipkart_price(flipkart_URL):
    browser = webdriver.Chrome(r"C:\Users\Cherry\AppData\Local\Temp\Temp1_chromedriver_win32.zip\chromedriver.exe")

    #flipkart_URL = "https://www.flipkart.com/nike-revolution-5-running-shoes-men/p/itm11637de31a718?pid=SHOFK455HPZXAGX8&lid=LSTSHOFK455HPZXAGX8XXOAA5&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_2_4.dealCard.OMU_PRQTA6S7GJ33_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_2_NA_view-all_2&fm=neo%2Fmerchandising&iid=0c0d74ec-dc9a-4cbc-9089-ec6c9e4389bb.SHOFK455HPZXAGX8.SEARCH&ppt=browse&ppn=browse&ssid=ybycqd2xm80000001610101772899"
    #test_URL 1 = "https://www.flipkart.com/nike-revolution-5-running-shoes-men/p/itm11637de31a718?pid=SHOFK455HPZXAGX8&lid=LSTSHOFK455HPZXAGX8XXOAA5&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_2_4.dealCard.OMU_PRQTA6S7GJ33_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_2_NA_view-all_2&fm=neo%2Fmerchandising&iid=0c0d74ec-dc9a-4cbc-9089-ec6c9e4389bb.SHOFK455HPZXAGX8.SEARCH&ppt=browse&ppn=browse&ssid=ybycqd2xm80000001610101772899"
    #test_URL 2 = "https://www.flipkart.com/realme-buds-q-bluetooth-headset/p/itm9d0d4b3692656?pid=ACCFVWN4PGNTEFGY&lid=LSTACCFVWN4PGNTEFGYNDRHV5&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Best%2Bof%2BElectronics_2_9.dealCard.OMU_T126A7GAOU58_5&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_2_NA_view-all_5&fm=neon%2Fmerchandising&iid=943e8260-493c-491e-bcac-d2d4370ffcbf.ACCFVWN4PGNTEFGY.SEARCH&ppt=browse&ppn=browse&ssid=cbidvt2hrk0000001610103690993"
    browser.get(flipkart_URL)

    try:
        product_price_flipkart = browser.find_element_by_class_name('_30jeq3._16Jk6d')
    except: 
        print("This product is not listed on this website anymore!!")

    product_price_flipkart_num = float(product_price_flipkart.text.replace(',','').replace('₹','').strip())
    
    return product_price_flipkart_num

