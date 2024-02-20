from selenium.webdriver.common.by import By


class HeaderOrderPageLocators:
    #Надпись "Самокат" в шапке страницы
    header_logo = By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR"
    #Надпись "Яндекс" в шапке страницы
    yandex_logo = By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"
    #Блок оформления заказа
    order_section = By.XPATH, ".//div[contains(@class,'Order_Content')]"
    #Заголовок на главной странице
    main_header = By.XPATH, ".//div[contains(@class,'Home_Header')]"
    #Форма поиска на главной странице яндекса
    yandex_search = By.XPATH, ".//form[contains(@class, 'dzen-search-arrow-common')]"