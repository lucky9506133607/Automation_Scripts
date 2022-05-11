import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

Valid_user = ['Admin']
Valid_pass = ['admin123']
Invalid_user = ['admin','ADMIN','aDMIN']
Invalid_Pass= ['Admin123','ADMIN123','aDMIN123']
def selenium():
    global driver 
    driver = webdriver.Chrome()
    time.sleep(6)
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")        
def Login():
    """selenium()
    driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(Valid_user[0])
    driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(Valid_pass[0]) """
    for i in Invalid_user:
        driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(i)
        driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(Valid_pass[0])
    try:
        driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
    except:
        print('Exception occur || Account Disabled')
    time.sleep(3)
    user_name = driver.find_element_by_xpath('//*[@id="welcome"]').getText()
    if (user_name == 'Welcome Paul'):
        print('Valid Employee')
    else:
        print('Invalid Employee')

    
    
    
    
    
    