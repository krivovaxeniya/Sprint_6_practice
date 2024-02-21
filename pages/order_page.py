from locators.order_page_locators import OrderButtonLocators, OrderPageLocators
from pages.base_page import BasePage
import allure


class MainPageSamokat(BasePage):

    @allure.step('Выполняется скролл до элемента и клик на него')
    def scroll_to_element_and_click(self, locator):
       self.scroll_to_element(locator)
       self.wait_clickable_element(locator)
       self.click_on_element(locator)

    @allure.step('Выполняется клик-подтверждение на кнопку куки, чтобы строка не закрывала экран')
    def click_on_cookie_button(self):
        self.wait_visibly_element(OrderButtonLocators.cookie_button)
        self.click_on_element(OrderButtonLocators.cookie_button)


class OrderPageSamokat(BasePage):

    @allure.step('На странице оформления заказа выполняется клик на поле выбора метро, осуществляется клик на конкретный элемент')
    def click_subway_field_and_choose_subway(self, locator):
        self.click_on_element(OrderPageLocators.subway_field)
        self.click_on_element(locator)

    @allure.step('На странице оформления заказа происходит заполнение полей - Имя, Фамилия, Адрес, Номер телефона')
    def set_user_info_to_order_in_first_order_page(self, name, surname, adress, phonenumber):
        self.wait_visibly_element(OrderPageLocators.name_field)
        self.send_keys_to_element(OrderPageLocators.name_field, name)
        self.send_keys_to_element(OrderPageLocators.surname_field, surname)
        self.send_keys_to_element(OrderPageLocators.adress_field, adress)
        self.send_keys_to_element(OrderPageLocators.phonenumber_field, phonenumber)

    @allure.step('Клик на кнопку "Далее" на странице оформления заказа')
    def next_button_click(self):
        self.wait_clickable_element(OrderPageLocators.next_button)
        self.click_on_element(OrderPageLocators.next_button)

    @allure.step('На странице оформления заказа происходит нажатие на "Когда привезти самокат", из календаря происходит выбор даты')
    def set_date_order(self, locator):
        self.wait_visibly_element(OrderPageLocators.date_field)
        self.click_on_element(OrderPageLocators.date_field)
        self.click_on_element(locator)

    @allure.step('На странице оформления заказа происходит нажатие на "Срок аренды", происходит выбор срока - для теста используются два варианта "сутки" и "двое суток", выбор происходит по вводу количества суток')
    def click_srok_value(self, srok):
        self.click_on_element(OrderPageLocators.srok_arrow)
        self.wait_visibly_element(OrderPageLocators.srok_choose_element_var_1)
        if srok == 1:
            self.click_on_element(OrderPageLocators.srok_choose_element_var_1)
        elif srok == 2:
            self.click_on_element(OrderPageLocators.srok_choose_element_var_2)

    @allure.step('На странице оформления заказа выбирается чек-бокс для цвета самоката согласно вводу цвета')
    def click_order_color_checkbox(self, color):
        if color == 'black':
            self.click_on_element(OrderPageLocators.order_black_color_checkbox)
        elif color == 'grey':
            self.click_on_element(OrderPageLocators.order_grey_color_checkbox)

    @allure.step('На странице оформления заказа происходит заполнение поля "Комментарий"')
    def set_comment(self, comment_text):
        self.send_keys_to_element(OrderPageLocators.comment_field, comment_text)

    @allure.step('На странице оформления заказа происходит заполнение полей - Когда привезти самокат, Срок аренды, Цвет и Комментарий')
    def set_order_info_in_second_order_page(self, date_locator, srok, color, comment_text):
        self.set_date_order(date_locator)
        self.click_srok_value(srok)
        self.click_order_color_checkbox(color)
        self.set_comment(comment_text)

    @allure.step('Клик на кнопку "Заказать" на странице оформления заказа')
    def order_button_click(self):
        self.wait_clickable_element(OrderPageLocators.order_button)
        self.click_on_element(OrderPageLocators.order_button)

    @allure.step('Клик на кнопку "Да" на форме подтверждения заказа')
    def click_order_confirmation_agree_button(self):
        self.wait_clickable_element(OrderPageLocators.order_confirmation_agree_button)
        self.click_on_element(OrderPageLocators.order_confirmation_agree_button)

    def get_text_from_success_order_form(self):
        return self.get_text_from_element(OrderPageLocators.success_order_section)
