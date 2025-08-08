<<<<<<< HEAD
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
=======
import os
import time
import pytest
from configparser import ConfigParser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils.helpers import wait_for_element, wait_for_clickable, save_screenshot
from utils.logger import logger

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(project_root, 'config', 'config.ini')
config = ConfigParser()
config.read(config_path)


@pytest.mark.usefixtures("init")
class TestLogin:

    def test_wrong_email_wrong_password(self):
        email = config.get("basic info", "username")
        self.enter_credentials(email, "wrong")
        self.click_signin()

        error = self.get_error_message()
        assert error == "Incorrect email or password", f"Unexpected error: {error}"
        save_screenshot(self.driver, "Error Screenshots/Login.png")

    def test_wrong_email_valid_password(self):
        self.enter_credentials("invalid@yopmail.com", "Jones@123")
        self.click_signin()

        error = self.get_error_message()
        assert error == "Incorrect email or password", f"Unexpected error: {error}"
        save_screenshot(self.driver, "Error Screenshots/login_error_two.png")

    def test_valid_email_valid_password(self):
        self.enter_credentials("jonesp@yopmail.com", "Jones@123")
        self.click_signin()

        WebDriverWait(self.driver, 10).until(EC.url_changes(self.driver.current_url))
        time.sleep(2)
        assert "dashboard" in self.driver.current_url or self.driver.current_url != config.get("basic info", "url"), "Login failed or wrong page"
        logger.info("User logged in successfully.")
        save_screenshot(self.driver, "Error Screenshots/valid_login.png")


    def enter_credentials(self, email, password):
        wait_for_element(self.driver, By.ID, "emailField", condition="visible").clear()
        wait_for_element(self.driver, By.ID, "emailField", condition="visible").send_keys(email)
        wait_for_element(self.driver, By.ID, "passwordField", condition="visible").clear()
        wait_for_element(self.driver, By.ID, "passwordField", condition="visible").send_keys(password)

    def click_signin(self):
        wait_for_element(self.driver, By.XPATH, "//button[contains(@data-cy,'Signin_signinBox')]", condition="clickable").click()

    def get_error_message(self):
        return wait_for_element(self.driver, By.XPATH, "//p[contains(@data-cy,'cy-passwordField-error')]", condition="visible").text

>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264
