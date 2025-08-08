<<<<<<< HEAD
import pytest
from Pages.job_page import JobPage
from utils.helpers import save_screenshot
from utils.logger import logger

=======
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils.helpers import wait_for_element, wait_for_clickable, save_screenshot
from utils.logger import logger


>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264
@pytest.mark.usefixtures("init", "login")
class TestJob:

    def test_create_job(self):
<<<<<<< HEAD
        job_page = JobPage(self.driver)

        checklist_name = "Automated checklist by JoneS"
        title = "RE Hunter quarterly service"
        tags = ["bike", "service"]
        description = "This is the report of quarterly service of your 2-wheeler"
        scheduled_date = "292025"
        cutoff_date = "11122025"
        assignee = "Jones Leo"
        supervisor = "Prod JoneS"

        job_page.create_job(
            checklist_name=checklist_name,
            title=title,
            tags=tags,
            description=description,
            scheduled_date=scheduled_date,
            cutoff_date=cutoff_date,
            assignee=assignee,
            supervisor=supervisor
        )

        job_name = job_page.get_created_job_title()
        logger.info("Job created: %s", job_name)
        save_screenshot(self.driver, "job_created","Error Screenshots")

        assert title in job_name
=======
        self.driver.refresh()
        wait_for_clickable(self.driver, By.XPATH, "//div[@id='cy-jobs-header']").click()
        wait_for_clickable(self.driver, By.XPATH, "//span[contains(@class,'w-fit')]").click()
        wait_for_clickable(self.driver, By.XPATH, "//*[text()='Automated checklist by JoneS']").click()

        wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Title')]").send_keys("RE Hunter quarterly service")
        tag_input = wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Add tags')]")
        for tag in ["bike", "service"]:
            tag_input.send_keys(tag, Keys.ENTER)

        wait_for_element(self.driver, By.XPATH, "//textarea[contains(@placeholder,'Description')]").send_keys(
            "This is the report of quarterly service of your 2-wheeler")

        wait_for_clickable(self.driver, By.ID, "checklist-select-standard").click()
        wait_for_clickable(self.driver, By.XPATH, "//li[contains(@data-cy,'cy-workorder-priority-high')]").click()

        wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Scheduled')]").send_keys("292025", Keys.ARROW_RIGHT, "1234", Keys.ARROW_RIGHT, "1")
        wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Cutoff At')]").send_keys("11122025", Keys.ARROW_RIGHT, "1234", Keys.ARROW_RIGHT, "2")

        wait_for_clickable(self.driver, By.XPATH, "//div[@data-cy='cy-workorder-assign-dropdown']//div[@id='checklist-select-standard']").click()
        assignee = wait_for_element(self.driver, By.XPATH, "//*[text()='Jones Leo']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", assignee)
        assignee.click()

        wait_for_clickable(self.driver, By.ID, "demo-multiple-chip").click()
        supervisor = wait_for_element(self.driver, By.XPATH, "//*[text()='Prod JoneS']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", supervisor)
        supervisor.click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-workorder-create-button')]").click()
        time.sleep(2)
        job_name = wait_for_element(self.driver, By.XPATH, "//div/p[2][@data-cy='cy-workorder-view-title-value']").text
        logger.info("Job created: %s", job_name)
        save_screenshot(self.driver, "job_created")
>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264
