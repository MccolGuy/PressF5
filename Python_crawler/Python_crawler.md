# 크롤링 이란?
**크롤링(crawling)** 은 웹에서 정보를 수집하는것을 말합니다.  
crawl이란 영어단어는 원래 "기어가다"라는 뜻이 있는데,     
크롤러가 웹사이트를 기어다니면서 정보를 수집한다고 이해하시면 될 것 같습니다.
##  사용 할 것들
- **Python** 쉽고 재밌는 언어로써 좋은 라이브러리를 가지고 있습니다.  
  - **requests** 파이썬 라이브러리로, 여기서는 웹사이트를 html로 저장하는 역할로 사용 됩니다.  
  - **BeautifulSoup** 역시 파이썬 라이브러리로 html를 파싱하게 해줍니다.  
- **웹에 대한 약간의 이해** 웹, 주로 html과, css를 안다면 좀 더 똑똑한 크롤러를 만들 수 있습니다.  
## 시작    
<code>
import requests
from bs4 import BeautifulSoup
def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
       _html = resp.text
   return _html
html = get_html("https://genie.co.kr/chart/top200")
soup = BeautifulSoup(html, 'html.parser')
print(soup.find_all("a",{"class":"title ellipsis"})[1])
</code>    
