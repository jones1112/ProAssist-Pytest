import os
import time
import pytest
<<<<<<< HEAD
from configparser import ConfigParser
from Pages.forgot_password_page import ForgotPasswordPage
from utils.helpers import save_screenshot
from utils.logger import logger

=======
from selenium.webdriver.common.by import By
from configparser import ConfigParser
from utils.helpers import wait_for_element, wait_for_clickable, save_screenshot
from utils.logger import logger


>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(project_root, 'config', 'config.ini')
config = ConfigParser()
config.read(config_path)

@pytest.mark.usefixtures("init")
class TestForgotPassword:

    def test_forgot_password(self):
<<<<<<< HEAD
        forgot_page = ForgotPasswordPage(self.driver)
        forgot_page.click_forgot_password_link()
        (forgot_page.enter_email_and_submit
        (config.get("credentials", "forgot_email")))
        time.sleep(2)
        toast_message = forgot_page.get_toast_message()
        logger.info("Toast message received: %s", toast_message)
        assert "Email sent successfully" in toast_message
        save_screenshot(self.driver, "forgot_password","Screenshots")
=======
        wait_for_clickable(self.driver, By.XPATH, "//p[contains(@data-cy,'forgot_password')]").click()
        time.sleep(2)
        wait_for_element(self.driver, By.ID, "forget-password-emailField").send_keys(config.get("basic info", "forgot_email"))
        wait_for_clickable(self.driver, By.XPATH, "//button[text()='Send']").click()
        toast = wait_for_element(self.driver, By.XPATH, "//div[contains(@class,'MuiSnackbarContent-message')]")
        logger.info("Toast message received: %s", toast.text)
        assert "Email sent successfully" in toast.text
        save_screenshot(self.driver, "forgot_password_new")
>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264
