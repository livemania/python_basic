from bs4 import BeautifulSoup
import urllib.request

# 중고 작터 게시판 url
url = "https://www.clien.net/service/board/use"
headers = {'User-Agent': 'Mozilla/5.0'} # User-Agent 설정 필요.

req= urllib.request.Request(url, headers=headers)
#data = urllib.request.urlopen(req).read()
#with 블록을 빠져나갈때 연결이 자동으로 답힘.
with urllib.request.urlopen(req) as response:
	data= response.read()
      
soup = BeautifulSoup(data, 'html.parser')

# 게시글 제목을 포함하는 태그를 찾기.
list = soup.find_all('span', attrs={'data-role':'list-title-text'})

# 제목 출력.
for item in list:
    title = item.text.strip()
    print(title)