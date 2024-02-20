import pytest
import allure
from locators.order_page_locators import OrderButtonLocators, OrderPageLocators
from pages.order_page import MainPageSamokat, OrderPageSamokat
from data import Data


class TestMakeOrder:
    @allure.title('Проверка заполнения полей для заказа и подтверждения заказа')
    @allure.description('На главной странице осуществляется переход к странице заказа, заполняются поля заказа, проверяется вывод сообщения об успешном заказе после подтверждения заказа')
    @pytest.mark.parametrize("locator_button", OrderButtonLocators.order_buttons)
    @pytest.mark.parametrize("name, surname, adress, phonenumber, subway_locator, date_locator, srok, color, comment_text",
                             Data.users)
    def test_go_to_order_page_and_make_order(self, driver, main_page, locator_button, name, surname, adress, phonenumber, subway_locator, date_locator, srok, color, comment_text):
        main_page.click_on_element_or_scroll_to_element(locator_button)
        order_page = OrderPageSamokat(driver)
        order_page.set_user_info_to_order_in_first_order_page(name, surname, adress, phonenumber)
        order_page.click_subway_field_and_choose_subway(subway_locator)
        order_page.next_button_click()
        order_page.set_order_info_in_second_order_page(date_locator, srok, color, comment_text)
        order_page.order_button_click()
        order_page.click_order_confirmation_agree_button()
        assert 'Заказ оформлен' in order_page.get_text_from_element(OrderPageLocators.success_order_section)

