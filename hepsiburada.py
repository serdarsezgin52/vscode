import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'


html = requests.get(url)

soup = BeautifulSoup(html.content,"html.parser")

list = soup.find_all("div",{"id":"SearchResults"})

for ls in list:
    company = div.section.find_all("div",{"class":"company"})

print(company)