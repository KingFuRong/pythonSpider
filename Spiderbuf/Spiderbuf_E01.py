import requests
from bs4 import BeautifulSoup

url = "http://spiderbuf.cn/e01/login"
data = {
    "username": "admin",
    "password": "123456"
}

response = requests.post(url, data=data).text
bs4 = BeautifulSoup(response, "html.parser")

table = bs4.find("table", class_="table")
tr = table.findAll("tr")

for message in tr:
    if message.find("th"):
        title_list = message.findAll("th")
    else:
        title_list = message.findAll("td")
    for title in title_list:
        print(title.string, end='\t')
    print()
