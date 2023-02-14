#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from credentials import *
import time

username = ventdrop_login
password = ventdrop_password

# place credentials here and uncomment it 
#username = "paster login here"
#password = "paster password here here"



print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)
print("Opening window")
#maximize the window size
driver.maximize_window()
time.sleep(1)
#navigate to browserstack.com
driver.get("https://ventdrop.com/login")
time.sleep(2)

print("trying to inser username")
uname = driver.find_element(By.ID, 'username')
uname.send_keys(username)

print("trying to inser pass")
pword = driver.find_element(By.ID, 'password')
pword.send_keys(password)

time.sleep(1)

print("trying to hit login button")
driver.find_element(By.NAME, 'submit').click()
print("waiting after login")
time.sleep(2)


print("trying to hit REWARD button")
driver.find_element(By.LINK_TEXT, 'Rewards').click()
time.sleep(7)

print("trying to hit 'Claim Chips' button")

## need to find out why this lixnk_text doens't work here, and how to make it work
#driver.find_element(By.LINK_TEXT, 'Claim Chips').click()

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[3]/p").click()

#def check_exists_by_xpath(xpath):
#    try:
#        webdriver.find_element_by_xpath(xpath)
#    except NoSuchElementException:
#        return False
#    return True

time.sleep(5)
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")

