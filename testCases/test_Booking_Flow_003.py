import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.SalonPage import SalonPage
from pageObjects.ServicesPage import ServicesPage
from pageObjects.AppointmentPage import AppointmentPage
from pageObjects.ConfirmAppointmentPage import ConfirmAppointmentPage
from pageObjects.PaymentPage import PaymentPage
from pageObjects.JuspayPage import JuspayPage
from pageObjects.PaymentStatusPage import PaymentStatusPage

from utilities.ReadProperties import ReadConfig


class TestLUZOBooking:

    def test_booking_flow_003(self, setup):

        driver = setup

        # ==========================================================
        # TEST DATA
        # ==========================================================

        salon_name = "Ambar Unisex Salon & Spa"

        mobile_number = "8108269082"

        otp = "140118"

        bill_amount = "1000"

        date = "07"

        time_1 = "7:45 PM"
        time_2 = "8:00 PM"
        time_3 = "8:15 PM"

        # ==========================================================
        # STEP 1: OPEN LUZO WEBSITE
        # ==========================================================

        driver.get(
            ReadConfig.get_base_url()
        )

        driver.maximize_window()

        print("\nSTEP 1: LUZO website opened successfully")

        # ==========================================================
        # STEP 2: HANDLE LOCATION POPUP
        # ==========================================================

        login_page = LoginPage(driver)

        login_page.handle_location_popup()

        time.sleep(2)

        print("STEP 2: Location popup handled successfully")

        # ==========================================================
        # STEP 3: OPEN LOGIN
        # ==========================================================

        login_page.open_login_popup()

        time.sleep(2)

        print("STEP 3: Login popup opened")

        # ==========================================================
        # STEP 4: ENTER MOBILE NUMBER
        # ==========================================================

        login_page.enter_mobile_number(
            mobile_number
        )

        print("STEP 4: Mobile number entered")

        # ==========================================================
        # STEP 5: CLICK CONTINUE
        # ==========================================================

        login_page.click_continue()

        time.sleep(3)

        print("STEP 5: Continue clicked")

        # ==========================================================
        # STEP 6: ENTER OTP
        # ==========================================================

        login_page.enter_otp(
            otp
        )

        time.sleep(5)

        print("STEP 6: OTP entered")

        print("\nLOGIN COMPLETED SUCCESSFULLY")

        # ==========================================================
        # STEP 7: SEARCH SALON
        # ==========================================================

        home_page = HomePage(driver)

        # home_page.close_membership()

        home_page.search_salon(salon_name)

        time.sleep(3)

        print("\nSTEP 7: Salon searched successfully")

        # ==========================================================
        # STEP 8: OPEN SALON
        # ==========================================================

        home_page.open_salon()

        time.sleep(3)

        print("STEP 8: Salon opened successfully")

        # ==========================================================
        # STEP 9: CLICK SALON
        # ==========================================================

        salon_page = SalonPage(driver)

        salon_page.click_services()

        time.sleep(3)
        print("STEP 9: Salon page opened successfully")


        # ==========================================================
        # STEP 10: SELECT BOOK SERVICES
        # ==========================================================

        services_page = ServicesPage(driver)

        services_page.book_services()

        print("STEP 10: Book services button click successfully")

        # ==========================================================
        # STEP 12: ADD HAIRCUT
        # ==========================================================
        
        services_page.add_haircut()
        
        print("STEP 12: Haircut added successfully")
        
        # ==========================================================
        # STEP 13: INCREASE QUANTITY
        # ==========================================================
        
        services_page.increase_haircut_quantity()
        
        print("STEP 13: Haircut quantity increased to 3")
        
        # ==========================================================
        # STEP 14: CONTINUE TO CART
        # ==========================================================
        
        services_page.continue_to_cart()
        
        print("STEP 14: Continue button clicked")
        
        # ==========================================================
        # STEP 15: SELECT DATE
        # ==========================================================
        
        appointment_page = AppointmentPage(driver)
        
        appointment_page.select_date(
            date
        )
        
        print(
            f"STEP 15: Appointment date selected: {date}"
        )
        
        # ==========================================================
        # STEP 16: SELECT TIME 1
        # ==========================================================
        
        appointment_page.select_time(
            time_1
        )
        
        print(
            f"STEP 16: Time slot selected: {time_1}"
        )
        
        # ==========================================================
        # STEP 17: SELECT TIME 2
        # ==========================================================
        
        appointment_page.select_time(
            time_2
        )
        
        print(
            f"STEP 17: Time slot selected: {time_2}"
        )
        
        # ==========================================================
        # STEP 18: SELECT TIME 3
        # ==========================================================
        
        appointment_page.select_time(
            time_3
        )
        
        print(
            f"STEP 18: Time slot selected: {time_3}"
        )
        
        # ==========================================================
        # STEP 19: BOOK & PAY AFTER SERVICE
        # ==========================================================
        
        appointment_page.book_appointment()
        
        print(
            "STEP 19: Book & Pay After Service clicked"
        )
        
        # ==========================================================
        # STEP 20: VERIFY CONFIRM APPOINTMENT PAGE
        # ==========================================================
        
        confirm_page = ConfirmAppointmentPage(driver)
        
        confirm_page.verify_page()
        
        print(
            "STEP 20: Confirm Appointment page verified"
        )
        
        # ==========================================================
        # STEP 21: PAY BILL
        # ==========================================================
        
        confirm_page.click_pay_bill()
        
        print(
            "STEP 21: Pay Bill clicked"
        )
        
        # ==========================================================
        # STEP 22: SELECT NO
        # ==========================================================
        
        confirm_page.click_no()
        
        print(
            "STEP 22: No selected from appointment completion popup"
        )
        
        # ==========================================================
        # STEP 23: PAYMENT PAGE
        # ==========================================================
        
        payment_page = PaymentPage(driver)
        
        print(
            "STEP 23: Payment page opened"
        )
        
        # ==========================================================
        # STEP 24: ENTER BILL AMOUNT
        # ==========================================================
        
        payment_page.enter_bill_amount(
            bill_amount
        )
        
        print(
            f"STEP 24: Bill amount entered: ₹{bill_amount}"
        )
        
        # ==========================================================
        # STEP 25: PROCEED TO OFFER
        # ==========================================================
        
        payment_page.proceed_to_offer()
        
        print(
            "STEP 25: Proceed to avail offer clicked"
        )
        
        # ==========================================================
        # STEP 26: VERIFY PAYMENT AMOUNT
        # ==========================================================
        
        payable_amount = (
            By.XPATH,
            "//*[contains(normalize-space(),'₹700') "
            "or contains(normalize-space(),'700')]"
        )
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                payable_amount
            )
        )
        
        print(
            "STEP 26: ₹700 payable amount displayed"
        )
        
        # ==========================================================
        # STEP 27: PAY
        # ==========================================================
        
        payment_page.pay()
        
        print(
            "STEP 27: Pay button clicked"
        )
        
        # ==========================================================
        # STEP 28: JUSPAY
        # ==========================================================
        
        WebDriverWait(driver, 30).until(
            lambda d:
            "juspay" in d.current_url.lower()
            or "sandbox" in d.current_url.lower()
        )
        
        juspay_page = JuspayPage(driver)
        
        print(
            "STEP 28: Juspay payment page opened"
        )
        
        # ==========================================================
        # STEP 29: WALLET
        # ==========================================================
        
        juspay_page.wallet()
        
        print(
            "STEP 29: Wallet payment selected"
        )
        
        # ==========================================================
        # STEP 30: TEST PAYMENT METHOD
        # ==========================================================
        
        juspay_page.paypal()
        
        print(
            "STEP 30: Test payment method selected"
        )
        
        # ==========================================================
        # STEP 31: PROCEED TO PAY
        # ==========================================================
        
        juspay_page.proceed_to_pay()
        
        print(
            "STEP 31: Proceed to pay clicked"
        )
        
        # ==========================================================
        # STEP 32: TRANSACTION STATE
        # ==========================================================
        
        juspay_page.select_option()
        
        print(
            "STEP 32: Transaction state dropdown opened"
        )
        
        # ==========================================================
        # STEP 33: SELECT CHARGED
        # ==========================================================
        
        juspay_page.charge()
        
        print(
            "STEP 33: CHARGED selected"
        )
        
        # ==========================================================
        # STEP 34: SUBMIT
        # ==========================================================
        
        juspay_page.submit_button()
        
        print(
            "STEP 34: Payment submitted successfully"
        )
        
        # ==========================================================
        # STEP 35: PAYMENT STATUS
        # ==========================================================
        
        WebDriverWait(driver, 30).until(
            lambda d:
            "payment" in d.current_url.lower()
            or "successful" in d.page_source.lower()
        )
        
        payment_status_page = PaymentStatusPage(driver)
        
        print(
            "STEP 35: Payment Status page opened"
        )
        
        # ==========================================================
        # STEP 36: VERIFY RATING
        # ==========================================================
        
        payment_status_page.verify_rating_section()
        
        print(
            "STEP 36: Rating section verified"
        )
        
        # ==========================================================
        # STEP 37: DONE
        # ==========================================================
        
        payment_status_page.click_done()
        
        print(
            "STEP 37: Done button clicked"
        )
        
        # ==========================================================
        # TEST COMPLETED
        # ==========================================================
        
        print("\n==========================================")
        print("LUZO BOOKING FLOW 003 COMPLETED")
        print("==========================================")