from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging,os

logger = logging.getLogger()

class TestLogin:
    #특정 상품의 장바구니 버튼 동작-장바구니 연동이 이상없는지    
    def test_item_check(self, login_user):
        logger.info(f"START: Add To Cart and Remove To Cart Test")
        try:
            
            pick_item = "-sauce-labs-backpack"
            
            action_add = "add-to-cart"
            action_remove = "remove"
            
            cart_backpack = self.wait.until(EC.element_to_be_clickable((By.ID, action_add + pick_item)))    
            item_bag = self.driver.find_element(By.CLASS_NAME, "inventory_item_name")
            cart_backpack.click()
            
            cart_badge = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")))
            if cart_badge.text:
                logger.info(f"NOW CART ITEM : {cart_badge.text}개")
                logger.info(f"[SUCCESS] ADD TO CART {item_bag.text} ") 
                
                remove_backpack = self.wait.until(EC.element_to_be_clickable((By.ID, action_remove + pick_item)))  
                assert "Remove" in remove_backpack.text, "TEST FAILED : EMPTY CART!!"
                logger.info("[SUCCESS] CHANGE TO BUTTON TEXT AND STATUS  ")
                
                item_img = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"img[alt='{item_bag.text}']")))
                item_img.click()
                
                if  "inventory-item" in self.driver.current_url:
                    remove_btn = self.wait.until(EC.visibility_of_element_located((By.ID, action_remove)))
                    if remove_btn:
                        assert "Remove" in remove_btn.text, "TEST FAILED : NOT MATCH BUTTON!"
                        logger.info("[SUCCESS] MATCH TO CHANGE STATUS")
                else:
                    logger.error("NOT CHANGE WEB PAGE!!")    
            
            else:
                logger.error("EMPTY CART!!")    
                
        except Exception as e:
            logger.error(f"TEST FAILED:  {str(e)}")
            raise
        
    #장바구니 아이템 개별 삭제
    def test_remove_cart_item(self,cart_setup):
        logger.info("START: Cart Item Test")

        try:
            
            pick_item = "-sauce-labs-bolt-t-shirt"
            
            action_add = "add-to-cart"
            action_remove = "remove"
            
            add_cart_item = self.wait.until(EC.element_to_be_clickable((By.ID, action_add + pick_item)))    
            add_cart_item.click()
            logger.info(f"[SUCCESS] ADD TO CART : {pick_item}")
            
            cart_add_btn = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            cart_add_btn.click()
            
            
            if "cart" in self.driver.current_url :
                logger.info(f"[SUCCESS] CART WEB PAGE")
                remove_cart_item = self.wait.until(EC.visibility_of_element_located((By.ID, action_remove + pick_item)))   
                logger.info(f"[SUCCESS] FIND REMOVE BUTTON : {remove_cart_item.text}")
                
                cart_remove_btn = self.wait.until(EC.element_to_be_clickable((By.ID, action_remove + pick_item)))    
                cart_remove_btn.click()
                
                check_item = self.wait.until(EC.invisibility_of_element_located((By.ID, action_remove + pick_item)))   
                
                assert check_item is True, f"TEST FAILED: REMAINED ITEM {check_item.text} "
                logger.info(f"[SUCCESS] REMOVE TO ITEM")
                


        except Exception as e:
            logger.error(f"TEST FAILED:  {str(e)}")
            raise