# coding: cp1252
from http.server import executable
import os, time, random
from selenium.webdriver import Firefox, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium import webdriver
import geckodriver_autoinstaller
import pickle



from webdriver_manager.chrome import ChromeDriverManager as CM

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions


import undetected_chromedriver as uc
from undetected_chromedriver import Chrome




import time

#geckodriver_autoinstaller.install()

class OnlyFans(uc.Chrome):

    # Constructor
    def __init__(self):
        #\
        # Ensures the caption is not too long
       
        
        # Setting the options for the Chrome instance
        #profile = webdriver.FirefoxProfile('/Users/owenj/AppData/Roaming/Mozilla/Firefox/Profiles/cp6yfp9b.default-release')

     
        options = ChromeOptions()
        options.headless = False
        
        super().__init__(options)
        self.get("https://twitter.com")
        time.sleep(5)
        file1 = open("nextlogin.txt","r")
        
        file1.seek(0)
        info = file1.readlines()[0]
        infolist = info.split(":")
        if (len(infolist) == 4):
            self.trylogin(infolist[0], infolist[1], infolist[2], infolist[3])
        else:
            self.trylogin(infolist[0], infolist[1], infolist[2])
    def random_type(self, element, s):

      
        driver = self
        time.sleep(1)

        el = driver.find_element(By.ID, element)
        for element in range(0, len(s)):
            el.send_keys(s[element])
            time.sleep(random.uniform(0.020, 0.050))
        time.sleep(1)
    def random_type_name(self, element, s):

      
        driver = self

        el = driver.find_element(By.NAME, element)
        for element in range(0, len(s)):
            el.send_keys(s[element])
            time.sleep(random.uniform(0.020, 0.050))
        time.sleep(1)
       

    def trylogin(self, email, password, way, username):
        driver = self
        if (way == "normal"):
            self.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(2) > .css-1rynq56 > .css-1qaijid:nth-child(1) > .css-1qaijid").click()
            time.sleep(1)
            self.find_element(By.NAME, "text").click()
            time.sleep(1)
            self.find_element(By.NAME, "text").send_keys(email)
            time.sleep(1)
            self.find_element(By.NAME, "text").send_keys(Keys.ENTER)
            time.sleep(2)
            self.find_element(By.NAME, "password").send_keys(password)
            time.sleep(2)
            self.find_element(By.CSS_SELECTOR, ".r-19yznuf > .css-1rynq56").click()
            
            
        if (way == "google"):
            driver.find_element(By.CSS_SELECTOR, ".m-google > span").click()
            
            time.sleep(2)
            self.random_type("identifierId", email)
            driver.find_element(By.ID, "identifierId").send_keys(Keys.ENTER)
            time.sleep(2)
            self.random_type_name("Passwd", password)
            driver.find_element(By.NAME, "Passwd").send_keys(Keys.ENTER)
            time.sleep(3)
            try:
                driver.find_element(By.CSS_SELECTOR, ".VfPpkd-ksKsZd-mWPk3d-OWXEXe-Tv8l5d-lJfZMc > .VfPpkd-vQzf8d").click()
            except:
                print("No Accept Button")
        if (way == "twitter"):
            driver.find_element(By.CSS_SELECTOR, ".m-twitter > span").click()
            time.sleep(3)
            driver.find_element(By.ID, "username_or_email").click()
            self.random_type("username_or_email", email)

            driver.find_element(By.ID, "password").click()
            self.random_type("password", password)
            
            driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
            time.sleep(3)
            try:
                self.random_type("challenge_response", username)
                driver.find_element(By.ID, "challenge_response").send_keys(Keys.ENTER)
            except:
                print("No Challenge Button")

            time.sleep(100)
            

        pickle.dump(self.get_cookies() , open("accounts/" + email + ".pkl","wb"))
           
            
        




        time.sleep(50)


OnlyFans()