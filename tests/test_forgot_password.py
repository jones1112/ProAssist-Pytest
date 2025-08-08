import os
import time
import pytest
from configparser import ConfigParser
from Pages.forgot_password_page import ForgotPasswordPage
from utils.helpers import save_screenshot
from utils.logger import logger

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(project_root, 'config', 'config.ini')
config = ConfigParser()
config.read(config_path)

@pytest.mark.usefixtures("init")
class TestForgotPassword:

    def test_forgot_password(self):
        forgot_page = ForgotPasswordPage(self.driver)
        forgot_page.click_forgot_password_link()
        (forgot_page.enter_email_and_submit
        (config.get("credentials", "forgot_email")))
        time.sleep(2)
        toast_message = forgot_page.get_toast_message()
        logger.info("Toast message received: %s", toast_message)
        assert "Email sent successfully" in toast_message
        save_screenshot(self.driver, "forgot_password","Screenshots")
