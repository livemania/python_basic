import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import sqlite3
import os.path

if os.path.exists("ProductList.db"):
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
else:
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
    cur.execute('''
        create table Products (id integer primary key autoincrement, Name text, Price integer)
    ''')

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm5.ui")[0]

class DemoForm5(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 초기값 세팅
        self.id = 0
        self.naem = ""
        self.price = 0

        # QTableWidget 의 행의 갯수와 컬럼의 갯수를 지정하기.
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(3)

        # QTableWidget 의 컬럼폭을 세팅하기.
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 100)

        # QTableWidget 의 헤더 셋팅하기.
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품이름","제품가격"])

        # 탭키로 네비게이션 금지.
        self.tableWidget.setTabKeyNavigation(False)
        # 엔터키를 클릭하면 다름 컨트롤로 이동.
        self.prodID.returnPressed.connect(lambda: self.fucusNextChild())
        self.prodName.returnPressed.connect(lambda: self.fucusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.fucusNextChild())

        # 더블 클릭시 시그널 처리.(코드에서)
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    def addProduct(self):
        # 입력 파라미터 처리
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()

        cur.execute("insert into Products (Name, Price) values (?,?)",(self.name, self.price))

        # 리프레시
        self.getProduct()
        # 입력, 수정, 삭제 작업 후에는 커밋을 해야함.
        con.commit()

    def updateProduct(self):
        # 입력 파라미터 처리
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        cur.execute("update Products set Name=?, Price=? where id=?",(self.name, self.price, self.id))

        # 리프레시
        self.getProduct()
        # 입력, 수정, 삭제 작업 후에는 커밋을 해야함.
        con.commit()

    def removeProduct(self):
        # 입력 파라미터 처리.
        self.id = self.prodID.text()
        cur.execute("delete from Products where id = ?",(self.id,))

        # 리프레시
        self.getProduct()
        # 입력, 수정, 삭제 작업 후에는 커밋을 해야함.
        con.commit()

    def getProduct(self):
        # 검색 결과를 보여주기 전에 기존 컨텐츠를 삭제(헤더는 제외)
        self.tableWidget.clearContents()
        cur.execute("select * from Products")

        # 행숫자 카운트
        row =  0
        for item in cur:
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])

            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력함.
            itemID = QTableWidgetItem(int_as_strID)
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)

            #제품명은 그대로 출력한다.
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬ㅎ서 출력함.
            itemPrice = QTableWidgetItem(int_as_strPrice)
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

            row += 1
            print("row = ", row)

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(),0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(),1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(),2).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm5()
    demoForm.show()
    app.exec_()
