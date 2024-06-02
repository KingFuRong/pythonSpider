import json

import requests
from bs4 import BeautifulSoup

url = "http://spiderbuf.cn/iplist/?order=asc"

response = requests.get(url)
response.encoding = 'utf-8'
response = response.json()

for message in response:
    print(message)
