Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".

import time

from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element(by ="id", value="treasure")
    element_attr = element.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x = element_attr
    y =calc(x)
    answer = browser.find_element(by="id", value="answer")
    answer.send_keys(y)
    checkBox = browser.find_element(by="id",value="robotCheckbox")
    checkBox.click()
    radioButton = browser.find_element(by="id", value="robotsRule")
    radioButton.click()

    button = browser.find_element(by="css selector", value="button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


