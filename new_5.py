<label for="dropdown">Выберите язык программирования:</label>
<select id="dropdown" class="custom-select">
 <option selected>--</option>
 <option value="1">Python</option>
 <option value="2">Java</option>
 <option value="3">JavaScript</option>
</select>



from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(link)


browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()



from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"


Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index).
 Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") 
 найдёт "Python" для нашего примера.

Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля.
 Для того чтобы найти элемент с текстом "Python", нужно использовать select.select_by_index(1),
 так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".
 
 
 
 
 from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    import math
    x = browser.find_element(by="id", value="num1")
    y = browser.find_element(by="id", value="num2")
    num1 = int(x.text)
    num2 = int(y.text)

    dropdown = browser.find_element(by="id", value="dropdown").click()
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num1+num2))
    button = browser.find_element(by="css selector", value="button.btn")
    button.click()
finally:
    time.sleep(7)
    browser.quit()



