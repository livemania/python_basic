import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?query=%EB%B0%98%EB%8F%84%EC%B2%B4&where=news"

# User-Agent 를 지정하여 봇이 아닌 것처럼 가장.
headers = {
    "User-Agent": "Mozilla/5.0 (Window NT 10.0, Win64, x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

response = requests.get(url, headers= headers)
soup = BeautifulSoup(response.text, "html.parser")


# 뉴스 기사 영역의 제목 찾기(2025 년 기준 구조는 다를수 있음)
#titles = soup.select("a.fender-ui_228e3bd1 _nzFvJJRkp44McW9 > span.sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1") # 뉴스 기사 제목에 해당하는 클래스.
titles = soup.find_all('span', attrs={'class': 'sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1'})
print("기사 제목 목록")
for idx, title in enumerate(titles, 1):
    print(f"{idx}, {title.text}")