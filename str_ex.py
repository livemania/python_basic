strA = "파이썬은 강력해"
strB = "python is very powerful"

print("---문자열 길이 출력---")
print(len(strA))
print(len(strB))

print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p", 7))

print("---"*30)
print("---시작패턴과 끝패턴을 체크---")
print(strB.startswith("python"))
print(strB.endswith("ful"))

print("---대문자 또는 소문자 변환---")
result = strB.upper()
print(result)
print(strB.lower())

print("==="* 30)
print("---앞뒤에 있는 불필요한 문자열 잘래내기---")
data = "<<<피자 햄버거 치킨>>>"
result2 = data.strip("<>")
print(result2)

print("==="* 30)
print("---문자열을 리스트로 변환하고 다시 합치기---")
lst = result2.split()
print("list:{0}".format(lst))
result3 = " ".join(lst)
print("다시 하나로 조립:{0}".format(result3))
