from pages.base_page import BasePage
from locators.question_page_locators import QuestionPageLocators
import allure


class QuestionPageSamokat(BasePage):

    @allure.step('Для списка вопросов и ответов в блоке "Вопросы о важном" формируется путь к каждому вопросу, выполняется клик на вопрос и возвращается текст ответа')
    def click_on_question_and_get_answer(self, question_locator, answer_locator, num):
        method, locator_ques = question_locator
        locator_ques = locator_ques.format(num)
        method, locator_answ = answer_locator
        locator_answ = locator_answ.format(num)
        self.click_on_element([method, locator_ques])
        return self.get_text_from_element([method, locator_answ])

    def scroll_to_question_section(self):
        self.scroll_to_element(QuestionPageLocators.SEARCH_QUESTIONS_SECTION)

    def wait_clickable_question(self):
        self.wait_clickable_element(QuestionPageLocators.SEARCH_QUESTION_LIST_SECT)