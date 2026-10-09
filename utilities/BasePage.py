from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            30
        )

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        element.click()

    def type_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(text)

    def wait_for_text(self, locator, text):

        self.wait.until(
            EC.text_to_be_present_in_element(
                locator,
                text
            )
        )

    def is_displayed(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()