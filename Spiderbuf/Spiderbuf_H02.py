import requests
from bs4 import BeautifulSoup

url = "http://www.spiderbuf.cn/h02/"

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

information = soup.findAll("div", class_="container")

title = information[0].h1.string
infos = information[1]

movie_infos = infos.findAll("div", class_="col-xs-12 col-lg-12")

for movie_info in movie_infos:
    print(movie_info.text.replace("\n\n", ""))

