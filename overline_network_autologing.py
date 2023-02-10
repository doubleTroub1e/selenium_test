#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from credentials import *
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username',
                    default='1',
                    dest='user_c',
                    help='Provide username to use. Defaults to overline_username_1',
                    type=str
                    )
args = parser.parse_args()

def get_valid_username(passed_value):
    if passed_value == "1":
        username = overline_username_1
    elif passed_value == "2":
        username = overline_username_2
    elif passed_value == "3":
        username = overline_username_3
    else:
        print("using default username and password")
        username = overline_username_1
    return (username)

def get_valid_password(passed_value):
    if passed_value == "1":
        password = overline_password_1
    elif passed_value == "2":
        password = overline_password_2
    elif passed_value == "3":
        password = overline_password_3
    else:
        print("using default username and password")
        password = overline_password_1
    return (password)
username = get_valid_username(args.user_c)
password = get_valid_password(args.user_c)

# place credentials here and uncomment it 
#username = "paster login here"
#password = "paster password here here"


print("Test Execution Started, using username " + username )
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
time.sleep(3)
#navigate to browserstack.com
driver.get("https://overline.network/app/auth")
time.sleep(5)
print("trying to inser username")
uname = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/input[1]")
uname.send_keys(username)
print("trying to inser pass")
pword = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/input[2]")
pword.send_keys(password)

time.sleep(1)
print("trying to hit login button")
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div/div[2]/form/button[1]").click()
print("waiting after login")
time.sleep(5)
print("trying to hit close button")
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/button[1]").click()

#def check_exists_by_xpath(xpath):
#    try:
#        webdriver.find_element_by_xpath(xpath)
#    except NoSuchElementException:
#        return False
#    return True

time.sleep(3)
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")

