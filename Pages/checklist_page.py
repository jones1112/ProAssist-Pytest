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
        logger.info(f"Entered checklist title: {title}")
        tag_input = wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Add tags')]", condition="visible")
        tag_input.send_keys(tag, Keys.ENTER)
        logger.info(f"Entered tag: {tag}")
        desc_input = wait_for_element(self.driver, By.XPATH, "//textarea[contains(@placeholder,'Description')]", condition="visible")
        desc_input.send_keys(description)
        logger.info("Entered description.")
        wait_for_element(self.driver, By.XPATH, "//button[@data-cy='cy-checklist-addfile']", condition="clickable").click()
        logger.info("Clicked on Add file button.")
        wait_for_element(self.driver, By.XPATH, "//div[@data-cy='cy-choice-button']", condition="clickable").click()
        time.sleep(2)
        wait_for_element(self.driver, By.XPATH, "//span[contains(@data-cy,'cy-Multiple answers')]",condition="clickable").click()
        ques_input = wait_for_element(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-add-option-button')]", condition="visible")
        ques_input.click()
        logger.info( "Add options clicked" )
        quest_ask = wait_for_element(self.driver, By.NAME, "tasks[0].description")
        quest_ask.send_keys(question)
        logger.info("Questions entered")
        opts = wait_for_element(self.driver, By.XPATH, "//input[@name='tasks[0].choices[0]']", condition="visible")
        opts.click()
        opts.send_keys(option1)
        logger.info("option 1 entered")
        otps2 = wait_for_element(self.driver, By.XPATH, "//input[@name='tasks[0].choices[1]']", condition="visible")
        otps2.click()
        time.sleep(2)
        otps2.send_keys(option2)
        logger.info("option 2 entered")
        wait_for_element(self.driver, By.XPATH, '//span[@data-cy="cy-checklist-add-task-copy-button"]').click()
        desc_input = wait_for_element(self.driver, By.XPATH, "//input[@name='tasks[1].description']")
        desc_input.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        desc_input.send_keys("jones")
        wait_for_element(self.driver, By.XPATH,
                           "//div[@data-cy='cy-task-card'][2]//span[2][@data-cy='cy-checklist-add-task-delete-button']").click()
        print("Copied task deleted")
        wait_for_element(self.driver, By.XPATH, '//button[@data-cy="cy-checklist-submit"]').click()
        checklist_name = wait_for_element(self.driver, By.CSS_SELECTOR, "input.MuiInputBase-input").get_attribute(
            'value')
        logger.info(f"Checklist published : {checklist_name}")

    def get_checklist_title(self):
        title_element = wait_for_element(self.driver, By.XPATH, "//*[@data-cy='checklist_title_value']",
                                         condition="visible")
        title_text = title_element.text
        logger.info(f"Fetched checklist title from UI: {title_text}")
        return title_text

