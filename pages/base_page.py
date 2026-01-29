from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging,os


class BasePage():
    HBG_BTN = (By.ID, "react-burger-menu-btn")
    ART_RESET_BTN = (By.ID, "reset_sidebar_link")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
    
    
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        
    def write(self, locator, text):
        element = self.find_element(locator)
        element.clear
        element.send_keys(text)
    
    def visibility_chk(self,locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
    
    def invisibility_chk(self,locator):
        return WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(locator))
    
    
    def open_side_bar(self):
        self.click(self.HBG_BTN)
    
    def reset_app_state(self):
        self.click(self.ART_RESET_BTN)