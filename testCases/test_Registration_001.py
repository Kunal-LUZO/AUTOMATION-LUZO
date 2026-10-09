import pytest
import time

from pageObjects.RegistrationPage import RegistrationPage
from utilities.ReadProperties import ReadConfig


@pytest.mark.smoke
def test_luzo_registration(setup):

    driver = setup

    driver.get(
        ReadConfig.get_base_url()
    )

    driver.maximize_window()

    registration = RegistrationPage(driver)

    registration.handle_location_popup()
    time.sleep(3)

    registration.open_login_popup()
    time.sleep(3)

    time.sleep(3)
    registration.enter_mobile_number(
        "8108269082"
    )

    time.sleep(3)
    registration.click_continue()

    time.sleep(3)
    registration.enter_otp(
        "140118"
    )
    time.sleep(5)

    registration.enter_full_name(
        "Kunal Automation"
    )

    time.sleep(2)

    registration.select_male()
    registration.select_female()
    registration.select_other()

    time.sleep(2)

    registration.click_continue()

    time.sleep(2)

    print("LUZO registration flow completed successfully.")