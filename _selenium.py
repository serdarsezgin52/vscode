from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://www.github.com"

driver.get(url)


url = "http://www.github.com/serdarsezgin52"

driver.get(url)

print(driver.title)

if "serdarsezgin52" in driver.title:
    driver.save_screenshot("gthub-serdar.png")

time.sleep(2)

driver.back()

time.sleep(2)

driver.close()