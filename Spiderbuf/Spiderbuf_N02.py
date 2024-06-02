import requests
from bs4 import BeautifulSoup
import base64

url = "http://www.spiderbuf.cn/n02/"

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

img_encode = soup.find('img', class_="img-responsive center-block")['src']
img_encode = img_encode.replace("data:image/png;base64,", "")

img_decode = base64.b64decode(img_encode)
with open('img/img_encode.png', 'wb') as f:
    f.write(img_decode)
    f.close()
