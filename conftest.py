<<<<<<< HEAD
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

=======
import time
import pytest
from selenium import webdriver
from tests.test_logout import config


@pytest.fixture()
def init(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get("https://proassist.tesseract.in/signin?returnUrl=%2F")
    driver.implicitly_wait(11)
    driver.maximize_window()
    driver.refresh()
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.quit()
>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264

@pytest.fixture
def login(request):
    driver = request.cls.driver
<<<<<<< HEAD
    from utils.helpers import wait_for_element
    wait_for_element(driver, "id", "emailField").send_keys(config.get("credentials", "username"))
    wait_for_element(driver, "id", "passwordField").send_keys(config.get("credentials", "password"))
    wait_for_element(driver, "xpath", "//button[contains(@data-cy,'Signin_signinBox')]").click()
=======
    driver.get("https://proassist.tesseract.in/signin?returnUrl=%2F")
    from utils.helpers import wait_for_element, wait_for_clickable
    wait_for_element(driver, "id", "emailField").send_keys(config.get("basic info", "username"))
    wait_for_element(driver, "id", "passwordField").send_keys(config.get("basic info", "password"))
    wait_for_clickable(driver, "xpath", "//button[contains(@data-cy,'Signin_signinBox')]").click()
>>>>>>> 06fde88e9d1ae37932d725e777849659cf491264
    time.sleep(2)
