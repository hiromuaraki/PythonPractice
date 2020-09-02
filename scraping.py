import requests
from bs4 import BeautifulSoup

target_url = "https://www.yahoo.co.jp/"
r = requests.get(target_url)
soup = BeautifulSoup(r.text, 'lxml')

soup.prettify()

