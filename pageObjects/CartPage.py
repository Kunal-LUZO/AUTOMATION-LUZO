from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage


class CartPage(BasePage):

    # DATE_07_OCT = (
    #     By.XPATH,
    #     "//*[contains(normalize-space(),'Wed') "
    #     "and contains(normalize-space(),'07') "
    #     "and contains(normalize-space(),'Oct')]"
    # )

    TIME_745 = (
        By.XPATH,
        "//div[@class='flex flex-col gap-1 items-center py-2 px-4 rounded-lg text-xs text-center cursor-pointer border transition-all duration-150 bg-primary text-white border-primary font-semibold']"
    )

    TIME_800 = (
        By.XPATH,
        "//p[normalize-space()='8:00 PM']"
    )

    TIME_815 = (
        By.XPATH,
        "//body//div//div[27]"
    )

    BOOK_PAY = (
        By.XPATH,
        "//div[@class='bg-white rounded-md p-4 flex flex-col gap-3 border border-primary items-center']//button[normalize-space()='Book & pay after service']"
    )

    # def select_date(self):
    #
    #     self.click(
    #         self.DATE_07_OCT
    #     )

    def select_time_slots(self):

        self.click(self.TIME_745)

        self.click(self.TIME_800)

        self.click(self.TIME_815)

    def book_and_pay(self):

        self.click(
            self.BOOK_PAY
        )