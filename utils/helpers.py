import os
from datetime import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by, value, timeout=10, condition="visible"):
    if condition == "visible":
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
    elif condition == "clickable":
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
    else:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

def wait_for_clickable(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )

# def save_screenshot(driver, path):
#     driver.save_screenshot(path)


def save_screenshot(driver, filename="screenshot.png", folder="Error Screenshots"):
    # Define absolute or relative path
    path = os.path.join(os.getcwd(), folder)
    os.makedirs(path, exist_ok=True)

    # Timestamp to avoid overwrites
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_path = os.path.join(path, f"{timestamp}_{filename}.png")

    driver.save_screenshot(full_path)
    print(f"Screenshot saved to {full_path}")