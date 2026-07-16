print("---파일입출력---")
print("--파일쓰기--")
f = open("C:\\Users\\xlimit\\Documents\\test.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
f.close()


print("--파일읽기--")
f = open("C:\\Users\\xlimit\\Documents\\test.txt", "rt")
print("--read() 메서드 호출--")
result = f.read()
print(result)

f.seek(0)

print("--readline() 메서드 호출--")
print(f.readline(), end="")
print(f.readline(), end="")
#print(f.readline())
#print(f.readline())

f.seek(0)

print("--readlines() 메서드 호출--")
lst = f.readlines()

print(lst)

f.close()