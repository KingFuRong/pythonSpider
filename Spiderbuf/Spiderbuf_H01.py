import requests
from bs4 import BeautifulSoup

url = "http://www.spiderbuf.cn/h01/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

information = soup.findAll("div", class_="container")
big_title = information[0]
small_title = information[1].findAll("div", class_="col-xs-6 col-lg-4")

# print(big_title.h1.text)
# print(big_title.p.text.strip())
for company_info in small_title:
    company_name = company_info.h2.findAll("i")
    company_name[0], company_name[1] = company_name[1], company_name[0]
    for name in company_name:
        print(name.text, end="")
    print()
    infos = company_info.findAll("p")
    for info in infos:
        print(info.text)
    print()
