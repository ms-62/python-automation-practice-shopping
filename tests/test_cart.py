import pytest
import logging

logger = logging.getLogger()

@pytest.mark.parametrize("item",[
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
    ])
def test_cart_remove_check(inventory_page,cart_page,cart_setup, item):
    logger.info(f"REMOVE TO CART ITEM: {item}")
    driver, wait = cart_setup
    inventory_page.inventory_page.item_add(item)
    cart_page.remove_cart_item(item)