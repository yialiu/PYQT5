# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\welcom.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(441, 162)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 401, 131))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #循环定义12个按钮，分别对应一位数加法、一位数减法、一位数乘法、一位数除法、一二位数加法、一二位数减法、一二位数乘法、一二位数除法、两位数加法、两位数减法、两位数乘法、两位数除法
        #3行4列grid
        for i in range(1,13):
            exec('self.pushButton_'+str(i) + '=' +'QtWidgets.QPushButton(self.widget)')
            eval('self.pushButton_'+str(i)).setObjectName("pushButton_"+str(i))
            self.gridLayout.addWidget(eval('self.pushButton_'+str(i)), int((i-1)/4), (i+3)%4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_1.clicked.connect(lambda: self.re('1+'))
        self.pushButton_2.clicked.connect(lambda: self.re('1-'))
        self.pushButton_3.clicked.connect(lambda: self.re('1*'))
        self.pushButton_4.clicked.connect(lambda: self.re('1/'))
        self.pushButton_5.clicked.connect(lambda: self.re('3+'))
        self.pushButton_6.clicked.connect(lambda: self.re('3-'))
        self.pushButton_7.clicked.connect(lambda: self.re('3*'))
        self.pushButton_8.clicked.connect(lambda: self.re('3/'))
        self.pushButton_9.clicked.connect(lambda: self.re('2+'))
        self.pushButton_10.clicked.connect(lambda: self.re('2-'))
        self.pushButton_11.clicked.connect(lambda: self.re('2*'))
        self.pushButton_12.clicked.connect(lambda: self.re('2/'))
		
        #for i in range(1,9):
        #    eval('self.pushButton_'+str(i)).clicked.connect(lambda: self.re(str(int(i/5)+1)+('+' if i%4==1 else '-' if i%4==2 else '*' if i%4==3 else '/')))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "小学算术  选择题目类型"))
        for i in range(1,13):
            eval('self.pushButton_'+str(i)).setText(_translate("Form", ("一" if int((i-1)/4)==0 else "一、二" if int((i-1)/4)==1 else "二")+"位数"+ ('加' if i%4==1 else '减' if i%4==2 else '乘' if i%4==3 else '除') +"法"))
