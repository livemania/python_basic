
from datetime import *
import time

print(time.time())
time.sleep(5)
print(time.time())
print("---표준시간---")
print(time.gmtime())
print("---한국시간---")
print(time.localtime())

d1 = date(2024, 6, 1)
print(d1)
print("---오늘 날짜--")
d2 = date.today()
print(d2)
print("---오늘 날짜에서 100일 후---")
d3 = timedelta(days=100)
print(d3)
print(d2 + d3)
d4 = datetime.now()
print(f"현재 날짜와 시간을 출력: {d4}")
