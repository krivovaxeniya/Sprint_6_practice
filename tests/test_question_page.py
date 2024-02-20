import pytest
from pages.question_page import QuestionPageSamokat
from locators.question_page_locators import QuestionPageLocators
from data import Data
import allure
from pages.base_page import BasePage


class TestClickOnQuestion:

    @allure.title('Проверка выпадающего списка с ответами в разделе "Вопросы о важном"')
    @allure.description('На главной странице осуществляется переход к блоку "Вопросы о важном", выполняется клик на каждый вопрос и возвращаемый ответ сверяется со списком ожидаемых ответов')
    @pytest.mark.parametrize("num, expected_result",
                             [(0, Data.answer_0),
                              (1, Data.answer_1),
                              (2, Data.answer_2),
                              (3, Data.answer_3),
                              (4, Data.answer_4),
                              (5, Data.answer_5),
                              (6, Data.answer_6),
                              (7, Data.answer_7)])
    def test_click_on_question_show_answer(self, driver, num, expected_result):
        question_page = QuestionPageSamokat(driver)
        question_page.scroll_to_element(QuestionPageLocators.SEARCH_QUESTIONS_SECTION)
        question_page.wait_clickable_element(QuestionPageLocators.SEARCH_QUESTION_LIST_SECT)
        result = question_page.click_on_question_and_get_answer(QuestionPageLocators.SEARCH_QUESTION_LIST, QuestionPageLocators.SEARCH_ANSWER_LIST, num)
        assert result == expected_result
