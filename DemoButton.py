import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DemoButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        btn1 = QPushButton("닫기", self)
        btn1.move(20,20)
        btn1.clicked.connect(QCoreApplication.instance().quit)

# 진입점 체크.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoButton = DemoButton()
    demoButton.show()
    app.exec_()