import sqlite3

class Products:
    def __init__(self, db_name='product2.db'):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                productID INTEGER PRIMARY KEY,
                productName TEXT NOT NULL,
                productPrice INTEGER NOT NULL             
            )
        ''')

        self.con.commit()

    def insert(self, productID, productName, productPrice):
        self.cur.execute('''
            INSERT INTO Products (productID, productName, productPrice) 
            VALUES (?,?,?)
        ''', (productID, productName, productPrice))

        self.con.commit()

    def update(self, productID, newName, newPrice):
        self.cur.execute('''
            UPDATE Products SET productName=?, productPrice=?
            WHERE productID = ?
        ''', (newName, newPrice, productID))

        self.con.commit()

    def delete(self, productID):
        self.cur.execute('''
            DELETE FROM Products
            WHERE productID = ?
        ''', (productID,))

        self.con.commit()

    def select(self):
        self.cur.execute('''
            SELECT * FROM Products
        ''')

        return self.cur.fetchall()
    
    def close(self):
        self.con.close()

# 테스트 코드
if __name__ == '__main__':
    db = Products()

    # 10 개의 데이터를 삽입
    sample_products = [
        (1, '노트북', 120000000),
        (2, '모니터', 1300000),
        (3, '키보드', 300000),
        (4, '마우스', 140000),
        (5, '스피커', 120000),
        (6, '프린터', 3200000),
        (7, '웹캠', 12000),
        (8, 'USB 허브', 12000),
        (9, 'SSD 1TB', 320000),
        (10, '헤드셋', 1000000)
    ]

    for pid, name, price in sample_products:
        db.insert(pid, name, price)

    # 전체 데이터 출력.
    print('==== 전체 데이터 출력 ====')
    for row in db.select():
        print(f'ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')

    # 제품 수정
    db.update(3, '기게식키보드', 75000)
    print('==== 수정후 목록 ====')
    for row in db.select():
        print(f'ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')

    # 제품 삭제
    db.delete(5)
    print('==== 삭제 후 목록 ====')
    for row in db.select():
        print(f'ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')

    db.close()    