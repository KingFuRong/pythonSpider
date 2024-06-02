import requests
from bs4 import BeautifulSoup

url = "http://spiderbuf.cn/e02/list"
cookies = {
    "admin": "42f3f2d0f3ae44b93dae12599eacfa1c"
}

response = requests.post(url, cookies=cookies).text
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
