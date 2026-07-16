from bs4 import BeautifulSoup
import urllib.request
import re

f = open("clien.txt","wt", encoding="utf-8")
for i in range(0, 10):
    # 중고 장터 게시판 URL
    url = 'https://www.clien.net/service/board/sold?&od=T31&category=0&po=' + str(i)
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0'}

    req = urllib.request.Request(url, headers = headers)
    with urllib.request.urlopen(req) as response:
        data = response.read()

    soup = BeautifulSoup(data, 'html.parser')

    # 게시글 제목을 포함하는 태그를 찾기.
    list = soup.find_all('span', attrs = {'data-role':'list-title-text'})

    # 제목 출력.
    for item in list:
        title = item.text.strip()
        if re.search("맥북", title):
            print(title)
            f.write(title + "\n")

# 파일 닫고 종료하기.
f.close()