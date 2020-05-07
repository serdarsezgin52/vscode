from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

search_input = driver.find_element_by_name("q")

time.sleep(1)
search_input.send_keys("Python")
time.sleep(2)
search_input.send_keys(Keys.ENTER)
time.sleep(2)

result = driver.find_elements_by_css_selector(".mt-n1 a")

for element in result:
    print(element.text)

driver.close()

