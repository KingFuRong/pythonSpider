import re
from bs4 import BeautifulSoup
from curl_cffi import requests
import execjs

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "referer": "https://www.dhl.com/cn-zh/home/tracking.html?tracking-id=1232343&submit=1&inputsource=marketingstage",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
# 1.首次请求
url = "https://www.dhl.com/cn-zh/home/tracking/tracking-supply-chain.html"
params = {"submit": "1", "tracking-id": "1232343"}
session = requests.Session()
response = session.get(url, headers=headers, params=params)
page_url = response.url
js_url = 'https://www.dhl.com' + re.search('type="text/javascript"  src="(.*?)">', response.text).group(1)
soup = BeautifulSoup(response.text, 'html.parser')
input_tags = [str(input_tag) for input_tag in soup.find_all('input')]
print(js_url)

# 2.get请求js链接
response = session.get(js_url, headers=headers)
bm_sz = dict(response.cookies)['bm_sz']
print(response, dict(response.cookies))

# 3.post请求js链接
with open("Akamai3.0.js", 'r', encoding='utf-8') as f:
    js_code = f.read()
    data = execjs.compile(js_code).call("Akamai_cookie", bm_sz, input_tags, page_url)

print(data)
response = session.post(url=js_url, headers=headers, data=data)
print(response, dict(response.cookies))

url = "https://www.dhl.com/utapi"
params = {
    "trackingNumber": "1232343",
    "language": "zh",
    "requesterCountryCode": "CN",
    "source": "tt"
}
response = session.get(url, headers=headers, params=params)

print(response.text)
print(response)
