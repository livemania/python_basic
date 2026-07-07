import sqlite3

con = sqlite3.connect('product.db')
cur = con.cursor()

# 테이블 생성.
cur.execute('''
    CREATE TABLE IF NOT EXISTS Products (
            productID INTEGER PRIMARY KEY,
            productName TEXT NOT NULL,
            productPrice INTEGER NOT NULL
            )
''')

con.commit()

# 데이터 삽입 함수
def insert_product(productID, productName, productPrice):
    cur.execute('''
        INSERT INTO Products (productID, productName, productPrice) 
        VALUES(?,?,?)
    ''', (productID, productName, productPrice))
    
    con.commit()

# 데이터 수정함수.
def update_product(productID, newName, newPrice):
    cur.execute('''
        UPDATE Products SET productName = ?, productPrice = ?
        WHERE productID = ?
    ''', (newName, newPrice, productID))

    con.commit()

# 데이터 삭제 함수.
def delete_product(productID):
    cur.execute('''
        DELETE FROM Products
        WHERE productID = ?
    ''', (productID,))

    con.commit()

# 데이터 조회 함수.
def select_product(productID):
    cur.execute('''
        SELECT * FROM Products
        WHERE productID
    ''')

    rows = cur.fetchall()

    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")

# 데스트 실행 예시.
# 삽입
insert_product(1, '노트북', 1200000)
insert_product(2, '모니터', 300000)

# 조회
print('----조회---')
select_product(1)

# 수정
update_product(2, '게이밍모니터', 3500000)
print('---수정후 조회---')
select_product(2)

# 삭제
delete_product(2)

# 연결 종료
con.close()
