import requests
from bs4 import BeautifulSoup

url = "http://spiderbuf.cn/s05/"

response = requests.get(url).text
bs4 = BeautifulSoup(response, "html.parser")

img_list = bs4.findAll("div", class_="col-sm-4")
for img in img_list:
    img_link = "http://spiderbuf.cn" + img.img["src"]
    print(img_link)
