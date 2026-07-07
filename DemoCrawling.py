import sys
from PyQt5.QtWidgets import *
import urllib.request
from bs4 import BeautifulSoup
import webbrowser
import re

class DemoForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        # 창의 시작 위치와 폭, 높이(x,y, width, height)
        self.setGeometry(200,200, 800,600)

        # 입력 테스트
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(20, 20)
        # 문자열 출력.
        self.lineEdit.setText("아이폰")

        # 버튼
        self.btn = QPushButton("검색", self)
        self.btn.move(120, 20)
        self.btn.clicked.connect(self.setTableWidgetData)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(20, 70)
        self.tableWidget.resize(700, 500)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(2)

        # 컬럼의 폭을 지정.
        self.tableWidget.setColumnWidth(0, 400)
        self.tableWidget.setColumnWidth(1, 200)

        # QTableWidget 헤더 지정하기.
        self.tableWidget.setHorizontalHeaderLabels(['중고장터 매물', 'URL 주소'])

        # 시그널-슬롯 연결.
        self.tableWidget.doubleClicked.connect(self.doubleClicked)

    def setTableWidgetData(self):
        row = 0
        for n in range(0, 10):
            # 클리앙의 중고 장터 주소.
            url = 'https://www.clien.net/service/board/sold?&od=T31&category=0&po=' + str(n)
           
            headers = {'User-Agent': 'Mozilla/5.0'} # User-Agent 설정 필요.

            req= urllib.request.Request(url, headers=headers)
            #data = urllib.request.urlopen(url).read()
            with urllib.request.urlopen(req) as response:
                data = response.read()
            soup = BeautifulSoup(data, 'html.parser')
            list = soup.find_all('a', attrs={'class':'list_subject'})

            f = open("clien.txt", "a+", encoding="utf-8")
            for item in list:
                try:
                    span = item.find("span", attrs={'class':'subejct_fixed'})
                    title = item.text.strip()

                    # 라인 에디터에 입력된 문자열 받아서 검색.
                    if(re.search(self.lineEdit.text(), title)):
                        title = title.replace("\t", "")
                        title = title.replace("\n", "")
                        print(title)

                        link = 'https://www.clien.net/' + item['href']
                        print(link.strip())

                        f.write(title + "\n")
                        f.write(link + "\n")

                        # 행데이터로 출력.
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(title))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(link))

                        row += 1
                        print("row : ", row)

                except:
                    pass
        f.close()

    def doubleClicked(self):
        url = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        webbrowser.open(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()