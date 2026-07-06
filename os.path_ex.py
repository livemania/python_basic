from os.path import *

print("---class_ex.py 파일이 있다면---")
if exists(r"C:\Users\xlimit\Documents\github_copilot\python_basic\class_ex.py"):
    print("파일크기 : {0}".format(getsize(r"C:\Users\xlimit\Documents\github_copilot\python_basic\class_ex.py")))
else:
    print("파일이 없습니다.")

print(basename("C:\\Users\\xlimit\\Documents\\github_copilot\\python_basic"))

print(abspath("C:\\Users\\xlimit\\Documents\\github_copilot\\python_basic\\"))