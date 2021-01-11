
# Returns the product price of the given AMAZON URL
from selenium import webdriver

def amazon_price(amazon_URL):
    browser = webdriver.Chrome(r"C:\Users\Cherry\AppData\Local\Temp\Temp1_chromedriver_win32.zip\chromedriver.exe")

    #amazon_URL = "https://www.amazon.in/MEDLER-Nylon-Expandable-Duffel-Trolley/dp/B07MWD4D4W/ref=sr_1_2_mod_primary_lightning_deal?crid=1J81RH3B0M58X&dchild=1&keywords=deal+of+the+day+sale+today&qid=1610102610&sbo=Tc8eqSFhUl4VwMzbE4fw%2Fw%3D%3D&smid=A2W2P4ZP2OW4Y0&sprefix=dea%2Caps%2C304&sr=8-2"
    #test_URL1 = "https://www.amazon.in/MEDLER-Nylon-Expandable-Duffel-Trolley/dp/B07MWD4D4W/ref=sr_1_2_mod_primary_lightning_deal?crid=1J81RH3B0M58X&dchild=1&keywords=deal+of+the+day+sale+today&qid=1610102610&sbo=Tc8eqSFhUl4VwMzbE4fw%2Fw%3D%3D&smid=A2W2P4ZP2OW4Y0&sprefix=dea%2Caps%2C304&sr=8-2"
    #test_URL2 = "https://www.amazon.in/Sennheiser-PC-Over-Ear-USB-Headphone/dp/B005HWEZGG?ref_=Oct_DLandingS_D_2cf56012_62&smid=A14CZOWI0VEHLG"
    browser.get(amazon_URL)

    try:
        product_price_amazon = browser.find_element_by_css_selector("#priceblock_ourprice")
    except:
        try:
            product_price_amazon = browser.find_element_by_css_selector("#priceblock_dealprice")
        except:
            print("The product is not listed on this website anymore!!")


    product_price_amazon_num = float(product_price_amazon.text.replace(',','').replace('₹','').strip())

    return product_price_amazon_num