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
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_visibly_element(HeaderOrderPageLocators.yandex_search)
