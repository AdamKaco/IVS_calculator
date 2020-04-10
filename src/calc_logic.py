## @file calc_logic.py
# @author Simon Kosina
# @date 28.3.2020
# @brief Logic component of the calculator app

import mathlib
import re
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from calc_view import Ui_MainWindow

## Used for checking if it is possible to insert an operator (different rules for '!')
operators = ('+','-','*','/','C','^','√') # ! is a unary operator, not needed here

## @brief Implements the logic for the @p Ui_MainWindows class
class CalcMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    ## @brief Sets up the UI, sets @p mem, @p ans to @p None and @p new_res, @p error to @p False
    def __init__(self, parent=None):
        super(CalcMainWindow, self).__init__(parent)
        self.setupUi(self)
        ## Stores the memory value
        self.mem = None
        ## Stores the last result
        self.ans = None
        ## True only after '=' was pressed, False after all other actions
        self.new_res = False
        ## True if the entered expression resulted in an error, False otherwise
        self.error = False

    ## @brief Enters a digit if possible
    def enterNum(self, text):
        if self.new_res: 
            self.result.setText('')
            self.new_res = False

        currText = self.result.text()
        
        if currText == '' or currText[-1] != '!': # to prevent index error, ! must be followed by an operator
            self.result.setText(self.result.text() + str(text))

    ## @brief Checks if the current number is already decimal
    # @return True if number isn't decimal
    # @return False if number is decimal
    def checkDec(self):
        currText = self.result.text()

        for char in currText[::-1]:
            if char == ',' or char == '!':
                return False
            if char in operators:
                break

        return True

    ## @brief Enters a decimal point if possible
    def enterDec(self):
        currText = self.result.text()

        if currText == '' or currText[-1] in operators:
            self.result.setText(currText + '0,')
        elif self.new_res:
            self.result.setText('0,')
            self.new_res = False
        elif self.checkDec():
            self.result.setText(self.result.text() + ',')

    ## @brief Enters an operator if possible
    def enterOp(self, text):
        currText = self.result.text()
        self.new_res = False

        if currText == '' or self.error:
            self.error = False # Remove error text
            self.result.setText('0' + text)     # Enters a zero if needed
        elif currText[-1] not in operators:  # max 1 operator in a row
            self.result.setText(currText + str(text))      

    ## @brief Enters a minus if possible
    def enterMinus(self):
        currText = self.result.text()
        self.new_res = False

        if len(currText) < 2:
            self.result.setText(currText + '-')
        elif self.error:
            self.error = False
            self.result.setText('-')
        elif currText[-2:] != '--':
            self.result.setText(currText + '-')
        
       
    ## @brief Removes the rightmost character 
    def erase(self):
        # in case of new result, clears the screen
        if self.new_res:
            self.result.setText('')
            self.new_res = False
        else:
            self.result.setText(self.result.text()[:-1])
    
    ## @brief Wrapper function for @p calculate
    # @details Displays the result or an error text.
    def showRes(self):
        self.new_res = True
        try:
            tmp = self.calculate()
            self.ans = tmp
            self.result.setText(tmp)
        except Exception as inst:
            self.result.setText(str(inst))
            self.error = True
    
    ## @brief Parses the entered expression and calculates the result
    # @exception TypeError Operator was used with wrong number type (e.g. 5.6!)
    # @exception ValueError Operator was used with a wrong value, but correct type (e.g. -1!)
    # @exception IndexError Unsupported amount of operands (e.g. 5^)
    # @exception ZeroDivisionError Cannot divide by zero
    # @return Calculalated result as a string.
    def calculate(self):
        # each dictionary represents one priority category
        # mathlib function is assigned to each operator for convenient calling
        priorities = [{'!': mathlib.fact, 'C': mathlib.comb}, {'√': mathlib.root, '^': mathlib.exp}, 
                    {'*': mathlib.mul, '/': mathlib.div}, {'+': mathlib.sum, '-': mathlib.sub}]
        expr_modified = self.result.text().replace(',','.')
        expr_modified = expr_modified.replace('--','+')
        # regex for creating a list of numbers and operands
        expr_list = re.findall(r"((?<!.)[+-][\d]+|(?<=[*/+√^C-])[-+]?[\d.]+|[\d.]+|[*/+√^!C-])", expr_modified)

        for p in priorities:
            length = len(expr_list)
            offset = 0      # makes sure the indexes are right, while expr_list is changing
            for i in range(length):
                if i + offset >= length:
                    break
                
                el = expr_list[i + offset]

                if el in p:
                    try:
                        if el != '!':
                            tmp_res = p[el](float(expr_list.pop(i + offset - 1)), float(expr_list.pop(i + offset))) # popping the values and calling the right function
                            expr_list[i + offset - 1] = tmp_res # the operator symbol is replaced with the result
                            offset -= 2 
                        else: 
                            tmp_res = p[el](float(expr_list.pop(i + offset - 1))) # samme as before, but '!' is unary
                            expr_list[i + offset - 1] = tmp_res
                            offset -= 1
                    except TypeError:
                        raise TypeError(f"Wrong operand type: {el}")
                    except ValueError:
                        raise ValueError(f"Wrong values: {el}")
                    except IndexError:
                        raise IndexError(f"Not enough operands: {el}")
                    except ZeroDivisionError:
                        raise ZeroDivisionError("Cannot divide by zero")
                    except:
                        raise Exception("Something went wrong.")

        try:
            res = float(expr_list[0])
            res = res if not res.is_integer() else int(res)
            res = str(res).replace('.',',')
        except IndexError:
            res = ''
        except:
            raise Exception("Something went wrong.")

        return res

    ## @brief Calculates the result and stores it in @p mem
    def mSet(self):
        self.mem = self.calculate()
    
    ## @brief Enters the value stored in @p mem
    def mRecall(self):
        if self.mem:
            self.enterNum(self.mem)

    ## @brief Sets @p mem to None
    def mClear(self):
        self.mem = None

    ## @brief Enters the last calculated result if possible
    def answer(self):
        if self.ans:
            self.enterNum(self.ans)
    
    ## @brief Opens guide.pdf file
    def showHelp(self):
        os.startfile(os.path.join(os.getcwd(), 'src', 'guide.pdf'))

if __name__ == "__main__":
    import sys
    ## QApplication instance
    app = QtWidgets.QApplication(sys.argv)
    ## QMainWindow instance
    MainWindow = QtWidgets.QMainWindow()
    ## CalcMainWindow instance
    ui = CalcMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())