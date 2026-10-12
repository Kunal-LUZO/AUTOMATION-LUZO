from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class SalonPage(BasePage):

    CLICK_ON_SALON = (
        By.XPATH,
        "//img[@alt='Ambar Unisex Salon & Spa salon']"
    )


    def click_services(self):

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])

        if "partner" not in self.driver.current_url.lower() and "salon" not in self.driver.current_url.lower():
            try:
                elem = self.wait.until(
                    EC.element_to_be_clickable(self.CLICK_ON_SALON)
                )
                self.driver.execute_script("arguments[0].click();", elem)
                if len(self.driver.window_handles) > 1:
                    self.driver.switch_to.window(self.driver.window_handles[-1])
            except Exception:
                pass

