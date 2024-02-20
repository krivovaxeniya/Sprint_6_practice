from pages.header_order_page import HeaderOrderPageSamokat
from pages.order_page import MainPageSamokat
from locators.order_page_locators import OrderButtonLocators
from locators.header_order_page_locators import HeaderOrderPageLocators
import allure


class TestGoFromOrderPage:

    @allure.title('Проверка перехода на главную страницу со страницы оформления заказа')
    @allure.description('На странице оформления заказа выполняется клик по логотипу "Самокат", проверяется переход на главную страницу сервиса заказа')
    def test_go_from_order_page_click_samokat_logo(self, driver):
        main_page = MainPageSamokat(driver)
        main_page.click_on_element(OrderButtonLocators.order_button_up)
        order_page = HeaderOrderPageSamokat(driver)
        order_page.click_header_logo()
        assert "Самокат" in order_page.get_text_from_element(HeaderOrderPageLocators.main_header) and "на пару дней" in order_page.get_text_from_element(HeaderOrderPageLocators.main_header)

    @allure.title('Проверка перехода на страницу Яндекс.Дзена со страницы оформления заказа')
    @allure.description(
        'На странице оформления заказа выполняется клик по логотипу "Яндекс", проверяется переход на страницу Яндекс.Дзен в новой вкладке')
    def test_go_from_order_page_click_yandex_logo(self, driver):
        main_page = MainPageSamokat(driver)
        main_page.click_on_element(OrderButtonLocators.order_button_up)
        order_page = HeaderOrderPageSamokat(driver)
        order_page.click_yandex_logo()
        order_page.switch_to_new_page()
        assert "Поиск Яндекса" in order_page.get_attribute_value_from_element(HeaderOrderPageLocators.yandex_search)
