import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 문서를 로딩.
form_class = uic.loadUiType("DemoForm.ui")[0]

# 윈도우 클래스 정의.
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫 번째 화면") # 기본적으로 objectName 이 label 로 설정되므로.

# 모듈을 직접 실행했는지 체크.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()  # 이벤트 루프 : 계속 대기하면서 사용자가 하는 작업을 처리하도록 함. 오른쪽 상단의 클로즈버튼을 클릭하면 이벤트 루프가 종료
