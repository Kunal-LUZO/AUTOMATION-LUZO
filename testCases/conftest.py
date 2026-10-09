"""
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@pytest.fixture()
def setup(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        raise Exception("Invalid browser")

    driver.maximize_window()

    yield driver

    driver.quit()

"""

import pytest
from selenium import webdriver


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


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