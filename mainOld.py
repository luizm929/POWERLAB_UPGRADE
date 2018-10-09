# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1371, 866)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1350, 751))
        self.tabWidget.setMaximumSize(QtCore.QSize(1350, 1200))
        self.tabWidget.setObjectName("tabWidget")
        self.Resistive = QtWidgets.QWidget()
        self.Resistive.setObjectName("Resistive")
        self.frame = QtWidgets.QFrame(self.Resistive)
        self.frame.setEnabled(False)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 1341, 721))
        self.frame.setMaximumSize(QtCore.QSize(1350, 1200))
        self.frame.setStyleSheet("border-image: url(:/img/Resistive.png);")

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnR1 = QtWidgets.QPushButton(self.frame)
        self.btnR1.setEnabled(False)
        self.btnR1.setGeometry(QtCore.QRect(130, 290, 65, 65))
        self.btnR1.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR1.setAutoFillBackground(False)
        self.btnR1.setStyleSheet("#btnR1 {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnR1:checked\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnR1.setText("")
        self.btnR1.setCheckable(True)
        self.btnR1.setAutoDefault(False)
        self.btnR1.setObjectName("btnR1")
        self.btnR2 = QtWidgets.QPushButton(self.frame)
        self.btnR2.setEnabled(False)
        self.btnR2.setGeometry(QtCore.QRect(240, 290, 65, 65))
        self.btnR2.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR2.setAutoFillBackground(False)
        self.btnR2.setStyleSheet("#btnR2 {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnR2:checked\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnR2.setText("")
        self.btnR2.setCheckable(True)
        self.btnR2.setAutoDefault(False)
        self.btnR2.setObjectName("btnR2")
        self.btnR3 = QtWidgets.QPushButton(self.frame)
        self.btnR3.setEnabled(False)
        self.btnR3.setGeometry(QtCore.QRect(350, 290, 65, 65))
        self.btnR3.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR3.setAutoFillBackground(False)
        self.btnR3.setStyleSheet("#btnR3 {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnR3:checked\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnR3.setText("")
        self.btnR3.setCheckable(True)
        self.btnR3.setAutoDefault(False)
        self.btnR3.setObjectName("btnR3")
        self.btnR4 = QtWidgets.QPushButton(self.frame)
        self.btnR4.setEnabled(False)
        self.btnR4.setGeometry(QtCore.QRect(520, 290, 65, 65))
        self.btnR4.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR4.setAutoFillBackground(False)
        self.btnR4.setStyleSheet("#btnR4 {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnR4:checked\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnR4.setText("")
        self.btnR4.setCheckable(True)
        self.btnR4.setAutoDefault(False)
        self.btnR4.setObjectName("btnR4")
        self.btnR5 = QtWidgets.QPushButton(self.frame)
        self.btnR5.setEnabled(False)
        self.btnR5.setGeometry(QtCore.QRect(630, 290, 65, 65))
        self.btnR5.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR5.setAutoFillBackground(False)
        self.btnR5.setStyleSheet("#btnR5 {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnR5:checked\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnR5.setText("")
        self.btnR5.setCheckable(True)
        self.btnR5.setAutoDefault(False)
        self.btnR5.setObjectName("btnR5")
        self.btnR7 = QtWidgets.QPushButton(self.frame)
        self.btnR7.setEnabled(False)
        self.btnR7.setGeometry(QtCore.QRect(910, 290, 65, 65))
        self.btnR7.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR7.setAutoFillBackground(False)
        self.btnR7.setStyleSheet("#btnR7 {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnR7:checked\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnR7.setText("")
        self.btnR7.setCheckable(True)
        self.btnR7.setAutoDefault(False)
        self.btnR7.setObjectName("btnR7")
        self.btnR9 = QtWidgets.QPushButton(self.frame)
        self.btnR9.setEnabled(False)
        self.btnR9.setGeometry(QtCore.QRect(1130, 290, 65, 65))
        self.btnR9.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR9.setAutoFillBackground(False)
        self.btnR9.setStyleSheet("#btnR9 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnR9:checked {\n"
"background-color: green;\n"
"}")
        self.btnR9.setText("")
        self.btnR9.setCheckable(True)
        self.btnR9.setAutoDefault(False)
        self.btnR9.setObjectName("btnR9")
        self.btnR8 = QtWidgets.QPushButton(self.frame)
        self.btnR8.setEnabled(False)
        self.btnR8.setGeometry(QtCore.QRect(1020, 290, 65, 65))
        self.btnR8.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR8.setAutoFillBackground(False)
        self.btnR8.setStyleSheet("#btnR8 {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnR8:checked\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnR8.setText("")
        self.btnR8.setCheckable(True)
        self.btnR8.setAutoDefault(False)
        self.btnR8.setObjectName("btnR8")
        self.btnR6 = QtWidgets.QPushButton(self.frame)
        self.btnR6.setEnabled(False)
        self.btnR6.setGeometry(QtCore.QRect(740, 290, 65, 65))
        self.btnR6.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR6.setAutoFillBackground(False)
        self.btnR6.setStyleSheet("#btnR6 {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnR6:checked\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnR6.setText("")
        self.btnR6.setCheckable(True)
        self.btnR6.setAutoDefault(False)
        self.btnR6.setObjectName("btnR6")
        self.btnAllOff = QtWidgets.QPushButton(self.frame)
        self.btnAllOff.setEnabled(False)
        self.btnAllOff.setGeometry(QtCore.QRect(10, 10, 80, 80))
        self.btnAllOff.setMaximumSize(QtCore.QSize(80, 80))
        self.btnAllOff.setAutoFillBackground(False)
        self.btnAllOff.setStyleSheet("QPushButton#btnAllOff {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:40px;\n"
"max-width:80px;\n"
"max-height:80px;\n"
"min-width:80px;\n"
"min-height:80px;\n"
"border-style: outset;\n"
"border-color: white;    \n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"QPushButton#btnAllOff:checked:hover\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnAllOff.setCheckable(True)
        self.btnAllOff.setAutoDefault(False)
        self.btnAllOff.setObjectName("btnAllOff")
        self.btnAllOn = QtWidgets.QPushButton(self.frame)
        self.btnAllOn.setEnabled(False)
        self.btnAllOn.setGeometry(QtCore.QRect(1240, 10, 80, 80))
        self.btnAllOn.setMaximumSize(QtCore.QSize(80, 80))
        self.btnAllOn.setAutoFillBackground(False)
        self.btnAllOn.setStyleSheet("QPushButton#btnAllOn {\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"background-color: red;\n"
"border-radius:40px;\n"
"max-width:80px;\n"
"max-height:80px;\n"
"min-width:80px;\n"
"min-height:80px;\n"
"border-style: outset;\n"
"border-color: white;    \n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"QPushButton#btnAllOn:checked:hover\n"
"{\n"
"    background-color: green;\n"
"}")
        self.btnAllOn.setCheckable(True)
        self.btnAllOn.setAutoDefault(False)
        self.btnAllOn.setObjectName("btnAllOn")
        self.tabWidget.addTab(self.Resistive, "")
        self.Inductive = QtWidgets.QWidget()
        self.Inductive.setObjectName("Inductive")
        self.frame_3 = QtWidgets.QFrame(self.Inductive)
        self.frame_3.setGeometry(QtCore.QRect(-1, -1, 1341, 721))
        self.frame_3.setMaximumSize(QtCore.QSize(1350, 1200))
        self.frame_3.setStyleSheet("border-image: url(:/img/Ind.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnL1 = QtWidgets.QPushButton(self.frame_3)
        self.btnL1.setEnabled(False)
        self.btnL1.setGeometry(QtCore.QRect(140, 290, 65, 65))
        self.btnL1.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL1.setAutoFillBackground(False)
        self.btnL1.setStyleSheet("#btnL1 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL1:checked {\n"
"background-color: green;\n"
"}")
        self.btnL1.setText("")
        self.btnL1.setCheckable(True)
        self.btnL1.setAutoDefault(False)
        self.btnL1.setObjectName("btnL1")
        self.btnL2 = QtWidgets.QPushButton(self.frame_3)
        self.btnL2.setEnabled(False)
        self.btnL2.setGeometry(QtCore.QRect(240, 290, 65, 65))
        self.btnL2.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL2.setAutoFillBackground(False)
        self.btnL2.setStyleSheet("#btnL2 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL2:checked {\n"
"background-color: green;\n"
"}")
        self.btnL2.setText("")
        self.btnL2.setCheckable(True)
        self.btnL2.setAutoDefault(False)
        self.btnL2.setObjectName("btnL2")
        self.btnL3 = QtWidgets.QPushButton(self.frame_3)
        self.btnL3.setEnabled(False)
        self.btnL3.setGeometry(QtCore.QRect(350, 290, 65, 65))
        self.btnL3.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL3.setAutoFillBackground(False)
        self.btnL3.setStyleSheet("#btnL3 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL3:checked {\n"
"background-color: green;\n"
"}")
        self.btnL3.setText("")
        self.btnL3.setCheckable(True)
        self.btnL3.setAutoDefault(False)
        self.btnL3.setObjectName("btnL3")
        self.btnL4 = QtWidgets.QPushButton(self.frame_3)
        self.btnL4.setEnabled(False)
        self.btnL4.setGeometry(QtCore.QRect(520, 290, 65, 65))
        self.btnL4.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL4.setAutoFillBackground(False)
        self.btnL4.setStyleSheet("#btnL4 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL4:checked {\n"
"background-color: green;\n"
"}")
        self.btnL4.setText("")
        self.btnL4.setCheckable(True)
        self.btnL4.setAutoDefault(False)
        self.btnL4.setObjectName("btnL4")
        self.btnL5 = QtWidgets.QPushButton(self.frame_3)
        self.btnL5.setEnabled(False)
        self.btnL5.setGeometry(QtCore.QRect(630, 290, 65, 65))
        self.btnL5.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL5.setAutoFillBackground(False)
        self.btnL5.setStyleSheet("#btnL5 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL5:checked {\n"
"background-color: green;\n"
"}")
        self.btnL5.setText("")
        self.btnL5.setCheckable(True)
        self.btnL5.setAutoDefault(False)
        self.btnL5.setObjectName("btnL5")
        self.btnL6 = QtWidgets.QPushButton(self.frame_3)
        self.btnL6.setEnabled(False)
        self.btnL6.setGeometry(QtCore.QRect(730, 290, 65, 65))
        self.btnL6.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL6.setAutoFillBackground(False)
        self.btnL6.setStyleSheet("#btnL6 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL6:checked {\n"
"background-color: green;\n"
"}")
        self.btnL6.setText("")
        self.btnL6.setCheckable(True)
        self.btnL6.setAutoDefault(False)
        self.btnL6.setObjectName("btnL6")
        self.btnL1_7 = QtWidgets.QPushButton(self.frame_3)
        self.btnL1_7.setEnabled(False)
        self.btnL1_7.setGeometry(QtCore.QRect(1340, 630, 65, 65))
        self.btnL1_7.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL1_7.setAutoFillBackground(False)
        self.btnL1_7.setStyleSheet("#btnL1 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL1:checked {\n"
"background-color: green;\n"
"}")
        self.btnL1_7.setText("")
        self.btnL1_7.setCheckable(True)
        self.btnL1_7.setAutoDefault(False)
        self.btnL1_7.setObjectName("btnL1_7")
        self.btnL7 = QtWidgets.QPushButton(self.frame_3)
        self.btnL7.setEnabled(False)
        self.btnL7.setGeometry(QtCore.QRect(910, 290, 65, 65))
        self.btnL7.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL7.setAutoFillBackground(False)
        self.btnL7.setStyleSheet("#btnL7 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL7:checked {\n"
"background-color: green;\n"
"}")
        self.btnL7.setText("")
        self.btnL7.setCheckable(True)
        self.btnL7.setAutoDefault(False)
        self.btnL7.setObjectName("btnL7")
        self.btnL8 = QtWidgets.QPushButton(self.frame_3)
        self.btnL8.setEnabled(False)
        self.btnL8.setGeometry(QtCore.QRect(1020, 290, 65, 65))
        self.btnL8.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL8.setAutoFillBackground(False)
        self.btnL8.setStyleSheet("#btnL8 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL8:checked {\n"
"background-color: green;\n"
"}")
        self.btnL8.setText("")
        self.btnL8.setCheckable(True)
        self.btnL8.setAutoDefault(False)
        self.btnL8.setObjectName("btnL8")
        self.btnL9 = QtWidgets.QPushButton(self.frame_3)
        self.btnL9.setEnabled(False)
        self.btnL9.setGeometry(QtCore.QRect(1130, 290, 65, 65))
        self.btnL9.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL9.setAutoFillBackground(False)
        self.btnL9.setStyleSheet("#btnL9 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnL9:checked {\n"
"background-color: green;\n"
"}")
        #-----------modified
        capPix = QPixmap('img/Cap.png')
        #----------------------------
        self.btnL9.setText("")
        self.btnL9.setCheckable(True)
        self.btnL9.setAutoDefault(False)
        self.btnL9.setObjectName("btnL9")
        self.tabWidget.addTab(self.Inductive, "")
        self.Capacitive = QtWidgets.QWidget()
        self.Capacitive.setObjectName("Capacitive")
        self.label = QtWidgets.QLabel(self.Capacitive)
        self.label.setGeometry(QtCore.QRect(0, 0, 1341, 721))
        #----------------------------- modified
        self.label.setScaledContents(True)
        self.label.setPixmap(capPix)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.label.setSizePolicy(sizePolicy)
        #------------------------------modified
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnC9 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC9.setEnabled(False)
        self.btnC9.setGeometry(QtCore.QRect(1130, 290, 65, 65))
        self.btnC9.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC9.setAutoFillBackground(False)
        self.btnC9.setStyleSheet("#btnC9 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnC9:checked {\n"
"background-color: green;\n"
"}")
        self.btnC9.setText("")
        self.btnC9.setCheckable(True)
        self.btnC9.setAutoDefault(False)
        self.btnC9.setObjectName("btnC9")
        self.btnC8 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC8.setEnabled(False)
        self.btnC8.setGeometry(QtCore.QRect(1020, 290, 65, 65))
        self.btnC8.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC8.setAutoFillBackground(False)
        self.btnC8.setStyleSheet("#btnC8 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnC8:checked {\n"
"background-color: green;\n"
"}")
        self.btnC8.setText("")
        self.btnC8.setCheckable(True)
        self.btnC8.setAutoDefault(False)
        self.btnC8.setObjectName("btnC8")
        self.btnC7 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC7.setEnabled(False)
        self.btnC7.setGeometry(QtCore.QRect(920, 290, 65, 65))
        self.btnC7.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC7.setAutoFillBackground(False)
        self.btnC7.setStyleSheet("#btnC7 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnC7:checked {\n"
"background-color: green;\n"
"}")
        self.btnC7.setText("")
        self.btnC7.setCheckable(True)
        self.btnC7.setAutoDefault(False)
        self.btnC7.setObjectName("btnC7")
        self.btnC6 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC6.setEnabled(False)
        self.btnC6.setGeometry(QtCore.QRect(730, 300, 65, 65))
        self.btnC6.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC6.setAutoFillBackground(False)
        self.btnC6.setStyleSheet("#btnC6 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnC6:checked {\n"
"background-color: green;\n"
"}")
        self.btnC6.setText("")
        self.btnC6.setCheckable(True)
        self.btnC6.setAutoDefault(False)
        self.btnC6.setObjectName("btnC6")
        self.btnC5 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC5.setEnabled(False)
        self.btnC5.setGeometry(QtCore.QRect(630, 290, 65, 65))
        self.btnC5.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC5.setAutoFillBackground(False)
        self.btnC5.setStyleSheet("#btnC5 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnC5:checked {\n"
"background-color: green;\n"
"}")
        self.btnC5.setText("")
        self.btnC5.setCheckable(True)
        self.btnC5.setAutoDefault(False)
        self.btnC5.setObjectName("btnC5")
        self.btnC4 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC4.setEnabled(False)
        self.btnC4.setGeometry(QtCore.QRect(530, 300, 65, 65))
        self.btnC4.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC4.setAutoFillBackground(False)
        self.btnC4.setStyleSheet("#btnC4 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnC4:checked {\n"
"background-color: green;\n"
"}")
        self.btnC4.setText("")
        self.btnC4.setCheckable(True)
        self.btnC4.setAutoDefault(False)
        self.btnC4.setObjectName("btnC4")
        self.btnC3 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC3.setEnabled(False)
        self.btnC3.setGeometry(QtCore.QRect(360, 300, 65, 65))
        self.btnC3.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC3.setAutoFillBackground(False)
        self.btnC3.setStyleSheet("#btnC3 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnC3:checked {\n"
"background-color: green;\n"
"}")
        self.btnC3.setText("")
        self.btnC3.setCheckable(True)
        self.btnC3.setAutoDefault(False)
        self.btnC3.setObjectName("btnC3")
        self.btnC2 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC2.setEnabled(False)
        self.btnC2.setGeometry(QtCore.QRect(240, 280, 65, 65))
        self.btnC2.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC2.setAutoFillBackground(False)
        self.btnC2.setStyleSheet("#btnC2 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnC2:checked {\n"
"background-color: green;\n"
"}")
        self.btnC2.setText("")
        self.btnC2.setCheckable(True)
        self.btnC2.setAutoDefault(False)
        self.btnC2.setObjectName("btnC2")
        self.btnC1 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC1.setEnabled(False)
        self.btnC1.setGeometry(QtCore.QRect(140, 290, 65, 65))
        self.btnC1.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC1.setAutoFillBackground(False)
        self.btnC1.setStyleSheet("#btnC1 {\n"
"background-color: red;\n"
"border-image: url(:/img/Power_off_icon.png);\n"
"border-radius:32px;\n"
"max-width:65px;\n"
"max-height:65px;\n"
"min-width:65px;\n"
"min-height:65px;\n"
"}\n"
"#btnC1:checked {\n"
"background-color: green;\n"
"}")
        self.btnC1.setText("")
        self.btnC1.setCheckable(True)
        self.btnC1.setAutoDefault(False)
        self.btnC1.setObjectName("btnC1")
        self.tabWidget.addTab(self.Capacitive, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1371, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnR1.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR2.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR3.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR4.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR5.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR7.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR9.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR8.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR6.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnAllOff.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnAllOff.setText(_translate("MainWindow", "All Off"))
        self.btnAllOn.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnAllOn.setText(_translate("MainWindow", "All On"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Resistive), _translate("MainWindow", "Resistive Loads"))
        self.btnL1.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL2.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL3.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL4.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL5.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL6.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL1_7.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL7.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL8.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL9.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inductive), _translate("MainWindow", "Inductive Loads"))
        self.btnC9.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC8.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC7.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC6.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC5.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC4.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC3.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC2.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC1.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Capacitive), _translate("MainWindow", "Capacitive Loads"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))

import resources_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

