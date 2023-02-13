from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:

    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(by="css selector", value="#input_value")
    x = x_element.text
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