from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import logging
from pages.base_page import BasePage

logger = logging.getLogger()

class InventoryPage(BasePage):
    
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_BADGE = (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")
    
    
    ITEM_IMG = "inventory-item-"
    ACTION_ADD = "add-to-cart-"
    ACTION_REMOVE = "remove-"
    DETAIL_REMOVE = "remove"
    
    def item_add(self,item):
        logger.info(f"ADD to CART : {item}")
        try:
            pick_item = item.lower().replace(" ", "-")
            logger.info(f"ADD TO CART | ITEM NAME : {self.ACTION_ADD + pick_item}")
            self.click((By.ID,self.ACTION_ADD + pick_item))
            

            cart_badge = self.find_element(self.CART_BADGE)
            if cart_badge:
                logger.info(f"NOW CART ITEM : {cart_badge.text}개")
            
            if self.visibility_chk((By.ID,self.ACTION_REMOVE + pick_item)):
                logger.info("[SUCCESS] CHANGE TO BUTTON TEXT")
                return True
            else:
                return False
        except Exception as e:
            logger.error(f"TEST FAILED:  {str(e)}")
            raise
    def item_detail(self,item):
        logger.info(f"{item}")    
        try:
            pick_item = item.lower().replace(" ", "-")
            logger.info(f"MOVE TO DETAIL PAGE | ITEM NAME : {self.ITEM_IMG + pick_item }-img")
            img = (By.CSS_SELECTOR,f"img[data-test='{self.ITEM_IMG + pick_item}-img']")
            
            img_element = self.find_element(img)
            
            if img_element.get_attribute("alt") == item :
                self.click(img_element)
                logger.info("[SUCCESS] CLICK TO ITEM DETAIL PAGE")
                if  "inventory-item" in self.driver.current_url:
                    logger.info("[SUCCESS] MOVE TO DETAIL PAGE")
                    if self.visibility_chk((By.ID,self.DETAIL_REMOVE)):
                        "Remove" in self.visibility_chk((By.ID,self.DETAIL_REMOVE)).text
                        logger.info("[SUCCESS] CHECK TO REMOVE BUTTON")
                        return True
        except Exception as e:
            logger.error(f"TEST FAILED:  {str(e)}")
            raise    
        
    def item_remove(self, item):
        logger.info(f"REMOVE to CART : {item}")
        pick_item = item.lower()
        pick_item = item.replace(" ", "-")
        logger.info(f"REMOVE TO CART | ITEM NAME : {self.ACTION_REMOVE + pick_item}")
        
    

        