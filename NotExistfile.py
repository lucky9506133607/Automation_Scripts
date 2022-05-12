import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from PIL import Image
import os
import re


driver = webdriver.Chrome()
sleep(6)
driver.get("https://demo.guru99.com/test/delete_customer.php") 
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input[1]').click()
#driver.implicitly_wait(30) #Wait driver for certain amount of time
sleep(5)
alert_obj = driver.switch_to.alert
print("Alert shows following message", alert_obj.text)
alert_obj.dismiss()
filename = input("Please! Enter your filename = ")

path = '/home/nteam/Desktop/Automation Script Github/'+filename+'.png'
isExist = os.path.exists(path)
print(isExist)

if isExist:
    print("File is already exist")
    newfilename = input("Enter new file name = ")
    driver.save_screenshot(newfilename+'.png')
    image = Image.open(newfilename+'.png')
    image.show()

else:
    print("File not exist")
    #filename = re.findall("([^\/]+\.png)", path)
    driver.save_screenshot(filename+'.png')
    image = Image.open(filename[0])
    image.show()
    

