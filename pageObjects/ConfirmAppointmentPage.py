from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class ConfirmAppointmentPage(BasePage):

    PAY_BILL = (
        By.XPATH,
        "//button[normalize-space()='Pay Bill']"
    )

    YES_BUTTON = (
        By.XPATH,
        "//button[contains(normalize-space(),'Yes')]"
    )

    NO_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='No']"
    )

    def verify_page(self):

        assert self.is_displayed(
            self.YES_BUTTON
        ), "Confirm Appointment page was not displayed"

    def click_pay_bill(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.PAY_BILL
            )
        ).click()

    def click_no(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.NO_BUTTON
            )
        ).click()