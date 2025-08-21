import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.helpers import wait_for_element
from utils.logger import logger


class ChecklistPage:
    def __init__(self, driver):
        self.driver = driver

    def create_checklist(self, title, tag, description, question, option1, option2):
        logger.info("Starting Checklist creation flow.")
        self.driver.refresh()

        wait_for_element(self.driver, By.ID, "cy-checklist-header", condition="clickable").click()

        title_input = wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Title')]", condition="visible")
        title_input.send_keys(title)
        logger.info("Entered checklist title")

        tag_input = wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Add tags')]", condition="visible")
        tag_input.send_keys(tag, Keys.ENTER)
        logger.info("Entered tag")

        desc_input = wait_for_element(self.driver, By.XPATH, "//textarea[contains(@placeholder,'Description')]", condition="visible")
        desc_input.send_keys(description)
        logger.info("Entered description")

        wait_for_element(self.driver, By.XPATH, "//button[@data-cy='cy-checklist-addfile']", condition="clickable").click()
        wait_for_element(self.driver, By.XPATH, "//div[@data-cy='cy-choice-button']", condition="clickable").click()
        time.sleep(1)
        wait_for_element(self.driver, By.XPATH, "//span[contains(@data-cy,'cy-Multiple answers')]", condition="clickable").click()

        # Add question and options
        wait_for_element(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-add-option-button')]", condition="clickable").click()
        quest_ask = wait_for_element(self.driver, By.NAME, "tasks[0].description")
        quest_ask.send_keys(question)

        opt1 = wait_for_element(self.driver, By.XPATH, "//input[@name='tasks[0].choices[0]']", condition="visible")
        opt1.send_keys(option1)

        opt2 = wait_for_element(self.driver, By.XPATH, "//input[@name='tasks[0].choices[1]']", condition="visible")
        opt2.send_keys(option2)

        # Copy & delete example task
        wait_for_element(self.driver, By.XPATH, '//span[@data-cy="cy-checklist-add-task-copy-button"]').click()
        desc_copy = wait_for_element(self.driver, By.XPATH, "//input[@name='tasks[1].description']")
        desc_copy.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        desc_copy.send_keys("jones")
        wait_for_element(
            self.driver,
            By.XPATH,
            "//div[@data-cy='cy-task-card'][2]//span[2][@data-cy='cy-checklist-add-task-delete-button']",
        ).click()

        wait_for_element(self.driver, By.XPATH, '//button[@data-cy="cy-checklist-submit"]', condition="clickable").click()

        checklist_name = wait_for_element(self.driver, By.CSS_SELECTOR, "input.MuiInputBase-input").get_attribute("value")
        logger.info(f"Checklist published: {checklist_name}")

    def get_checklist_title(self):
        title_element = wait_for_element(self.driver, By.XPATH, "//*[@data-cy='checklist_title_value']", condition="visible")
        return title_element.text
