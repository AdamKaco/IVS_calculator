# -*- coding: utf-8 -*-

## @file calc_view.py
# @author Simon Kosina
# @date 28.3.2020
# @brief View component of the calculator app

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

## @mainpage IVS Calculator
# @tableofcontents
# @section intro Introduction
# This is a documentation for the second project in the IVS course, created by @b xbaris03, @b xkaco00, @b xkosin09.
# The project is a simple calculator app written in Python (using PyQt5 and Qt Creator), which manages to do addition, subtraction, multiplication, division,
# exponentation, calculating the n-th root, factorial and combination number. Here you will also find the @ref man and the @ref install.
# @section install Installation guide
# TODO
# @section man Manual
# Simple guide created for the purpose of explaining the usage of the app. It can also be accessed from within the application by clicking on
# Help -> View Help or pressing the Shift + H keyboard shortcut.
# @subsection man1 Inserting numbers and operators.
# Numbers and operators can be entered either by pressing the representing buttons or by pressing the keys 0-9, +, -, *, /, ^ (must be pressed twice),
# ! or c. The √ symbol can be also entered by the Shift + V keyboard shortcut.
# @n The calculator won't allow you to insert two or more operators in a row, except for the minus sign and the factorial:
# @n @li - - will be interpreted as a +
# @n @li ! must be followed by an operator
# @subsection man2 Using the operators.
# Following rules apply:
# @li @b + Expects 2 arguments. Can be followed by a - sign.Supports integers and also real numbers, e.g. 3.5+4, 2+-1 ...
# @li @b - Same rules as for +. '- -' will be interpreted as '+', e.g. 1--1 = 1+1 ...
# @li @b * Same rules as for +.
# @li @b / Same rules as for +, but the second operand cannot be 0, e.g. 1/0 will result in an error
# @li @b * Expects 2 arguments. First argument can be either integer or a real number. Second argument can only be an integer 
# (positive or negative). Doesn't work if the first argument is 0 and second argument is negative.
# @n - Working examples: 7^2, -7^2, 7.3^2, 7^-2 ...
# @n - Results in an error: 0^-1, 1^2.3, 1^-2.3 ...
# @li @b √ Expects 2 arguments. First argument must be an integer (positive or negative). Second argument can be an integer or a real number.
# Results in an error if the first argument is 0, first argument is negative and second argument is 0, also doesn't work if the first argument is even and second
# argument is negative.
# @n - Working examples: 2√2, -2√2, 2√2.1, 0√0 ...
# @n - Results in an error: 0√3, -2√0, 1.5√2, 2√-1, -2√-2...
# @li @b ! Excepts 1 argument on the left, must be followed by an operator. The argument needs to be a non-negative integer, e.g. 0!, 2! ...
# @li @b C Excepts 2 arguments, both must be non-negative and the first argument needs to be bigger or equal to the second one, e.g. 0C0, 2C1 ... 
# @subsection man3 Equal and erase buttons
# When the = button is clicked (or by pressing Enter) the expression is evaluated and the result appears on the screen. If an error has occurred then
# the error info is displayed. You can use the result immediately in the next calculation by entering an operator or remove it from the screen
# by using the ⌫ button or by entering a number. Last result can be accessed by clicking the ANS button. 
# @n By clicking the ⌫ button (or by pressing Backspace) you are able to remove the rightmost character or the whole result (as described above).
# @subsection man4 Operator priorities.
# Operators are organized into 4 categories. The order of evaluation is from top to bottom. Operators of equal priorities are
# evaluated from left to right as entered in the expression in the calculator (not by the order shown below!).
# @n The categories are:
# @li !, C
# @li √, ^
# @li *, /
# @li +, -
# @subsection man5 Using the ANS, MR, MC, MS buttons.
# Used by clicking the buttons or by keyboard shortcuts Shit + A (ANS), Shift + R (MR), Shift + C (MC), Shift + S (MS)
# @n Actions performed when used:
# @li @b ANS If there is any previous result available, it will be entered otherwise nothing will happen.
# @li @b MS Calculates the currently entered expression and stores the result.
# @li @b MR If available enters the stored value, otherwise nothing happens.
# @li @b MC Clears the stored value (won't be available for further usage).
# @subsection man6 Keyboard shortcuts round-up
# List of all keyboard shortcuts:
# @li @b 0-9 chosen number is entered
# @li @b , enters the decimal comma
# @li @b Shift @b + @b A represents the @b ANS button
# @li @b Shift @b + @b R represents the @b MR button
# @li @b Shift @b + @b C represents the @b MC button
# @li @b Shift @b + @b S represents the @b MS button
# @li @b Shift @b + @b H opens the guide
# @li @b Shift @b + @b V enters the √ symbol
# @li @b +, @b -, @b *, @b /, @b ^, @b !, @b c chosen operator is entered
# @li @b Backspace represents the ⌫ button
# @li @b Enter represents the equal button

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

