from pages.base_page import BasePage
from locators.header_order_page_locators import HeaderOrderPageLocators
import allure


class HeaderOrderPageSamokat(BasePage):

    @allure.step('Выполняется ожидание появления логотипа Самоката, осуществляется клик на логотип')
    def click_header_logo(self):
        self.wait_visibly_element(HeaderOrderPageLocators.order_section)
        self.click_on_element(HeaderOrderPageLocators.header_logo)

    @allure.step('Выполняется ожидание появляется логотипа Яндекса, осуществляется клик на логотип')
    def click_yandex_logo(self):
        self.wait_visibly_element(HeaderOrderPageLocators.order_section)
        self.click_on_element(HeaderOrderPageLocators.yandex_logo)

    @allure.step('Происходит переход на новую открытую вкладку браузера')
    def switch_to_new_page(self):
        self.switch_new_page()
        self.wait_visibly_element(HeaderOrderPageLocators.yandex_search)

    @allure.step('Происходит переход на страницу заказа по клику на кнопку "Заказать" в шапке')
    def go_to_order_page(self):
        self.click_on_element(HeaderOrderPageLocators.order_button)

    def get_text_from_header(self):
        return self.get_text_from_element(HeaderOrderPageLocators.main_header)

    def get_text_from_yandex_search_section(self):
        return self.get_attribute_value_from_element(HeaderOrderPageLocators.yandex_search)