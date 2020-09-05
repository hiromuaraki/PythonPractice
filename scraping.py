import requests
import re
from bs4 import BeautifulSoup

target_url = "https://www.yahoo.co.jp/"
r = requests.get(target_url)
soup = BeautifulSoup(r.text, 'lxml')
soup.find_all(href=re.compile("https://news.yahoo.co.jp/flash"))
print("<pre>" + soup.prettify() + "</pre>")

