from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError, HTTPError

for i in range(0,10):
    # 중고 장터 게시판 URL.
    url = 'https://www.clien.net/service/board/sold?od=T3&category=0&po='+ str(i)
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0'}

    req = urllib.request.Request(url, headers = headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
    except HTTPError as e:
        print(f"HTTP 에러 발생: {e.code}")
    except URLError as e:
        print(f"서버 연결 실패이유: {e.reason}")

    soup = BeautifulSoup(data, 'html.parser')

    # 게시글 제목을 포함하는 태그를 찾기.
    list = soup.find_all('span', attrs={'data-role':'list-title-text'})
   
    # 제목 출력.
    for item in list:
        title = item.text.strip()
        print(title)