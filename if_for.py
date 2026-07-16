score = int(input("점수를 입력: ")) # input() 함수는 입력을 받을 때 사용. str 형식으로 리턴되므로 int 형식으로 형변환.
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"

print(f"등급은 {grade}")

value = 5
while value > 0:
    print(value)
    value -= 1

# 대부분 갯수가 정해져 있는 경우.
lst = [100, 200, 300]
for item in lst:
    print(item)

fruit = {"apple": 100, "banana": 200, "kiwi": 300}
for item in fruit:
    print(item)

print("key, value을 별도로 처리하는 경우")
for k , v in fruit.items(): # key와 value 를 모두 리턴 : items(), key 를 리턴: keys(), value를 리턴: values()
    print(k, v)

print("-----break-----")
lst  = list(range(1,11))
print(lst)
for i in lst:
    if i > 5:
        break
    print("item:{0}".format(i))

print("----continue-----")
lst = list(range(1, 11))
print(lst)
for i in lst:
    if i % 2 ==0:
        continue
    print(i)

# 리스트 컴프리헨션(함축, comprehension)
lst = list(range(1, 11))
print([i**2 for i in lst if i > 5])

fruits = ("apple", "banana", "kiwi")
print([len(i) for i in fruits])

fruits2 = {100: "apple", 200: "banana", 300: "kiwi"}
print([v.upper() for v in fruits2.values()])