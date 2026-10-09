from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppointmentPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    BOOKING_BUTTON = (
        By.XPATH,
        "//button[contains(normalize-space(),'Book') and contains(normalize-space(),'pay')]"
    )

    def select_date(self, date):

        date_locator = (
            By.XPATH,
            f"//*[normalize-space()='{date}' or contains(normalize-space(), ' {date} ')]"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                date_locator
            )
        ).click()

    def select_time(self, time):

        time_locator = (
            By.XPATH,
            f"//*[normalize-space()='{time}']"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                time_locator
            )
        ).click()

    def book_appointment(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.BOOKING_BUTTON
            )
        ).click()

    # --------------------------------------------------
    # CONFIRMATION
    # --------------------------------------------------

    CONFIRM_BUTTON = (
        By.XPATH,
        "//button[contains(normalize-space(),'Confirm')]"
    )

    def confirm_appointment(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CONFIRM_BUTTON
            )
        ).click()