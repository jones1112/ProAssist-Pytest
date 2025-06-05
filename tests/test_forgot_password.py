import os
import time
import pytest
from selenium.webdriver.common.by import By
from configparser import ConfigParser
from utils.helpers import wait_for_element, wait_for_clickable, save_screenshot
from utils.logger import logger


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(project_root, 'config', 'config.ini')
config = ConfigParser()
config.read(config_path)

@pytest.mark.usefixtures("init")
class TestForgotPassword:

    def test_forgot_password(self):
        wait_for_clickable(self.driver, By.XPATH, "//p[contains(@data-cy,'forgot_password')]").click()
        time.sleep(2)
        wait_for_element(self.driver, By.ID, "forget-password-emailField").send_keys(config.get("basic info", "forgot_email"))
        wait_for_clickable(self.driver, By.XPATH, "//button[text()='Send']").click()
        toast = wait_for_element(self.driver, By.XPATH, "//div[contains(@class,'MuiSnackbarContent-message')]")
        logger.info("Toast message received: %s", toast.text)
        assert "Email sent successfully" in toast.text
        save_screenshot(self.driver, "forgot_password_new")
