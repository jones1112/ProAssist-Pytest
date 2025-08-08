from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element

class LogoutPage:

    def __init__(self, driver):
        self.driver = driver

    def perform_logout(self):
        self.driver.refresh()
        wait_for_element(self.driver, By.XPATH, "//div[contains(@data-cy,'profile_avatar')]").click()
        wait_for_element(self.driver, By.XPATH, "//div[text()='Logout']").click()
        wait_for_element(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-popup-confirm')]").click()
