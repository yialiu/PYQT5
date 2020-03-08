# -*- coding: utf-8 -*-

# Jump.py
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_welcom import Ui_Main
from Ui_welcom2 import Ui_Main2

class Ui_MainWindow(Ui_Main2):

    def __init__(self, s):

        self.s1 = s[0]
        self.s2 = s[1]
        self.s3 = 4
        self.s4 = ('+' if self.s2 == '+' else '-' if self.s2 == '-' else '×' if self.s2 == '*' else '÷')

#主界面
class login(QtWidgets.QMainWindow,Ui_Main):
    def __init__(self):
        super(login,self).__init__()
        self.setupUi(self)
    #定义登录按钮的功能
    def re(self, s):
        self.MainWindow1 = QtWidgets.QMainWindow()
        self.ui1 = Ui_MainWindow(s)
        self.ui1.setupUi(self.MainWindow1)
        self.MainWindow1.show()

#运行窗口Login
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())