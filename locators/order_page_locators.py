from selenium.webdriver.common.by import By


class OrderButtonLocators:
    #Кнопка принятия куки
    cookie_button = By.XPATH, ".//button[text()='да все привыкли']"
    #Кнопка "Заказать в шапке страницы
    order_button_up = By.XPATH, ".//button[@class='Button_Button__ra12g']"
    #Кнопка "Заказать" в середине страницы
    order_button_low = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    #Список кнопок "Заказать", нужен для параметризации теста
    order_buttons = [order_button_up, order_button_low]


class OrderPageLocators:
    #Поле ввода имени
    name_field = By.XPATH, ".//input[contains(@placeholder,'Имя')]"
    #Поле ввода фамилии
    surname_field = By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"
    #Поле ввода адреса
    adress_field = By.XPATH, ".//input[contains(@placeholder,'Адрес')]"
    #Поле выбора метро
    subway_field = By.XPATH, ".//input[contains(@class,'select-search')]"
    #Выбор метро
    subway_choose_var_1 = By.XPATH, ".//*[text() = 'Черкизовская']"
    subway_choose_var_2 = By.XPATH, ".//*[text() = 'Чистые пруды']"
    #Поле ввода номера телефона
    phonenumber_field = By.XPATH, ".//input[contains(@placeholder,'Телефон')]"
    #Кнопка "Далее" на странице ввода информации о заказчике
    next_button = By.XPATH, ".//button[text()='Далее']"
    #Поле выбора дата привоза самоката
    date_field = By.XPATH, ".//input[contains(@placeholder,'Когда привезти самокат')]"
    #Выбор сегодняшней даты в календаре
    date_today_in_calendar = By.XPATH, ".//div[contains(@class, 'today')]"
    #Выбор даты в календаре
    date_some_date_in_calendar = By.XPATH, ".//div[contains(text(), '29')]"
    #Стрелка, которая выводит выпадающий список для выбора срока аренды
    srok_arrow = By.CLASS_NAME, "Dropdown-root"
    #Выбор срока аренды
    srok_choose_element_var_1 = By.XPATH, ".//*[text() = 'сутки']"
    srok_choose_element_var_2 = By.XPATH, ".//*[text() = 'двое суток']"
    #Чекбоксы для выбора цвета самоката
    order_black_color_checkbox = By.XPATH, ".//input[@id = 'black']"
    order_grey_color_checkbox = By.XPATH, ".//input[@id = 'grey']"
    #Поле ввода номера комментария
    comment_field = By.XPATH, ".//input[contains(@placeholder,'Комментарий')]"
    #Кнопка "Заказать"
    order_button = By.XPATH, ".//button[contains(@class,'Button_Middle') and text()='Заказать']"
    #Кнопка "Да" на форме подтверждения заказа
    order_confirmation_agree_button = [By.XPATH, ".//button[text()='Да']"]
    #Форма успешного заказа
    success_order_section = By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]"