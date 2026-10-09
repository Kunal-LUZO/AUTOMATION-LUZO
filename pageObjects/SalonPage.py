from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class SalonPage(BasePage):

    CLICK_ON_SALON = (
        By.XPATH,
        "//img[@alt='Ambar Unisex Salon & Spa salon']"
    )


    def click_services(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CLICK_ON_SALON
            )
        ).click()

