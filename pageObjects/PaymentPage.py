from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class PaymentPage(BasePage):

    BILL_AMOUNT = (
        By.XPATH,
        "//input[@value='₹1,000' or @value='1000' or @value='₹1000']"
    )

    PROCEED_TO_OFFER = (
        By.XPATH,
        "//button[normalize-space()='Proceed to avail offer']"
    )

    PAY = (
        By.XPATH,
        "//button[contains(normalize-space(),'Pay ₹') or starts-with(normalize-space(),'Pay')]"
    )

    def enter_bill_amount(self, amount):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.BILL_AMOUNT
            )
        )

        element.click()
        element.clear()
        element.send_keys(str(amount))

    def proceed_to_offer(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.PROCEED_TO_OFFER
            )
        ).click()

    def pay(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.PAY
            )
        ).click()