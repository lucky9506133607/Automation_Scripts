import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def selenium():
    global driver 
    driver = webdriver.Chrome()
    time.sleep(6)
    driver.get("https://demo.guru99.com/test/delete_customer.php")  

def AcceptPop_UP():
    selenium()
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input[1]').click()
    alert_obj = driver.switch_to.alert
    print("Alert shows following message", alert_obj.text)
    alert_obj.accept()
    driver.implicitly_wait(20) #Wait driver for certain amount of time
    
    #For second pop-up
    alert_obj2 = driver.switch_to.alert
    print("second pop up shows following message", alert_obj2.text)
    time.sleep(2)    
    alert_obj2.accept()

def Reject_Pop_UP():
    selenium()
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input[1]').click()
    alert_obj = driver.switch_to.alert
    print("Alert shows following message", alert_obj.text)
    time.sleep(1)
    alert_obj.dismiss()
    
    
Calling_function = int(input("1 for Accept Pop-up and 2 for reject pop up = "))
if Calling_function == 1:
    print("You select Accept pop up function ", Calling_function)
    AcceptPop_UP()
else:
    print("You select Accept pop up function ", Calling_function)
    Reject_Pop_UP()
    
    
    




