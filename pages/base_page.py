



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #Открытие страницы
    def open(self, url):
        self.driver.get(url)

    #получение текста
    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    
    #прокрутка
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )
        return element
    
    #ликает по элементу
    def click_element(self, locator):
        element = self.scroll_to_element(locator)
        element.click()