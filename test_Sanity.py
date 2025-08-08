#
#
# import time
# import os
# import pytest
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from configparser import ConfigParser
#
#
# config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.ini')
# config = ConfigParser()
# config.read(config_path)
#
#
# def wait_for_element(driver, by, value, timeout=10):
#     return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
#
#
# def wait_for_clickable(driver, by, value, timeout=10):
#     return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
#
#
# @pytest.fixture
# def login(request):
#     driver = request.cls.driver
#     wait_for_element(driver, By.ID, "emailField").send_keys("jonesp@yopmail.com")
#     wait_for_element(driver, By.ID, "passwordField").send_keys("Jones@123")
#     wait_for_clickable(driver, By.XPATH, "//button[contains(@data-cy,'Signin_signinBox')]").click()
#     time.sleep(2)
#
#
# @pytest.mark.usefixtures("init")
# class TestLogin:
#
#     def test_wrong_email_wrong_password(self):
#         email = config.get("basic info", "username")
#         wait_for_element(self.driver, By.ID, "emailField").send_keys(email)
#         wait_for_element(self.driver, By.ID, "passwordField").send_keys("wrong")
#         wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'Signin_signinBox')]").click()
#         error = wait_for_element(self.driver, By.XPATH, "//p[contains(@data-cy,'cy-passwordField-error')]").text
#         assert error == "Incorrect email or password"
#         print("Login error message:", error)
#         self.driver.save_screenshot("Error Screenshots/Login.png")
#
#     def test_wrong_email_valid_password(self):
#         wait_for_element(self.driver, By.ID, "emailField").send_keys("invalid@yopmail.com")
#         wait_for_element(self.driver, By.ID, "passwordField").send_keys("Jones@123")
#         wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'Signin_signinBox')]").click()
#         error = wait_for_element(self.driver, By.XPATH, "//p[contains(@data-cy,'cy-passwordField-error')]").text
#         assert error == "Incorrect email or password"
#         print("Login error message:", error)
#         self.driver.save_screenshot("Error Screenshots/login_error_two.png")
#
#     def test_valid_email_valid_password(self):
#         wait_for_element(self.driver, By.ID, "emailField").send_keys("jonesp@yopmail.com")
#         wait_for_element(self.driver, By.ID, "passwordField").send_keys("Jones@123")
#         wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'Signin_signinBox')]").click()
#         WebDriverWait(self.driver, 10).until(EC.url_changes(self.driver.current_url))
#         print("Login successful:", self.driver.current_url)
#         self.driver.save_screenshot("Error Screenshots/valid_login.png")
#
#
# @pytest.mark.usefixtures("init", "login")
# class TestChecklist:
#
#     def test_create_checklist(self):
#         self.driver.refresh()
#         wait_for_clickable(self.driver, By.XPATH, "//div[@id='cy-checklist-header']").click()
#         time.sleep(2)
#         wait_for_element(self.driver, By.CSS_SELECTOR, "input.MuiInputBase-input").send_keys("Automated checklist by JoneS")
#         wait_for_element(self.driver, By.XPATH, '//input[@name="tags"]').send_keys("jones", Keys.SPACE)
#         wait_for_element(self.driver, By.NAME, "description").send_keys("This checklist is automated in Python using Selenium")
#
#         wait_for_clickable(self.driver, By.XPATH, '//button[@data-cy="cy-checklist-addfile"]').click()
#         wait_for_clickable(self.driver, By.XPATH, '//div[@data-cy="cy-choice-button"]').click()
#         wait_for_clickable(self.driver, By.XPATH, "//span[contains(@data-cy,'cy-Multiple answers')]").click()
#         wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-add-option-button')]").click()
#
#         wait_for_element(self.driver, By.NAME, "tasks[0].description").send_keys("Which bike do you have?")
#         wait_for_element(self.driver, By.XPATH, '//input[@name="tasks[0].choices[0]"]').send_keys("Pulsar")
#         wait_for_element(self.driver, By.XPATH, '//input[@name="tasks[0].choices[1]"]').send_keys("Hunter")
#
#         wait_for_clickable(self.driver, By.XPATH, '//span[@data-cy="cy-checklist-add-task-copy-button"]').click()
#
#         desc_input = wait_for_element(self.driver, By.XPATH, "//input[@name='tasks[1].description']")
#         desc_input.send_keys(Keys.CONTROL + "a", Keys.DELETE)
#         desc_input.send_keys("jones")
#
#         wait_for_clickable(self.driver, By.XPATH, "//div[@data-cy='cy-task-card'][2]//span[2][@data-cy='cy-checklist-add-task-delete-button']").click()
#         print("Copied task deleted")
#
#         wait_for_clickable(self.driver, By.XPATH, '//button[@data-cy="cy-checklist-submit"]').click()
#         checklist_name = wait_for_element(self.driver, By.CSS_SELECTOR, "input.MuiInputBase-input").get_attribute('value')
#         print("Created checklist:", checklist_name)
#         self.driver.save_screenshot("Error Screenshots/checklist.png")
#
#
# @pytest.mark.usefixtures("init", "login")
# class TestJob:
#
#     def test_create_job(self):
#         self.driver.refresh()
#         wait_for_clickable(self.driver, By.XPATH, "//div[@id='cy-jobs-header']").click()
#         wait_for_clickable(self.driver, By.XPATH, "//span[contains(@class,'w-fit')]").click()
#         wait_for_clickable(self.driver, By.XPATH, "//*[text()='Automated checklist by JoneS']").click()
#
#         wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Title')]").send_keys("RE Hunter quarterly service")
#         tag_input = wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Add tags')]")
#         for tag in ["bike", "service"]:
#             tag_input.send_keys(tag, Keys.ENTER)
#
#         wait_for_element(self.driver, By.XPATH, "//textarea[contains(@placeholder,'Description')]").send_keys(
#             "This is the report of quarterly service of your 2-wheeler")
#
#         wait_for_clickable(self.driver, By.ID, "checklist-select-standard").click()
#         wait_for_clickable(self.driver, By.XPATH, "//li[contains(@data-cy,'cy-workorder-priority-high')]").click()
#
#         schedule = wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Scheduled')]")
#         schedule.send_keys("292025", Keys.ARROW_RIGHT, "1234", Keys.ARROW_RIGHT, "1")
#
#         cutoff = wait_for_element(self.driver, By.XPATH, "//input[contains(@placeholder,'Cutoff At')]")
#         cutoff.send_keys("11122025", Keys.ARROW_RIGHT, "1234", Keys.ARROW_RIGHT, "2")
#
#         wait_for_clickable(self.driver, By.XPATH, "//div[@data-cy='cy-workorder-assign-dropdown']//div[@id='checklist-select-standard']").click()
#         assignee = wait_for_element(self.driver, By.XPATH, "//*[text()='Jones Leo']")
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", assignee)
#         wait_for_clickable(self.driver, By.XPATH, "//div[contains(@data-cy,'cy-workorder-user-data-Jones Leo')]").click()
#
#         jl = wait_for_element(self.driver, By.ID, "demo-multiple-chip")
#         jl.click()
#         supervisor = wait_for_element(self.driver, By.XPATH, "//*[text()='Prod JoneS']")
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", supervisor)
#         supervisor.click()
#         ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
#
#         wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-workorder-create-button')]").click()
#         job_name = wait_for_element(self.driver, By.XPATH, "//*[@id='__next']/section/section/div[2]/main/section/section/div/div/span[2]").text
#         print("Job created:", job_name)
#         self.driver.save_screenshot("Error Screenshots/Job.png")
#
#
# @pytest.mark.usefixtures("init", "login")
# class TestLogout:
#
#     def test_logout(self):
#         self.driver.refresh()
#         wait_for_clickable(self.driver, By.XPATH, "//div[contains(@data-cy,'profile_avatar')]").click()
#         wait_for_clickable(self.driver, By.XPATH, "//div[text()='Logout']").click()
#         wait_for_clickable(self.driver, By.XPATH, "//button[contains(@data-cy,'cy-popup-confirm')]").click()
#         print("Logout successful")
#
#
# @pytest.mark.usefixtures("init")
# class TestForgotPassword:
#     def test_forgot_password(self):
#         wait_for_clickable(self.driver, By.XPATH, "//p[contains(@data-cy,'forgot_password')]").click()
#         email_field = wait_for_element(self.driver, By.ID, "forget-password-emailField")
#         email_field.send_keys("jonleo@yopmail.com")
#         wait_for_clickable(self.driver, By.XPATH, "//button[text()='Send']").click()
#         time.sleep(1)
#         toast_msg = self.driver.find_element(By.XPATH, "//div[contains(@class,'MuiSnackbarContent-message')]")
#         assert "Email sent successfully" in toast_msg.text
#         print("Toast message:", toast_msg)
