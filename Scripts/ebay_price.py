
# Returns the product price for the given EBAY URL
from selenium import webdriver

def ebay_price(ebay_URL):
    browser = webdriver.Chrome(r"C:\Users\Cherry\AppData\Local\Temp\Temp1_chromedriver_win32.zip\chromedriver.exe")

    #ebay_URL = "https://www.ebay.com/itm/Lenovo-ThinkBook-14s-Yoga-Laptop-14-0-FHD-IPS-Touch-300-nits-i5-1135G7/164564602735?_trkparms=aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D20201210111314%26meid%3D3c49f3d339524050b859f91d1c53d6a1%26pid%3D101195%26rk%3D3%26rkt%3D12%26mehot%3Dco%26sd%3D293806741891%26itm%3D164564602735%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv5PairwiseWebWithDarwoV3BBEV2b%26brand%3DLenovo&_trksid=p2047675.c101195.m1851"
    #test_URL 1 = "https://www.ebay.com/itm/Lenovo-Legion-5-15-6-144Hz-Ryzen-7-4800H-16GB-RAM-256GB-SSD-GTX-1660-Ti-6GB/293806741891"
    #test_URL 2 = "https://www.ebay.com/itm/Lenovo-ThinkBook-14s-Yoga-Laptop-14-0-FHD-IPS-Touch-300-nits-i5-1135G7/164564602735?_trkparms=aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D20201210111314%26meid%3D3c49f3d339524050b859f91d1c53d6a1%26pid%3D101195%26rk%3D3%26rkt%3D12%26mehot%3Dco%26sd%3D293806741891%26itm%3D164564602735%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv5PairwiseWebWithDarwoV3BBEV2b%26brand%3DLenovo&_trksid=p2047675.c101195.m1851"
    browser.get(ebay_URL)

    try:
        product_price_ebay = browser.find_element_by_id('prcIsum')
    except: 
        print("This product is not listed on this website anymore!!")

    product_price_ebay_num = float(product_price_ebay.text.replace(',','').replace('US','').replace('$','').strip())
    
    return product_price_ebay_num