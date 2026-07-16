phone = {"kim" : "010-1234-5678", "lee": "010-9876-5432", "park": "010-1111-2222"}

# 검색 
print(phone["kim"])

# 입력.
phone["kang"] = "010-3333-4444"

# 수정.
phone["lee"] = "010-0000-0000"

# 삭제.
del phone["kim"]

# 반복 구문.
for item in phone.items():
    print(item)

# 2개의 반복 변수 사용.
for key, value in phone.items():
    print(key, value)

# 키만 받는 경우.
for key in phone.keys():
    print(key)

# 값만 받는 경우.
for value in phone.values():
    print(value)

print("***"* 20)

# Set
a = {1, 2, 3, 4}
b = {3, 4, 4, 5}

print(a)
print(b)
print(type(a))
print(a.union(b))           # 합집합
print(a.intersection(b))    # 교집합
print(a.difference(b))      # 차집합

print("***"* 20)

a = set((1,2,3))
print(type(a))
b = list(a)
print(type(b))
c = tuple(b)
print(type(c))
print(c)