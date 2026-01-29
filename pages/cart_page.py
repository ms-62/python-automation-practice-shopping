from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import logging
from pages.base_page import BasePage

logger = logging.getLogger()

class CartPage(BasePage):
    ACTION_ADD = "add-to-cart-"
    ACTION_REMOVE = "remove-"
    DETAIL_REMOVE = "remove"
    
    CART_BTN = (By.CLASS_NAME, "shopping_cart_link")
    
    def remove_cart_item(self, item):
        logger.info("START REMOVE CART ITEM")
        try:
            self.click(self.CART_BTN)
            pick_item = item.lower().replace(" ", "-")
            if "cart" in self.driver.current_url:
                remove_cart_item = self.visibility_chk((By.ID, self.ACTION_REMOVE + pick_item))
                logger.info(f"[SUCCESS] FIND REMOVE BUTTON : {remove_cart_item.text}")  
                self.click((By.ID, self.ACTION_REMOVE + pick_item))
                
                check_item = self.invisibility_chk((By.ID, self.ACTION_REMOVE + pick_item))
                if not check_item:
                    logger.error("TEST FAILED")
                else:
                    logger.info(f"[SUCCESS] REMOVE TO ITEM : {remove_cart_item.text}")  
                    return True
        except Exception as e:
            logger.error(f"TEST FAILED:  {str(e)}")
            raise    