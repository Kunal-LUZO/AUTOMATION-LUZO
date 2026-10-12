import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from utilities.BasePage import BasePage


class ServicesPage(BasePage):

    BOOK_SERVICES = (
        By.XPATH,
        "//button[normalize-space()='Book Services']"
    )

    FIRST_HAIRCUT = (
        By.XPATH,
        "//button[contains(., 'Haircut')]"
    )

    ADD_HAIRCUT = (
        By.XPATH,
        "//button[contains(normalize-space(),'ADD')]"
    )

    # Quantity + button
    HAIRCUT_PLUS = (
        By.XPATH,
        "//button[normalize-space()='+']"
    )

    CART_CONTINUE = (
        By.XPATH,
        "//button[normalize-space()='Continue']"
    )

    def book_services(self):
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])

        btn = self.wait.until(
            EC.presence_of_element_located(self.BOOK_SERVICES)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        time.sleep(1)
        try:
            btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", btn)

    def add_haircut(self):
        haircut = self.wait.until(
            EC.presence_of_element_located(self.FIRST_HAIRCUT)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", haircut)
        time.sleep(1)
        try:
            haircut.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", haircut)

        time.sleep(1)
        add_button = self.wait.until(
            EC.presence_of_element_located(self.ADD_HAIRCUT)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", add_button)
        try:
            add_button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", add_button)

    def increase_haircut_quantity(self):
        for _ in range(2):
            plus_button = self.wait.until(
                EC.presence_of_element_located(self.HAIRCUT_PLUS)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", plus_button)
            try:
                plus_button.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", plus_button)
            time.sleep(1)

    def continue_to_cart(self):
        btn = self.wait.until(
            EC.presence_of_element_located(self.CART_CONTINUE)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        try:
            btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", btn)

