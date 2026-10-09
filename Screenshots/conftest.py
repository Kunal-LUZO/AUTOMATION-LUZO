import os
from datetime import datetime

import pytest


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