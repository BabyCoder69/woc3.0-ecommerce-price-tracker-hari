from selenium import webdriver

def make_dict(org_list):
    temp_dict = {}
    for link in org_list:
        technologies = []
        browser = webdriver.Chrome(r"C:\Users\Cherry\AppData\Local\Temp\Temp1_chromedriver_win32.zip\chromedriver.exe")
        browser.get(link)
        # Get name of Org
        org_name = browser.find_element_by_class_name("banner__title").text
        # Get technologies 
        ul_element = browser.find_element_by_class_name("org__tag-container")
        items = ul_element.find_elements_by_tag_name('li')
        # To maintain connections with the respective link
        technologies.append(link)
        for item in items:
            technologies.append(item.text)
        # Making a dictionary [key : Org name , value : list of technologies] 
        temp_dict[org_name] = technologies
        print(temp_dict)
        # Closing the browser
        browser.quit()
    return temp_dict

def scrape():
    # Target URL 
    URL = "https://summerofcode.withgoogle.com/archive/2020/organizations/"
    # Give webdriver location for your particular system
    browser = webdriver.Chrome(r"C:\Users\Cherry\AppData\Local\Temp\Temp1_chromedriver_win32.zip\chromedriver.exe")
    browser.get(URL)
    # Identifying elements with links to the different organizations 
    org_list = browser.find_elements_by_class_name("organization-card__link")
    # Creating a list of all links 
    org_list_links = []
    for org in org_list:
        org_list_links.append(org.get_attribute('href'))
    # Closing the browser
    browser.quit()

    # Making a dictionary [key : Org name , value : list of technologies]
    org_dict = make_dict(org_list_links)

    return org_dict

