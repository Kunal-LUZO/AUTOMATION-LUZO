import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from utilities.BasePage import BasePage


class ServicesPage(BasePage):

    BOOK_SERVICES = (
        By.XPATH,
        "//button[normalize-space()='Book Services']"
    )

    FIRST_HAIRCUT = (
        By.XPATH,
        "//button[@id='radix-_r_o_']"
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
        self.wait.until(
            EC.element_to_be_clickable(
                self.BOOK_SERVICES
            )
        ).click()


    def add_haircut(self):

        haircut = self.wait.until(
            EC.presence_of_element_located(
                self.FIRST_HAIRCUT
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            haircut
        )

        add_buttons = haircut.find_elements(
            By.XPATH,
            ".//following::button[contains(normalize-space(),'ADD')][1]"
        )

        if add_buttons:
            add_buttons[0].click()
        else:
            add_button = self.wait.until(
                EC.element_to_be_clickable(
                    self.ADD_HAIRCUT
                )
            )
            add_button.click()

    def increase_haircut_quantity(self):

        for _ in range(2):

            plus_button = self.wait.until(
                EC.element_to_be_clickable(
                    self.HAIRCUT_PLUS
                )
            )

            plus_button.click()

    def continue_to_cart(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CART_CONTINUE
            )
        ).click()

