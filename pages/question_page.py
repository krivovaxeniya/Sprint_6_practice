from pages.base_page import BasePage
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
