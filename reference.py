# 참조를 복사해서 전달한다.
phone = {"kim": "010-1234-5678", "lee": "010-9876-5432", "park": "010-1111-2222"}
print(phone)
print("포함 여부 체크: ", "park" in phone)
print("포함되어 있지 않은 경우 체크: ", "moon" in phone)

p = phone # Reference Type
print(id(phone), id(p))
p["moon"] = "010-0000-0000"
print(phone)
print(p)

# 파이선의 연산자 사용하기.
print("------"* 15)

print(3 + 5)
print(2 * 3)
print(2 ** 10) 
print(5/2)
# 정수값만 결과를 받을 때.
print(5//2)
# and 연산자
print(True and True and True)
print(True and True and False)
# or 연산자
print(True or True or False)