from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class JuspayPage(BasePage):

    WALLET = (
        By.XPATH,
        "//div[@id='60000032']//article[@role='none'][normalize-space()='Wallets']"
    )

    TEST_PAYMENT_METHOD = (
        By.XPATH,
        "//*[normalize-space()='Test Payment Method']"
    )

    PROCEED_TO_PAY = (
        By.XPATH,
        "//*[contains(normalize-space(),'Proceed to pay')]"
    )

    SELECT_OPTION = (
        By.XPATH,
        "//button[@id='txnStateDropdownToggle']"
    )

    CHARGED = (
        By.XPATH,
        "//li[@data-value='CHARGED']"
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[@id='submitButton']"
    )

    def wallet(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.WALLET
            )
        ).click()

    def paypal(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.TEST_PAYMENT_METHOD
            )
        ).click()

    def proceed_to_pay(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.PROCEED_TO_PAY
            )
        ).click()

    def select_option(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SELECT_OPTION
            )
        ).click()

    def charge(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CHARGED
            )
        ).click()

    def submit_button(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON
            )
        ).click()