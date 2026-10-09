from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class PaymentStatusPage(BasePage):

    RATING = (
        By.XPATH,
        "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/*[name()='svg'][5]/*[name()='path'][1]"
    )

    DONE = (
        By.XPATH,
        "//*[name()='button' and contains(@class,'inline-fle')]"
    )

    def verify_rating_section(self):

        assert self.is_displayed(
            self.RATING
        ), "Rating section was not displayed"

    def click_done(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.DONE
            )
        ).click()