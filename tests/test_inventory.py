import pytest
import logging

logger = logging.getLogger()

#상품명 파라미터 라이즈 형식 유의 !! ! 
@pytest.mark.parametrize("item",[
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
    ])
def test_item_add_and_check(inventory_page,login_user, item):
    logger.info(f"ADD TO AND REMOVE ITEM: {item}")
    driver, wait = login_user
    
    assert inventory_page.item_add(item) is True, "TEST FAILED : EMPTY CART!!" 
    logger.info(f"[SUCCESS] ADD TO CART AND CHECK")
    
    assert inventory_page.item_detail(item) is True, "TEST FAILED : NOT MATCH ITEM!!"
    logger.info(f"[SUCCESS] MOVE TO ITEM DETAIL PAGE")
    
    
