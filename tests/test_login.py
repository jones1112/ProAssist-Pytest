import time
import pytest
from Pages.login_page import LoginPage
from conftest import config

@pytest.mark.usefixtures("init")
class TestLogin:
    def setup_method(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.login_page = LoginPage(self.driver)
        self.valid_email = config.get("credentials", "username")
        self.valid_password = config.get("credentials", "password")
        self.invalid_email = config.get("credentials", "wrong_email")

    def test_wrong_email_wrong_password(self):
        self.login_page.enter_credentials("wrong@wrong.com", "wrongpass")
        self.login_page.click_signin()
        assert "Incorrect" in self.login_page.get_error_message()

    def test_wrong_email_valid_password(self):
        self.login_page.enter_credentials(self.invalid_email, self.valid_password)
        self.login_page.click_signin()
        assert "Incorrect" in self.login_page.get_error_message()

    def test_valid_email_valid_password(self):
        self.login_page.enter_credentials(self.valid_email, self.valid_password)
        self.login_page.click_signin()
        time.sleep(2)
        assert "Dashboard" in self.driver.page_source or "dashboard" in self.driver.page_source

