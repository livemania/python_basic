#list
lst = [1,2,3,4,5]

print(type(lst))
print(len(lst))
print(lst)

# 리스테에 입력 수정하기.
lst.append(6)
lst.insert(1, 20)
lst[0] = 100
lst.remove(5)
print(lst)

# Tuple
tp = (100, 200, 300)
print(len(tp))
print(tp.index(200))
print(tp.count(100))
print("id: %s, name: %s" % ("kim", "김유신")) # %s 문자열 치환, %d 정수값 지원.

# 함수 정의.
def time(a, b):
    return a+b, a*b
# 호출
result = time(3, 4)
print(result)

# Dict
device = {"아이폰": 5, "아이패드": 19, "윈도우 노트북": 20}
print("---"* 10)
print(device)
print(type(device))
print(len(device))

# 검색 
print(device["아이폰"])

# 입력
device["맥북"] = 15

# 수정.
device["아이폰"] = 7

# 삭제.
del device["아이패드"]

print(device)