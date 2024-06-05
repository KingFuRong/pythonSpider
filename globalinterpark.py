import requests
from bs4 import BeautifulSoup

session = requests.Session()
first_url = ('https://challenges.cloudflare.com/cdn-cgi/challenge-platform/h/g/turnstile/if/ov2/av0/rcv1'
             '/h2gvC4Mvkw1DP0f/2sv5h/0x4AAAAAAAKC1nc26lcmHwc5/light/normal')
first_respones = session.get(first_url)
bs4 = BeautifulSoup(first_respones.text, 'html.parser')
first_js, second_url = bs4.find('head').findAll('script')
print(first_js.get_text().strip())
print(second_url['src'])


