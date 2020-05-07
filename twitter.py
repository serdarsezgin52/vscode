from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    
    def singIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        btnSubmit = self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
        btnSubmit.click()

        time.sleep(2)

        twitter = Twitter(username,password)
        twitter.singIn()