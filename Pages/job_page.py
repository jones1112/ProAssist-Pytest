import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.helpers import wait_for_element


class JobPage:
    def __init__(self, driver):
        self.driver = driver

    def create_job(self, checklist_name, title, tags, description, scheduled_date, cutoff_date, assignee, supervisor):
        self.driver.refresh()
        time.sleep(2)

        wait_for_element(self.driver, By.XPATH, "//div[@id='cy-jobs-header']", condition="clickable").click()
        wait_for_element(self.driver, By.XPATH, "//span[contains(@class,'w-fit')]", condition="clickable").click()
        wait_for_element(self.driver, By.XPATH, f"//*[text()='{checklist_name}']", condition="clickable").click()

        wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Title')]", condition="visible").send_keys(title)

        tag_input = wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Add tags')]", condition="visible")
        for tag in tags:
            tag_input.send_keys(tag, Keys.ENTER)

        wait_for_element(self.driver, By.XPATH, "//textarea[contains(@placeholder,'Description')]", condition="visible").send_keys(description)

        wait_for_element(self.driver, By.ID, "checklist-select-standard", condition="clickable").click()
        wait_for_element(self.driver, By.XPATH, "//li[contains(@data-cy,'cy-workorder-priority-high')]", condition="clickable").click()

        wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Scheduled')]", condition="visible").send_keys(
            scheduled_date, Keys.ARROW_RIGHT, "1234", Keys.ARROW_RIGHT, "1"
        )
        wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Cutoff At')]", condition="visible").send_keys(
            cutoff_date, Keys.ARROW_RIGHT, "1234", Keys.ARROW_RIGHT, "2"
        )

        wait_for_element(self.driver, By.XPATH, "//div[@data-cy='cy-workorder-assign-dropdown']//div[@id='checklist-select-standard']", condition="clickable").click()
        assignee_el = wait_for_element(self.driver, By.XPATH, f"//*[text()='{assignee}']", condition="visible")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", assignee_el)
        assignee_el.click()

        wait_for_element(self.driver, By.ID, "demo-multiple-chip", condition="clickable").click()
        supervisor_el = wait_for_element(self.driver, By.XPATH, f"//*[text()='{supervisor}']", condition="visible")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", supervisor_el)
        supervisor_el.click()

        time.sleep(0.5)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        wait_for_element(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-workorder-create-button')]", condition="clickable").click()
        time.sleep(1)

    def get_created_job_title(self):
        return wait_for_element(self.driver, By.XPATH, "//div/p[2][@data-cy='cy-workorder-view-title-value']", condition="visible").text
