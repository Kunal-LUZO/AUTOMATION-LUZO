import os
from datetime import datetime
import pytest
from selenium import webdriver


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup")

        if driver:

            os.makedirs("Screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_path = (
                f"Screenshots/{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_path)


@pytest.fixture()
def setup(request):

    browser = request.config.getoption("--browser")

    # ==========================================
    # CHROME
    # ==========================================

    if browser == "chrome":

        options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(
            options=options
        )

        # --------------------------------------
        # GRANT LOCATION PERMISSION
        # --------------------------------------

        driver.execute_cdp_cmd(
            "Browser.grantPermissions",
            {
                "origin": "https://ts1.luzo.app",
                "permissions": [
                    "geolocation"
                ]
            }
        )

        # --------------------------------------
        # SET TEST LOCATION
        # --------------------------------------

        driver.execute_cdp_cmd(
            "Emulation.setGeolocationOverride",
            {
                "latitude": 19.0760,
                "longitude": 72.8777,
                "accuracy": 100
            }
        )

    # ==========================================
    # FIREFOX
    # ==========================================

    elif browser == "firefox":

        driver = webdriver.Firefox()

    # ==========================================
    # EDGE
    # ==========================================

    elif browser == "edge":

        options = webdriver.EdgeOptions()

        driver = webdriver.Edge(
            options=options
        )

        driver.execute_cdp_cmd(
            "Browser.grantPermissions",
            {
                "origin": "https://ts1.luzo.app",
                "permissions": [
                    "geolocation"
                ]
            }
        )

    else:

        raise Exception(
            "Invalid browser"
        )

    # ==========================================
    # MAXIMIZE
    # ==========================================

    driver.maximize_window()

    yield driver

    driver.quit()