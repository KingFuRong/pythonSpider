import time

import requests
from bs4 import BeautifulSoup


def print_information(infos):
    for info in infos:
        print(info.text)


for page in range(1, 21):
    url = "http://www.spiderbuf.cn/n03/" + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    information = soup.find("div", style="margin-top: 30px")
    title_list = information.find_all("h2")
    title_describe = information.find_all("p")
    data_list = information.find_all("tr")

    if page == 1:
        print_information(title_list)
        print_information(title_describe)

    for datas in data_list:
        if datas.find("th"):
            info = datas.find_all("th")
        else:
            info = datas.find_all("td")
        for infos in info:
            print(infos.text, end='\t')
        print()
    time.sleep(1)