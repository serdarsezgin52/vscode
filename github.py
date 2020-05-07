from githubUsr import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self, username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        
    def SignIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").click()
    
    def getFollowers(self):
        self.browser.get("https://github.com/{self.username}?tab=followers")

        time.sleep(2)
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray.p1-1").text)

github = Github(username, password)
github.SignIn()
github.getFollowers()
print(github.followers)