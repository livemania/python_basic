# 소수점 자릿수.
pi = 3.141592653589793
print(f"pi:.2f") # 소수점 2자리 까지 표시. float 형식으로 표시.

# 천단위 콤마.
money = 1000000000
print(f"{money:,}") # 천단위 콤마 표시.

# 자릿수 맞추기.
num = 42
print(f"{num:5}") # 전체 폭 5자리.

# 0 으로 채우기.
print(f"{num:05}") 

# 정렬.
text = "Hi"

print(f"{text:<10}") # 왼쪽 정렬(숫자만큼 공백포함)
print(f"{text:>10}") # 오른쪽 정렬(숫자만큼 공백 포함.)
print(f"{text:^10}") # 가운데 정렬.

# 채우기 문자 지정.
print(f"{'Hi':*^10}")

# 여러줄의 문자열.
name = "Tom"

text = """
    Name: {name}
    Language: Python
"""

# 날짜 포맷팅.
from datetime import datetime

now = datetime.now()

print(f"{now:%Y-%m-%d}")

# 조건식 사용.
score = 98

print(f"{'Pass' if score > 90 else 'Fail'}")

# 리스트/ 딕셔너리 접근.

date = {"name": "tom", "age": 24}
print(f"{date["name"]}")

# format()과의 비교.
# 기존 format()
name = "jace"
print("Hello {}".format(name))

# f-string literal
print(f"Hello {name}")

# 전역 변수.
x = 10
y = 20

# 함수 정의
def func():
    x = 1
    return x + y  #local 변수가 있으므로 로컬 변수사용

# 호출
print(func())

# 함수정의 
def func2():
    return x + y # local 변수가 없으므로 global 변수 사용.

# 호출
print(func2())

# 함수 정의
def times(a = 10, b = 20):
    return a + b

# 호출 
print(times())
print(times(5))
print(times(5, 6))

# 키워드 인자전달 (파리미터명을 명시)
def connectURI(server, port):
    strURI = "http://" + server + ":" + port
    return strURI

# 호출.
print(connectURI("naver.com", "80"))
print(connectURI(port="80", server="naver.com"))

# 가변인자를 처리하는 함수.
def union(*tp):
    result = []
    for item in tp:
        for x in item:
            if x not in result:
                result.append(x)

    return result

print(union("HAM","SPAM"))

# 람다 함수 정의

q = lambda x, y: x * y
print(q(1,2))
print(q(2,3))
print((lambda x: x*x)(3))
print(dir())

# 필터링하는 함수.
lst = [10, 25, 30]
iterL = filter(None, lst) # 조건 함수가 없는 경우 None 을 사용.
for item in iterL:
    print(item)

# 조건에 해당하는 함수.
def getBiggerThan20(i):
    return i> 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("--람다 함수--")
iterL = filter(lambda i: i> 20, lst)
for item in iterL:
    print(item)