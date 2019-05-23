#크롤링을 통해 웹브라우저에 들어가지 않고 학교홈페이지 파일을 다운받을수 있게 하는 프로그램 입니다!
import urllib.request
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path =filedialog.askdirectory()
def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
       _html = resp.text
   return _html
def get_download_link(URL):
    download_links = []
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    notice = soup.find_all("li", {"class": "common_display_inline_block"})
    for i in range(0,len(notice)):
     download_link = (str(notice[i]).split("\"")[7])
     download_links.append(download_link)
    return download_links;
def get_filename(URL):
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    notice = soup.find_all("li",{"class":"common_display_inline_block"})
    filenames = []
    for j in notice:
           filename = j.find_all("a")
           filename = (str(filename[0]).split("\xa0")[1])
           filenames.append(filename)
    return filenames;
import re
page_nums = []
page_names = []
filenumber = []
regex = r'[가-힣,0-9]+'
for jay in range(0,12):
      URL = "http://daeam-h.gne.go.kr/daeam-h/na/ntt/selectNttList.do?mi=98144&bbsId=83666"
      html = get_html(URL)
      soup = BeautifulSoup(html, 'html.parser')
      notice = soup.find_all("td", {"class": "ta_l"})
      #page_num = str((str(notice[i]).split()[2])).split("\"")[1]
      page_name = " " .join(re.findall(regex, str(notice[jay])))
      page_num = int(page_name.split()[0])
      page_nums.append(page_num)
      page_names.append(page_name)
      filenumber.append(jay)
      print("%d"%(jay+1)+". "+page_name)
num = int(input())
page_url="http://daeam-h.gne.go.kr/daeam-h//na/ntt/selectNttInfo.do?nttSn="+"%d"%(page_nums[num-1])
download_links = get_download_link(page_url)
filenames = get_filename(page_url)
print(file_path)
for i , j in enumerate(download_links):
    download_link = "http://daeam-h.gne.go.kr"+j
    urllib.request.urlretrieve(download_link,file_path+"/%s"%filenames[i])




