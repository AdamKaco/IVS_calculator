# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(470, 540)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.button_m_rec = QtWidgets.QPushButton(self.centralwidget)
        self.button_m_rec.setGeometry(QtCore.QRect(20, 80, 100, 50))
        self.button_m_rec.setObjectName("button_m_rec")
        
        self.button_m_clr = QtWidgets.QPushButton(self.centralwidget)
        self.button_m_clr.setGeometry(QtCore.QRect(130, 80, 100, 50))
        self.button_m_clr.setObjectName("button_m_clr")
        
        self.button_m_set = QtWidgets.QPushButton(self.centralwidget)
        self.button_m_set.setGeometry(QtCore.QRect(240, 80, 100, 50))
        self.button_m_set.setObjectName("button_m_set")
        
        self.button_erase = QtWidgets.QPushButton(self.centralwidget)
        self.button_erase.setGeometry(QtCore.QRect(350, 80, 100, 50))
        self.button_erase.setObjectName("button_erase")
        
        self.button_exp = QtWidgets.QPushButton(self.centralwidget)
        self.button_exp.setGeometry(QtCore.QRect(20, 140, 100, 50))
        self.button_exp.setObjectName("button_exp")
        
        
        self.button_root = QtWidgets.QPushButton(self.centralwidget)
        self.button_root.setGeometry(QtCore.QRect(130, 140, 100, 50))
        self.button_root.setObjectName("button_root")
        
        self.button_fact = QtWidgets.QPushButton(self.centralwidget)
        self.button_fact.setGeometry(QtCore.QRect(240, 140, 100, 50))
        self.button_fact.setObjectName("button_fact")
        
        self.button_ans = QtWidgets.QPushButton(self.centralwidget)
        self.button_ans.setGeometry(QtCore.QRect(350, 140, 100, 50))
        self.button_ans.setObjectName("button_ans")
        
        self.button_sq = QtWidgets.QPushButton(self.centralwidget)
        self.button_sq.setGeometry(QtCore.QRect(20, 200, 100, 50))
        self.button_sq.setObjectName("button_sq")
        
        self.button_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.button_sqrt.setGeometry(QtCore.QRect(130, 200, 100, 50))
        self.button_sqrt.setObjectName("button_sqrt")
        
        self.button_C = QtWidgets.QPushButton(self.centralwidget)
        self.button_C.setGeometry(QtCore.QRect(240, 200, 100, 50))
        self.button_C.setObjectName("button_C")
        
        self.button_mult = QtWidgets.QPushButton(self.centralwidget)
        self.button_mult.setGeometry(QtCore.QRect(350, 200, 100, 50))
        self.button_mult.setObjectName("button_mult")
        
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(20, 260, 100, 50))
        self.button_7.setObjectName("button_7")
        
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(130, 260, 100, 50))
        self.button_8.setObjectName("button_8")
        
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(240, 260, 100, 50))
        self.button_9.setObjectName("button_9")
        
        self.button_div = QtWidgets.QPushButton(self.centralwidget)
        self.button_div.setGeometry(QtCore.QRect(350, 260, 100, 50))
        self.button_div.setObjectName("button_div")
        
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(20, 320, 100, 50))
        self.button_4.setObjectName("button_4")
        
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(130, 320, 100, 50))
        self.button_5.setObjectName("button_5")
        
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(240, 320, 100, 50))
        self.button_6.setObjectName("button_6")
        
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(350, 320, 100, 50))
        self.button_plus.setObjectName("button_plus")
                
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(20, 380, 100, 50))
        self.button_1.setObjectName("button_1")
        
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(130, 380, 100, 50))
        self.button_2.setObjectName("button_2")

        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(240, 380, 100, 50))
        self.button_3.setObjectName("button_3")
        
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(350, 380, 100, 50))
        self.button_minus.setObjectName("button_minus")
        
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(20, 440, 210, 50))
        self.button_0.setObjectName("button_0")
        
        self.button_decim = QtWidgets.QPushButton(self.centralwidget)
        self.button_decim.setGeometry(QtCore.QRect(240, 440, 100, 50))
        self.button_decim.setObjectName("button_decim")
        
        self.button_eq = QtWidgets.QPushButton(self.centralwidget)
        self.button_eq.setGeometry(QtCore.QRect(350, 440, 100, 50))
        self.button_eq.setObjectName("button_eq")
        
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(20, 20, 430, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.result.setFont(font)
        self.result.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.result.setMouseTracking(False)
        self.result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result.setWordWrap(False)
        self.result.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.result.setObjectName("result")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # number buttons
        self.button_1.clicked.connect(lambda: self.enterNum(1))
        self.button_2.clicked.connect(lambda: self.enterNum(2))
        self.button_3.clicked.connect(lambda: self.enterNum(3))
        self.button_4.clicked.connect(lambda: self.enterNum(4))
        self.button_0.clicked.connect(lambda: self.enterNum(0))
        self.button_5.clicked.connect(lambda: self.enterNum(5))
        self.button_6.clicked.connect(lambda: self.enterNum(6))
        self.button_7.clicked.connect(lambda: self.enterNum(7))
        self.button_9.clicked.connect(lambda: self.enterNum(9))
        self.button_8.clicked.connect(lambda: self.enterNum(8))
        self.button_decim.clicked.connect(self.enterDec)

        # erase button
        self.button_erase.clicked.connect(self.erase)

        # operator buttons
        self.button_plus.clicked.connect(lambda: self.enterOp('+'))
        self.button_minus.clicked.connect(self.enterMinus)
        self.button_mult.clicked.connect(lambda: self.enterOp('x'))
        self.button_div.clicked.connect(lambda: self.enterOp('/'))
        self.button_exp.clicked.connect(lambda: self.enterOp('^'))
        self.button_sq.clicked.connect(lambda: self.enterOp('^2'))
        self.button_root.clicked.connect(lambda: self.enterOp('√'))
        self.button_sqrt.clicked.connect(lambda: self.enterNum('2√'))
        self.button_C.clicked.connect(lambda: self.enterOp('C'))
        self.button_fact.clicked.connect(lambda: self.enterOp('!'))

        # action buttons
        self.button_eq.clicked.connect(self.showRes)
        self.button_m_set.clicked.connect(self.mSet)
        self.button_m_rec.clicked.connect(self.mRecall)
        self.button_m_clr.clicked.connect(self.mClear)
        self.button_ans.clicked.connect(self.answer)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_m_rec.setText(_translate("MainWindow", "MR"))
        self.button_m_clr.setText(_translate("MainWindow", "MC"))
        self.button_m_set.setText(_translate("MainWindow", "MS"))
        self.button_ans.setText(_translate("MainWindow", "ANS"))
        self.button_sq.setText(_translate("MainWindow", "x^2"))
        self.button_sqrt.setText(_translate("MainWindow", "2√x"))
        self.button_mult.setText(_translate("MainWindow", "x"))
        self.button_fact.setText(_translate("MainWindow", "!"))
        self.button_exp.setText(_translate("MainWindow", "x^n"))
        self.button_root.setText(_translate("MainWindow", "n√x"))
        self.button_div.setText(_translate("MainWindow", "/"))
        self.button_C.setText(_translate("MainWindow", "nCk"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_eq.setText(_translate("MainWindow", "="))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_decim.setText(_translate("MainWindow", ","))
        self.result.setText(_translate("MainWindow", ""))
        self.button_erase.setText(_translate("MainWindow", "⌫"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
