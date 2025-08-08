from utils.helpers import wait_for_element

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def send_text(self, by, locator, value, timeout=10):
        element = wait_for_element(self.driver, by, locator, timeout, condition="visible")
        element.clear()
        element.send_keys(value)

    def click(self, by, locator, timeout=10):
        element = wait_for_element(self.driver, by, locator, timeout, condition="clickable")
        element.click()

    def get_text(self, by, locator, timeout=10):
        element = wait_for_element(self.driver, by, locator, timeout, condition="visible")
        return element.text

    def is_visible(self, by, locator, timeout=10):
        try:
            wait_for_element(self.driver, by, locator, timeout, condition="visible")
            return True
        except:
            return False

class BaseTest:
    driver = None  # Will be assigned by init fixture