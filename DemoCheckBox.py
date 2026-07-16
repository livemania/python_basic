import sys
from PyQt5.QtWidgets import *


class DemoCheckBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.checkBoxState()

    def setupUi(self):
        # x축과 y축, width, height 를 모두 저장.
        self.setGeometry(800,200,300,300)

        # 코드로 CheckBox 위젯을 생성.
        self.CheckBox1 = QCheckBox("아이폰", self)
        self.CheckBox1.move(10,20)
        self.CheckBox1.resize(150,30)
        self.CheckBox1.stateChanged.connect(self.checkBoxState)

        self.CheckBox2 = QCheckBox("안드로이드폰", self)
        self.CheckBox2.move(10,50)
        self.CheckBox2.resize(150,30)
        self.CheckBox2.stateChanged.connect(self.checkBoxState)

        self.CheckBox3 = QCheckBox("갤럭시폰", self)
        self.CheckBox3.move(10,80)
        self.CheckBox3.resize(150,30)
        self.CheckBox3.stateChanged.connect(self.checkBoxState)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBoxState(self):
        msg = ""
        if self.CheckBox1.isChecked() == True:
            msg += "아이폰"
        if self.CheckBox2.isChecked() == True:
            msg += "안드로이드폰"
        if self.CheckBox3.isChecked() == True:
            msg += "갤럭시폰"

        self.statusBar.showMessage(msg if msg else "선택된 항목이 없습니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoCheckBox()
    demoWindow.show()
    app.exec_()
