from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_first_item_to_cart(self):
        self.driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()

    def get_cart_badge_text(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
