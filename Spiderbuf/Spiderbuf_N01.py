import requests
from bs4 import BeautifulSoup

url = "http://spiderbuf.cn/n01/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    'Referer': 'http://www.spiderbuf.cn/list'
}

response = requests.get(url, headers=headers).text
bs4 = BeautifulSoup(response, 'html.parser')

container = bs4.findAll("div", class_="col-xs-6 col-lg-4")

for message in container:
    name = message.h2.string
    information = message.findAll("p")
    print(name, end="\t\t")
    for info in information:
        print(info.string, end="\t\t")
    print()
