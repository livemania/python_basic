print("Hello VS Code")

lst = [1,2,3,4,5]
for i in lst:
    print(i)

x = 100
y= 3.14

print(type(x))
print(type(y))


strA = "python is very powerful"
strB = "파이썬은 강력해"

strC = """
    다중라인으로 저장할 경우
    이렇게 묶으면
    다중 라인으로 인식합니다.
"""
print(strC)

print(strA[0])
print(strA[1])
print(strA[-1])
print(strA[-2])

# 맵핑하는 함수
print('***'* 20)
lst = [1, 2, 3]
def add10(i):
    return i + 10

for item in map(add10, lst):
    print(item)