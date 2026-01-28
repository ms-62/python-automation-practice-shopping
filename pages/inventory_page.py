from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import logging
from pages.base_page import BasePage

logger = logging.getLogger()

class InventoryPage(BasePage):
    
    HBG_BTN = (By.ID, "react-burger-menu-btn")
    ART_RESET_BTN = (By.ID, "reset_sidebar_link")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_BADGE = (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")
    
    ACTION_ADD = "add-to-cart-"
    ACTION_REMOVE = "remove-"
    
    def open_side_bar(self):
        self.click(self.HBG_BTN)
    
    def reset_app_state(self):
        self.click(self.ART_RESET_BTN)
    
    def item_add(self,item):
        logger.info(f"ADD to CART : {item}")
        pick_item = item.lower()
        pick_item = pick_item.replace(" ", "-")
        logger.info(f"ADD TO CART | ITEM NAME : {self.ACTION_ADD + pick_item}")
        self.click((By.ID,self.ACTION_ADD + pick_item))
        

        cart_badge = self.find_element(self.CART_BADGE)
        item_name = self.find_element(self.ITEM_NAME)
        if cart_badge:
            logger.info(f"NOW CART ITEM : {cart_badge.text}개")
            logger.info(f"[SUCCESS] ADD TO CART {item_name.text} ") 
        
        if self.visibility_chk((By.ID,self.ACTION_REMOVE + pick_item)):
            logger.info("CHANGE TO BUTTON TEXT")
            return True
        
    def item_remove(self, item):
        logger.info(f"REMOVE to CART : {item}")
        pick_item = item.lower()
        pick_item = item.replace(" ", "-")
        logger.info(f"REMOVE TO CART | ITEM NAME : {self.ACTION_REMOVE + pick_item}")