## @brief Implements the UI of the calculator app.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Calculator")
        MainWindow.resize(410, 500)
        MainWindow.setMinimumSize(QtCore.QSize(410, 500))
        
        ## @brief Qt Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget.setObjectName("centralwidget")
        
        ## @brief Qt Vertical layout, holds the @p result and the @p gridLayout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        ## @brief Qt Grid Layout, holds the buttons
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        
        ## @brief Qt Label for displaying the result and entered text
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setSizePolicy(sizePolicy)
        self.result.setMinimumSize(QtCore.QSize(0, 60))
        self.result.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.result.setFont(font)
        self.result.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.result.setMouseTracking(False)
        self.result.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result.setWordWrap(False)
        self.result.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        
        ## @brief Triggers the @p enterNum method with argument @p 0
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setAutoDefault(False)
        self.button_0.setDefault(False)
        self.button_0.setFlat(False)
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 6, 0, 1, 2)
        
        ## @brief Triggers the @p enterNum method with argument @p 1
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 5, 0, 1, 1)
        
        ## @brief Triggers the @p enterNum method with argument @p 2
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 5, 1, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p 3
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 5, 2, 1, 1)
        
        ## @brief Triggers the @p enterNum method with argument @p 4
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 4, 0, 1, 1)
        
        ## @brief Triggers the @p enterNum method with argument @p 5
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 4, 1, 1, 1)
        
        ## @brief Triggers the @p enterNum method with argument @p 6
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 4, 2, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p 7
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 3, 0, 1, 1)
        
        ## @brief Triggers the @p enterNum method with argument @p 8
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 3, 1, 1, 1)
        
        ## @brief Triggers the @p enterNum method with argument @p 9
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 3, 2, 1, 1)
        
        ## @brief Triggers the @p enterDec method
        self.button_decim = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_decim.sizePolicy().hasHeightForWidth())
        self.button_decim.setSizePolicy(sizePolicy)
        self.button_decim.setObjectName("button_decim")
        self.gridLayout.addWidget(self.button_decim, 6, 2, 1, 1)
        
        ## @brief Triggers the @p enterMinus method
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        self.button_minus.setObjectName("button_minus")
        self.gridLayout.addWidget(self.button_minus, 5, 3, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p '+'
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        self.button_plus.setObjectName("button_plus")
        self.gridLayout.addWidget(self.button_plus, 4, 3, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p '*'
        self.button_mult = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_mult.sizePolicy().hasHeightForWidth())
        self.button_mult.setSizePolicy(sizePolicy)
        self.button_mult.setObjectName("button_mult")
        self.gridLayout.addWidget(self.button_mult, 2, 3, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p '/'
        self.button_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy)
        self.button_div.setObjectName("button_div")
        self.gridLayout.addWidget(self.button_div, 3, 3, 1, 1)

        ## @brief Triggers the @p enterOp method with argument @p '^'
        self.button_exp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_exp.sizePolicy().hasHeightForWidth())
        self.button_exp.setSizePolicy(sizePolicy)
        self.button_exp.setShortcut("")
        self.button_exp.setObjectName("button_exp")
        self.gridLayout.addWidget(self.button_exp, 1, 0, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p '2^'
        self.button_sq = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sq.sizePolicy().hasHeightForWidth())
        self.button_sq.setSizePolicy(sizePolicy)
        self.button_sq.setObjectName("button_sq")
        self.gridLayout.addWidget(self.button_sq, 2, 0, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p '√'
        self.button_root = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_root.sizePolicy().hasHeightForWidth())
        self.button_root.setSizePolicy(sizePolicy)
        self.button_root.setObjectName("button_root")
        self.gridLayout.addWidget(self.button_root, 1, 1, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p '2√'
        self.button_sqrt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sqrt.sizePolicy().hasHeightForWidth())
        self.button_sqrt.setSizePolicy(sizePolicy)
        self.button_sqrt.setObjectName("button_sqrt")
        self.gridLayout.addWidget(self.button_sqrt, 2, 1, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p '!'
        self.button_fact = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_fact.sizePolicy().hasHeightForWidth())
        self.button_fact.setSizePolicy(sizePolicy)
        self.button_fact.setObjectName("button_fact")
        self.gridLayout.addWidget(self.button_fact, 1, 2, 1, 1)
        
        ## @brief Triggers the @p enterOp method with argument @p 'C'
        self.button_C = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_C.sizePolicy().hasHeightForWidth())
        self.button_C.setSizePolicy(sizePolicy)
        self.button_C.setObjectName("button_C")
        self.gridLayout.addWidget(self.button_C, 2, 2, 1, 1)
        
        ## @brief Triggers the @p showRes method
        self.button_eq = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_eq.sizePolicy().hasHeightForWidth())
        self.button_eq.setSizePolicy(sizePolicy)
        self.button_eq.setObjectName("button_eq")
        self.gridLayout.addWidget(self.button_eq, 6, 3, 1, 1)
        
        ## @brief Triggers the @p erase method
        self.button_erase = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_erase.sizePolicy().hasHeightForWidth())
        self.button_erase.setSizePolicy(sizePolicy)
        self.button_erase.setObjectName("button_erase")
        self.gridLayout.addWidget(self.button_erase, 0, 3, 1, 1)
        
        ## @brief Triggers the @p mRecall method
        self.button_m_rec = QtWidgets.QPushButton(self.centralwidget)
        self.button_m_rec.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_m_rec.sizePolicy().hasHeightForWidth())
        self.button_m_rec.setSizePolicy(sizePolicy)
        self.button_m_rec.setObjectName("button_m_rec")
        self.gridLayout.addWidget(self.button_m_rec, 0, 0, 1, 1)
        
        ## @brief Triggers the @p mClear method
        self.button_m_clr = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_m_clr.sizePolicy().hasHeightForWidth())
        self.button_m_clr.setSizePolicy(sizePolicy)
        self.button_m_clr.setObjectName("button_m_clr")
        self.gridLayout.addWidget(self.button_m_clr, 0, 1, 1, 1)
        
        ## @brief Triggers the @p mSet method
        self.button_m_set = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_m_set.sizePolicy().hasHeightForWidth())
        self.button_m_set.setSizePolicy(sizePolicy)
        self.button_m_set.setObjectName("button_m_set")
        self.gridLayout.addWidget(self.button_m_set, 0, 2, 1, 1)
        
        ## @brief Triggers the @p answer method
        self.button_ans = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ans.sizePolicy().hasHeightForWidth())
        self.button_ans.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.button_ans.setFont(font)
        self.button_ans.setObjectName("button_ans")
        self.gridLayout.addWidget(self.button_ans, 1, 3, 1, 1)
        
        self.gridLayout.setRowMinimumHeight(0, 50)
        self.gridLayout.setRowMinimumHeight(1, 50)
        self.gridLayout.setRowMinimumHeight(2, 50)
        self.gridLayout.setRowMinimumHeight(3, 50)
        self.gridLayout.setRowMinimumHeight(4, 50)
        self.gridLayout.setRowMinimumHeight(5, 50)
        self.gridLayout.setRowMinimumHeight(6, 50)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        
        ## @brief Qt MenuBar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 26))
        self.menubar.setObjectName("menubar")
        
        ## @brief Qt Menu
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        
        ## @brief Triggers the @p showHelp method
        self.actionShow_manual = QtWidgets.QAction(MainWindow)
        self.actionShow_manual.setObjectName("actionShow_manual")
        self.menuMenu.addAction(self.actionShow_manual)
        self.menubar.addAction(self.menuMenu.menuAction())
        
        # Show manual
        self.actionShow_manual.triggered.connect(self.showHelp)

        # number buttons
        self.button_1.clicked.connect(lambda: self.enterNum(1))
        self.button_2.clicked.connect(lambda: self.enterNum(2))
        self.button_3.clicked.connect(lambda: self.enterNum(3))
        self.button_4.clicked.connect(lambda: self.enterNum(4))
        self.button_5.clicked.connect(lambda: self.enterNum(5))
        self.button_6.clicked.connect(lambda: self.enterNum(6))
        self.button_7.clicked.connect(lambda: self.enterNum(7))
        self.button_8.clicked.connect(lambda: self.enterNum(8))
        self.button_9.clicked.connect(lambda: self.enterNum(9))
        self.button_0.clicked.connect(lambda: self.enterNum(0))
        self.button_decim.clicked.connect(self.enterDec)

        # erase button
        self.button_erase.clicked.connect(self.erase)

        # operator buttons
        self.button_plus.clicked.connect(lambda: self.enterOp('+'))
        self.button_minus.clicked.connect(self.enterMinus)
        self.button_mult.clicked.connect(lambda: self.enterOp('*'))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        
        self.button_m_rec.setText(_translate("MainWindow", "MR"))
        self.button_m_rec.setShortcut(_translate("MainWindow", "Shift+R"))

        self.button_m_clr.setText(_translate("MainWindow", "MC"))
        self.button_m_clr.setShortcut(_translate("MainWindow", "Shift+C"))
        
        self.button_m_set.setText(_translate("MainWindow", "MS"))
        self.button_m_set.setShortcut(_translate("MainWindow", "Shift+S"))
        
        self.button_ans.setText(_translate("MainWindow", "ANS"))
        self.button_ans.setShortcut(_translate("MainWindow", "Shift+A"))
        
        self.button_sq.setText(_translate("MainWindow", "x^2"))
        
        self.button_sqrt.setText(_translate("MainWindow", "2√x"))
        
        self.button_mult.setText(_translate("MainWindow", "*"))
        self.button_mult.setShortcut(_translate("MainWindow", "*"))

        self.button_fact.setText(_translate("MainWindow", "!"))
        self.button_fact.setShortcut(_translate("MainWindow", "!"))

        self.button_exp.setText(_translate("MainWindow", "x^n"))
        self.button_exp.setShortcut(_translate("MainWindow", "Shift+6"))

        self.button_root.setText(_translate("MainWindow", "n√x"))
        self.button_root.setShortcut(_translate("MainWindow", "Shift+V"))
        
        self.button_div.setText(_translate("MainWindow", "/"))
        self.button_div.setShortcut(_translate("MainWindow", "/"))

        self.button_C.setText(_translate("MainWindow", "nCk"))
        self.button_C.setShortcut(_translate("MainWindow", "C"))

        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_7.setShortcut(_translate("MainWindow", "7"))

        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_8.setShortcut(_translate("MainWindow", "8"))

        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_9.setShortcut(_translate("MainWindow", "9"))

        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_4.setShortcut(_translate("MainWindow", "4"))

        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_5.setShortcut(_translate("MainWindow", "5"))

        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_6.setShortcut(_translate("MainWindow", "6"))

        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_1.setShortcut(_translate("MainWindow", "1"))

        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_2.setShortcut(_translate("MainWindow", "2"))
        
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_3.setShortcut(_translate("MainWindow", "3"))

        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_plus.setShortcut(_translate("MainWindow", "+"))

        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_minus.setShortcut(_translate("MainWindow", "-"))

        self.button_eq.setText(_translate("MainWindow", "="))
        self.button_eq.setShortcut(_translate("MainWindow", "Return"))

        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_0.setShortcut(_translate("MainWindow", "0"))

        self.button_decim.setText(_translate("MainWindow", ","))
        self.button_decim.setShortcut(_translate("MainWindow", ","))

        self.button_erase.setText(_translate("MainWindow", "⌫"))
        self.button_erase.setShortcut(_translate("MainWindow", "Backspace"))

        self.menuMenu.setTitle(_translate("MainWindow", "Help"))
        self.actionShow_manual.setText(_translate("MainWindow", "View Help"))
        self.actionShow_manual.setShortcut(_translate("MainWindow", "Shift+H"))

        self.result.setText(_translate("MainWindow", ""))
