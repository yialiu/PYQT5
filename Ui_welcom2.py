# -*- coding: utf-8 -*-

import time, os
import random as ra
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSplitter, QApplication, QWidget,\
    QVBoxLayout, QPushButton, QMessageBox, QLabel,QLineEdit
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QTimer

number_timu = 10

Time = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
path = './'+Time[5:7]+Time[8:10]

d = 0
d1 = 0

def get_history():
    global d1
    name = []
    name_dt = []
    for root,dirs,files in os.walk(path):
        for i in range(len(files)):
            if(files[i][-3:] == 'jpg'):
                d1 += 1
                name.append(files[i][-(len(files[i])):-4])
                name_dt.append(files[i][-23:-4])

    name1 = sorted(name_dt)
    name_new = []
    
    for i in range(len(name_dt)):
        for j in range(len(name_dt)):
            if name1[i] in name[j]:
                name_new.append(name[j])
    return name_new

class Ui_Main2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 629)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        #倒计时UI
        self.label_date = QtWidgets.QLabel(self.centralwidget) 
        self.label_date.setText('日期:')
        self.label_jishi = QtWidgets.QLabel(self.centralwidget) 

        self.label_date.setGeometry(QtCore.QRect(210,5,60,45))
        self.label_jishi.setGeometry(QtCore.QRect(100,52,200,45))

        self.label_date_1 = QtWidgets.QLabel(self.centralwidget)  
        self.label_jishi_1 = QtWidgets.QLabel(self.centralwidget) 
        self.label_date_1.setGeometry(QtCore.QRect(300,5,250,45))
        self.label_jishi_1.setGeometry(QtCore.QRect(300,52,250,45))
        self.label_date_1.setText(time.strftime("%Y-%m-%d ", time.localtime())) 
        self.start = QtWidgets.QPushButton(self.centralwidget)  
        self.start.setText('开始')
        self.start.setGeometry(230,100,70,50)
        self.start.clicked.connect(self.counterClock)
		
        self.label_date.setSizePolicy(sizePolicy)
        self.label_date_1.setSizePolicy(sizePolicy)
        self.start.setSizePolicy(sizePolicy)
        self.label_jishi.setSizePolicy(sizePolicy)
        self.label_jishi_1.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_date.setFont(font)
        self.label_date_1.setFont(font)
        self.label_jishi_1.setFont(font)
        self.label_jishi.setFont(font)
        self.start.setFont(font)

        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)

        #定义第一、二个LCD数、标准结果LCD数
        for i in range(1,number_timu+1):
            exec('self.lineEdit'+str(i)+ '='+ 'QtWidgets.QLineEdit(self.centralwidget)')#你的结果
            exec('self.LCD'+str(i) +'='+ 'QtWidgets.QLCDNumber(self.centralwidget)')#第一个LCD数
            exec('self.LCD'+str(i)+str(i) +'='+ 'QtWidgets.QLCDNumber(self.centralwidget)')#第二个LCD数
            exec('self.LCD'+str(i)+str(i)+str(i) +'='+ 'QtWidgets.QLCDNumber(self.centralwidget)')#标准结果LCD数
            exec('self.label'+str(i)+ '='+ 'QtWidgets.QLabel(self.centralwidget)')
            exec('self.label_6'+str(i)+ '=' +'QtWidgets.QLabel(self.centralwidget)')
            exec('self.label_7'+str(i)+ '=' +'QtWidgets.QLabel(self.centralwidget)')
            exec('self.lineEditR'+str(i)+ '='+ 'QtWidgets.QLineEdit(self.centralwidget)')#除法的余数
            exec('self.LCDR'+str(i)+str(i)+str(i) +'='+ 'QtWidgets.QLCDNumber(self.centralwidget)')#除法余数的LCD数

            eval('self.LCD'+str(i)).setGeometry(QtCore.QRect(10, 170+45*(i-1), 50, 30))
            eval('self.LCD'+str(i)+str(i)).setGeometry(QtCore.QRect(110, 170+45*(i-1), 50, 30))
            eval('self.LCD'+str(i)+str(i)+str(i)).setGeometry(QtCore.QRect(360, 170+45*(i-1), 120, 30))
            eval('self.LCDR'+str(i)+str(i)+str(i)).setGeometry(QtCore.QRect(630, 170+45*(i-1), 120, 30))
            eval('self.lineEdit'+str(i)).setGeometry(QtCore.QRect(230, 170+45*(i-1), 120, 30))
            eval('self.lineEdit'+str(i)).setReadOnly(True)
            eval('self.lineEditR'+str(i)).setGeometry(QtCore.QRect(500, 170+45*(i-1), 120, 30))
            eval('self.label'+str(i)).setGeometry(QtCore.QRect(500, 170+45*(i-1), 50, 30))
            eval('self.label_6'+str(i)).setGeometry(QtCore.QRect(170, 170+45*(i-1), 50, 30))
            eval('self.label_7'+str(i)).setGeometry(QtCore.QRect(60, 170+45*(i-1), 50, 30))

            sizePolicy.setHeightForWidth(eval('self.LCD'+str(i)+str(i)).sizePolicy().hasHeightForWidth())
            eval('self.LCD'+str(i)+str(i)).setSizePolicy(sizePolicy)
            eval('self.LCD'+str(i)).setSizePolicy(sizePolicy)
            eval('self.LCD'+str(i)+str(i)+str(i)).setSizePolicy(sizePolicy)
            eval('self.lineEdit'+str(i)).setSizePolicy(sizePolicy)

            eval('self.LCDR'+str(i)+str(i)+str(i)).setSizePolicy(sizePolicy)
            eval('self.lineEditR'+str(i)).setSizePolicy(sizePolicy)

            eval('self.label_6'+str(i)).setSizePolicy(sizePolicy)
            eval('self.label_7'+str(i)).setSizePolicy(sizePolicy)
			
            font = QtGui.QFont()
            font.setPointSize(16)
            eval('self.LCD'+str(i)+str(i)).setFont(font)
            eval('self.LCD'+str(i)+str(i)).setDigitCount(int(self.s1))
            eval('self.LCD'+str(i)+str(i)).setObjectName("LCD"+str(i)+str(i))	

            eval('self.LCD'+str(i)).setFont(font)
            eval('self.LCD'+str(i)).setDigitCount(int(self.s1))
            eval('self.LCD'+str(i)).setObjectName("LCD"+str(i))

            eval('self.LCD'+str(i)+str(i)+str(i)).setFont(font)
            eval('self.LCD'+str(i)+str(i)+str(i)).setDigitCount(int(self.s3))
            eval('self.LCD'+str(i)+str(i)+str(i)).setObjectName("LCD"+str(i)+str(i)+str(i))	

            eval('self.LCDR'+str(i)+str(i)+str(i)).setFont(font)
            eval('self.LCDR'+str(i)+str(i)+str(i)).setDigitCount(int(self.s3))
            eval('self.LCDR'+str(i)+str(i)+str(i)).setObjectName("LCDR"+str(i)+str(i)+str(i))	
			
            font1 = QtGui.QFont()
            font1.setPointSize(16)
            font1.setStyleStrategy(QtGui.QFont.PreferDefault)
            eval('self.lineEdit'+str(i)).setFont(font1)
            eval('self.lineEdit'+str(i)).setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
            eval('self.lineEdit'+str(i)).setAlignment(QtCore.Qt.AlignCenter)
            eval('self.lineEdit'+str(i)).setObjectName("lineEdit"+str(i))
			
            eval('self.lineEditR'+str(i)).setFont(font1)
            eval('self.lineEditR'+str(i)).setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
            eval('self.lineEditR'+str(i)).setAlignment(QtCore.Qt.AlignCenter)
            eval('self.lineEditR'+str(i)).setObjectName("lineEditR"+str(i))


            eval('self.label_6'+str(i)).setFont(font)
            eval('self.label_6'+str(i)).setAlignment(QtCore.Qt.AlignCenter)
            eval('self.label_6'+str(i)).setObjectName("label_6"+str(i))
            eval('self.label_7'+str(i)).setFont(font)
            eval('self.label_7'+str(i)).setAlignment(QtCore.Qt.AlignCenter)
            eval('self.label_7'+str(i)).setObjectName("label_7"+str(i))

            font3 = QtGui.QFont()
            font3.setPointSize(18)
            eval('self.label'+str(i)).setFont(font3)
            eval('self.label'+str(i)).setObjectName("label"+ str(i))
			
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(60, 650, 331, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
		
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(60, 710, 301, 51))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_81 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_81.setFont(font)
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")

        self.LCDgoal = QtWidgets.QLCDNumber(self.splitter_2)

        sizePolicy.setHeightForWidth(self.LCDgoal.sizePolicy().hasHeightForWidth())
        self.LCDgoal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LCDgoal.setFont(font)
        self.LCDgoal.setDigitCount(3)
        self.LCDgoal.setObjectName("LCDgoal")

        #用时结果显示
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(60, 770, 301, 51))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_82 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_82.setFont(font)
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setObjectName("label_82")

        self.label_90 = QtWidgets.QLCDNumber(self.splitter_3)
        sizePolicy.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_90.setFont(font)
        self.label_90.setDigitCount(3)
        self.label_90.setObjectName("label_90")
		
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.che)
        self.pushButton_2.clicked.connect(self.fre)
		
        self.pushButton_3.clicked.connect(self.history)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.setEnabled(False)
        self.fre()
		
        #设置倒计时提示标题
        if (self.s1 == '1'  or self.s1 == '3') and (self.s2 == '+' or self.s2 == '-'):
            self.label_jishi.setText('一分钟倒计时:')
        if (self.s1 == '1'  or self.s1 == '3') and self.s2 == '*':
            self.label_jishi.setText('一分半钟倒计时:')
        if (self.s1 == '1'  or self.s1 == '3') and self.s2 == '/':
            self.label_jishi.setText('二分钟倒计时:')
        if self.s1 == '2' and (self.s2 == '+' or self.s2 == '-'):
            self.label_jishi.setText('一分半钟倒计时:')
        if self.s1 == '2' and self.s2 == '*':
            self.label_jishi.setText('三分钟倒计时:')
        if self.s1 == '2' and self.s2 == '/':
            self.label_jishi.setText('四分钟倒计时:')

        #除法时多显示余数和余数LCD，label位置向右移动，否则不显示
        if self.s2 == '/':
            MainWindow.setFixedSize(820, 839)
            for i in range(1,11):
                eval('self.lineEditR'+str(i)).show()
                eval('self.LCDR'+str(i)+str(i)+str(i)).show()
                eval('self.label'+str(i)).setGeometry(QtCore.QRect(760, 170+45*(i-1), 50, 30))	
        else:
            MainWindow.setFixedSize(570, 839)
            for i in range(1,11):
                eval('self.lineEditR'+str(i)).hide()
                eval('self.LCDR'+str(i)+str(i)+str(i)).hide()			
		
        #限定输入答案框只能输入数字0-9999
        if (self.s1 == '1' or self.s1 == '3') and (self.s2 == '+' or self.s2 == '-'):		
            IntValidator = QIntValidator()
            IntValidator.setRange(0, 20)
            #my_regex = QtCore.QRegExp("[0-9][0-9]")
            #my_validator = QtGui.QRegExpValidator()
            for i in range(1,11):
                eval('self.lineEdit'+str(i)).setValidator(IntValidator)
                eval('self.lineEditR'+str(i)).setValidator(IntValidator)

        if (self.s1 == '1' or self.s1 == '3') and (self.s2 == '*' or self.s2 == '/'):		
            IntValidator = QIntValidator()
            IntValidator.setRange(0, 100)
            for i in range(1,11):
                eval('self.lineEdit'+str(i)).setValidator(IntValidator)
                eval('self.lineEditR'+str(i)).setValidator(IntValidator)

        if self.s1 == '2' and (self.s2 == '+' or self.s2 == '-'):		
            IntValidator = QIntValidator()
            IntValidator.setRange(0, 200)
            for i in range(1,11):
                eval('self.lineEdit'+str(i)).setValidator(IntValidator)
                eval('self.lineEditR'+str(i)).setValidator(IntValidator)

        if self.s1 == '2' and (self.s2 == '*' or self.s2 == '/'):		
            IntValidator = QIntValidator()
            IntValidator.setRange(0, 9999)
            for i in range(1,11):
                eval('self.lineEdit'+str(i)).setValidator(IntValidator)
                eval('self.lineEditR'+str(i)).setValidator(IntValidator)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小学算术({}位数{}法)".format(('一' if self.s1=='1' else '一、二' if self.s1=='3' else '二'), ('加' if self.s2 == '+' else '减' if self.s2 == '-' else '乘' if self.s2=='*' else '除'))))
        self.label1.setText(_translate("MainWindow", ""))
        for i in range(1,11):
            eval('self.label_6'+str(i)).setText(_translate("MainWindow", "="))
            eval('self.label_7'+str(i)).setText(_translate("MainWindow", self.s4))

        self.pushButton.setText(_translate("MainWindow", "提交试卷"))
        self.pushButton_2.setText(_translate("MainWindow", "刷新题目"))
        self.pushButton_3.setText(_translate("MainWindow", "历史记录"))
        self.label_81.setText(_translate("MainWindow", "你的得分:"))
        self.label_82.setText(_translate("MainWindow", "用时(秒):"))

    #倒计时		
    def counterClock(self):
        global interval 
        if (self.s1 == '1' or self.s1 == '3') and (self.s2 == '+' or self.s2 == '-'):
            interval = 60
        if (self.s1 == '1' or self.s1 == '3') and self.s2 == '*':
            interval = 90
        if (self.s1 == '1' or self.s1 == '3') and self.s2 == '/':
            interval = 120
        if self.s1 == '2' and (self.s2 == '+' or self.s2 == '-'):
            interval = 90
        if self.s1 == '2' and self.s2 == '*':
            interval = 180
        if self.s1 == '2' and self.s2 == '/':
            interval = 240

        self.timer.start(1000)
        self.start.setEnabled(False)
        self.pushButton.setEnabled(True)
        for i in range(1,number_timu+1):
            eval('self.lineEdit'+str(i)).setReadOnly(False)
        #self.fre()
        for i in range(1,number_timu+1):
            eval('self.LCD'+str(i)+str(i)+str(i)).display('')  
            eval('self.lineEdit'+str(i)).clear()
            eval('self.LCDR'+str(i)+str(i)+str(i)).display('')  
            eval('self.lineEditR'+str(i)).clear()
            eval('self.label'+str(i)).clear()  
            eval('self.label'+str(i)).setStyleSheet('color:black')
            eval('self.lineEdit'+str(i)).setStyleSheet('color:black')	
            eval('self.lineEditR'+str(i)).setStyleSheet('color:black')				
        self.LCDgoal.display('')
        self.label_90.display('')

    #更新界面显示的倒计时
    def refresh(self):
        global interval
        if interval >= 0:
            #self.label_jishi_1.setText('01:00')
            min = int(interval/60)
            sec = interval%60
            if sec < 10:
                sec = '0'+str(sec)
            else:
                sec =  str(sec)
            intervals = '0'+str(min) + ':' + sec
            self.label_jishi_1.setText(intervals)
            interval -= 1
        else:
            self.timer.stop()
            self.pushButton.setEnabled(False)
            QMessageBox.information(self.centralwidget,'时间到','时间已到，如果没有提交，你将不能再提交！点击刷新题目重新开始。')

    def history(self):
        Time = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())#保存题目和结果截图 用时间命名
        #print(Time[5:7]+Time[8:10])
        #print(os.path.exists(Time[5:7]+Time[8:10]))
        if os.path.exists(Time[5:7]+Time[8:10]):
            self.newWindow = SecondWindow()
            self.newWindow.show()
        else:
            QMessageBox.information(self.centralwidget,'没有历史记录','今天你尚未开始考试，没有历史记录！点击开始然后提交试卷。')

    def fre(self):
        self.start.setEnabled(True)

        first = []
        second = []

        if self.s1 == '1': 
            first = ra.sample(range(0,10),number_timu)        #避免生成相同的题目
            second = ra.sample(range(0,10),number_timu)        #避免生成相同的题目

        if self.s1 == '2':
            first = ra.sample(range(10,99),number_timu)        #避免生成相同的题目
            second = ra.sample(range(10,99),number_timu)       #避免生成相同的题目

        if self.s1 == '3':
            first = ra.sample(range(10,100),number_timu)        #避免生成相同的题目
            second = ra.sample(range(0,10),number_timu)        #避免生成相同的题目
            cursor = ra.randint(1,9)
            cur_list = ra.sample(range(0,9),cursor)
            for cur in cur_list:
                p = first[cur]
                first[cur] = second[cur]
                second[cur] = p


        #避免出现小数减去大数结果是负数的情况，小学一二三四五年级还没学负数
        if self.s2 == '-' or self.s2 == '/':
            for i in range(10):
                if first[i] < second[i]:
                    p = first[i]
                    first[i] = second[i]
                    second[i] = p
            #避免大小数交换后出现相同题目的情况
            for i in range(9):
                for d in range(1,(10-i)):
                    if first[i] == first[i+d] and second[i] == second[i+d]:
                        second[i+d] = second[i+d] + 1

        #除法的时候避免出现除数为0的情况
        if self.s2 == '/':
            for i in range(10):
                if second[i] == 0:
                    second[i] = ra.randint(1,9)  
                    if first[i] < second[i] and first[i] != 0:
                        p = first[i]
                        first[i] = second[i]
                        second[i] = p	
                    if first[i] < second[i] and first[i] == 0:
                        p = first[i] + 1
                        first[i] = second[i]
                        second[i] = p				

        for i in range(1,number_timu+1):
            eval('self.LCD'+str(i)+str(i)+str(i)).display('')  
            eval('self.lineEdit'+str(i)).clear()
            eval('self.LCDR'+str(i)+str(i)+str(i)).display('')  
            eval('self.lineEditR'+str(i)).clear()
            eval('self.lineEdit'+str(i)).setReadOnly(True)
            exec('self.l'+str(i) +'='+ str(first[i-1]))
            exec('self.l'+str(i)+str(i) +'='+ str(second[i-1]))
            eval('self.LCD'+str(i)).display(eval('self.l'+str(i)))  
            eval('self.LCD'+str(i)+str(i)).display(eval('self.l'+str(i)+str(i)))  
            eval('self.label'+str(i)).clear()  			
        self.LCDgoal.display('')
        self.label_90.display('')
        self.timer.stop()
        self.label_jishi_1.setText('')
        self.pushButton.setEnabled(False)

    def che(self):
        self.goal = 0#总分数
        Time = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())#保存题目和结果截图 用时间命名

        def calculate():
            for i in range(1,number_timu+1):
                if eval('self.lineEdit'+str(i)).text() == '':
                    eval('self.label'+str(i)).setText("?")   
                    eval('self.label'+str(i)).setStyleSheet("color:rgb(0, 0, 255);")
                    eval('self.LCD'+str(i)+str(i)+str(i)).display("")
                else:
                    n = int(eval('self.l'+str(i)+str(i)))
                    m = int(eval('self.l'+str(i)))

                    if eval('%d%s%d'%(m,self.s2,n)) == int(eval('self.lineEdit'+str(i)+'.text()')):
                        eval('self.label'+str(i)).setText("✔")
                        eval('self.LCD'+str(i)+str(i)+str(i)).display(eval('%d%s%d'%(m,self.s2,n)))
                        eval('self.label'+str(i)).setStyleSheet("color:rgb(0, 128, 0);")
                        eval('self.lineEdit'+str(i)).setStyleSheet('color:green')
                        self.goal += 10
                    else:
                        eval('self.label'+str(i)).setText("✘")
                        eval('self.label'+str(i)).setStyleSheet("color:rgb(255, 0, 0);")
                        eval('self.lineEdit'+str(i)).setStyleSheet('color:red')
                        eval('self.LCD'+str(i)+str(i)+str(i)).display(eval('%d%s%d'%(m,self.s2,n)))
 
        #除法计算方式比较特殊，牵涉到整除和不能整除的余数的情况,分类讨论很复杂
        def calculateR():
            for i in range(1,number_timu+1):
                if eval('self.lineEdit'+str(i)).text() == '':
                    eval('self.label'+str(i)).setText("?")   
                    eval('self.label'+str(i)).setStyleSheet("color:rgb(0, 0, 255);")
                    eval('self.LCD'+str(i)+str(i)+str(i)).display("")
                else:
                    n = int(eval('self.l'+str(i)+str(i)))
                    m = int(eval('self.l'+str(i)))
                    #能够整除的情况
                    if m%n == 0:
                        if m/n == int(eval('self.lineEdit'+str(i)+'.text()')):
                            if eval('self.lineEditR'+str(i)+'.text()') == '':
                                eval('self.label'+str(i)).setText("✔")
                                eval('self.LCD'+str(i)+str(i)+str(i)).display(eval('%d%s%d'%(m,self.s2,n)))
                                eval('self.LCDR'+str(i)+str(i)+str(i)).display('0')
                                #eval('self.LCD'+str(i)+str(i)+str(i)).setSegmentStyle(QtWidgets.QLCDNumber.Flat)#Mac系统需要加上，否则下面的color不生效。
                                #eval('self.LCD'+str(i)+str(i)+str(i)).setStyleSheet("border: 2px solid black; color: green; background: silver;")
                                eval('self.label'+str(i)).setStyleSheet("color:rgb(0, 128, 0);")
                                eval('self.lineEdit'+str(i)).setStyleSheet('color:green')
                                self.goal += 10
                            else:
                                if int(eval('self.lineEditR'+str(i)+'.text()')) == 0:
                                    eval('self.label'+str(i)).setText("✔")
                                    eval('self.LCD'+str(i)+str(i)+str(i)).display(eval('%d%s%d'%(m,self.s2,n)))
                                    eval('self.LCDR'+str(i)+str(i)+str(i)).display('0')
                                    eval('self.lineEdit'+str(i)).setStyleSheet('color:green')
                                    eval('self.lineEditR'+str(i)).setStyleSheet('color:green')
                                    eval('self.label'+str(i)).setStyleSheet("color:rgb(0, 128, 0);")
                                    self.goal += 10
                                else:
                                    eval('self.label'+str(i)).setText("✘")
                                    eval('self.label'+str(i)).setStyleSheet("color:rgb(255, 0, 0);")
                                    eval('self.lineEdit'+str(i)).setStyleSheet('color:green')
                                    eval('self.lineEditR'+str(i)).setStyleSheet('color:red')
                                    eval('self.LCD'+str(i)+str(i)+str(i)).display("")
                                    eval('self.LCDR'+str(i)+str(i)+str(i)).display('')

                        else:
                            eval('self.label'+str(i)).setText("✘")
                            eval('self.label'+str(i)).setStyleSheet("color:rgb(255, 0, 0);")
                            eval('self.lineEdit'+str(i)).setStyleSheet('color:red')
                            eval('self.LCD'+str(i)+str(i)+str(i)).display("")
                            eval('self.LCDR'+str(i)+str(i)+str(i)).display('')
                    else:
                        if int(m/n) != int(eval('self.lineEdit'+str(i)+'.text()')):
                            eval('self.label'+str(i)).setText("✘")
                            eval('self.label'+str(i)).setStyleSheet("color:rgb(255, 0, 0);")
                            eval('self.lineEdit'+str(i)).setStyleSheet('color:red')
                            eval('self.lineEditR'+str(i)).setStyleSheet('color:red')
                            eval('self.LCD'+str(i)+str(i)+str(i)).display("")
                        else:							
                            if eval('self.lineEditR'+str(i)).text() == '':
                                eval('self.label'+str(i)).setText("?")   
                                eval('self.label'+str(i)).setStyleSheet("color:rgb(0, 0, 255);")
                                eval('self.LCD'+str(i)+str(i)+str(i)).display("")
                            else:
                                if m%n == int(eval('self.lineEditR'+str(i)+'.text()')):
                                    eval('self.label'+str(i)).setText("✔")
                                    eval('self.LCD'+str(i)+str(i)+str(i)).display(str(int(m/n)))
                                    eval('self.LCDR'+str(i)+str(i)+str(i)).display(str(m%n))
                                    eval('self.label'+str(i)).setStyleSheet("color:rgb(0, 128, 0);")
                                    eval('self.lineEdit'+str(i)).setStyleSheet('color:green')
                                    eval('self.lineEditR'+str(i)).setStyleSheet('color:green')
                                    self.goal += 10
                                elif m%n != int(eval('self.lineEditR'+str(i)+'.text()')):
                                    eval('self.label'+str(i)).setText("✘")
                                    eval('self.label'+str(i)).setStyleSheet("color:rgb(255, 0, 0);")
                                    eval('self.lineEdit'+str(i)).setStyleSheet('color:red')
                                    eval('self.lineEditR'+str(i)).setStyleSheet('color:red')
                                    eval('self.LCD'+str(i)+str(i)+str(i)).display("")

        if self.s2 == '+' or self.s2 == '*' or self.s2 == '-':
            calculate()
            self.timer.stop()
            self.pushButton.setEnabled(False)

        else:
            calculateR()
            self.timer.stop()
            self.pushButton.setEnabled(False)

        self.LCDgoal.display(self.goal)
        if self.goal == 100:
            self.LCDgoal.setStyleSheet("border: 2px solid black; color: green; background: silver;")
        elif self.goal == 90:
            self.LCDgoal.setStyleSheet("border: 2px solid black; color: blue; background: silver;")
        elif self.goal >= 60 and self.goal < 90:
            self.LCDgoal.setStyleSheet("border: 2px solid black; color: yellow; background: silver;")
        else:
            self.LCDgoal.setStyleSheet("border: 2px solid black; color: red; background: silver;")

        #计算耗时
        counter = self.label_jishi_1.text()
        counter = counter.split(':')
        counter_m = int(counter[0])	
        counter_s = int(counter[1])	
        counter_s_left = 60*counter_m + counter_s		
        if (self.s1 == '1'  or self.s1 == '3') and (self.s2 == '+' or self.s2 == '-'):
            remaind = 60 - counter_s_left
        if (self.s1 == '1'  or self.s1 == '3') and self.s2 == '*':
            remaind = 90 - counter_s_left
        if (self.s1 == '1'  or self.s1 == '3') and self.s2 == '/':
            remaind = 120 - counter_s_left
        if self.s1 == '2' and (self.s2 == '+' or self.s2 == '-'):
            remaind = 90 - counter_s_left
        if self.s1 == '2' and self.s2 == '*':
            remaind = 180 - counter_s_left
        if self.s1 == '2' and self.s2 == '/':
            remaind = 240 - counter_s_left

        self.label_90.display(remaind)
        #提交之后，保存题目和结果截图
        QApplication.processEvents()#刷新当前屏幕
        screen = QApplication.primaryScreen()
        pix = screen.grabWindow(self.centralwidget.window().winId())#截取当前屏幕并命名，然后保存在当前目录下
        if os.path.exists(Time[5:7]+Time[8:10]):
            os.chdir('./'+Time[5:7]+Time[8:10])
            pix.save("{}位数{}法_{}.jpg".format(('一' if self.s1=='1' else '一、二' if self.s1=='3' else '二'), ('加' if self.s2 == '+' else '减' if self.s2 == '-' else '乘' if self.s2=='*' else '除'),Time))
        else:
            os.makedirs(Time[5:7]+Time[8:10])
            os.chdir('./'+Time[5:7]+Time[8:10])
            pix.save("{}位数{}法_{}.jpg".format(('一' if self.s1=='1' else '一、二' if self.s1=='3' else '二'), ('加' if self.s2 == '+' else '减' if self.s2 == '-' else '乘' if self.s2=='*' else '除'),Time))
        os.chdir('../')
           # d1 += 1

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.newWindowUI()

    def newWindowUI(self):
        self.resize(570,839)
        self.move(400,100)
        global name_new, d, d1
        d = 0
        d1 = 0
        name_new = get_history()

        if "除法" in name_new[0]:
            self.setFixedSize(820,839)	
        else:
            self.setFixedSize(570,839)

        self.setWindowTitle(name_new[0])
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(path +"/"+name_new[0]+ ".jpg")))
        self.setPalette(window_pale)

        self.pushButton_next = QtWidgets.QPushButton(self)
        self.pushButton_next.setGeometry(QtCore.QRect(400, 780, 75, 23))
        self.pushButton_next.setText('下一页')
		
        self.pushButton_prev = QtWidgets.QPushButton(self)
        self.pushButton_prev.setGeometry(QtCore.QRect(5, 780, 75, 23))
        self.pushButton_prev.setText('上一页')

        self.pushButton_prev.clicked.connect(self.previous)
        self.pushButton_next.clicked.connect(self.next)
        self.pushButton_prev.setEnabled(False) 
        if d1 == 1:
            self.pushButton_next.setEnabled(False) 
		
    def next(self):
        global name_new
        global d
        if d < d1-1:
            d += 1
            self.setWindowTitle(name_new[d])#setObjectName("MainWindow")
            window_pale = QtGui.QPalette()
            window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(path +"/"+name_new[d]+ ".jpg")))
            self.setPalette(window_pale)

            if "除法" in name_new[d]:
                self.setFixedSize(820,839)	
            else:
                self.setFixedSize(570,839)
            self.pushButton_prev.setEnabled(True)
			
            if d == d1-1:	
                self.pushButton_next.setEnabled(False) 			

    def previous(self):
        global name_new
        global d
        if d > 0:
            d -= 1
            self.pushButton_next.setEnabled(True) 
            self.setWindowTitle(name_new[d])#setObjectName("MainWindow")
            window_pale = QtGui.QPalette()
            window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(path +"/"+name_new[d]+ ".jpg")))
            self.setPalette(window_pale)  

            if "除法" in name_new[d]:
                self.setFixedSize(820,839)	
            else:
                self.setFixedSize(570,839)	
            if d == 0:	
                self.pushButton_prev.setEnabled(False) 					