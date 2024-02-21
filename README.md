<h2>Sprint_6</h2>
<h3>Автотесты, реализованные для сервиса Яндекс.Самокат</h3>

<h4>test_question_page.py - тесты для проверки блока "Вопросы о важном" на главной странице</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_click_on_question_show_answer</td>
      <td>Проверка ответов на вопросы в выпадающем списке в разделе "Вопросы о важном" - осуществляется клик на вопрос и возвращаемый ответ сверяется со списком ожидаемых ответов</td>
    </tr>
  </tbody>
</table>

<h4>test_order_page.py - тест для проверки страницы заказа самоката</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_go_to_order_page_and_make_order</td>
      <td>Проверка успешного оформления заказа самоката - на странице заказа заполняются все поля, выполняется подтверждение заказа и осуществляется проверка вывода сообщения об успешном заказе</td>
    </tr>
  </tbody>
</table>

<h4>test_header_order_page.py - тесты для проверки ссылок в шапке сервиса</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_go_from_order_page_click_samokat_logo</td>
      <td>Проверка перехода на главную страницу сервиса по нажатию на логотип "Самокат"</td>
    </tr>
    <tr>
      <td>test_go_from_order_page_click_yandex_logo</td>
      <td>Проверка перехода на главную страницу Яндекс.Дзен по нажатию на логотип "Яндекс"</td>
    </tr>
  </tbody>
</table>

Для работы необходимы библиотеки: </br>
<li>pytest</li>
<li>selenium</li>
<li>allure</li>

Запуск тестов:  <b>pytest -v</b> </br>
Построение отчета о тестировании: <b>allure serve allure_results</b> 