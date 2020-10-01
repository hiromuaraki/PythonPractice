# coding: utf-8
# Your code here!
import requests
import re
from bs4 import BeautifulSoup as bs4

target_url = "https://stand.fm/episodes/5f726a0118e909da1e3e3f25"
res = requests.get(target_url)
soup = bs4(res.content, 'lxml')
soup.find_all(class_= 'css-901oao r-190imx5 r-n6v787 r-14yzgew')
print("<pre>" + soup.prettify() + "</pre>")


