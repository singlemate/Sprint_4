import allure
from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Нажать на логотип "Яндекс"')
    def yandex_logo_click(self):
        self.browser.find_element(*MainPageLocators.YANDEX_LOGO).click()

    @allure.step('Нажать на логотип "Самокат"')
    def scooter_logo_click(self):
        self.browser.find_element(*MainPageLocators.SCOOTER_LOGO).click()

    @allure.step('Принять соглашение cookie')
    def agree_cookie_click(self):
        self.browser.find_element(*MainPageLocators.COOKIE_BUTTON).click()

    @allure.step('Нажать на кнопку "Заказать" в шапке страницы')
    def first_order_button_click(self):
        self.browser.find_elements(*MainPageLocators.ORDER_BUTTON)[0].click()

    @allure.step('Нажать на кнопку "Заказать" снизу страницы')
    def second_order_button_click(self):
        self.browser.find_elements(*MainPageLocators.ORDER_BUTTON)[2].click()