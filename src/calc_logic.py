import mathlib
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from calc_view import Ui_MainWindow

# ! is a unary operator
operators = {'+','-','x','/','C','^','√'}

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.mem = None
        self.ans = None
        self.new_res = False

    def enterNum(self, text):
        if self.new_res: 
            self.result.setText('')
            self.new_res = False

        currText = self.result.text()
        
        if currText == '' or currText[-1] != '!': # to prevent index error, ! must be followed by an operator
            self.result.setText(self.result.text() + str(text))

    def checkDec(self):
        currText = self.result.text()

        for char in currText[::-1]:
            if char == ',' or char == '!':
                return False
            if char in operators:
                break

        return True

    def enterDec(self):
        currText = self.result.text()

        if currText == '' or currText[-1] in operators:
            self.result.setText(currText + '0,')
        elif self.new_res:
            self.result.setText('0,')
            self.new_res = False
        elif self.checkDec():
            self.result.setText(self.result.text() + ',')

    def enterOp(self, text):
        currText = self.result.text()
        self.new_res = False

        if currText == '':
            self.result.setText('0' + text)     # Enters a zero if needed
        elif currText[-1] not in operators:
            self.result.setText(self.result.text() + str(text))     # Not possible to enter 2 operators in a row

    def erase(self):
        # in case of new result, clears the screen
        if self.new_res:
            self.result.setText('')
            self.new_res = False
        else:
            self.result.setText(self.result.text()[:-1])
    
    def showRes(self):
        self.new_res = True
        self.result.setText(str(self.calculate()))

    def calculate(self):
        # each dictionary represents one priority category
        # mathlib function is assigned to each operator for convenient calling
        priorities = [{'!': mathlib.fact, 'C': mathlib.comb}, {'√': mathlib.root, '^': mathlib.exp}, 
                    {'x': mathlib.mul, '/': mathlib.div}, {'+': mathlib.sum, '-': mathlib.sub}]
        expr_list = re.findall(r"([\d.]+|[x/+-√^!C])", self.result.text().replace(',','.'))

        for p in priorities:
            length = len(expr_list)
            offset = 0      # makes sure the indexes are right, while expr_list is changing
            for i in range(length):
                if i + offset >= length:
                    break
                
                el = expr_list[i + offset]

                if el in p:
                    if el != '!':
                        tmp_res = p[el](float(expr_list.pop(i + offset - 1)), float(expr_list.pop(i + offset))) # popping the values and calling the right function
                        expr_list[i + offset - 1] = tmp_res # the operator symbol is replaced with the result
                        offset -= 2 
                    else: 
                        tmp_res = p[el](float(expr_list.pop(i + offset - 1))) # samme as before, but '!' is unary
                        expr_list[i + offset - 1] = tmp_res
                        offset -= 1

        return str(expr_list[0]).replace('.',',')

    def mSet(self):
        self.mem = self.calculate()

    def mRecall(self):
        if self.mem:
            self.enterNum(self.mem)

    def mClear(self):
        self.mem = None

    def answer(self):
        if self.ans:
            self.enterNum(self.ans)
    
    def keyPressEvent(self, e):
        self.result.setText('bim bam bum')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())