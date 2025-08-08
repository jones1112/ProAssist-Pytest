import os
from datetime import datetime
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
