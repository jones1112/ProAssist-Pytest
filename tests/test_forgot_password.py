import pytest
from configparser import ConfigParser
import os
import time
from Pages.forgot_password_page import ForgotPasswordPage
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
        forgot_page.enter_email_and_submit(config.get("credentials", "forgot_email"))
        time.sleep(1)
        toast_message = forgot_page.get_toast_message()
        logger.info("Toast message: %s", toast_message)
        assert "Email sent successfully" in toast_message
