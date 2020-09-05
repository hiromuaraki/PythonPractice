print("Hello World")

# import requests
# import lxml.html

# # WebサイトのURLを指定
# url = "https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja"

# # Requestsを利用してWebページを取得する
# r = requests.get(url)

# # lxmlを利用してWebページを解析する
# html = lxml.html.fromstring(r.text)

# # lxmlのfindallを利用して、ヘッドラインのタイトルを取得する
# elems = html.findall(".//a[@class='ipQwMb Q7tWef']//span")
# for elem in elems:
#     print(elem.text)