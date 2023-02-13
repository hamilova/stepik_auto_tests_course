нажать кнопку OK в алерте 
alert = browser.switch_to.alert
alert.accept()
Чтобы получить текст из alert, используйте свойство text объекта alert:
alert = browser.switch_to.alert
alert_text = alert.text

Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется confirm. Для переключения на окно confirm используется та же команда, что и в случае с alert:

confirm = browser.switch_to.alert
confirm.accept()

Для confirm-окон можно использовать следующий метод для отказа:

confirm.dismiss()
То же самое, что и при нажатии пользователем кнопки "Отмена". 

Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()




Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(by="xpath",value="//button[contains(text(),'I want to go on a magical journey!')]")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(by="css selector", value="#input_value")
    x = x_element.text
    y = calc(x)
    field = browser.find_element(by="css selector", value="#answer")
    field.send_keys(y)
    sButton = browser.find_element(by="xpath", value="//button[contains(text(),'Submit')]")
    sButton.click()
finally:
    time.sleep(10)
    browser.quit()

    #