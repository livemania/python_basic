import glob

lst = glob.glob("*.py") # 현재 경로의 파일 리스트를 추출하여 리턴
for item in lst:
    print(item)

