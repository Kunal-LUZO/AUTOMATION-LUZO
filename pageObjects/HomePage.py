from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class HomePage(BasePage):

    # CLOSE_MEMBERSHIP = (
    #     By.XPATH,
    #     "//*[@class='h-5 w-5']"
    # )

    SEARCH_SALON = (
        By.XPATH,
        "//div[@class='w-full text-sm text-gray-600 bg-transparent border-none p-0 h-5 flex items-center justify-start']"
    )

    SEARCH_INPUT = (
        By.XPATH,
        "//input[@placeholder='Search for a place or service']"
    )

    SALON_RESULT = (
        By.XPATH,
        "//p[contains(text(), 'Ambar Unisex Salon')]/ancestor::a | //a[contains(@href, 'ambar-unisex-salon')] | //a[contains(@href, '/partners/')]"
    )

    def close_membership(self):
        self.click(self.CLOSE_MEMBERSHIP)

    def search_salon(self, salon_name):

        # Click the visible search area
        search_box = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_SALON)
        )

        search_box.click()

        # Wait for actual input field
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )

        search_input.clear()
        search_input.send_keys(salon_name)

    def open_salon(self):
        initial_handles = list(self.driver.window_handles)

        salon = self.wait.until(
            EC.presence_of_element_located(self.SALON_RESULT)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", salon)
        try:
            salon.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", salon)

        # Wait for navigation or new tab
        for _ in range(10):
            if len(self.driver.window_handles) > len(initial_handles):
                self.driver.switch_to.window(self.driver.window_handles[-1])
                print("Switched to newly opened salon tab:", self.driver.current_url)
                break
            time.sleep(0.5)