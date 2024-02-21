from selenium.webdriver.common.by import By


class QuestionPageLocators:
    #Раздел "Вопросы о важном"
    SEARCH_QUESTIONS_SECTION = [By.XPATH, "//div[contains(@class,'Home_FourPart')]"]
    #Блок со списком вопросов
    SEARCH_QUESTION_LIST_SECT = By.XPATH, '//div[@class = "accordion"]'
    #вопросы в блоке
    SEARCH_QUESTION_LIST = By.XPATH, "//div[@id = 'accordion__heading-{}']"
    #ответы на вопросы
    SEARCH_ANSWER_LIST = By.XPATH, '//div[@id = "accordion__panel-{}"]'
