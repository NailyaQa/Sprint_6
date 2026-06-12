from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import BASE_URL


class MainPage(BasePage):

    def open_main_page(self):
        self.open(BASE_URL)
    #прокруктка к эллементу 
    def scroll_to_question(self, index):
        self.scroll_to_element(
            MainPageLocators.question_locator(index)
        )
    # Клик по элементу 
    def click_question(self, index):
        self.click_element(
            MainPageLocators.question_locator(index)
        )

    def click_main_order_button(self, button_type):
        

        if button_type == "top":
            self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

        elif button_type == "bottom":
            self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

            import time
            time.sleep(5)

            self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    #срасниваем  текст 
    def get_answer_text(self, index):
        return self.get_text(
            MainPageLocators.answer_locator(index)
        )
    

    
    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)


    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    