from bs4 import BeautifulSoup

page = open('C:\\Users\\xlimit\\Documents\\github_copilot\\python_basic\\Chap9_test.html', 'rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify())
# find_all() 메서드를 이용해서 <p> 태그를 검색해서 결과를 리스트 형태로 리턴함.
print(soup.find_all('p'))

# open() 'rt' 모드값을 지정하고, 혹 한글이 깨지는 문제를 방지하기 위해 encoding='utf-8'로 지정.
# 체인방식(함수 체인 방식)을 이용해서 open() 함수에 연속으로 read() 메서드를 연속적으로 호출할 수 있음.
#BeautifulSoup() 클래스의 초기화  메서드(생성자)에 읽어온 문자열 변수 page 를 넘기고 'html.parser'라고 지정하면, HTML 문서를 파싱(읽어서 처리)하는 작업을 수행할 수있음.hasattr
#이렇게 생성된 soup 객체를 사용해서 검색하는 작업을 soup.prettify() 메서드를 사용해서 로딩된 전체 문서를 출력함.

# 하나의 p 태그만 검색하기 위해서는 find() 메서드 사용.
print('====== 하나의 p 태그만 검색 ======')
print(soup.find("p"))


# 특징이 있는 p 태그만 검색하는 경우.
print('====== 특징이 있는 p 태그만 검색 ======')
print(soup.find("p", class_="outer-text"))

# 특정 태그의 class 를 지정하기 위해 class 키워드를 사용하지만, 파이썬에서 class는 새로운 형식을 사용하는 키워드 이므로, 
#class_ 와 같은 매개 변수 명을 사용함.

#특정 태그의 class 속성을 지정하기 위해서는 attrs (attributes)를 사용함.
#보통은 Class 가 아닌 다른 속성을 태그에서 지정해서 사용하기도 함. 이런 경우 attrs={'class': 'outer-text'} 와 같이 사용할 수 있음.
print('====== attrs 를 통해서 검색 ======')
print(soup.find('p', attrs={'class':'outer-text'}))

# 태크 안쪽에 있는 문자열만 추출해 봄.
# text 속성을 사용하면, 태그 안에 있는 텍스트만 가져올수 있음.
# 또는 get_text() 메서드를 사용하면됨.
# tag.text.strip() 를 지정하면 text 속성을 사용하면서 앞위에 있는 공백을 strip() 메서드를 통해 자동으로 제거해 줌.
print('----- text 만 출력---------')
for tag in soup.find_all('p'):
    print(tag.text.strip())
# 출력된 결과를 보면 빈줄이 출력되는데 이는 개행 문자 때문임.
# str 클래스의 replace 함수를 사용해서 '\n'과 같은 개행 문자를 제거하면 됨.
print('----- 개행문자 제거-------')
for tag in soup.find_all('p'):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)