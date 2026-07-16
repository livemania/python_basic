import sqlite3

# 연결객체 생성(임시로 메모리에 저장)
con = sqlite3.connect(":memory:")
# SQL 구문을 시행할 커서 객체 반환.
cur = con.cursor()

cur.execute("create table if not exists PhoneBook " + " (id integer primary key autoincrement,  name text, phoneNumber text);")

# 한건의 데이터를 입력.
cur.execute("insert into PhoneBook (name, phoneNumber) values ('홍길동', '010-111-1111');")

# 입력 파라미터를 처리하는 경우. ? 를 사용하면 파라미터로 변환되어 처리됨.
name = "임승비"
phoneNumber = "010-4297-8992"
cur.execute("insert into PhoneBook (name, phoneNumber) values (?,?)", (name, phoneNumber))


# 다중의 데이터를 입력하는 경우 executemany를 사용함.
# Tuple 내부에 tuple을 넘겨서 2개의 데이터를 미리 입력해 두고, executemany() 메서드에 넘기면 해당 데이터의 입력 구문을 실행.
dataList = (("전우치","010-222-2222"), ("박문수", "010-333-3333"))
cur.executemany("insert into PhoneBook (name, phoneNumber) values(?,?)", dataList)

# 각 행의 컴럼 데이터는 Tuple 형태로 리턴됨.
cur.execute("select * from PhoneBook")
for row in cur:
    print(row)

# 수정 구문.
cur.execute("update PhoneBook set name='홍길동', phoneNumber='010-222-3333' where id = 1;")

# 삭제 구문.
cur.execute("delete from PhoneBook where id = 2;")

# 실행 결과를 리턴 받을때는 fetchone(), fetchmany(size=k), fetchall() 메서드를 사용할 수 있음
# 1건을 처리할 때 fetchone(), 10건씩 잘라서 블롣단위로 리턴 받는 함수 fetchmany(크기), 데이터가 많지 않은 경우라면 fetchall() 메서드를 사용함.

# 다만 주의해야 할 점은 데이터베이스의 테이블에 데이터는 저장되어 있지만,
#임시 버퍼로 검색한 결과를 로딩해서 사용하기 때문에 패치 명령어를 수행하면, 임시 버퍼에서는 데이터가 삭제됨.

cur.execute("select * from  PhoneBook")
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2)) #임시 데이터 삭제.
print("---fetchall()---")
# 다시 검색 구문을 수행해서 버퍼를 채워야 함.
cur.execute("select * from PhoneBook")
print(cur.fetchall())