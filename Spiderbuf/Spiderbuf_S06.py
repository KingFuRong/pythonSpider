import requests
from bs4 import BeautifulSoup

url = "http://spiderbuf.cn/inner/"

response = requests.get(url).text
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