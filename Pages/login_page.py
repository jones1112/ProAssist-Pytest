from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from utils.helpers import wait_for_element

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_credentials(self, email, password):
        self.send_text(By.ID, "emailField", email)
        self.send_text(By.ID, "passwordField", password)

    def click_signin(self):
        self.click(By.XPATH, "//button[contains(@data-cy,'Signin_signinBox')]")

    def get_error_message(self):
        return wait_for_element(self.driver, By.XPATH, "//p[contains(@data-cy,'cy-passwordField-error')]", condition="visible").text

