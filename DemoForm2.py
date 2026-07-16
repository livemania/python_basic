import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 문서를 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 윈도우 클래스 정의 (QMainWindow 로 변경.)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 슬롯 메서드 추가.
    def firstClick(self):
        self.label.setText("첫 번째 버튼 클릭")

    def secondClick(self):
        self.label.setText("두 번째 버튼 클릭")

    def thirdClick(self):
        self.label.setText("세 번째 버튼 클릭")

# 직접 모듈을 실행했는지 체크.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
    
