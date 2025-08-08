import os
<<<<<<< HEAD
import time
from configparser import ConfigParser
import pytest
from utils.helpers import save_screenshot
from utils.logger import logger
from Pages.logout_page import LogoutPage
=======
from configparser import ConfigParser
import pytest
from selenium.webdriver.common.by import By
from utils.helpers import wait_for_clickable, save_screenshot
from utils.logger import logger

>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(project_root, 'config', 'config.ini')
config = ConfigParser()
config.read(config_path)

@pytest.mark.usefixtures("init", "login")
class TestLogout:

    def test_logout(self):
<<<<<<< HEAD
        logout_page = LogoutPage(self.driver)
        logout_page.perform_logout()

        logger.info("User logged out successfully.")
        time.sleep(2)
        save_screenshot(self.driver, "log-out successful", "Screenshots")
=======
        self.driver.refresh()
        wait_for_clickable(self.driver, By.XPATH, "//div[contains(@data-cy,'profile_avatar')]").click()
        wait_for_clickable(self.driver, By.XPATH, "//div[text()='Logout']").click()
        wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-popup-confirm')]").click()
        logger.info("User logged out successfully.")
        save_screenshot(self.driver, "logout_successnew")
>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264
