#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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


def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

print("Test Execution Started, using username " + username )
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--enable-javascript")
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)

def check_exists_by_CSS_SELECTOR( value):
    try:
        driver.find_element(By.CSS_SELECTOR, value)
    except NoSuchElementException:
        return False
    return True


def open_web_site():
    #opening overline.network
    driver.get("https://overline.network/app/auth")
    time.sleep(5)
#    try:
#        WebDriverWait(driver, 20).until(
#            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Sign In']"))
#        )
#    finally:
#        driver.quit()


def login():
    print("starting login process...")
    driver.maximize_window()

    #-------login process starts
    #finding input boxes for username and password and pasing the appropriate values
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email address']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
    # get element
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
    #-------login process ends
    print("login success...")

def close_pop_up():
    time.sleep(7)
    driver.find_element(By.CSS_SELECTOR, "img[alt='cross-btn']").click()



#def check_exists_by_xpath(xpath):
#    try:
#        webdriver.find_element_by_xpath(xpath)
#    except NoSuchElementException:
#        return False
#    return True

open_web_site()
login()
close_pop_up()

time.sleep(3)
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
