#Qt5实验
from PyQt5 import QtWidgets
import sys

def showWindow():
    app = QtWidgets.QApplication(sys.argv)
    firstWindow = QtWidgets.QWidget()
    firstWindow.resize(1000,200)
    firstWindow.setWindowTitle("我是一个小宝宝")
    firstWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    showWindow()