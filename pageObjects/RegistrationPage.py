from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    Allow_location = (
        By.XPATH,
        "//button[normalize-space()='Allow']"
    )

    login_buttons = [
        (
            By.XPATH,
            "// button[@ aria-label='User account']")
    ]

    mobile_input = (
        By.XPATH,
        "//input[@placeholder='Enter Mobile Number']"
    )

    continue_button = (
        By.XPATH,
        "//*[name()='button' and contains(@class,'w-full py-')]"
    )

    otp_inputs = (
        By.XPATH,
        "//*[name()='div' and contains(@class,'flex items')]//*[name()='input' and contains(@class,'disabled:c')]"
    )

    full_name_input = (
        By.XPATH,
        "//input[@placeholder='Full Name*']"
    )

    male_button = (
        By.XPATH,
        "//button[normalize-space()='male']"
    )

    female_button = (
        By.XPATH,
        "//button[normalize-space()='female']"
    )

    other_button = (
        By.XPATH,
        "//button[normalize-space()='other']"
    )

    invite_code_input = (
        By.XPATH,
        "//input[@placeholder='Invite Code (optional)']"
    )

    continue_button = (
        By.XPATH,
        "//button[normalize-space()='Continue']"
    )

    # =================================================
    # LOCATION POPUP
    # =================================================

    def handle_location_popup(self):

        try:

            deny = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.element_to_be_clickable(
                    self.Allow_location
                )
            )

            deny.click()

            print("Location popup handled successfully.")

        except TimeoutException:

            print("Location popup not displayed. Continuing...")

    # =================================================
    # OPEN LOGIN / REGISTRATION
    # =================================================

    def open_login_popup(self):

        for locator in self.login_buttons:

            try:

                element = WebDriverWait(
                    self.driver,
                    3
                ).until(
                    EC.element_to_be_clickable(locator)
                )

                if element.is_displayed():
                    self.driver.execute_script(
                        "arguments[0].click();",
                        element
                    )

                    print("Login/Profile button clicked.")

                    return

            except Exception:
                continue

        # Diagnostic information
        print("\nCould not automatically find Login/Profile button.")
        print("Available buttons on page:")

        buttons = self.driver.find_elements(
            By.TAG_NAME,
            "button"
        )

        for index, button in enumerate(buttons):

            try:

                print(
                    index,
                    "| text=",
                    button.text,
                    "| aria-label=",
                    button.get_attribute("aria-label"),
                    "| title=",
                    button.get_attribute("title")
                )

            except Exception:
                pass

        self.driver.save_screenshot(
            "Screenshots/login_button_not_found.png"
        )

        raise Exception(
            "Could not find LUZO Login/Profile button. "
            "Check Screenshots/login_button_not_found.png"
        )

    # =================================================
    # MOBILE NUMBER
    # =================================================

    def enter_mobile_number(self, mobile):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.mobile_input
            )
        )

        element.clear()

        element.send_keys(mobile)

        print("Mobile number entered successfully.")

    # =================================================
    # CONTINUE
    # =================================================

    def click_continue(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.continue_button
            )
        )

        button.click()

        print("Continue button clicked.")

    # =================================================
    # OTP
    # =================================================

    def enter_otp(self, otp):

        otp_inputs = self.wait.until(
            EC.presence_of_all_elements_located(
                self.otp_inputs
            )
        )

        print("OTP fields found:", len(otp_inputs))

        if not otp_inputs:
            raise Exception("OTP input field not found")

        first_otp_field = self.wait.until(
            EC.visibility_of(otp_inputs[0])
        )

        first_otp_field.click()
        first_otp_field.clear()
        first_otp_field.send_keys(str(otp))

        print("OTP entered successfully:", otp)

    # =================================================
    # FULL NAME
    # =================================================

    def enter_full_name(self, name):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.full_name_input
            )
        )

        element.clear()

        element.send_keys(name)

    # =================================================
    # GENDER
    # =================================================

    def select_male(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.male_button
            )
        ).click()

    def select_female(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.female_button
            )
        ).click()

    def select_other(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.other_button
            )
        ).click()

    # =================================================
    # INVITE CODE
    # =================================================

    def enter_invite_code(self, code):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.invite_code_input
            )
        )

        element.clear()

        element.send_keys(code)

    # =================================================
    # CONTINUE Button
    # =================================================

    def click_continue(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.continue_button
            )
        )

        button.click()

        print("Continue button clicked.")