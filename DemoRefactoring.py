import sys
import sqlite3
import os.path
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5 import uic

# SQLite 데이터베이스 처리 클래스
class productDB:
    def __init__(self, db_name="ProductList.db"):
        is_new = not os.path.exists(db_name)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        if is_new :
            self.cursor.execute("CREATE TABLE Products (id integer primary key autoincrement, Name text, Price integer")
            self.conn.commit()

    def insert(self, name, price):
        self.cursor.execute("INSERT INTO Products (Name, Price) VALUES (?,?);", (name, price))
        self.conn.commit()

    def update(self, pid, name, price):
        self.cursor.execute("UPDATE Products SET Name= ?, Price= ? WHERE id =?", (name, price, pid))
        self.conn.commit()

    def delete(self, pid):
        self.cursor.execute("DELETE FROM Products WHERE id =?", (pid,))
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM Products")
        return self.cursor.fetchall()
    
# UI 클래스.
class ProductUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = productDB()

        uic.loadUiType("DemoForm3.ui")[0]

        # 버튼 연결.
        self.pushButton.clicked.connect(self.get_product)
        self.pushButton_2.clicked.connect(self.add_product)
        self.pushButton_3.clicked.connect(self.remove_product)
        self.pushButton_4.clicked.connect(self.update_product)

        self.tabelWidget.doubleClicked.connect(self.fill_input_fields)

        self.init_table()
        self.get_products()

    def init_table(self):
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,100)

        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabkeyNavigation(False)

    def show_message(self, text, title="알림"):
        QMessageBox.information(self, title, text)

    def validate_input(self, require_id = False):
        name = self.prodName.text().strip()
        price = self.prodPrice.text().strip()
        pid = self.prodID.text().strip()

        if require_id and not pid.isdigit():
            self.show_message("제품 ID는 숫자여야 합니다.")
            return None, None, None
        if not name:
            self.show_message("제품명을 입력하세요.")
            return None, None, None
        if not price.isdigit():
            self.show_message("가격은 숫자로 입력하세요.")
            return None, None, None
        
        return pid if pid else None, name, int(price)
    
    def add_product(self):
        _, name, price = self.validate_input()
        if name :
            self.db.insert(name, price)
            self.get_products()
            self.clear_inputs()

    def update_product(self):
        pid, name, price = self.validate_input(require_id = True)
        if pid:
            self.db.update(pid, name, price)
            self.get_products()
            self.clear_inputs()

    def remove_product(self):
        pid = self.prodID.text().strip()

        if pid.isdigit():
            self.db.delete(int(pid))
            self.get_products()
            self.clear_inputs()

        else:
            self.show_message("삭제할 제품의 ID를 올바르게 입력하세요.")

    def get_products(self):
        self.tableWidget.clearContents()
        products = self.db.fatch_all()

        for row, (pid, name, price) in  enumerate(products):
            item_id = QTableWidgetItem(str(pid))
            item_id.setTextAlignment(Qt.AlignRight)
            item_price = QTableWidgetItem(str(price))
            item_id.setTextAlignment(Qt.AlignRight)

            self.tableWidget.setItem(row, 0, item_id)
            self.tablewidget.setItem(row, 1, QTableWidgetItem(name))
            self.tablewidget.setItem(row, 2, item_price)

    def fill_input_fields(self):
        row = self.tableWidget.currentRow()

        self.prodID.setText(self.tableWidget.item(row, 0).text())
        self.prodName.setText(self.tableWidget.item(row, 1).text())
        self.prodPrice.setText(self.tableWidget.item(row, 2).text())

    def clear_inputs(self):
        self.prodID.clear()
        self.prodName.clear()
        self.prodPrice.clear()


    # UI 파일 슬롯 이름과 매칭되는 메서드
    def addProduct(self):
        self.add_product()

    def updateProduct(self):
        self.update_product()

    def removeProduct(self):
        self.remove_product()

    def getProduct(self):
        self.get_products()

# 메인 함수.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductUI()
    window.show()
    sys.exit(app.exec_)
