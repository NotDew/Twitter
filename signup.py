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
from twocaptcha import TwoCaptcha
import re


from webdriver_manager.chrome import ChromeDriverManager as CM
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions


import undetected_chromedriver as uc
from undetected_chromedriver import Chrome
import email_verify




import time
solver = TwoCaptcha('92449afaa253261e8a8743154f82f288')

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
        self.get("https://google.com")
       
 
        self.signup_try()
        
        
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
       

    def signup_try(self):
        driver = self
        email = email_verify.get_email(self)
        print(email)
     
        self.get("https://twitter.com")
        time.sleep(5)
        self.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(4) .css-1qaijid > .css-1qaijid").click()
        time.sleep(2)
        self.find_element(By.NAME, "name").send_keys("testshawty12312111")
        time.sleep(2)
        self.find_element(By.CSS_SELECTOR, ".r-1ff274t > .css-1qaijid").click()
        time.sleep(2)
        self.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(1) > .css-175oi2r:nth-child(1) > .css-175oi2r:nth-child(2) .css-175oi2r:nth-child(2) > .css-175oi2r:nth-child(2) > .css-175oi2r:nth-child(1) .css-175oi2r:nth-child(2)").click()
        time.sleep(2)
        self.find_element(By.NAME, "email").click()
        time.sleep(2)
        self.find_element(By.NAME, "email").send_keys(email)
        time.sleep(2)
        self.find_element(By.ID, "SELECTOR_1").click()
        time.sleep(2)
        dropdown = self.find_element(By.ID, "SELECTOR_1")
        time.sleep(2)
        dropdown.find_element(By.XPATH, "//option[. = 'March']").click()
        time.sleep(2)
        self.find_element(By.ID, "SELECTOR_2").click()
        time.sleep(2)
        dropdown = self.find_element(By.ID, "SELECTOR_2")
        time.sleep(2)
        dropdown.find_element(By.XPATH, "//option[. = '15']").click()
        time.sleep(2)
        self.find_element(By.ID, "SELECTOR_3").click()
        time.sleep(2)
        dropdown = self.find_element(By.ID, "SELECTOR_3")
        time.sleep(2)
        dropdown.find_element(By.XPATH, "//option[. = '1981']").click()
        time.sleep(2)
        self.find_element(By.CSS_SELECTOR, ".r-19yznuf > .css-1rynq56").click()
        time.sleep(8)
        # Find the iframe and switch to it
       
      
  
       


        
        result = solver.funcaptcha(sitekey='2CB16598-CB82-4CF7-B332-5990DB66F3AB', url=driver.current_url, surl='https://client-api.arkoselabs.com')
        print(result)
        self.form_submit(result)
        # switch to selected iframe
       
            
            
        
           
            

        #pickle.dump(self.get_cookies() , open("accounts/" + email + ".pkl","wb"))
           
            
        




        time.sleep(50)
    def form_submit(driver, token):
        script = """
        document.getElementById('FunCaptcha-Token').value = decodeURIComponent('{0}');
        document.getElementById('verification-token').value = decodeURIComponent('{0}');
        document.getElementById('submit-btn').disabled = false;
        """.format(
            quote(token)
        )
        time.sleep(1)
        # as example call callback - not required in that example
        driver.execute_script("ArkoseEnforcement.funcaptchaCallback[0]('{}')".format(token))
        driver.find_element(By.ID, "submit-btn").click()
        time.sleep(1)


OnlyFans()