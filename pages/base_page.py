from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_visibly_element(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((locator)))

    def wait_clickable_element(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((locator)))

    def click_on_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys_to_element(self, locator, value):
        element = self.find_element(locator)
        element.send_keys(value)

    def scroll_to_element(self, locator):
        self.wait_visibly_element(locator)
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    def get_attribute_value_from_element(self, locator):
        return self.find_element(locator).get_attribute('data-params')

    def switch_new_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
