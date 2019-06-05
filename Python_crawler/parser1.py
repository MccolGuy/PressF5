import requests
from bs4 import BeautifulSoup
import re
def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
       _html = resp.text
   return _html
html = get_html("https://genie.co.kr/chart/top200")
soup = BeautifulSoup(html, 'html.parser')
print(soup.find_all("a", {"class": "title ellipsis"}))
