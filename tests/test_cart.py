# ❌ Not this:
# @retry_on_failure
# def test_add_to_cart(driver):

# ✅ Do this:
import pytest
from utils.retry import retry_on_failure

def test_add_to_cart(driver):
    @retry_on_failure(retries=2)
    def add_to_cart_logic():
        from pages.login_page import LoginPage
        from pages.inventory_page import InventoryPage
        from utils.config_reader import read_config
        from utils.logger import get_logger

        log = get_logger()
        config = read_config()

        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        login.load(config['base_url'])
        login.login(config['username'], config['password'])

        inventory.add_first_item_to_cart()
        assert inventory.get_cart_badge_text() == "1"
        log.info("Cart test passed")

    add_to_cart_logic()
