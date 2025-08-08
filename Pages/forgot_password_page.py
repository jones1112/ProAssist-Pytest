import time
from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element

class ForgotPasswordPage:

    def __init__(self, driver):
        self.driver = driver

    def click_forgot_password_link(self):
        wait_for_element(self.driver, By.XPATH, "//p[contains(@data-cy,'forgot_password')]").click()
        time.sleep(2)

    def enter_email_and_submit(self, email7):
        email_field = wait_for_element(self.driver, By.ID, "forget-password-emailField")
        email_field.send_keys(email7)
        wait_for_element(self.driver, By.XPATH, "//button[text()='Send']").click()

    def get_toast_message(self):
        toast = wait_for_element(self.driver, By.XPATH, "//div[contains(@class,'MuiSnackbarContent-message')]")
        return toast.text
