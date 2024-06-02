import requests
from bs4 import BeautifulSoup
import execjs

with open('天津市公共资源交易平台url还原.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

url = 'http://ggzy.zwfwb.tj.gov.cn/jyxx/index_1.jhtml'
encode_url_response = requests.get(url)

bs4 = BeautifulSoup(encode_url_response.text, 'html.parser')
encode_url_dict = bs4.find('ul', class_='article-list2').findAll('li')

for encode_info in encode_url_dict:
    encode_url = encode_info.find('a')['url']
    information = encode_info.get_text().strip()
    project_name, *_, project_time = information.split('\n')
    decode_url = execjs.compile(js_file).call('decode_url', encode_url)
    print(project_name, decode_url, project_time)
