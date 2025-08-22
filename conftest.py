import os
import time
import configparser
import pytest
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_html

from utils.logger import setup_logger
from utils.helpers import  wait_for_element

logger = setup_logger()

# Load config.ini
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "config", "config.ini")
config.read(config_path)


@pytest.fixture(scope="class")
def init(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(config.get("credentials", "base_url"))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.refresh()

    # attach driver to test class
    request.cls.driver = driver
    logger.info("Chrome browser launched and navigated to login page.")

    yield driver   # ✅ return driver so funcargs.get("init") works

    time.sleep(2)
    driver.quit()
    logger.info("Browser session ended.")


# attach screenshots on failure (HTML only) ----
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("init")  # ✅ now this will give driver
        if driver:
            # Take screenshot as raw bytes (no file saved)
            png_bytes = driver.get_screenshot_as_png()
            encoded_img = base64.b64encode(png_bytes).decode("utf-8")

            # Embed screenshot into HTML report
            extra = getattr(rep, "extra", [])
            html = (
                f'<div><img src="data:image/png;base64,{encoded_img}" '
                f'alt="screenshot" style="width:400px;height:300px;" '
                f'onclick="window.open(this.src)" /></div>'
            )
            extra.append(pytest_html.extras.html(html))
            rep.extra = extra


@pytest.fixture
def login(request):
    """Perform login with valid credentials from config.ini."""
    driver = request.cls.driver

    wait_for_element(driver, By.ID, "emailField").send_keys(config.get("credentials", "username"))
    wait_for_element(driver, By.ID, "passwordField").send_keys(config.get("credentials", "password"))
    wait_for_element(driver, By.XPATH, "//button[contains(@data-cy,'Signin_signinBox')]").click()

    time.sleep(2)
