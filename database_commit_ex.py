# 데이터베이스의 테이블에 입력, 수정, 삭제 와 같은 쓰기 작업을 실행한 경우는 종료하기전에 commit() 메서드를 실행해야함.
# Sqlite 는 자동 커밋 되지 않으므로 commit() 메소드를 실행하지 않으면 작업이 취소되고 종료됨.

import sqlite3

# 연결객체 생성. (이번에는 데이터베이스파일을 지정)
con = sqlite3.connect("C:\\Users\\xlimit\\Documents\\test.db")
# SQL 구문을 실행할 커서 객체 리턴.
cur = con.cursor()

cur.execute("create table if not exists PhoneBook (id integer primary key autoincrement, name text, phoneNumber text);")

# 1건 입력.
cur.execute("insert into PhoneBook(name, phoneNumber) values('홍길동', '010-111-1111');")
# 파라미터로 입력.
name = "이순식"
phoneNumber = "010-222-2222"
cur.execute("insert into PhoneBook(name, phoneNumber) values (?,?);", (name, phoneNumber))

# 다중 데이터 입력.
dataList = (("전우치", "010-3333-3333"), ("박문수","010-444-4444"))
cur.executemany("insert into PhoneBook(name, phoneNumber) values(?,?);", dataList)

# 결과를 확인
cur.execute("select * from PhoneBook")
for row in cur:
    print(row)
