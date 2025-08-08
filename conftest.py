import os
import time
import pytest
import configparser
from selenium import webdriver
from utils.logger import setup_logger
from utils.helpers import save_screenshot

logger = setup_logger()

# Load config.ini
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "config", "config.ini")
config.read(config_path)

@pytest.fixture(scope="class")
def init(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(config.get("credentials", "url"))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.refresh()

    request.cls.driver = driver
    logger.info("Chrome browser launched and navigated to login page.")

    yield
    time.sleep(2)
    driver.quit()
    logger.info("Browser session ended.")

# Save screenshot on failure only
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            test_name = item.name.replace(" ", "_")
            save_screenshot(driver, f"FAILED_{test_name}")


@pytest.fixture
def login(request):
    driver = request.cls.driver
    from utils.helpers import wait_for_element
    wait_for_element(driver, "id", "emailField").send_keys(config.get("credentials", "username"))
    wait_for_element(driver, "id", "passwordField").send_keys(config.get("credentials", "password"))
    wait_for_element(driver, "xpath", "//button[contains(@data-cy,'Signin_signinBox')]").click()
    time.sleep(2)
