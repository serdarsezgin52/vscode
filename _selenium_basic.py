from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

time.sleep(2)

driver.maximize_window()
driver.save_screenshot("github-homePage.png")

url = "http://github.com/sadikturan"
driver.get(url)

print(driver.title)

if "sadikturan" in driver.title:
    driver.save_screenshot("git_sadiktur.png")

time.sleep(2)
driver.back()
time.sleep(2)
driver.close()