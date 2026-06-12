from selenium.webdriver.common.by import By


class MainPageLocators:

    # Верхняя кнопка "Заказать"
    TOP_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")

    # Нижняя кнопка "Заказать"
    BOTTOM_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")

    @staticmethod
    def question_locator(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def answer_locator(index):
        return By.ID, f"accordion__panel-{index}"
        