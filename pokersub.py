# -*- coding: utf-8 -*-
"""

@author: Luis Martinez
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'substation.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow,QSizePolicy, QMessageBox,QWidget, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)

import sys
import random
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from matplotlib import pyplot as plt

import matplotlib.animation as animation
from matplotlib import style
import sys
import numpy as np
import pokerPlots
#from window_at_load_level import Ui_Form as Form 
#from window_at_load_level import Ui_Form



####################################################################################


class Window(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        #self.
        self.label = QLabel("What would you like to do?", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#       self.label.setAlignment(Qt.AlignCenter)
        #self.label.setStyleSheet("QLabel {background-color: red;}")

        self.button = QPushButton("Open Breaker", self)
        self.button2 = QPushButton("Close Breaker", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)    
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreaker)
        self.button2.clicked.connect(self.CloseBreaker)
        ######################################################
    def OpenBreaker(self):
        print('Opening  Breaker')
    def CloseBreaker(self):
        print('Closing Breaker')
        
        
##############################################################################################



class Ui_MainWindow(QWidget):
    def click1(self):
        if not hasattr(self, 'dialog'):
            self.dialog= Window(self)
        self.dialog.show()
        print("1 Clicked")
    def click2(self):
        if not hasattr(self, 'dialog'):
            self.dialog= Window(self)
        self.dialog.show()
        print("2 Clicked")
    def click3(self):
        if not hasattr(self, 'dialog'):
            self.dialog= Window(self)
        self.dialog.show()
        print("3 Clicked")   
    def click4(self):
        if not hasattr(self, 'dialog'):
            self.dialog= Window(self)
        self.dialog.show()
        print("4 Clicked")
    def clickMom(self):
        if not hasattr(self, 'dialog'):
            self.dialog= Window(self)
        self.dialog.show()
        print("Mother Clicked")
   
  ############################## Main Window ##################################  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(130, 100, 20, 81))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 180, 81, 3))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.brkr4_A = QtWidgets.QPushButton(self.centralwidget)
        self.brkr4_A.setGeometry(QtCore.QRect(160, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr4_A.setFont(font)
        self.brkr4_A.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr4_A.setObjectName("brkr4_A")
        ############ Button Event ##############
        self.brkr4_A.clicked.connect(self.click4)
        ########################################
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(140, 90, 81, 16))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.brkr2_A = QtWidgets.QPushButton(self.centralwidget)
        self.brkr2_A.setGeometry(QtCore.QRect(120, 120, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr2_A.setFont(font)
        self.brkr2_A.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr2_A.setObjectName("brkr2_A")
        ############ Button Event ##############
        self.brkr2_A.clicked.connect(self.click2)
        ########################################
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 60, 20, 41))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(210, 100, 20, 81))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.brkr1_A = QtWidgets.QPushButton(self.centralwidget)
        self.brkr1_A.setGeometry(QtCore.QRect(160, 80, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr1_A.setFont(font)
        self.brkr1_A.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr1_A.setObjectName("brkr1_A")
        ############ Button Event ##############
        self.brkr1_A.clicked.connect(self.click1)
        ########################################
        self.ace_label = QtWidgets.QLabel(self.centralwidget)
        self.ace_label.setGeometry(QtCore.QRect(210, 42, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.ace_label.setFont(font)
        self.ace_label.setObjectName("ace_label")
        self.brkr3_A = QtWidgets.QPushButton(self.centralwidget)
        self.brkr3_A.setGeometry(QtCore.QRect(200, 120, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr3_A.setFont(font)
        self.brkr3_A.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr3_A.setObjectName("brkr3_A")
        ############ Button Event ##############
        self.brkr3_A.clicked.connect(self.click3)
        ########################################
        self.mother_ace = QtWidgets.QPushButton(self.centralwidget)
        self.mother_ace.setGeometry(QtCore.QRect(70, 40, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.mother_ace.setFont(font)
        self.mother_ace.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mother_ace.setObjectName("mother_ace")
        ############ Button Event ##############
        self.mother_ace.clicked.connect(self.clickMom)
        ########################################
        self.line_30 = QtWidgets.QFrame(self.centralwidget)
        self.line_30.setGeometry(QtCore.QRect(110, 50, 31, 16))
        self.line_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_30.setLineWidth(3)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setObjectName("line_30")
        MainWindow.setCentralWidget(self.centralwidget)
       
        ######################################################
        layout = QGridLayout()
        ##This is where the embedded widgets which hold the live plots live. If
        ##there are performance issues we will use pyqtgraph which is suppossed
        ##to be built for perfomrance
        #This is we call the canvas and put it in the main gui(or centralwidget). 
        self.PowPlotHouse1 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse2 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse3 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse4 = QtWidgets.QWidget(self.centralwidget)
        #Create the layout horizontally of the plots above
        #if we want a vertical layout QVBoxLayout()
        
        #lay = QHBoxLayout(self.PowPlotHouse1)
        #lay2 = QHBoxLayout(self.PowPlotHouse2)
        
        #We call the function with the plot or idata to create the plot
        power = dynPlot1(self.PowPlotHouse1, width=2, height=1, dpi=80)
        power2 = dynPlot2(self.PowPlotHouse2, width=2, height=1, dpi=80)
        power3 = dynPlot3(self.PowPlotHouse3, width=2, height=1, dpi=80)  
        power4 = dynPlot4(self.PowPlotHouse4, width=2, height=1, dpi=80)

        #Location and name in the GUI of the widget
        #self.PowPlotHouse1.setGeometry(QtCore.QRect(1190, 20, 374, 350))
        #self.PowPlotHouse1.setObjectName("Plot of Power")

        #self.PowPlotHouse2.setGeometry(QtCore.QRect(1190, 380, 375, 350))
        #self.PowPlotHouse2.setObjectName("Plot of Power")
        
        
        layout.addWidget(power,1,1 )
        layout.addWidget(power2,1,2)
        layout.addWidget(power3,2,1)
        layout.addWidget(power4,2,2)
                
        self.PowPlotHouse1.setFocus()
        self.PowPlotHouse2.setFocus()
        self.PowPlotHouse3.setFocus()
        self.PowPlotHouse4.setFocus()

        
        #Here we set the size of different rows and columnsof the gridlayout
        #QGridLayout.setRowMinimumHeight (self, int row, int minSize)
        #minSize in pixels
         
        #range(start, end, step)
        #for r in range(0,8, 2):
            #for c in range(0,8,2):
        layout.setColumnMinimumWidth(0,300)
        layout.setRowMinimumHeight(1,300)
        layout.setRowMinimumHeight(2,300)
        

        self.centralwidget.setLayout(layout)
        self.centralwidget.show()



        ####################Menu Bar#########################3
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionAll_Substations = QtWidgets.QAction(MainWindow)
        self.actionAll_Substations.setObjectName("actionAll_Substations")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Poker Substation"))
        self.brkr4_A.setText(_translate("MainWindow", "4"))
        self.brkr2_A.setText(_translate("MainWindow", "2"))
        self.brkr1_A.setText(_translate("MainWindow", "1"))
        self.ace_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Poker</span></p></body></html>"))
        self.brkr3_A.setText(_translate("MainWindow", "3"))
        self.mother_ace.setText(_translate("MainWindow", "Mother"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionAll_Substations.setText(_translate("MainWindow", "All Substations"))

from pokerPlots import dynPlot1, dynPlot2, dynPlot3, dynPlot4

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

