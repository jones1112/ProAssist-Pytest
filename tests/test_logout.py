import os
import time
from configparser import ConfigParser
import pytest
from utils.helpers import save_screenshot
from utils.logger import logger
from Pages.logout_page import LogoutPage

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(project_root, 'config', 'config.ini')
config = ConfigParser()
config.read(config_path)

@pytest.mark.usefixtures("init", "login")
class TestLogout:

    def test_logout(self):
        logout_page = LogoutPage(self.driver)
        logout_page.perform_logout()

        logger.info("User logged out successfully.")
        time.sleep(2)
        save_screenshot(self.driver, "log-out successful", "Screenshots")