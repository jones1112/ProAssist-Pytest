import time
import pytest
from utils.logger import logger
from Pages.logout_page import LogoutPage


@pytest.mark.usefixtures("init", "login")
class TestLogout:

    def test_logout(self):
        logout_page = LogoutPage(self.driver)
        logout_page.perform_logout()
        logger.info("User logged out successfully.")
        time.sleep(1)

