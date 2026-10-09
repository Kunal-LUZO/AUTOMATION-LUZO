import pytest
import time

from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig


@pytest.mark.smoke
def test_luzo_login(setup):

    driver = setup

    # -----------------------------------------
    # Step 1 : Open LUZO
    # -----------------------------------------

    driver.get(
        ReadConfig.get_base_url()
    )

    driver.maximize_window()

    login = LoginPage(driver)

    # -----------------------------------------
    # Step 2 : Handle location popup
    # -----------------------------------------

    login.handle_location_popup()
    time.sleep(3)
    # -----------------------------------------
    # Step 3 : Open Login / login popup
    # -----------------------------------------

    login.open_login_popup()
    time.sleep(3)
    # -----------------------------------------
    # Step 4 : Enter mobile number
    # -----------------------------------------
    time.sleep(3)
    login.enter_mobile_number(
        "8108269082"
    )

    # -----------------------------------------
    # Step 5 :Click Continue
    # -----------------------------------------
    time.sleep(3)
    login.click_continue()

    time.sleep(3)

    # -----------------------------------------
    # Step 6 : Enter 6 digit OTP
    # -----------------------------------------
    login.enter_otp(
        "140118"
    )
    time.sleep(5)



    print(
        "LUZO Login flow completed successfully."
    )