Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
Три способа задать путь к файлу:

1. вбить руками

element.send_keys("/home/user/stepik/Chapter2/file_example.txt")

 

2. задать с помощью переменных

# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# собираем путь к файлу
file_path = os.path.join(directory, file_name)
# отправляем файл
element.send_keys(file_path)


3.путь автоматизатора.
если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# импортируем модуль
import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# отправляем файл
element.send_keys(file_path)
"""
итоговый код:

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)



Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(by='css selector', value='input[name="firstname"]')
    first.send_keys("Eva")
    last = browser.find_element(by='css selector', value='input[name="lastname"]')
    last.send_keys("Mendes")
    email = browser.find_element(by='css selector', value='input[name="email"]')
    email.send_keys('abc@gmail.com')
    chooseF = browser.find_element(by='id', value='file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Privet.txt"
    file_path = os.path.join(current_dir, file_name)
    print(os.path.abspath(os.path.dirname(__file__)))

    print(file_path)
    chooseF.send_keys(file_path)
    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()

    #




