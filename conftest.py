import pytest
from selenium import webdriver
from data import Data
from locators.order_page_locators import OrderButtonLocators, OrderPageLocators
from pages.order_page import MainPageSamokat


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.fullscreen_window()
    driver.get(Data.site_main_page)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    try:
        main_page = MainPageSamokat(driver)
        main_page.wait_visibly_element(OrderButtonLocators.cookie_button)
        main_page.click_on_element(OrderButtonLocators.cookie_button)
        yield main_page
    except:
        pass