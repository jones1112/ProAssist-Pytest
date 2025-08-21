import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger
from selenium.common.exceptions import StaleElementReferenceException

def _normalize_by(by):
    """Accept either selenium By.* or a string like 'id', 'xpath'."""
    if isinstance(by, str):
        key = by.strip().lower()
        mapping = {
            "id": By.ID,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "css_selector": By.CSS_SELECTOR,
            "name": By.NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "tag": By.TAG_NAME,
            "tag_name": By.TAG_NAME,
            "class": By.CLASS_NAME,
            "class_name": By.CLASS_NAME,
        }
        if key not in mapping:
            raise ValueError(f"Unsupported locator string: {by}")
        return mapping[key]
    return by


def wait_for_element(driver, by, locator, condition="visible", timeout=15):
    wait = WebDriverWait(driver, timeout, ignored_exceptions=[StaleElementReferenceException])

    if condition == "clickable":
        return wait.until(EC.element_to_be_clickable((by, locator)))
    elif condition == "present":
        return wait.until(EC.presence_of_element_located((by, locator)))
    else:  # default visible
        return wait.until(EC.visibility_of_element_located((by, locator)))


def save_screenshot(driver, filename="screenshot", folder="Screenshots"):
    """Save a screenshot under project_root/<folder>/<timestamp>_<filename>.png"""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(project_root, folder)
    os.makedirs(path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_path = os.path.join(path, f"{timestamp}_{filename}.png")

    try:
        driver.save_screenshot(full_path)
        logger.info(f"[Saved] Screenshot → {full_path}")
        return full_path
    except Exception as e:
        logger.error(f"Screenshot capture failed: {e}")
        return None
