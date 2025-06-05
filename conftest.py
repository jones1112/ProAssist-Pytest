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

@pytest.fixture
def login(request):
    driver = request.cls.driver
    driver.get("https://proassist.tesseract.in/signin?returnUrl=%2F")
    from utils.helpers import wait_for_element, wait_for_clickable
    wait_for_element(driver, "id", "emailField").send_keys(config.get("basic info", "username"))
    wait_for_element(driver, "id", "passwordField").send_keys(config.get("basic info", "password"))
    wait_for_clickable(driver, "xpath", "//button[contains(@data-cy,'Signin_signinBox')]").click()
    time.sleep(2)
