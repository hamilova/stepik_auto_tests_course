Выполнение JavaScript на странице - это неописанный в документации Selenium способ поиска элемента.
Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
element = browser.execute_script('document.getElementsByName("name")')

Так же есть конструкции:
getElementById
getElementsByTagName
getElementsByClassName
querySelector - для CSS
querySelectorAll - для CSS (находит все совпадения)

evaluate - для XPATH.



driver = webdriver.Chrome()
driver.get("https://SunInJuly.github.io/execute_script.html")

try:
    button = driver.find_element_by_tag_name("button")
    _ = button.location_once_scrolled_into_view

   button.click()
    assert True
finally:
    driver.quit()
	
	
#можно использовать метод .submit() вместо .click(), в этом случае кнопка нажмется даже если она скрыта	




Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x.text)))))

    result = browser.find_element(by="css selector", value="#input_value")

    y = calc(result)
    answer = browser.find_element(by="id", value="answer")
    answer.send_keys(y)

    cBox = browser.find_element(by="id", value="robotCheckbox")
    cBox.click()
    rButton = browser.find_element(by="css selector", value="#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rButton)
    rButton.click()

    button = browser.find_element(by="css selector", value="button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()

