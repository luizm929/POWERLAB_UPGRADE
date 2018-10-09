#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------
# Packages needed
#Matplotlib
#Python3
#PyQt5
#
#------------------------------------------------------------
#
# Written by Luis Martinez : luizmartines@gmail.com
#                          : luizm929@nmsu.edu
# Thanks to Jose Tabarez for his help.
#------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1690, 935)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setSizeIncrement(QtCore.QSize(1, 0))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 252);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(61, 144, 9, 516))
        self.pushButton_15.setMinimumSize(QtCore.QSize(1, 500))
        self.pushButton_15.setMaximumSize(QtCore.QSize(32, 600))
        self.pushButton_15.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_15.setStyleSheet("#pushButton_15{\n"
"background-color: green;\n"
"border-style: outset;\n"
"\n"
"\n"
"}\n"
"#pushButton_15:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_15.setText("")
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(84, 13, 31, 31))
        self.pushButton_34.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_34.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_34.setStyleSheet("#pushButton_34{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_34:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_34.setText("")
        self.pushButton_34.setCheckable(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(70, 24, 15, 9))
        self.pushButton_35.setMinimumSize(QtCore.QSize(15, 9))
        self.pushButton_35.setStyleSheet("#pushButton_35{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_35:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_35.setText("")
        self.pushButton_35.setCheckable(True)
        self.pushButton_35.setObjectName("pushButton_35")
        self.Ace_LoadBulbButton = QtWidgets.QPushButton(self.centralwidget)
        self.Ace_LoadBulbButton.setGeometry(QtCore.QRect(18, 0, 53, 53))
        self.Ace_LoadBulbButton.setStyleSheet("#Ace_LoadBulbButton{\n"
"border-image: url(:/img/Outliner_Mac_greyBulb.png);\n"
"background-color: gray;\n"
"border-style: outset;\n"
"padding:2px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"}\n"
"#Ace_LoadBulbButton:checked{\n"
"border-color: rgb(255, 0, 0);\n"
"border-image: url(:/img/lightBulb.svg);\n"
"}")
        self.Ace_LoadBulbButton.setText("")
        self.Ace_LoadBulbButton.setCheckable(True)
        self.Ace_LoadBulbButton.setObjectName("Ace_LoadBulbButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(70, 32, 251, 224))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_12.setGeometry(QtCore.QRect(31, 191, 46, 9))
        self.pushButton_12.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_12.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_12.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_12.setStyleSheet("#pushButton_12{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_12:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_12.setText("")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_14.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.pushButton_8.setStyleSheet("#pushButton_8{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_8:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_21.setGeometry(QtCore.QRect(31, 23, 89, 9))
        self.pushButton_21.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_21.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_21.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_21.setStyleSheet("#pushButton_21{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_21:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_21.setText("")
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_31 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_31.setGeometry(QtCore.QRect(10, 67, 31, 31))
        self.pushButton_31.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_31.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_31.setStyleSheet("#pushButton_31{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_31:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_31.setText("")
        self.pushButton_31.setCheckable(True)
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_13.setGeometry(QtCore.QRect(129, 191, 89, 9))
        self.pushButton_13.setMinimumSize(QtCore.QSize(26, 4))
        self.pushButton_13.setMaximumSize(QtCore.QSize(300, 40))
        self.pushButton_13.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_13.setStyleSheet("#pushButton_13{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_13:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_13.setText("")
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_25.setGeometry(QtCore.QRect(129, 23, 15, 9))
        self.pushButton_25.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_25.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_25.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_25.setStyleSheet("#pushButton_25{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_25:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_25.setText("")
        self.pushButton_25.setCheckable(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_28.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.pushButton_28.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_28.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_28.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_28.setStyleSheet("#pushButton_28{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_28:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_28.setText("")
        self.pushButton_28.setCheckable(True)
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_24.setGeometry(QtCore.QRect(205, 135, 31, 31))
        self.pushButton_24.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_24.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_24.setStyleSheet("#pushButton_24{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_24:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_24.setText("")
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_33.setGeometry(QtCore.QRect(22, 120, 9, 80))
        self.pushButton_33.setStyleSheet("#pushButton_33{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_33:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_33.setText("")
        self.pushButton_33.setCheckable(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_26.setGeometry(QtCore.QRect(218, 121, 9, 15))
        self.pushButton_26.setStyleSheet("#pushButton_26{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_26:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_26.setText("")
        self.pushButton_26.setCheckable(True)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(76, 180, 31, 31))
        self.pushButton_5.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_5.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_5:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_32.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.pushButton_32.setStyleSheet("#pushButton_32{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_32:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_32.setText("")
        self.pushButton_32.setCheckable(True)
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_11.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.pushButton_11.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_11.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_11.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_11.setStyleSheet("#pushButton_11{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_11:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_11.setText("")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_27.setGeometry(QtCore.QRect(143, 12, 31, 31))
        self.pushButton_27.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_27.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_27.setStyleSheet("#pushButton_27{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_27:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_27.setText("")
        self.pushButton_27.setCheckable(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_9.setGeometry(QtCore.QRect(218, 32, 9, 80))
        self.pushButton_9.setStyleSheet("#pushButton_9{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_9:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_9.setText("")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_10.setGeometry(QtCore.QRect(218, 164, 9, 36))
        self.pushButton_10.setStyleSheet("#pushButton_10{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_10:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_10.setText("")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_17.setGeometry(QtCore.QRect(22, 23, 9, 45))
        self.pushButton_17.setStyleSheet("#pushButton_17{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_17:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_17.setText("")
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_29.setGeometry(QtCore.QRect(105, 191, 15, 9))
        self.pushButton_29.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_29.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_29.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_29.setStyleSheet("#pushButton_29{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_29:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_29.setText("")
        self.pushButton_29.setCheckable(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_20.setGeometry(QtCore.QRect(172, 23, 55, 9))
        self.pushButton_20.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_20.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_20.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_20.setStyleSheet("#pushButton_20{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_20:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_20.setText("")
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(1539, 144, 9, 516))
        self.pushButton_16.setMinimumSize(QtCore.QSize(1, 500))
        self.pushButton_16.setMaximumSize(QtCore.QSize(32, 600))
        self.pushButton_16.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_16.setStyleSheet("#pushButton_16{\n"
"background-color: green;\n"
"border-style: outset;\n"
"\n"
"\n"
"}\n"
"#pushButton_16:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_16.setText("")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setGeometry(QtCore.QRect(190, 256, 369, 9))
        self.pushButton_36.setMinimumSize(QtCore.QSize(50, 9))
        self.pushButton_36.setStyleSheet("#pushButton_36{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_36:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_36.setText("")
        self.pushButton_36.setCheckable(True)
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_38.setGeometry(QtCore.QRect(321, 651, 967, 9))
        self.pushButton_38.setMinimumSize(QtCore.QSize(50, 9))
        self.pushButton_38.setStyleSheet("#pushButton_38{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_38:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_38.setText("")
        self.pushButton_38.setCheckable(True)
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setGeometry(QtCore.QRect(320, 144, 968, 9))
        self.pushButton_39.setMinimumSize(QtCore.QSize(50, 9))
        self.pushButton_39.setStyleSheet("#pushButton_39{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_39:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_39.setText("")
        self.pushButton_39.setCheckable(True)
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(114, 24, 85, 9))
        self.pushButton_18.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_18.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_18.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_18.setStyleSheet("#pushButton_18{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_18:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_18.setText("")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(92, 129, 9, 15))
        self.pushButton_19.setStyleSheet("#pushButton_19{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_19:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_19.setText("")
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_74 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_74.setGeometry(QtCore.QRect(190, 530, 369, 9))
        self.pushButton_74.setMinimumSize(QtCore.QSize(50, 9))
        self.pushButton_74.setStyleSheet("#pushButton_74{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_74:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_74.setText("")
        self.pushButton_74.setCheckable(True)
        self.pushButton_74.setObjectName("pushButton_74")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 0, 83, 77))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_14.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_14.setMaximumSize(QtCore.QSize(80, 20))
        self.pushButton_14.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_14.setStyleSheet("#pushButton_14{\n"
"background-color: blue;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_14:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_3.addWidget(self.pushButton_14)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(70, 539, 251, 224))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_22.setGeometry(QtCore.QRect(31, 191, 46, 9))
        self.pushButton_22.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_22.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_22.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_22.setStyleSheet("#pushButton_22{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_22:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_22.setText("")
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_15.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_23.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.pushButton_23.setStyleSheet("#pushButton_23{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_23:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_23.setText("")
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_30.setGeometry(QtCore.QRect(31, 23, 89, 9))
        self.pushButton_30.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_30.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_30.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_30.setStyleSheet("#pushButton_30{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_30:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_30.setText("")
        self.pushButton_30.setCheckable(True)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_37 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_37.setGeometry(QtCore.QRect(10, 67, 31, 31))
        self.pushButton_37.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_37.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_37.setStyleSheet("#pushButton_37{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_37:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_37.setText("")
        self.pushButton_37.setCheckable(True)
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_40 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_40.setGeometry(QtCore.QRect(129, 191, 89, 9))
        self.pushButton_40.setMinimumSize(QtCore.QSize(26, 4))
        self.pushButton_40.setMaximumSize(QtCore.QSize(300, 40))
        self.pushButton_40.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_40.setStyleSheet("#pushButton_40{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_40:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_40.setText("")
        self.pushButton_40.setCheckable(True)
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_41.setGeometry(QtCore.QRect(129, 23, 15, 9))
        self.pushButton_41.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_41.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_41.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_41.setStyleSheet("#pushButton_41{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_41:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_41.setText("")
        self.pushButton_41.setCheckable(True)
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_42.setGeometry(QtCore.QRect(120, 0, 9, 33))
        self.pushButton_42.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_42.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_42.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_42.setStyleSheet("#pushButton_42{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_42:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_42.setText("")
        self.pushButton_42.setCheckable(True)
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_43.setGeometry(QtCore.QRect(205, 135, 31, 31))
        self.pushButton_43.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_43.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_43.setStyleSheet("#pushButton_43{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_43:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_43.setText("")
        self.pushButton_43.setCheckable(True)
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_44.setGeometry(QtCore.QRect(22, 120, 9, 80))
        self.pushButton_44.setStyleSheet("#pushButton_44{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_44:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_44.setText("")
        self.pushButton_44.setCheckable(True)
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_45.setGeometry(QtCore.QRect(218, 121, 9, 15))
        self.pushButton_45.setStyleSheet("#pushButton_45{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_45:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_45.setText("")
        self.pushButton_45.setCheckable(True)
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setGeometry(QtCore.QRect(76, 180, 31, 31))
        self.pushButton_6.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_6.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_6:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_46 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_46.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.pushButton_46.setStyleSheet("#pushButton_46{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_46:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_46.setText("")
        self.pushButton_46.setCheckable(True)
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_47.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.pushButton_47.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_47.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_47.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_47.setStyleSheet("#pushButton_47{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_47:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_47.setText("")
        self.pushButton_47.setCheckable(True)
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_48.setGeometry(QtCore.QRect(143, 12, 31, 31))
        self.pushButton_48.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_48.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_48.setStyleSheet("#pushButton_48{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_48:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_48.setText("")
        self.pushButton_48.setCheckable(True)
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_49.setGeometry(QtCore.QRect(218, 32, 9, 80))
        self.pushButton_49.setStyleSheet("#pushButton_49{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_49:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_49.setText("")
        self.pushButton_49.setCheckable(True)
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_50.setGeometry(QtCore.QRect(218, 164, 9, 36))
        self.pushButton_50.setStyleSheet("#pushButton_50{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_50:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_50.setText("")
        self.pushButton_50.setCheckable(True)
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_51.setGeometry(QtCore.QRect(22, 23, 9, 45))
        self.pushButton_51.setStyleSheet("#pushButton_51{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_51:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_51.setText("")
        self.pushButton_51.setCheckable(True)
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_52.setGeometry(QtCore.QRect(105, 191, 15, 9))
        self.pushButton_52.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_52.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_52.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_52.setStyleSheet("#pushButton_52{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_52:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_52.setText("")
        self.pushButton_52.setCheckable(True)
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_53.setGeometry(QtCore.QRect(172, 23, 55, 9))
        self.pushButton_53.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_53.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_53.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_53.setStyleSheet("#pushButton_53{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_53:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_53.setText("")
        self.pushButton_53.setCheckable(True)
        self.pushButton_53.setObjectName("pushButton_53")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(320, 690, 83, 77))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame1 = QtWidgets.QFrame(self.layoutWidget1)
        self.frame1.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addWidget(self.frame1)
        self.pushButton_54 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_54.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_54.setMaximumSize(QtCore.QSize(80, 20))
        self.pushButton_54.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_54.setStyleSheet("#pushButton_54{\n"
"background-color: blue;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_54:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.pushButton_54.setCheckable(True)
        self.pushButton_54.setObjectName("pushButton_54")
        self.verticalLayout_4.addWidget(self.pushButton_54)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(430, 287, 251, 224))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.pushButton_55 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_55.setGeometry(QtCore.QRect(31, 191, 46, 9))
        self.pushButton_55.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_55.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_55.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_55.setStyleSheet("#pushButton_55{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_55:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_55.setText("")
        self.pushButton_55.setCheckable(True)
        self.pushButton_55.setObjectName("pushButton_55")
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_19.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.pushButton_56 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_56.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.pushButton_56.setStyleSheet("#pushButton_56{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_56:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_56.setText("")
        self.pushButton_56.setCheckable(True)
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_57.setGeometry(QtCore.QRect(31, 23, 89, 9))
        self.pushButton_57.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_57.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_57.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_57.setStyleSheet("#pushButton_57{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_57:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_57.setText("")
        self.pushButton_57.setCheckable(True)
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_58.setGeometry(QtCore.QRect(10, 67, 31, 31))
        self.pushButton_58.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_58.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_58.setStyleSheet("#pushButton_58{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_58:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_58.setText("")
        self.pushButton_58.setCheckable(True)
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_59.setGeometry(QtCore.QRect(129, 191, 89, 9))
        self.pushButton_59.setMinimumSize(QtCore.QSize(26, 4))
        self.pushButton_59.setMaximumSize(QtCore.QSize(300, 40))
        self.pushButton_59.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_59.setStyleSheet("#pushButton_59{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_59:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_59.setText("")
        self.pushButton_59.setCheckable(True)
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_60.setGeometry(QtCore.QRect(129, 23, 15, 9))
        self.pushButton_60.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_60.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_60.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_60.setStyleSheet("#pushButton_60{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_60:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_60.setText("")
        self.pushButton_60.setCheckable(True)
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_61.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.pushButton_61.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_61.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_61.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_61.setStyleSheet("#pushButton_61{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_61:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_61.setText("")
        self.pushButton_61.setCheckable(True)
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_62 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_62.setGeometry(QtCore.QRect(205, 135, 31, 31))
        self.pushButton_62.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_62.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_62.setStyleSheet("#pushButton_62{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_62:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_62.setText("")
        self.pushButton_62.setCheckable(True)
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_63 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_63.setGeometry(QtCore.QRect(22, 120, 9, 80))
        self.pushButton_63.setStyleSheet("#pushButton_63{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_63:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_63.setText("")
        self.pushButton_63.setCheckable(True)
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_64 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_64.setGeometry(QtCore.QRect(218, 121, 9, 15))
        self.pushButton_64.setStyleSheet("#pushButton_64{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_64:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_64.setText("")
        self.pushButton_64.setCheckable(True)
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(76, 180, 31, 31))
        self.pushButton_7.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_7.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_7:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_65 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_65.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.pushButton_65.setStyleSheet("#pushButton_65{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_65:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_65.setText("")
        self.pushButton_65.setCheckable(True)
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_66.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.pushButton_66.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_66.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_66.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_66.setStyleSheet("#pushButton_66{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_66:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_66.setText("")
        self.pushButton_66.setCheckable(True)
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_67 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_67.setGeometry(QtCore.QRect(143, 12, 31, 31))
        self.pushButton_67.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_67.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_67.setStyleSheet("#pushButton_67{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_67:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_67.setText("")
        self.pushButton_67.setCheckable(True)
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_68.setGeometry(QtCore.QRect(218, 32, 9, 80))
        self.pushButton_68.setStyleSheet("#pushButton_68{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_68:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_68.setText("")
        self.pushButton_68.setCheckable(True)
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_69 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_69.setGeometry(QtCore.QRect(218, 164, 9, 36))
        self.pushButton_69.setStyleSheet("#pushButton_69{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_69:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_69.setText("")
        self.pushButton_69.setCheckable(True)
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_70.setGeometry(QtCore.QRect(22, 23, 9, 45))
        self.pushButton_70.setStyleSheet("#pushButton_70{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_70:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_70.setText("")
        self.pushButton_70.setCheckable(True)
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_71 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_71.setGeometry(QtCore.QRect(105, 191, 15, 9))
        self.pushButton_71.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_71.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_71.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_71.setStyleSheet("#pushButton_71{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_71:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_71.setText("")
        self.pushButton_71.setCheckable(True)
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_72.setGeometry(QtCore.QRect(172, 23, 55, 9))
        self.pushButton_72.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_72.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_72.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_72.setStyleSheet("#pushButton_72{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_72:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_72.setText("")
        self.pushButton_72.setCheckable(True)
        self.pushButton_72.setObjectName("pushButton_72")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(1288, 32, 251, 224))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_20 = QtWidgets.QLabel(self.groupBox_6)
        self.label_20.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_73 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_73.setGeometry(QtCore.QRect(172, 191, 46, 9))
        self.pushButton_73.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_73.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_73.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_73.setStyleSheet("#pushButton_73{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_73:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_73.setText("")
        self.pushButton_73.setCheckable(True)
        self.pushButton_73.setObjectName("pushButton_73")
        self.label_21 = QtWidgets.QLabel(self.groupBox_6)
        self.label_21.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_21.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.pushButton_75 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_75.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.pushButton_75.setStyleSheet("#pushButton_75{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_75:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_75.setText("")
        self.pushButton_75.setCheckable(True)
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_76.setGeometry(QtCore.QRect(128, 23, 99, 9))
        self.pushButton_76.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_76.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_76.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_76.setStyleSheet("#pushButton_76{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_76:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_76.setText("")
        self.pushButton_76.setCheckable(True)
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_77.setGeometry(QtCore.QRect(10, 131, 31, 31))
        self.pushButton_77.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_77.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_77.setStyleSheet("#pushButton_77{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_77:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_77.setText("")
        self.pushButton_77.setCheckable(True)
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_78.setGeometry(QtCore.QRect(31, 191, 89, 9))
        self.pushButton_78.setMinimumSize(QtCore.QSize(26, 4))
        self.pushButton_78.setMaximumSize(QtCore.QSize(300, 40))
        self.pushButton_78.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_78.setStyleSheet("#pushButton_78{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_78:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_78.setText("")
        self.pushButton_78.setCheckable(True)
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_79 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_79.setGeometry(QtCore.QRect(106, 23, 15, 9))
        self.pushButton_79.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_79.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_79.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_79.setStyleSheet("#pushButton_79{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_79:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_79.setText("")
        self.pushButton_79.setCheckable(True)
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_80.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.pushButton_80.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_80.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_80.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_80.setStyleSheet("#pushButton_80{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_80:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_80.setText("")
        self.pushButton_80.setCheckable(True)
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_81 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_81.setGeometry(QtCore.QRect(205, 67, 31, 31))
        self.pushButton_81.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_81.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_81.setStyleSheet("#pushButton_81{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_81:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_81.setText("")
        self.pushButton_81.setCheckable(True)
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_82 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_82.setGeometry(QtCore.QRect(22, 31, 9, 81))
        self.pushButton_82.setStyleSheet("#pushButton_82{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_82:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_82.setText("")
        self.pushButton_82.setCheckable(True)
        self.pushButton_82.setObjectName("pushButton_82")
        self.pushButton_83 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_83.setGeometry(QtCore.QRect(218, 97, 9, 15))
        self.pushButton_83.setStyleSheet("#pushButton_83{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_83:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_83.setText("")
        self.pushButton_83.setCheckable(True)
        self.pushButton_83.setObjectName("pushButton_83")
        self.pushButton_84 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_84.setGeometry(QtCore.QRect(142, 180, 31, 31))
        self.pushButton_84.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_84.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_84.setStyleSheet("#pushButton_84{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_84:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_84.setText("")
        self.pushButton_84.setCheckable(True)
        self.pushButton_84.setObjectName("pushButton_84")
        self.pushButton_85 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_85.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.pushButton_85.setStyleSheet("#pushButton_85{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_85:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_85.setText("")
        self.pushButton_85.setCheckable(True)
        self.pushButton_85.setObjectName("pushButton_85")
        self.pushButton_86 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_86.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.pushButton_86.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_86.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_86.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_86.setStyleSheet("#pushButton_86{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_86:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_86.setText("")
        self.pushButton_86.setCheckable(True)
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_87 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_87.setGeometry(QtCore.QRect(76, 12, 31, 31))
        self.pushButton_87.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_87.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_87.setStyleSheet("#pushButton_87{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_87:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_87.setText("")
        self.pushButton_87.setCheckable(True)
        self.pushButton_87.setObjectName("pushButton_87")
        self.pushButton_88 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_88.setGeometry(QtCore.QRect(218, 121, 9, 79))
        self.pushButton_88.setStyleSheet("#pushButton_88{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_88:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_88.setText("")
        self.pushButton_88.setCheckable(True)
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_89 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_89.setGeometry(QtCore.QRect(218, 23, 9, 46))
        self.pushButton_89.setStyleSheet("#pushButton_89{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_89:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_89.setText("")
        self.pushButton_89.setCheckable(True)
        self.pushButton_89.setObjectName("pushButton_89")
        self.pushButton_90 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_90.setGeometry(QtCore.QRect(22, 160, 9, 40))
        self.pushButton_90.setStyleSheet("#pushButton_90{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_90:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_90.setText("")
        self.pushButton_90.setCheckable(True)
        self.pushButton_90.setObjectName("pushButton_90")
        self.pushButton_91 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_91.setGeometry(QtCore.QRect(129, 191, 15, 9))
        self.pushButton_91.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_91.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_91.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_91.setStyleSheet("#pushButton_91{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_91:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_91.setText("")
        self.pushButton_91.setCheckable(True)
        self.pushButton_91.setObjectName("pushButton_91")
        self.pushButton_92 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_92.setGeometry(QtCore.QRect(22, 23, 55, 9))
        self.pushButton_92.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_92.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_92.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_92.setStyleSheet("#pushButton_92{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_92:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_92.setText("")
        self.pushButton_92.setCheckable(True)
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_131 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_131.setGeometry(QtCore.QRect(1046, 255, 371, 9))
        self.pushButton_131.setMinimumSize(QtCore.QSize(50, 9))
        self.pushButton_131.setStyleSheet("#pushButton_131{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_131:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_131.setText("")
        self.pushButton_131.setCheckable(True)
        self.pushButton_131.setObjectName("pushButton_131")
        self.pushButton_132 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_132.setGeometry(QtCore.QRect(1046, 531, 371, 9))
        self.pushButton_132.setMinimumSize(QtCore.QSize(50, 9))
        self.pushButton_132.setStyleSheet("#pushButton_132{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_132:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_132.setText("")
        self.pushButton_132.setCheckable(True)
        self.pushButton_132.setObjectName("pushButton_132")
        self.pushButton_133 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_133.setGeometry(QtCore.QRect(1046, 264, 9, 23))
        self.pushButton_133.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_133.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_133.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_133.setStyleSheet("#pushButton_133{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_133:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_133.setText("")
        self.pushButton_133.setCheckable(True)
        self.pushButton_133.setObjectName("pushButton_133")
        self.pushButton_134 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_134.setGeometry(QtCore.QRect(1046, 510, 9, 23))
        self.pushButton_134.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_134.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_134.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_134.setStyleSheet("#pushButton_134{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_134:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_134.setText("")
        self.pushButton_134.setCheckable(True)
        self.pushButton_134.setObjectName("pushButton_134")
        self.pushButton_135 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_135.setGeometry(QtCore.QRect(550, 264, 9, 23))
        self.pushButton_135.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_135.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_135.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_135.setStyleSheet("#pushButton_135{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_135:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_135.setText("")
        self.pushButton_135.setCheckable(True)
        self.pushButton_135.setObjectName("pushButton_135")
        self.pushButton_136 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_136.setGeometry(QtCore.QRect(550, 510, 9, 23))
        self.pushButton_136.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_136.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_136.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_136.setStyleSheet("#pushButton_136{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_136:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_136.setText("")
        self.pushButton_136.setCheckable(True)
        self.pushButton_136.setObjectName("pushButton_136")
        self.pushButton_137 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_137.setGeometry(QtCore.QRect(92, 636, 9, 15))
        self.pushButton_137.setStyleSheet("#pushButton_137{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_137:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_137.setText("")
        self.pushButton_137.setCheckable(True)
        self.pushButton_137.setObjectName("pushButton_137")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(660, 310, 83, 77))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.pushButton_138 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_138.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_138.setMaximumSize(QtCore.QSize(80, 20))
        self.pushButton_138.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_138.setStyleSheet("#pushButton_138{\n"
"background-color: blue;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_138:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.pushButton_138.setCheckable(True)
        self.pushButton_138.setObjectName("pushButton_138")
        self.verticalLayout_7.addWidget(self.pushButton_138)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(1170, 310, 83, 77))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13)
        self.label_26 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_11.addWidget(self.label_26)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_12.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_12.addWidget(self.label_28)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_10.addWidget(self.frame_3)
        self.pushButton_139 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_139.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_139.setMaximumSize(QtCore.QSize(80, 20))
        self.pushButton_139.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_139.setStyleSheet("#pushButton_139{\n"
"background-color: blue;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_139:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.pushButton_139.setCheckable(True)
        self.pushButton_139.setObjectName("pushButton_139")
        self.verticalLayout_10.addWidget(self.pushButton_139)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(1230, 0, 83, 77))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_4 = QtWidgets.QFrame(self.layoutWidget_4)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_29 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_14.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_14.addWidget(self.label_30)
        self.horizontalLayout_5.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_31 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_15.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_15.addWidget(self.label_32)
        self.horizontalLayout_5.addLayout(self.verticalLayout_15)
        self.verticalLayout_13.addWidget(self.frame_4)
        self.pushButton_140 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_140.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_140.setMaximumSize(QtCore.QSize(80, 20))
        self.pushButton_140.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_140.setStyleSheet("#pushButton_140{\n"
"background-color: blue;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_140:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.pushButton_140.setCheckable(True)
        self.pushButton_140.setObjectName("pushButton_140")
        self.verticalLayout_13.addWidget(self.pushButton_140)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(1210, 690, 83, 77))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_5 = QtWidgets.QFrame(self.layoutWidget_5)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_33 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_17.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_17.addWidget(self.label_34)
        self.horizontalLayout_6.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_35 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_18.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_18.addWidget(self.label_36)
        self.horizontalLayout_6.addLayout(self.verticalLayout_18)
        self.verticalLayout_16.addWidget(self.frame_5)
        self.pushButton_141 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_141.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_141.setMaximumSize(QtCore.QSize(80, 20))
        self.pushButton_141.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_141.setStyleSheet("#pushButton_141{\n"
"background-color: blue;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_141:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.pushButton_141.setCheckable(True)
        self.pushButton_141.setObjectName("pushButton_141")
        self.verticalLayout_16.addWidget(self.pushButton_141)
        self.pushButton_142 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_142.setGeometry(QtCore.QRect(452, 384, 9, 15))
        self.pushButton_142.setStyleSheet("#pushButton_142{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_142:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_142.setText("")
        self.pushButton_142.setCheckable(True)
        self.pushButton_142.setObjectName("pushButton_142")
        self.pushButton_144 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_144.setGeometry(QtCore.QRect(1310, 153, 9, 15))
        self.pushButton_144.setStyleSheet("#pushButton_144{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_144:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_144.setText("")
        self.pushButton_144.setCheckable(True)
        self.pushButton_144.setObjectName("pushButton_144")
        self.King_LoadBulbButton = QtWidgets.QPushButton(self.centralwidget)
        self.King_LoadBulbButton.setGeometry(QtCore.QRect(18, 740, 53, 53))
        self.King_LoadBulbButton.setStyleSheet("#King_LoadBulbButton{\n"
"border-image: url(:/img/Outliner_Mac_greyBulb.png);\n"
"background-color: gray;\n"
"border-style: outset;\n"
"padding:2px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"}\n"
"#King_LoadBulbButton:checked{\n"
"border-color: rgb(255, 0, 0);\n"
"border-image: url(:/img/lightBulb.svg);\n"
"}")
        self.King_LoadBulbButton.setText("")
        self.King_LoadBulbButton.setCheckable(True)
        self.King_LoadBulbButton.setObjectName("King_LoadBulbButton")
        self.pushButton_146 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_146.setGeometry(QtCore.QRect(70, 762, 15, 9))
        self.pushButton_146.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_146.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_146.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_146.setStyleSheet("#pushButton_146{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_146:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_146.setText("")
        self.pushButton_146.setCheckable(True)
        self.pushButton_146.setObjectName("pushButton_146")
        self.pushButton_147 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_147.setGeometry(QtCore.QRect(84, 753, 31, 31))
        self.pushButton_147.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_147.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_147.setStyleSheet("#pushButton_147{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_147:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_147.setText("")
        self.pushButton_147.setCheckable(True)
        self.pushButton_147.setObjectName("pushButton_147")
        self.pushButton_148 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_148.setGeometry(QtCore.QRect(114, 763, 85, 9))
        self.pushButton_148.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_148.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_148.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_148.setStyleSheet("#pushButton_148{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_148:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_148.setText("")
        self.pushButton_148.setCheckable(True)
        self.pushButton_148.setObjectName("pushButton_148")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(926, 287, 251, 224))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_37 = QtWidgets.QLabel(self.groupBox_9)
        self.label_37.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.pushButton_149 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_149.setGeometry(QtCore.QRect(172, 191, 46, 9))
        self.pushButton_149.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_149.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_149.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_149.setStyleSheet("#pushButton_149{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_149:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_149.setText("")
        self.pushButton_149.setCheckable(True)
        self.pushButton_149.setObjectName("pushButton_149")
        self.label_38 = QtWidgets.QLabel(self.groupBox_9)
        self.label_38.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_38.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.pushButton_150 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_150.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.pushButton_150.setStyleSheet("#pushButton_150{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_150:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_150.setText("")
        self.pushButton_150.setCheckable(True)
        self.pushButton_150.setObjectName("pushButton_150")
        self.pushButton_151 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_151.setGeometry(QtCore.QRect(128, 23, 99, 9))
        self.pushButton_151.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_151.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_151.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_151.setStyleSheet("#pushButton_151{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_151:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_151.setText("")
        self.pushButton_151.setCheckable(True)
        self.pushButton_151.setObjectName("pushButton_151")
        self.pushButton_152 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_152.setGeometry(QtCore.QRect(10, 131, 31, 31))
        self.pushButton_152.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_152.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_152.setStyleSheet("#pushButton_152{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_152:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_152.setText("")
        self.pushButton_152.setCheckable(True)
        self.pushButton_152.setObjectName("pushButton_152")
        self.pushButton_153 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_153.setGeometry(QtCore.QRect(31, 191, 89, 9))
        self.pushButton_153.setMinimumSize(QtCore.QSize(26, 4))
        self.pushButton_153.setMaximumSize(QtCore.QSize(300, 40))
        self.pushButton_153.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_153.setStyleSheet("#pushButton_153{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_153:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_153.setText("")
        self.pushButton_153.setCheckable(True)
        self.pushButton_153.setObjectName("pushButton_153")
        self.pushButton_154 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_154.setGeometry(QtCore.QRect(106, 23, 15, 9))
        self.pushButton_154.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_154.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_154.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_154.setStyleSheet("#pushButton_154{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_154:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_154.setText("")
        self.pushButton_154.setCheckable(True)
        self.pushButton_154.setObjectName("pushButton_154")
        self.pushButton_155 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_155.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.pushButton_155.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_155.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_155.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_155.setStyleSheet("#pushButton_155{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_155:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_155.setText("")
        self.pushButton_155.setCheckable(True)
        self.pushButton_155.setObjectName("pushButton_155")
        self.pushButton_156 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_156.setGeometry(QtCore.QRect(205, 67, 31, 31))
        self.pushButton_156.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_156.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_156.setStyleSheet("#pushButton_156{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_156:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_156.setText("")
        self.pushButton_156.setCheckable(True)
        self.pushButton_156.setObjectName("pushButton_156")
        self.pushButton_157 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_157.setGeometry(QtCore.QRect(22, 31, 9, 81))
        self.pushButton_157.setStyleSheet("#pushButton_157{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_157:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_157.setText("")
        self.pushButton_157.setCheckable(True)
        self.pushButton_157.setObjectName("pushButton_157")
        self.pushButton_158 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_158.setGeometry(QtCore.QRect(218, 97, 9, 15))
        self.pushButton_158.setStyleSheet("#pushButton_158{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_158:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_158.setText("")
        self.pushButton_158.setCheckable(True)
        self.pushButton_158.setObjectName("pushButton_158")
        self.pushButton_159 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_159.setGeometry(QtCore.QRect(142, 180, 31, 31))
        self.pushButton_159.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_159.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_159.setStyleSheet("#pushButton_159{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_159:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_159.setText("")
        self.pushButton_159.setCheckable(True)
        self.pushButton_159.setObjectName("pushButton_159")
        self.pushButton_160 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_160.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.pushButton_160.setStyleSheet("#pushButton_160{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_160:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_160.setText("")
        self.pushButton_160.setCheckable(True)
        self.pushButton_160.setObjectName("pushButton_160")
        self.pushButton_161 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_161.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.pushButton_161.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_161.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_161.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_161.setStyleSheet("#pushButton_161{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_161:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_161.setText("")
        self.pushButton_161.setCheckable(True)
        self.pushButton_161.setObjectName("pushButton_161")
        self.pushButton_162 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_162.setGeometry(QtCore.QRect(76, 12, 31, 31))
        self.pushButton_162.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_162.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_162.setStyleSheet("#pushButton_162{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_162:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_162.setText("")
        self.pushButton_162.setCheckable(True)
        self.pushButton_162.setObjectName("pushButton_162")
        self.pushButton_163 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_163.setGeometry(QtCore.QRect(218, 121, 9, 79))
        self.pushButton_163.setStyleSheet("#pushButton_163{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_163:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_163.setText("")
        self.pushButton_163.setCheckable(True)
        self.pushButton_163.setObjectName("pushButton_163")
        self.pushButton_164 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_164.setGeometry(QtCore.QRect(218, 23, 9, 46))
        self.pushButton_164.setStyleSheet("#pushButton_164{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_164:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_164.setText("")
        self.pushButton_164.setCheckable(True)
        self.pushButton_164.setObjectName("pushButton_164")
        self.pushButton_165 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_165.setGeometry(QtCore.QRect(22, 160, 9, 40))
        self.pushButton_165.setStyleSheet("#pushButton_165{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_165:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_165.setText("")
        self.pushButton_165.setCheckable(True)
        self.pushButton_165.setObjectName("pushButton_165")
        self.pushButton_166 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_166.setGeometry(QtCore.QRect(129, 191, 15, 9))
        self.pushButton_166.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_166.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_166.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_166.setStyleSheet("#pushButton_166{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_166:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_166.setText("")
        self.pushButton_166.setCheckable(True)
        self.pushButton_166.setObjectName("pushButton_166")
        self.pushButton_167 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_167.setGeometry(QtCore.QRect(22, 23, 55, 9))
        self.pushButton_167.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_167.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_167.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_167.setStyleSheet("#pushButton_167{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_167:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_167.setText("")
        self.pushButton_167.setCheckable(True)
        self.pushButton_167.setObjectName("pushButton_167")
        self.pushButton_143 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_143.setGeometry(QtCore.QRect(22, 120, 9, 15))
        self.pushButton_143.setStyleSheet("#pushButton_143{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_143:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_143.setText("")
        self.pushButton_143.setCheckable(True)
        self.pushButton_143.setObjectName("pushButton_143")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(1288, 539, 251, 224))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_22 = QtWidgets.QLabel(self.groupBox_7)
        self.label_22.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.pushButton_93 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_93.setGeometry(QtCore.QRect(172, 191, 46, 9))
        self.pushButton_93.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_93.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_93.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_93.setStyleSheet("#pushButton_93{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_93:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_93.setText("")
        self.pushButton_93.setCheckable(True)
        self.pushButton_93.setObjectName("pushButton_93")
        self.label_23 = QtWidgets.QLabel(self.groupBox_7)
        self.label_23.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_23.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.pushButton_94 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_94.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.pushButton_94.setStyleSheet("#pushButton_94{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_94:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_94.setText("")
        self.pushButton_94.setCheckable(True)
        self.pushButton_94.setObjectName("pushButton_94")
        self.pushButton_95 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_95.setGeometry(QtCore.QRect(128, 23, 99, 9))
        self.pushButton_95.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_95.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_95.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_95.setStyleSheet("#pushButton_95{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_95:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_95.setText("")
        self.pushButton_95.setCheckable(True)
        self.pushButton_95.setObjectName("pushButton_95")
        self.pushButton_96 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_96.setGeometry(QtCore.QRect(10, 131, 31, 31))
        self.pushButton_96.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_96.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_96.setStyleSheet("#pushButton_96{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_96:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_96.setText("")
        self.pushButton_96.setCheckable(True)
        self.pushButton_96.setObjectName("pushButton_96")
        self.pushButton_97 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_97.setGeometry(QtCore.QRect(31, 191, 89, 9))
        self.pushButton_97.setMinimumSize(QtCore.QSize(26, 4))
        self.pushButton_97.setMaximumSize(QtCore.QSize(300, 40))
        self.pushButton_97.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_97.setStyleSheet("#pushButton_97{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_97:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_97.setText("")
        self.pushButton_97.setCheckable(True)
        self.pushButton_97.setObjectName("pushButton_97")
        self.pushButton_98 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_98.setGeometry(QtCore.QRect(106, 23, 15, 9))
        self.pushButton_98.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_98.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_98.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_98.setStyleSheet("#pushButton_98{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_98:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_98.setText("")
        self.pushButton_98.setCheckable(True)
        self.pushButton_98.setObjectName("pushButton_98")
        self.pushButton_99 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_99.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.pushButton_99.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_99.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_99.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_99.setStyleSheet("#pushButton_99{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_99:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_99.setText("")
        self.pushButton_99.setCheckable(True)
        self.pushButton_99.setObjectName("pushButton_99")
        self.pushButton_100 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_100.setGeometry(QtCore.QRect(205, 67, 31, 31))
        self.pushButton_100.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_100.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_100.setStyleSheet("#pushButton_100{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_100:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_100.setText("")
        self.pushButton_100.setCheckable(True)
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_101 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_101.setGeometry(QtCore.QRect(22, 31, 9, 81))
        self.pushButton_101.setStyleSheet("#pushButton_101{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_101:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_101.setText("")
        self.pushButton_101.setCheckable(True)
        self.pushButton_101.setObjectName("pushButton_101")
        self.pushButton_102 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_102.setGeometry(QtCore.QRect(218, 97, 9, 15))
        self.pushButton_102.setStyleSheet("#pushButton_102{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_102:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_102.setText("")
        self.pushButton_102.setCheckable(True)
        self.pushButton_102.setObjectName("pushButton_102")
        self.pushButton_103 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_103.setGeometry(QtCore.QRect(142, 180, 31, 31))
        self.pushButton_103.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_103.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_103.setStyleSheet("#pushButton_103{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_103:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_103.setText("")
        self.pushButton_103.setCheckable(True)
        self.pushButton_103.setObjectName("pushButton_103")
        self.pushButton_104 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_104.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.pushButton_104.setStyleSheet("#pushButton_104{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_104:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_104.setText("")
        self.pushButton_104.setCheckable(True)
        self.pushButton_104.setObjectName("pushButton_104")
        self.pushButton_105 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_105.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.pushButton_105.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_105.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_105.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_105.setStyleSheet("#pushButton_105{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_105:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_105.setText("")
        self.pushButton_105.setCheckable(True)
        self.pushButton_105.setObjectName("pushButton_105")
        self.pushButton_106 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_106.setGeometry(QtCore.QRect(76, 12, 31, 31))
        self.pushButton_106.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_106.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_106.setStyleSheet("#pushButton_106{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_106:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_106.setText("")
        self.pushButton_106.setCheckable(True)
        self.pushButton_106.setObjectName("pushButton_106")
        self.pushButton_107 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_107.setGeometry(QtCore.QRect(218, 121, 9, 79))
        self.pushButton_107.setStyleSheet("#pushButton_107{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_107:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_107.setText("")
        self.pushButton_107.setCheckable(True)
        self.pushButton_107.setObjectName("pushButton_107")
        self.pushButton_108 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_108.setGeometry(QtCore.QRect(218, 23, 9, 46))
        self.pushButton_108.setStyleSheet("#pushButton_108{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_108:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_108.setText("")
        self.pushButton_108.setCheckable(True)
        self.pushButton_108.setObjectName("pushButton_108")
        self.pushButton_109 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_109.setGeometry(QtCore.QRect(22, 160, 9, 40))
        self.pushButton_109.setStyleSheet("#pushButton_109{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_109:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_109.setText("")
        self.pushButton_109.setCheckable(True)
        self.pushButton_109.setObjectName("pushButton_109")
        self.pushButton_110 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_110.setGeometry(QtCore.QRect(129, 191, 15, 9))
        self.pushButton_110.setMinimumSize(QtCore.QSize(15, 4))
        self.pushButton_110.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_110.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_110.setStyleSheet("#pushButton_110{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_110:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_110.setText("")
        self.pushButton_110.setCheckable(True)
        self.pushButton_110.setObjectName("pushButton_110")
        self.pushButton_111 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_111.setGeometry(QtCore.QRect(22, 23, 55, 9))
        self.pushButton_111.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_111.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_111.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_111.setStyleSheet("#pushButton_111{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_111:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_111.setText("")
        self.pushButton_111.setCheckable(True)
        self.pushButton_111.setObjectName("pushButton_111")
        self.pushButton_145 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_145.setGeometry(QtCore.QRect(22, 120, 9, 15))
        self.pushButton_145.setStyleSheet("#pushButton_145{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_145:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_145.setText("")
        self.pushButton_145.setCheckable(True)
        self.pushButton_145.setObjectName("pushButton_145")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(722, 460, 151, 151))
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(10, 20, 121, 121))
        self.label_24.setStyleSheet("border-image: url(:/img/Solar_energy128px.png);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.pushButton_112 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_112.setGeometry(QtCore.QRect(680, 399, 85, 9))
        self.pushButton_112.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_112.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_112.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_112.setStyleSheet("#pushButton_112{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_112:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_112.setText("")
        self.pushButton_112.setCheckable(True)
        self.pushButton_112.setObjectName("pushButton_112")
        self.pushButton_168 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_168.setGeometry(QtCore.QRect(746, 420, 31, 31))
        self.pushButton_168.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_168.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_168.setStyleSheet("#pushButton_168{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_168:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_168.setText("")
        self.pushButton_168.setCheckable(True)
        self.pushButton_168.setObjectName("pushButton_168")
        self.pushButton_169 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_169.setGeometry(QtCore.QRect(756, 408, 9, 16))
        self.pushButton_169.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_169.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_169.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_169.setStyleSheet("#pushButton_169{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_169:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_169.setText("")
        self.pushButton_169.setCheckable(True)
        self.pushButton_169.setObjectName("pushButton_169")
        self.pushButton_170 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_170.setGeometry(QtCore.QRect(756, 450, 9, 12))
        self.pushButton_170.setMinimumSize(QtCore.QSize(1, 1))
        self.pushButton_170.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_170.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_170.setStyleSheet("#pushButton_170{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_170:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_170.setText("")
        self.pushButton_170.setCheckable(True)
        self.pushButton_170.setObjectName("pushButton_170")
        self.layoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(870, 530, 83, 77))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_19.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_6 = QtWidgets.QFrame(self.layoutWidget_6)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_25 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_20.addWidget(self.label_25)
        self.label_39 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_20.addWidget(self.label_39)
        self.horizontalLayout_7.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_40 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_21.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_21.addWidget(self.label_41)
        self.horizontalLayout_7.addLayout(self.verticalLayout_21)
        self.verticalLayout_19.addWidget(self.frame_6)
        self.pushButton_171 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton_171.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_171.setMaximumSize(QtCore.QSize(80, 20))
        self.pushButton_171.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_171.setStyleSheet("#pushButton_171{\n"
"background-color: blue;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_171:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.pushButton_171.setCheckable(True)
        self.pushButton_171.setObjectName("pushButton_171")
        self.verticalLayout_19.addWidget(self.pushButton_171)
        self.Deuce_LoadBulbButton = QtWidgets.QPushButton(self.centralwidget)
        self.Deuce_LoadBulbButton.setGeometry(QtCore.QRect(1538, 0, 53, 53))
        self.Deuce_LoadBulbButton.setStyleSheet("#Deuce_LoadBulbButton{\n"
"border-image: url(:/img/Outliner_Mac_greyBulb.png);\n"
"background-color: gray;\n"
"border-style: outset;\n"
"padding:2px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"}\n"
"#Deuce_LoadBulbButton:checked{\n"
"border-color: rgb(255, 0, 0);\n"
"border-image: url(:/img/lightBulb.svg);\n"
"}")
        self.Deuce_LoadBulbButton.setText("")
        self.Deuce_LoadBulbButton.setCheckable(True)
        self.Deuce_LoadBulbButton.setObjectName("Deuce_LoadBulbButton")
        self.Queen_LoadBulbButton = QtWidgets.QPushButton(self.centralwidget)
        self.Queen_LoadBulbButton.setGeometry(QtCore.QRect(1538, 730, 53, 53))
        self.Queen_LoadBulbButton.setStyleSheet("#Queen_LoadBulbButton{\n"
"border-image: url(:/img/Outliner_Mac_greyBulb.png);\n"
"background-color: gray;\n"
"border-style: outset;\n"
"padding:2px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"}\n"
"#Queen_LoadBulbButton:checked{\n"
"border-color: rgb(255, 0, 0);\n"
"border-image: url(:/img/lightBulb.svg);\n"
"}")
        self.Queen_LoadBulbButton.setText("")
        self.Queen_LoadBulbButton.setCheckable(True)
        self.Queen_LoadBulbButton.setObjectName("Queen_LoadBulbButton")
        self.pushButton_172 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_172.setGeometry(QtCore.QRect(1408, 763, 85, 9))
        self.pushButton_172.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_172.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_172.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_172.setStyleSheet("#pushButton_172{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_172:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_172.setText("")
        self.pushButton_172.setCheckable(True)
        self.pushButton_172.setObjectName("pushButton_172")
        self.pushButton_173 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_173.setGeometry(QtCore.QRect(1492, 753, 31, 31))
        self.pushButton_173.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_173.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_173.setStyleSheet("#pushButton_173{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_173:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_173.setText("")
        self.pushButton_173.setCheckable(True)
        self.pushButton_173.setObjectName("pushButton_173")
        self.pushButton_174 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_174.setGeometry(QtCore.QRect(1521, 762, 20, 9))
        self.pushButton_174.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_174.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_174.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_174.setStyleSheet("#pushButton_174{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_174:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_174.setText("")
        self.pushButton_174.setCheckable(True)
        self.pushButton_174.setObjectName("pushButton_174")
        self.pushButton_175 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_175.setGeometry(QtCore.QRect(1408, 24, 85, 9))
        self.pushButton_175.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton_175.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton_175.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_175.setStyleSheet("#pushButton_175{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton_175:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_175.setText("")
        self.pushButton_175.setCheckable(True)
        self.pushButton_175.setObjectName("pushButton_175")
        self.pushButton_176 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_176.setGeometry(QtCore.QRect(1490, 13, 31, 31))
        self.pushButton_176.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_176.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_176.setStyleSheet("#pushButton_176{\n"
"border-image: url(:/img/relaySPDT.png);\n"
"background-color: green;\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"border-color:beige;\n"
"font-size:12px;\n"
"font-weight:100;\n"
"color: white;\n"
"max-width:23px;\n"
"max-height:23px;\n"
"min-width:23px;\n"
"min-height:23px;\n"
"padding:2px;\n"
"\n"
"}\n"
"#pushButton_176:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton_176.setText("")
        self.pushButton_176.setCheckable(True)
        self.pushButton_176.setObjectName("pushButton_176")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1520, 24, 20, 9))
        self.pushButton.setMinimumSize(QtCore.QSize(20, 4))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 20))
        self.pushButton.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton.setStyleSheet("#pushButton{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#pushButton:checked{\n"
"    background-color: red;\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.groupBox_7.raise_()
        self.groupBox_9.raise_()
        self.groupBox_3.raise_()
        self.pushButton_35.raise_()
        self.pushButton_15.raise_()
        self.pushButton_34.raise_()
        self.Ace_LoadBulbButton.raise_()
        self.pushButton_36.raise_()
        self.pushButton_38.raise_()
        self.pushButton_39.raise_()
        self.pushButton_16.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.pushButton_74.raise_()
        self.layoutWidget.raise_()
        self.groupBox_4.raise_()
        self.layoutWidget.raise_()
        self.groupBox_5.raise_()
        self.groupBox_6.raise_()
        self.pushButton_131.raise_()
        self.pushButton_133.raise_()
        self.pushButton_134.raise_()
        self.pushButton_135.raise_()
        self.pushButton_136.raise_()
        self.pushButton_137.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.layoutWidget_4.raise_()
        self.layoutWidget_5.raise_()
        self.pushButton_142.raise_()
        self.pushButton_144.raise_()
        self.King_LoadBulbButton.raise_()
        self.pushButton_146.raise_()
        self.pushButton_147.raise_()
        self.pushButton_148.raise_()
        self.pushButton_132.raise_()
        self.groupBox.raise_()
        self.pushButton_112.raise_()
        self.pushButton_168.raise_()
        self.pushButton_169.raise_()
        self.pushButton_170.raise_()
        self.layoutWidget_6.raise_()
        self.Deuce_LoadBulbButton.raise_()
        self.Queen_LoadBulbButton.raise_()
        self.pushButton_172.raise_()
        self.pushButton_173.raise_()
        self.pushButton_174.raise_()
        self.pushButton_175.raise_()
        self.pushButton_176.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1690, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_16.setText(_translate("MainWindow", "Ace"))
        self.label.setText(_translate("MainWindow", " V ="))
        self.label_2.setText(_translate("MainWindow", "  I ="))
        self.label_4.setText(_translate("MainWindow", " 000.0 "))
        self.label_5.setText(_translate("MainWindow", " 00.00 "))
        self.pushButton_14.setText(_translate("MainWindow", "Expand"))
        self.label_17.setText(_translate("MainWindow", "King"))
        self.label_3.setText(_translate("MainWindow", " V ="))
        self.label_6.setText(_translate("MainWindow", "  I ="))
        self.label_7.setText(_translate("MainWindow", " 000.0 "))
        self.label_8.setText(_translate("MainWindow", " 00.00 "))
        self.pushButton_54.setText(_translate("MainWindow", "Expand"))
        self.label_18.setText(_translate("MainWindow", "Poker"))
        self.label_20.setText(_translate("MainWindow", "Deuce"))
        self.label_9.setText(_translate("MainWindow", " V ="))
        self.label_10.setText(_translate("MainWindow", "  I ="))
        self.label_11.setText(_translate("MainWindow", " 000.0 "))
        self.label_12.setText(_translate("MainWindow", " 00.00 "))
        self.pushButton_138.setText(_translate("MainWindow", "Expand"))
        self.label_13.setText(_translate("MainWindow", " V ="))
        self.label_26.setText(_translate("MainWindow", "  I ="))
        self.label_27.setText(_translate("MainWindow", " 000.0 "))
        self.label_28.setText(_translate("MainWindow", " 00.00 "))
        self.pushButton_139.setText(_translate("MainWindow", "Expand"))
        self.label_29.setText(_translate("MainWindow", " V ="))
        self.label_30.setText(_translate("MainWindow", "  I ="))
        self.label_31.setText(_translate("MainWindow", " 000.0 "))
        self.label_32.setText(_translate("MainWindow", " 00.00 "))
        self.pushButton_140.setText(_translate("MainWindow", "Expand"))
        self.label_33.setText(_translate("MainWindow", " V ="))
        self.label_34.setText(_translate("MainWindow", "  I ="))
        self.label_35.setText(_translate("MainWindow", " 000.0 "))
        self.label_36.setText(_translate("MainWindow", " 00.00 "))
        self.pushButton_141.setText(_translate("MainWindow", "Expand"))
        self.label_37.setText(_translate("MainWindow", "Joker"))
        self.label_22.setText(_translate("MainWindow", "Queen"))
        self.label_25.setText(_translate("MainWindow", " V ="))
        self.label_39.setText(_translate("MainWindow", "  I ="))
        self.label_40.setText(_translate("MainWindow", " 000.0 "))
        self.label_41.setText(_translate("MainWindow", " 00.00 "))
        self.pushButton_171.setText(_translate("MainWindow", "Expand"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))

import resources_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())