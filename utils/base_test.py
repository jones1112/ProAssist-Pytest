from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import wait_for_element, wait_for_clickable

class BaseTest:
    def send_text(self, by, locator, value):
        wait_for_element(self.driver, by, locator).send_keys(value)

    def click(self, by, locator):
        wait_for_clickable(self.driver, by, locator).click()

    def wait_for_element(driver, by, value, timeout=45, condition="visible"):
        if condition == "visible":
            return WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        elif condition == "clickable":
            return WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
        else:
            return WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )

