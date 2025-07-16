import os
import time

def take_screenshot(driver, name="failure"):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename
