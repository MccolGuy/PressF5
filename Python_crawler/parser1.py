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
<<<<<<< HEAD
print(soup.find_all("a", {"class": "title ellipsis"}))
=======
print(soup.find_all("a",{"class":"title ellipsis"}))
>>>>>>> 68f65da1db1c8d4cac42017a7164ff90429183b5
