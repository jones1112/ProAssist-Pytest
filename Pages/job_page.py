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
        time.sleep(3)
        wait_for_element(self.driver, By.XPATH, "//div[@id='cy-jobs-header']").click()
        wait_for_element(self.driver, By.XPATH, "//span[contains(@class,'w-fit')]").click()
        wait_for_element(self.driver, By.XPATH, f"//*[text()='{checklist_name}']").click()

        wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Title')]").send_keys(title)

        tag_input = wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Add tags')]")
        for tag in tags:
            tag_input.send_keys(tag, Keys.ENTER)

        wait_for_element(self.driver, By.XPATH, "//textarea[contains(@placeholder,'Description')]").send_keys(description)

        wait_for_element(self.driver, By.ID, "checklist-select-standard").click()
        wait_for_element(self.driver, By.XPATH, "//li[contains(@data-cy,'cy-workorder-priority-high')]").click()

        wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Scheduled')]").send_keys(scheduled_date, Keys.ARROW_RIGHT, "1234", Keys.ARROW_RIGHT, "1")
        wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Cutoff At')]").send_keys(cutoff_date, Keys.ARROW_RIGHT, "1234", Keys.ARROW_RIGHT, "2")

        wait_for_element(self.driver, By.XPATH, "//div[@data-cy='cy-workorder-assign-dropdown']//div[@id='checklist-select-standard']").click()
        assignee_el = wait_for_element(self.driver, By.XPATH, f"//*[text()='{assignee}']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", assignee_el)
        assignee_el.click()

        wait_for_element(self.driver, By.ID, "demo-multiple-chip").click()
        supervisor_el = wait_for_element(self.driver, By.XPATH, f"//*[text()='{supervisor}']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", supervisor_el)
        supervisor_el.click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        wait_for_element(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-workorder-create-button')]").click()
        time.sleep(2)

    def get_created_job_title(self):
        return wait_for_element(self.driver, By.XPATH, "//div/p[2][@data-cy='cy-workorder-view-title-value']").text
