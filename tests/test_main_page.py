import allure
from page_objects.main_page import MainPage


class TestMainPage:

    @allure.description('По нажатию на логотип "Яндекс" в новом окне открывается главная страница Яндекса')
    @allure.title('Нажатие на логотип "Яндекс"')
    def test_yandex_logo_click(self, browser):
        main_page = MainPage(browser)
        browser.get("https://qa-scooter.praktikum-services.ru/")
        main_page.yandex_logo_click()
        assert len(browser.window_handles) == 2

    @allure.description('При нажатии на логотип "Самокат" переброс на главную страницу "Самоката"')
    @allure.title('Нажатие на логотип "Самокат"')
    def test_click_samokat_logo(self, browser):
        main_page = MainPage(browser)
        browser.get("https://qa-scooter.praktikum-services.ru/order")
        main_page.scooter_logo_click()
        assert browser.current_url == "https://qa-scooter.praktikum-services.ru/"







