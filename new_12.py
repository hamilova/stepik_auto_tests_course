if browser.find_element_by_id("check_message").text == "Проверка прошла успешно!":
    browser.close() 
	
	
	from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(1)

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

Есть способы получше,чем time.sleep(1), оно не масштабируемое и трудно поддерживаемое.

Идеальное решение могло бы быть таким: нам всё равно надо избежать ложного падения тестов из-за асинхронной работы скриптов или задержек от сервера, поэтому мы будем ждать появление элемента на странице в течение заданного количества времени (например, 5 секунд). Проверять наличие элемента будем каждые 500 мс. Как только элемент будет найден, мы сразу перейдем к следующему шагу в тесте. Таким образом, мы сможем получить нужный элемент в идеальном случае сразу, в худшем случае за 5 секунд.

В Selenium WebDriver есть специальный способ организации такого ожидания, который позволяет задать ожидание при инициализации драйвера, чтобы применить его ко всем тестам. Ожидание называется неявным (Implicit wait), так как его не надо явно указывать каждый раз, когда мы выполняем поиск элементов, оно автоматически будет применяться при вызове каждой последующей команды.

Улучшим наш тест с помощью неявных ожиданий. Для этого нам нужно будет убрать time.sleep() и добавить одну строчку с методом implicitly wait:

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
Теперь мы можем быть уверены, что при небольших задержках в работе сайта наши тесты продолжат работать стабильно. На каждый вызов команды find_element WebDriver будет ждать 5 секунд до появления элемента на странице прежде, чем выбросить исключение NoSuchElementException.

№Не сработало для меня. Пытается кликнуть раньше чем нужно =(

Мой тест вводит поисковый запрос и структура страницы не меняется, а только подставляются новые данные в уже созданные категории. Во время поиска страница закрывается прозрачным spanом становится не кликабельной, но селениум похоже не в курсе

is not clickable at point (912, 151). Other element would receive the click

Мне бы метод который наоборот ждет когда эта хрень пропадет

Решил проблему благодаря.staleness_of(element)

NoSuchElementException - нет такого вообще
StaleElementReferenceException -  был элемент да сплыл
ElementNotVisibleException - видишь элемент? И я не вижу, а он есть.