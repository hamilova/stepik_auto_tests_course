Переход на новую вкладку браузера
При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера.
 WebDriver может работать только с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит 
 работать со старой вкладкой. Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим 
 перейти. Это делается с помощью команды switch_to.window:

browser.switch_to.window(window_name)

Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех
 вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]

Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

first_window = browser.window_handles[0]

После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ


import math
import time

from selenium import webdriver


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(by="xpath", value="//button[contains(text(),'I want to go on a magical journey!')]")
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(by="css selector", value="#input_value")
    x = x_element.text
    y = calc(x)
    field = browser.find_element(by="css selector", value="#answer")
    field.send_keys(y)
    button = browser.find_element(by="xpath", value="//button[contains(text(),'Submit')]")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

    #
