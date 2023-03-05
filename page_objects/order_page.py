import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Ввод имени')
    def set_name(self):
        self.browser.find_elements(*OrderPageLocators.inputs)[0].send_keys('Санта')

    @allure.step('Ввод имени 2')
    def set_name_2(self):
        self.browser.find_elements(*OrderPageLocators.inputs)[0].send_keys('Дед')

    @allure.step('Ввод фамилии')
    def set_surname(self):
        self.browser.find_elements(*OrderPageLocators.inputs)[1].send_keys('Клаусов')

    @allure.step('Ввод фамилии 2')
    def set_surname_2(self):
        self.browser.find_elements(*OrderPageLocators.inputs)[1].send_keys('Морозов')

    @allure.step('Ввод адреса')
    def set_address(self):
        self.browser.find_elements(*OrderPageLocators.inputs)[2].send_keys('Новосибирск, Котовского 10')

    @allure.step('Ввод адреса 2')
    def set_address_2(self):
        self.browser.find_elements(*OrderPageLocators.inputs)[2].send_keys('Красноярск, Ленина 24')

    @allure.step('Ввод станции метро')
    def set_metro_station(self):
        self.browser.find_element(*OrderPageLocators.metro_station_input).send_keys('Ле')
        self.browser.find_element(*OrderPageLocators.metro_station_row).click()

    @allure.step('Ввод станции метро 2')
    def set_metro_station_2(self):
        self.browser.find_element(*OrderPageLocators.metro_station_input).send_keys('Проспект Мира')
        self.browser.find_element(*OrderPageLocators.metro_station_row).click()

    @allure.step('Введите номер телефона')
    def set_phone_number(self):
        self.browser.find_elements(*OrderPageLocators.inputs)[3].send_keys('+79111351234')

    @allure.step('Введите номер телефона 2')
    def set_phone_number_2(self):
        self.browser.find_elements(*OrderPageLocators.inputs)[3].send_keys('+79990001177')

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        self.browser.find_element(*OrderPageLocators.next_button).click()

    @allure.step('Введите дату')
    def set_date(self):
        self.browser.find_elements(*OrderPageLocators.inputs_second_page)[0].send_keys('03.12.2022')
        self.browser.find_element(*OrderPageLocators.date_picker_selected).click()

    @allure.step('Введите дату 2')
    def set_date_2(self):
        self.browser.find_elements(*OrderPageLocators.inputs_second_page)[0].send_keys('12.12.2012')
        self.browser.find_element(*OrderPageLocators.date_picker_selected).click()

    @allure.step('Выберите срок аренды')
    def set_rental_period(self):
        self.browser.find_element(*OrderPageLocators.dropdown_control).click()
        self.browser.find_elements(*OrderPageLocators.dropdown_option)[0].click()

    @allure.step('Выберите срок аренды 2')
    def set_rental_period_2(self):
        self.browser.find_element(*OrderPageLocators.dropdown_control).click()
        self.browser.find_elements(*OrderPageLocators.dropdown_option)[1].click()

    @allure.step('Нажать на черный чек-бокс')
    def click_black_checkbox(self):
        self.browser.find_element(*OrderPageLocators.black_checkbox).click()

    @allure.step('Нажать на серый чек-бокс')
    def click_grey_checkbox(self):
        self.browser.find_element(*OrderPageLocators.grey_checkbox).click()

    @allure.step('Написать комментарий')
    def set_comment(self):
        self.browser.find_elements(*OrderPageLocators.inputs_second_page)[1].send_keys('Заказать самокат')

    @allure.step('Написать комментарий 2')
    def set_comment_2(self):
        self.browser.find_elements(*OrderPageLocators.inputs_second_page)[1].send_keys('Нужен самокат с фарами')

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self):
        self.browser.find_element(*OrderPageLocators.order_button).click()

    @allure.step('Нажать кнопку Да')
    def click_yes_button(self):
        self.browser.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Получить текст "Заказ оформлен"')
    def order_has_been_placed_text(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.order_has_been_placed)).text