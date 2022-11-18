# urls 리스트 or url 변수에 들어간 값이 알맞은 링크가 아닐 경우 예외처리

# 앞에 /가 붙은 경우 url 삽입
# url이 아닌 경우 걸러내기 
# 위 사이트의 url이 아닌 경우 나누기

# post를 보낼때는 url 맨 뒤에 / 삭제

# list | dict 에 각 url 에 맞는 속성 추가하여 request post 보내기

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import requests
from bs4 import BeautifulSoup
import pprint
import ssl
context = ssl._create_unverified_context()
url = ""
find = ""
f = open('url_list.txt', 'w')

urls = []

url_dict = {}
for url in urls:
    try:
        res = urlopen(url)
        status = res.status

    except HTTPError as e:
        err = e.read()
        code = e.getcode()
        print(url, code) # 죽은 url이라면 404

    url_dict.update({url:status})

    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    find = soup.find_all('a')
    cell = []
    for i in find:
        href = i.attrs['href']
        cell.append(href)
        set(cell) # 중복 url이 없도록 set로 처리

    pprint.pprint(cell)
    print(cell, file=f)

f.close()
# pprint.pprint(url_dict)
