from utils.helpers import wait_for_element

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator, timeout=10):
        """Wait for element to be clickable and click it"""
        element = wait_for_element(self.driver, by, locator, timeout=timeout, condition="clickable")
        element.click()

    def send_text(self, by, locator, value, timeout=10):
        """Wait for element to be visible, clear existing text, and send input"""
        element = wait_for_element(self.driver, by, locator, timeout=timeout, condition="visible")
        element.clear()
        element.send_keys(value)

    def get_text(self, by, locator, timeout=10):
        """Wait for element to be visible and return its text"""
        element = wait_for_element(self.driver, by, locator, timeout=timeout, condition="visible")
        return element.text
