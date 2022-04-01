## Поиск элементов с помощью Selenium ##
'''
find_element_by_id - поиск по уникальному атрибуту id элемента. Он наиболее стабильный
find_element_by_css_selector - поиск элемента с помощью правил на основе CSS
find_element_by_xpath - поиск с помощью языка запросов XPath
find_element_by_name - поиск по атрибуту name элемента
find_element_by_tag_name -  поиск элемента по названию тега элемента
find_element_by_class_name - поиск по значению атрибута class
find_element_by_link_text - поиск ссылки на странице по полному совпадению
find_element_by_partial_link_text - поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки
find_element() - универсальный метод поиска (библиотека By)
eg: from selenium.webdriver.common.by import By
- By.ID – поиск по уникальному атрибуту id элемента;
- By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
- By.XPATH – поиск элементов с помощью языка запросов XPath;
- By.NAME – поиск по атрибуту name элемента;
- By.TAG_NAME – поиск по названию тега;
- By.CLASS_NAME – поиск по атрибуту class элемента;
- By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
- By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.
'''
'''
find_element_by - возвращает только первый из всех элементов, которые подходят под условия поиска
find_elements_by - возвращает список всех найденных элементов по заданному условию
Если первый метод не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException, 
которая прервёт выполнение вашего кода. Второй же метод всегда возвращает валидный результат: 
если ничего не было найдено, то он вернёт пустой список и ваша программа перейдет к выполнению следующего шага в коде.
'''
## 1.6-2 ##
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
# закрываем браузер после всех манипуляций
browser.quit()
--
browser.close() закрывает текущее окно браузера
browser.quit() закрывает все окна, вкладки, и процессы вебдрайвера
'''
## 1.6-4 ##
'''
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
'''
## 1.6-5 ##
'''
import math
from selenium import webdriver


link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)


text_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = browser.find_element_by_partial_link_text(text_link)
link.click()


input1 = browser.find_element_by_tag_name('input')
input1.send_keys("Ivan")
input2 = browser.find_element_by_name('last_name')
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name('city')
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id('country')
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
'''
## 1.6-7 ##
'''
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements_by_tag_name("input")
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(30)
browser.quit()
'''
## 1.6-8 ##
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
'''