"""
Title: Palomar Specialty Insurance Automation Script
Authors: Bruce Tukuafu
Start_Date: 6/15/21
Description: 
The purpose of this script is to automate the manual click & point process that was formerly used to requeue and remove errors within the Broken Queue
in Pega Designer Studio Code which was used by Palomar Insurance. This script consists of four python files: (main.py, page.py, locators.py, element.py) 
which purpose is modeled after the framework suggested by the Selenium library which is the primary library used wihthin this script. The program can be 
ran on main.py only. Code for the automation process are located primarily on page.py and element locators can be found within locators.py. The element.py
allows for element locators to be properly processed before being used.
"""

import unittest
import stdiomask
import os, sys
import time
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import page
from getpass import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



class PegaProdPage(unittest.TestCase):
    
    def setUp(self):
        self.username = input("Enter your Username: ")
        self.password = stdiomask.getpass("Enter your Password: ")
        self.filepath = input("Enter XCEL PATH: ")
        self.xcel_file = r'' + self.filepath
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
        self.driver.get("https://palomr-psic-prod1.pegacloud.net/prweb/")

    def test_login(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.login(self.username, self.password)
        time.sleep(2)
        main_page.agent_toggle(self.xcel_file)
        time.sleep(5)

    # def test_requeue(self):
    #     studio_page = page.StudioPage(self.driver)
    #     studio_page.login(self.username, self.password)
    #     studio_page.remove(self.xcel_file)
    #     time.sleep(2)
    #     self.requeue_file = input("Enter the Requeue File Path: ")
    #     studio_page.requeue(self.requeue_file)
        
        

    
    


if __name__ == "__main__":
    unittest.main()
