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
driver.get("https://demoqa.com/alerts") 
driver.find_element_by_xpath('//*[@id="promtButton"]').click()
sleep(2)
alert_obj = driver.switch_to.alert
print("Alert shows following message", alert_obj.text)
alert_obj.send_keys("Lucky")
alert_obj.accept()
msg = driver.find_element_by_xpath('//*[@id="promptResult"]').text
print(msg)