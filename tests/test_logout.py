import os
from configparser import ConfigParser
import pytest
from selenium.webdriver.common.by import By
from utils.helpers import wait_for_clickable, save_screenshot
from utils.logger import logger


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(project_root, 'config', 'config.ini')
config = ConfigParser()
config.read(config_path)

@pytest.mark.usefixtures("init", "login")
class TestLogout:

    def test_logout(self):
        self.driver.refresh()
        wait_for_clickable(self.driver, By.XPATH, "//div[contains(@data-cy,'profile_avatar')]").click()
        wait_for_clickable(self.driver, By.XPATH, "//div[text()='Logout']").click()
        wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-popup-confirm')]").click()
        logger.info("User logged out successfully.")
        save_screenshot(self.driver, "logout_successnew")
