from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until_clickable(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, locator))
    )

def wait_until_visible(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, locator))
    )
