import os
from datetime import datetime
<<<<<<< HEAD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

def wait_for_element(driver, by, value, timeout=15, condition="visible"):
    wait = WebDriverWait(driver, timeout)
    if condition == "clickable":
        return wait.until(EC.element_to_be_clickable((by, value)))
    elif condition == "visible":
        return wait.until(EC.visibility_of_element_located((by, value)))
    elif condition == "present":
        return wait.until(EC.presence_of_element_located((by, value)))
    else:
        raise ValueError(f"Unsupported wait condition: {condition}")

def save_screenshot(driver, filename="screenshot", folder="Screenshots"):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    path = os.path.join(project_root, folder)
    os.makedirs(path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_path = os.path.join(path, f"{timestamp}_{filename}.png")

    try:
        driver.save_screenshot(full_path)
        logger.info(f"[Saved] Screenshot → {full_path}")
    except Exception as e:
        logger.error(f"Screenshot capture failed: {str(e)}")
=======

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
>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264
