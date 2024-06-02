import requests
from bs4 import BeautifulSoup

url = "http://spiderbuf.cn/e03/"

response = requests.get(url).text
bs4 = BeautifulSoup(response, 'html.parser')

url_list = bs4.find("ul", class_="pagination")
url_href = url_list.findAll("a")

for url_link in url_href:
    url = url_link["href"]
    url = "http://spiderbuf.cn/e03" + url.replace(".", "")

    response = requests.get(url).text
    bs4 = BeautifulSoup(response, 'html.parser')

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

