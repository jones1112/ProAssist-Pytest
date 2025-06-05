import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.helpers import wait_for_element, wait_for_clickable, save_screenshot
from utils.logger import logger


@pytest.mark.usefixtures("init", "login")
class TestChecklist:

    def test_create_checklist(self):
        self.driver.refresh()
        wait_for_clickable(self.driver, By.XPATH, "//div[@id='cy-checklist-header']").click()
        wait_for_element(self.driver, By.CSS_SELECTOR, "input.MuiInputBase-input").send_keys("Automated checklist by JoneS 20th may")
        wait_for_element(self.driver, By.XPATH, '//input[@name="tags"]').send_keys("jones", Keys.SPACE)
        wait_for_element(self.driver, By.NAME, "description").send_keys("This checklist is automated in Python using Selenium")

        wait_for_clickable(self.driver, By.XPATH, '//button[@data-cy="cy-checklist-addfile"]').click()
        wait_for_clickable(self.driver, By.XPATH, '//div[@data-cy="cy-choice-button"]').click()
        wait_for_clickable(self.driver, By.XPATH, "//span[contains(@data-cy,'cy-Multiple answers')]").click()

        wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-add-option-button')]").click()
        wait_for_element(self.driver, By.NAME, "tasks[0].description").send_keys("Which bike do you have?")
        wait_for_element(self.driver, By.XPATH, '//input[@name="tasks[0].choices[0]"]').send_keys("Pulsar")
        wait_for_element(self.driver, By.XPATH, '//input[@name="tasks[0].choices[1]"]').send_keys("Hunter")

        wait_for_clickable(self.driver, By.XPATH, '//span[@data-cy="cy-checklist-add-task-copy-button"]').click()

        desc_input = wait_for_element(self.driver, By.XPATH, "//input[@name='tasks[1].description']")
        desc_input.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        desc_input.send_keys("jones")
        wait_for_clickable(self.driver, By.XPATH, "//div[@data-cy='cy-task-card'][2]//span[2][@data-cy='cy-checklist-add-task-delete-button']").click()

        wait_for_clickable(self.driver, By.XPATH, '//button[@data-cy="cy-checklist-submit"]').click()
        name = wait_for_element(self.driver, By.CSS_SELECTOR, "input.MuiInputBase-input").get_attribute('value')
        logger.info("Checklist created: %s", name)
        save_screenshot(self.driver, "checklist_createdjonnnnnnnnnessss")
