for x in range(10):
    print(x, "*", x, "=", x*x)

print("---오른쪽 정렬---")
for x in range(1, 10):
    print(x, "*", x, "=", str(x*x).rjust(3))  # rjust() 메서드는 문자열을 오른쪽 정렬. 괄호 안의 숫자는 전체 길이.

print("---오른쪽 정렬---")
for x in range(1, 10):
    print(x, "*", x, "=", str(x*x).zfill(3))  # zfill() 메서드는 문자열을 오른쪽 정렬하고, 왼쪽에 0을 채움. 괄호 안의 숫자는 전체 길이.

print("-----"* 10)
print("---서식 문자 사용---")
print("{0:x}".format(10))  # 10진수를 16진수로 변환. hexadecimal.
print("{0:b}".format(10))  # 10진수를 2진수로 변환. binary.
print("{0:e}".format(4/3)) # 과학 연산의 결과(e) 로 출력
print("{0:.2f}".format(4/3)) # 소수점 이하 2자리까지 출력.
print("{0:f}".format(4/3))  # 소수점 이하 모든 자리수 출력.
print("{0:,}".format(100000))  # 천 단위 구분 기호를 넣어 출력.

print("-----"* 10)
value = 12345
formatted_str = f"{value:>10}"
print(formatted_str)

print("-----"* 10)
value = 12345
formatted_str = f"{value:*>20,}"
print(formatted_str)

