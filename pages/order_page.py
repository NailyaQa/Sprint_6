from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    def fill_customer_info(
            self,
            name,
            surname,
            address,
            metro,
            phone
    ):
        self.driver.find_element(
            *OrderPageLocators.NAME_FIELD
        ).send_keys(name)

        self.driver.find_element(
            *OrderPageLocators.SURNAME_FIELD
        ).send_keys(surname)

        self.driver.find_element(
            *OrderPageLocators.ADDRESS_FIELD
        ).send_keys(address)

        self.click_element(
            OrderPageLocators.METRO_FIELD
        )

        self.click_element(OrderPageLocators.metro_station(metro))

        self.driver.find_element(
            *OrderPageLocators.PHONE_FIELD
        ).send_keys(phone)

        self.click_element(
            OrderPageLocators.NEXT_BUTTON
        )


    def fill_rent_info(self, comment):
        self.click_element(
            OrderPageLocators.DATE_FIELD
        )

        self.click_element(
            OrderPageLocators.CALENDAR_DAY
        )

        self.click_element(
            OrderPageLocators.RENTAL_PERIOD_FIELD
        )

        self.click_element(
            OrderPageLocators.THREE_DAYS_OPTION
        )

        self.click_element(
            OrderPageLocators.GREY_CHECKBOX
        )

        self.driver.find_element(
            *OrderPageLocators.COMMENT_FIELD
        ).send_keys(comment)


    def submit_order(self):
        print("Подтверждаем заказ")

        self.click_element(
        OrderPageLocators.ORDER_BUTTON
    )

    def confirm_order(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(
            OrderPageLocators.CONFIRM_YES_BUTTON
        )
    ).click()


    

    def get_success_header_text(self):
        return self.get_text(
            OrderPageLocators.SUCCESS_MODAL_HEADER
        )
    
    
   
    