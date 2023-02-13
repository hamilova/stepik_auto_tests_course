<input class="form-check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

people_radio = browser.find_element_by_id("peopleRule")

print(people_radio.get_attribute("name"))
# Напечатает ruler, т.е. текстовое значение аттрибута

print(people_radio.get_attribute("checked"))
# Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.

print(people_radio.get_attribute("href"))
# Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(by="css selector", value="#treasure")
    x_element_attr = x_element.get_attribute("valuex")
    x = x_element_attr
    y = calc(x)
    field = browser.find_element(by="css selector", value="#answer")
    field.send_keys(y)
    box = browser.find_element( by="id", value="robotCheckbox")
    box.click()
    radio = browser.find_element(by="id", value='robotsRule')
    radio.click()

    button = browser.find_element(by="css selector", value="button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()