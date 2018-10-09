# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\NMSU_Software_Projects\POWERLAB_UPGRADE\Power_Lab_GUI_Main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1909, 1081)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setSizeIncrement(QtCore.QSize(1, 0))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 252);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Window_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Window_groupBox.setEnabled(True)
        self.Window_groupBox.setGeometry(QtCore.QRect(0, 0, 1906, 926))
        self.Window_groupBox.setTitle("")
        self.Window_groupBox.setObjectName("Window_groupBox")
        self.Deuce_TLine1_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Deuce_TLine1_butt.setEnabled(False)
        self.Deuce_TLine1_butt.setGeometry(QtCore.QRect(1831, 30, 20, 9))
        self.Deuce_TLine1_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Deuce_TLine1_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Deuce_TLine1_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine1_butt.setStyleSheet("#Deuce_TLine1_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine1_butt.setText("")
        self.Deuce_TLine1_butt.setCheckable(True)
        self.Deuce_TLine1_butt.setObjectName("Deuce_TLine1_butt")
        self.Joker_to_Queen_TLine_butt1 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Joker_to_Queen_TLine_butt1.setEnabled(False)
        self.Joker_to_Queen_TLine_butt1.setGeometry(QtCore.QRect(1358, 671, 371, 9))
        self.Joker_to_Queen_TLine_butt1.setMinimumSize(QtCore.QSize(50, 9))
        self.Joker_to_Queen_TLine_butt1.setStyleSheet("#Joker_to_Queen_TLine_butt1{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_to_Queen_TLine_butt1:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_to_Queen_TLine_butt1.setText("")
        self.Joker_to_Queen_TLine_butt1.setCheckable(True)
        self.Joker_to_Queen_TLine_butt1.setObjectName("Joker_to_Queen_TLine_butt1")
        self.Ace_L_or_G_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Ace_L_or_G_butt.setEnabled(False)
        self.Ace_L_or_G_butt.setGeometry(QtCore.QRect(8, 6, 53, 53))
        self.Ace_L_or_G_butt.setStyleSheet("#Ace_L_or_G_butt{\n"
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
"#Ace_L_or_G_butt:checked{\n"
"border-color: rgb(255, 0, 0);\n"
"border-image: url(:/img/lightBulb.svg);\n"
"}")
        self.Ace_L_or_G_butt.setText("")
        self.Ace_L_or_G_butt.setCheckable(True)
        self.Ace_L_or_G_butt.setObjectName("Ace_L_or_G_butt")
        self.Deuce_to_Joker_TLine_butt1 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Deuce_to_Joker_TLine_butt1.setEnabled(False)
        self.Deuce_to_Joker_TLine_butt1.setGeometry(QtCore.QRect(1358, 261, 371, 9))
        self.Deuce_to_Joker_TLine_butt1.setMinimumSize(QtCore.QSize(50, 9))
        self.Deuce_to_Joker_TLine_butt1.setStyleSheet("#Deuce_to_Joker_TLine_butt1{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_to_Joker_TLine_butt1:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_to_Joker_TLine_butt1.setText("")
        self.Deuce_to_Joker_TLine_butt1.setCheckable(True)
        self.Deuce_to_Joker_TLine_butt1.setObjectName("Deuce_to_Joker_TLine_butt1")
        self.Ace_to_Deuce_TLine_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Ace_to_Deuce_TLine_butt.setEnabled(False)
        self.Ace_to_Deuce_TLine_butt.setGeometry(QtCore.QRect(311, 150, 1289, 9))
        self.Ace_to_Deuce_TLine_butt.setMinimumSize(QtCore.QSize(50, 9))
        self.Ace_to_Deuce_TLine_butt.setStyleSheet("#Ace_to_Deuce_TLine_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_to_Deuce_TLine_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_to_Deuce_TLine_butt.setText("")
        self.Ace_to_Deuce_TLine_butt.setCheckable(True)
        self.Ace_to_Deuce_TLine_butt.setObjectName("Ace_to_Deuce_TLine_butt")
        self.Queen_groupBox = QtWidgets.QGroupBox(self.Window_groupBox)
        self.Queen_groupBox.setGeometry(QtCore.QRect(1600, 680, 251, 224))
        self.Queen_groupBox.setTitle("")
        self.Queen_groupBox.setObjectName("Queen_groupBox")
        self.label_22 = QtWidgets.QLabel(self.Queen_groupBox)
        self.label_22.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.Queen_TLine17_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine17_butt.setEnabled(False)
        self.Queen_TLine17_butt.setGeometry(QtCore.QRect(172, 191, 46, 9))
        self.Queen_TLine17_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Queen_TLine17_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Queen_TLine17_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine17_butt.setStyleSheet("#Queen_TLine17_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine17_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine17_butt.setText("")
        self.Queen_TLine17_butt.setCheckable(True)
        self.Queen_TLine17_butt.setObjectName("Queen_TLine17_butt")
        self.label_23 = QtWidgets.QLabel(self.Queen_groupBox)
        self.label_23.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_23.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.Queen_TLine15_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine15_butt.setEnabled(False)
        self.Queen_TLine15_butt.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.Queen_TLine15_butt.setStyleSheet("#Queen_TLine15_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine15_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine15_butt.setText("")
        self.Queen_TLine15_butt.setCheckable(True)
        self.Queen_TLine15_butt.setObjectName("Queen_TLine15_butt")
        self.Queen_TLine12_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine12_butt.setEnabled(False)
        self.Queen_TLine12_butt.setGeometry(QtCore.QRect(128, 23, 99, 9))
        self.Queen_TLine12_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Queen_TLine12_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Queen_TLine12_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine12_butt.setStyleSheet("#Queen_TLine12_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine12_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine12_butt.setText("")
        self.Queen_TLine12_butt.setCheckable(True)
        self.Queen_TLine12_butt.setObjectName("Queen_TLine12_butt")
        self.Queen_Rel2_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_Rel2_butt.setGeometry(QtCore.QRect(10, 131, 31, 31))
        self.Queen_Rel2_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Queen_Rel2_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Queen_Rel2_butt.setStyleSheet("#Queen_Rel2_butt{\n"
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
"#Queen_Rel2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_Rel2_butt.setText("")
        self.Queen_Rel2_butt.setCheckable(True)
        self.Queen_Rel2_butt.setObjectName("Queen_Rel2_butt")
        self.Queen_TLine4_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine4_butt.setEnabled(False)
        self.Queen_TLine4_butt.setGeometry(QtCore.QRect(31, 191, 89, 9))
        self.Queen_TLine4_butt.setMinimumSize(QtCore.QSize(26, 4))
        self.Queen_TLine4_butt.setMaximumSize(QtCore.QSize(300, 40))
        self.Queen_TLine4_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine4_butt.setStyleSheet("#Queen_TLine4_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine4_butt.setText("")
        self.Queen_TLine4_butt.setCheckable(True)
        self.Queen_TLine4_butt.setObjectName("Queen_TLine4_butt")
        self.Queen_TLine10_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine10_butt.setEnabled(False)
        self.Queen_TLine10_butt.setGeometry(QtCore.QRect(106, 23, 15, 9))
        self.Queen_TLine10_butt.setMinimumSize(QtCore.QSize(15, 4))
        self.Queen_TLine10_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Queen_TLine10_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine10_butt.setStyleSheet("#Queen_TLine10_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine10_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine10_butt.setText("")
        self.Queen_TLine10_butt.setCheckable(True)
        self.Queen_TLine10_butt.setObjectName("Queen_TLine10_butt")
        self.Queen_TLine11_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine11_butt.setEnabled(False)
        self.Queen_TLine11_butt.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.Queen_TLine11_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Queen_TLine11_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Queen_TLine11_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine11_butt.setStyleSheet("#Queen_TLine11_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine11_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine11_butt.setText("")
        self.Queen_TLine11_butt.setCheckable(True)
        self.Queen_TLine11_butt.setObjectName("Queen_TLine11_butt")
        self.Queen_Rel4_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_Rel4_butt.setGeometry(QtCore.QRect(205, 67, 31, 31))
        self.Queen_Rel4_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Queen_Rel4_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Queen_Rel4_butt.setStyleSheet("#Queen_Rel4_butt{\n"
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
"#Queen_Rel4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_Rel4_butt.setText("")
        self.Queen_Rel4_butt.setCheckable(True)
        self.Queen_Rel4_butt.setObjectName("Queen_Rel4_butt")
        self.Queen_TLine8_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine8_butt.setEnabled(False)
        self.Queen_TLine8_butt.setGeometry(QtCore.QRect(22, 31, 9, 81))
        self.Queen_TLine8_butt.setStyleSheet("#Queen_TLine8_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine8_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine8_butt.setText("")
        self.Queen_TLine8_butt.setCheckable(True)
        self.Queen_TLine8_butt.setObjectName("Queen_TLine8_butt")
        self.Queen_TLine14_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine14_butt.setEnabled(False)
        self.Queen_TLine14_butt.setGeometry(QtCore.QRect(218, 97, 9, 15))
        self.Queen_TLine14_butt.setStyleSheet("#Queen_TLine14_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine14_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine14_butt.setText("")
        self.Queen_TLine14_butt.setCheckable(True)
        self.Queen_TLine14_butt.setObjectName("Queen_TLine14_butt")
        self.Queen_Rel5_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_Rel5_butt.setGeometry(QtCore.QRect(142, 180, 31, 31))
        self.Queen_Rel5_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Queen_Rel5_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Queen_Rel5_butt.setStyleSheet("#Queen_Rel5_butt{\n"
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
"#Queen_Rel5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_Rel5_butt.setText("")
        self.Queen_Rel5_butt.setCheckable(True)
        self.Queen_Rel5_butt.setObjectName("Queen_Rel5_butt")
        self.Queen_TLine7_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine7_butt.setEnabled(False)
        self.Queen_TLine7_butt.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.Queen_TLine7_butt.setStyleSheet("#Queen_TLine7_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine7_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine7_butt.setText("")
        self.Queen_TLine7_butt.setCheckable(True)
        self.Queen_TLine7_butt.setObjectName("Queen_TLine7_butt")
        self.Queen_TLine3_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine3_butt.setEnabled(False)
        self.Queen_TLine3_butt.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.Queen_TLine3_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Queen_TLine3_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Queen_TLine3_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine3_butt.setStyleSheet("#Queen_TLine3_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine3_butt.setText("")
        self.Queen_TLine3_butt.setCheckable(True)
        self.Queen_TLine3_butt.setObjectName("Queen_TLine3_butt")
        self.Queen_Rel3_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_Rel3_butt.setEnabled(True)
        self.Queen_Rel3_butt.setGeometry(QtCore.QRect(76, 12, 31, 31))
        self.Queen_Rel3_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Queen_Rel3_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Queen_Rel3_butt.setStyleSheet("#Queen_Rel3_butt{\n"
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
"#Queen_Rel3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_Rel3_butt.setText("")
        self.Queen_Rel3_butt.setCheckable(True)
        self.Queen_Rel3_butt.setObjectName("Queen_Rel3_butt")
        self.Queen_TLine16_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine16_butt.setEnabled(False)
        self.Queen_TLine16_butt.setGeometry(QtCore.QRect(218, 121, 9, 79))
        self.Queen_TLine16_butt.setStyleSheet("#Queen_TLine16_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine16_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine16_butt.setText("")
        self.Queen_TLine16_butt.setCheckable(True)
        self.Queen_TLine16_butt.setObjectName("Queen_TLine16_butt")
        self.Queen_TLine13_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine13_butt.setEnabled(False)
        self.Queen_TLine13_butt.setGeometry(QtCore.QRect(218, 23, 9, 45))
        self.Queen_TLine13_butt.setStyleSheet("#Queen_TLine13_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine13_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine13_butt.setText("")
        self.Queen_TLine13_butt.setCheckable(True)
        self.Queen_TLine13_butt.setObjectName("Queen_TLine13_butt")
        self.Queen_TLine5_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine5_butt.setEnabled(False)
        self.Queen_TLine5_butt.setGeometry(QtCore.QRect(22, 161, 9, 39))
        self.Queen_TLine5_butt.setStyleSheet("#Queen_TLine5_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine5_butt.setText("")
        self.Queen_TLine5_butt.setCheckable(True)
        self.Queen_TLine5_butt.setObjectName("Queen_TLine5_butt")
        self.Queen_TLine18_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine18_butt.setEnabled(False)
        self.Queen_TLine18_butt.setGeometry(QtCore.QRect(129, 191, 14, 9))
        self.Queen_TLine18_butt.setMinimumSize(QtCore.QSize(12, 4))
        self.Queen_TLine18_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Queen_TLine18_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine18_butt.setStyleSheet("#Queen_TLine18_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine18_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine18_butt.setText("")
        self.Queen_TLine18_butt.setCheckable(True)
        self.Queen_TLine18_butt.setObjectName("Queen_TLine18_butt")
        self.Queen_TLine9_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine9_butt.setEnabled(False)
        self.Queen_TLine9_butt.setGeometry(QtCore.QRect(22, 23, 55, 9))
        self.Queen_TLine9_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Queen_TLine9_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Queen_TLine9_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine9_butt.setStyleSheet("#Queen_TLine9_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine9_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine9_butt.setText("")
        self.Queen_TLine9_butt.setCheckable(True)
        self.Queen_TLine9_butt.setObjectName("Queen_TLine9_butt")
        self.Queen_TLine6_butt = QtWidgets.QPushButton(self.Queen_groupBox)
        self.Queen_TLine6_butt.setEnabled(False)
        self.Queen_TLine6_butt.setGeometry(QtCore.QRect(22, 120, 9, 12))
        self.Queen_TLine6_butt.setStyleSheet("#Queen_TLine6_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine6_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine6_butt.setText("")
        self.Queen_TLine6_butt.setCheckable(True)
        self.Queen_TLine6_butt.setObjectName("Queen_TLine6_butt")
        self.layoutWidget_6 = QtWidgets.QWidget(self.Window_groupBox)
        self.layoutWidget_6.setGeometry(QtCore.QRect(820, 600, 83, 84))
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
        self.PV_Va_label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PV_Va_label.setFont(font)
        self.PV_Va_label.setObjectName("PV_Va_label")
        self.verticalLayout_20.addWidget(self.PV_Va_label)
        self.PV_Ia_label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PV_Ia_label.setFont(font)
        self.PV_Ia_label.setObjectName("PV_Ia_label")
        self.verticalLayout_20.addWidget(self.PV_Ia_label)
        self.horizontalLayout_7.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.PV_live_Va_label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.PV_live_Va_label.setFont(font)
        self.PV_live_Va_label.setObjectName("PV_live_Va_label")
        self.verticalLayout_21.addWidget(self.PV_live_Va_label)
        self.PV_live_Ia_label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.PV_live_Ia_label.setFont(font)
        self.PV_live_Ia_label.setObjectName("PV_live_Ia_label")
        self.verticalLayout_21.addWidget(self.PV_live_Ia_label)
        self.horizontalLayout_7.addLayout(self.verticalLayout_21)
        self.verticalLayout_19.addWidget(self.frame_6)
        self.PV_expand_butt = QtWidgets.QPushButton(self.layoutWidget_6)
        self.PV_expand_butt.setMinimumSize(QtCore.QSize(70, 20))
        self.PV_expand_butt.setMaximumSize(QtCore.QSize(80, 20))
        self.PV_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.PV_expand_butt.setStyleSheet("#PV_expand_butt{\n"
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
"#PV_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.PV_expand_butt.setCheckable(True)
        self.PV_expand_butt.setObjectName("PV_expand_butt")
        self.verticalLayout_19.addWidget(self.PV_expand_butt)
        self.Poker_to_PV_Rel_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_to_PV_Rel_butt.setGeometry(QtCore.QRect(734, 548, 31, 31))
        self.Poker_to_PV_Rel_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Poker_to_PV_Rel_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Poker_to_PV_Rel_butt.setStyleSheet("#Poker_to_PV_Rel_butt{\n"
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
"#Poker_to_PV_Rel_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_to_PV_Rel_butt.setText("")
        self.Poker_to_PV_Rel_butt.setCheckable(True)
        self.Poker_to_PV_Rel_butt.setObjectName("Poker_to_PV_Rel_butt")
        self.Ace_TLine1_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Ace_TLine1_butt.setEnabled(False)
        self.Ace_TLine1_butt.setGeometry(QtCore.QRect(60, 30, 15, 9))
        self.Ace_TLine1_butt.setMinimumSize(QtCore.QSize(15, 9))
        self.Ace_TLine1_butt.setStyleSheet("#Ace_TLine1_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine1_butt.setText("")
        self.Ace_TLine1_butt.setCheckable(True)
        self.Ace_TLine1_butt.setObjectName("Ace_TLine1_butt")
        self.Ace_to_Poker_TLine_butt1 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Ace_to_Poker_TLine_butt1.setEnabled(False)
        self.Ace_to_Poker_TLine_butt1.setGeometry(QtCore.QRect(180, 262, 369, 9))
        self.Ace_to_Poker_TLine_butt1.setMinimumSize(QtCore.QSize(50, 9))
        self.Ace_to_Poker_TLine_butt1.setStyleSheet("#Ace_to_Poker_TLine_butt1{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_to_Poker_TLine_butt1:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_to_Poker_TLine_butt1.setText("")
        self.Ace_to_Poker_TLine_butt1.setCheckable(True)
        self.Ace_to_Poker_TLine_butt1.setObjectName("Ace_to_Poker_TLine_butt1")
        self.Poker_to_PV_TLine_butt2 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_to_PV_TLine_butt2.setEnabled(False)
        self.Poker_to_PV_TLine_butt2.setGeometry(QtCore.QRect(746, 480, 9, 69))
        self.Poker_to_PV_TLine_butt2.setMinimumSize(QtCore.QSize(1, 1))
        self.Poker_to_PV_TLine_butt2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Poker_to_PV_TLine_butt2.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_to_PV_TLine_butt2.setStyleSheet("#Poker_to_PV_TLine_butt2{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_to_PV_TLine_butt2:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_to_PV_TLine_butt2.setText("")
        self.Poker_to_PV_TLine_butt2.setCheckable(True)
        self.Poker_to_PV_TLine_butt2.setObjectName("Poker_to_PV_TLine_butt2")
        self.Ace_to_Poker_TLine_butt2 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Ace_to_Poker_TLine_butt2.setEnabled(False)
        self.Ace_to_Poker_TLine_butt2.setGeometry(QtCore.QRect(540, 270, 9, 89))
        self.Ace_to_Poker_TLine_butt2.setMinimumSize(QtCore.QSize(1, 1))
        self.Ace_to_Poker_TLine_butt2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Ace_to_Poker_TLine_butt2.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_to_Poker_TLine_butt2.setStyleSheet("#Ace_to_Poker_TLine_butt2{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_to_Poker_TLine_butt2:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_to_Poker_TLine_butt2.setText("")
        self.Ace_to_Poker_TLine_butt2.setCheckable(True)
        self.Ace_to_Poker_TLine_butt2.setObjectName("Ace_to_Poker_TLine_butt2")
        self.layoutWidget_5 = QtWidgets.QWidget(self.Window_groupBox)
        self.layoutWidget_5.setGeometry(QtCore.QRect(1150, 360, 86, 84))
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
        self.Joker_Va_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.Joker_Va_label.setFont(font)
        self.Joker_Va_label.setObjectName("Joker_Va_label")
        self.verticalLayout_17.addWidget(self.Joker_Va_label)
        self.Joker_Ia_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        self.Joker_Ia_label.setFont(font)
        self.Joker_Ia_label.setObjectName("Joker_Ia_label")
        self.verticalLayout_17.addWidget(self.Joker_Ia_label)
        self.horizontalLayout_6.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.Joker_live_Va_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Joker_live_Va_label.setFont(font)
        self.Joker_live_Va_label.setObjectName("Joker_live_Va_label")
        self.verticalLayout_18.addWidget(self.Joker_live_Va_label)
        self.Joker_live_Ia_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Joker_live_Ia_label.setFont(font)
        self.Joker_live_Ia_label.setObjectName("Joker_live_Ia_label")
        self.verticalLayout_18.addWidget(self.Joker_live_Ia_label)
        self.horizontalLayout_6.addLayout(self.verticalLayout_18)
        self.verticalLayout_16.addWidget(self.frame_5)
        self.Joker_expand_butt = QtWidgets.QPushButton(self.layoutWidget_5)
        self.Joker_expand_butt.setMinimumSize(QtCore.QSize(70, 20))
        self.Joker_expand_butt.setMaximumSize(QtCore.QSize(80, 20))
        self.Joker_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_expand_butt.setStyleSheet("#Joker_expand_butt{\n"
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
"#Joker_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.Joker_expand_butt.setCheckable(True)
        self.Joker_expand_butt.setObjectName("Joker_expand_butt")
        self.verticalLayout_16.addWidget(self.Joker_expand_butt)
        self.Deuce_to_Queen_TLine_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Deuce_to_Queen_TLine_butt.setEnabled(False)
        self.Deuce_to_Queen_TLine_butt.setGeometry(QtCore.QRect(1851, 150, 9, 651))
        self.Deuce_to_Queen_TLine_butt.setMinimumSize(QtCore.QSize(1, 500))
        self.Deuce_to_Queen_TLine_butt.setMaximumSize(QtCore.QSize(32, 651))
        self.Deuce_to_Queen_TLine_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_to_Queen_TLine_butt.setStyleSheet("#Deuce_to_Queen_TLine_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"\n"
"\n"
"}\n"
"#Deuce_to_Queen_TLine_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_to_Queen_TLine_butt.setText("")
        self.Deuce_to_Queen_TLine_butt.setCheckable(True)
        self.Deuce_to_Queen_TLine_butt.setObjectName("Deuce_to_Queen_TLine_butt")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Window_groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(660, 360, 86, 84))
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
        self.Poker_Va_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Poker_Va_label.setFont(font)
        self.Poker_Va_label.setObjectName("Poker_Va_label")
        self.verticalLayout_8.addWidget(self.Poker_Va_label)
        self.Poker_Ia_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Poker_Ia_label.setFont(font)
        self.Poker_Ia_label.setObjectName("Poker_Ia_label")
        self.verticalLayout_8.addWidget(self.Poker_Ia_label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Poker_live_Va_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Poker_live_Va_label.setFont(font)
        self.Poker_live_Va_label.setObjectName("Poker_live_Va_label")
        self.verticalLayout_9.addWidget(self.Poker_live_Va_label)
        self.Poker_live_Ia_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Poker_live_Ia_label.setFont(font)
        self.Poker_live_Ia_label.setObjectName("Poker_live_Ia_label")
        self.verticalLayout_9.addWidget(self.Poker_live_Ia_label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.Poker_expand_butt = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Poker_expand_butt.setMinimumSize(QtCore.QSize(70, 20))
        self.Poker_expand_butt.setMaximumSize(QtCore.QSize(80, 20))
        self.Poker_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_expand_butt.setStyleSheet("#Poker_expand_butt{\n"
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
"#Poker_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.Poker_expand_butt.setCheckable(True)
        self.Poker_expand_butt.setObjectName("Poker_expand_butt")
        self.verticalLayout_7.addWidget(self.Poker_expand_butt)
        self.Poker_to_King_TLine_butt1 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_to_King_TLine_butt1.setEnabled(False)
        self.Poker_to_King_TLine_butt1.setGeometry(QtCore.QRect(180, 671, 369, 9))
        self.Poker_to_King_TLine_butt1.setMinimumSize(QtCore.QSize(50, 9))
        self.Poker_to_King_TLine_butt1.setStyleSheet("#Poker_to_King_TLine_butt1{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_to_King_TLine_butt1:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_to_King_TLine_butt1.setText("")
        self.Poker_to_King_TLine_butt1.setCheckable(True)
        self.Poker_to_King_TLine_butt1.setObjectName("Poker_to_King_TLine_butt1")
        self.layoutWidget = QtWidgets.QWidget(self.Window_groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 10, 86, 84))
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
        self.Ace_Va_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Ace_Va_label.setFont(font)
        self.Ace_Va_label.setObjectName("Ace_Va_label")
        self.verticalLayout.addWidget(self.Ace_Va_label)
        self.Ace_Ia_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Ace_Ia_label.setFont(font)
        self.Ace_Ia_label.setObjectName("Ace_Ia_label")
        self.verticalLayout.addWidget(self.Ace_Ia_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Ace_live_Va_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Ace_live_Va_label.setFont(font)
        self.Ace_live_Va_label.setObjectName("Ace_live_Va_label")
        self.verticalLayout_2.addWidget(self.Ace_live_Va_label)
        self.Ace_live_Ia_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Ace_live_Ia_label.setFont(font)
        self.Ace_live_Ia_label.setObjectName("Ace_live_Ia_label")
        self.verticalLayout_2.addWidget(self.Ace_live_Ia_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.Ace_expand_butt = QtWidgets.QPushButton(self.layoutWidget)
        self.Ace_expand_butt.setMinimumSize(QtCore.QSize(70, 20))
        self.Ace_expand_butt.setMaximumSize(QtCore.QSize(80, 20))
        self.Ace_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_expand_butt.setStyleSheet("#Ace_expand_butt{\n"
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
"#Ace_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.Ace_expand_butt.setCheckable(True)
        self.Ace_expand_butt.setObjectName("Ace_expand_butt")
        self.verticalLayout_3.addWidget(self.Ace_expand_butt)
        self.Queen_to_King_TLine_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Queen_to_King_TLine_butt.setEnabled(False)
        self.Queen_to_King_TLine_butt.setGeometry(QtCore.QRect(311, 792, 1289, 9))
        self.Queen_to_King_TLine_butt.setMinimumSize(QtCore.QSize(50, 9))
        self.Queen_to_King_TLine_butt.setStyleSheet("#Queen_to_King_TLine_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_to_King_TLine_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_to_King_TLine_butt.setText("")
        self.Queen_to_King_TLine_butt.setCheckable(True)
        self.Queen_to_King_TLine_butt.setObjectName("Queen_to_King_TLine_butt")
        self.Deuce_Rel1_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Deuce_Rel1_butt.setGeometry(QtCore.QRect(1801, 19, 31, 31))
        self.Deuce_Rel1_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel1_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel1_butt.setStyleSheet("#Deuce_Rel1_butt{\n"
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
"#Deuce_Rel1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_Rel1_butt.setText("")
        self.Deuce_Rel1_butt.setCheckable(True)
        self.Deuce_Rel1_butt.setObjectName("Deuce_Rel1_butt")
        self.Deuce_groupBox = QtWidgets.QGroupBox(self.Window_groupBox)
        self.Deuce_groupBox.setGeometry(QtCore.QRect(1600, 38, 251, 224))
        self.Deuce_groupBox.setTitle("")
        self.Deuce_groupBox.setObjectName("Deuce_groupBox")
        self.label_20 = QtWidgets.QLabel(self.Deuce_groupBox)
        self.label_20.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.Deuce_TLine9_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine9_butt.setEnabled(False)
        self.Deuce_TLine9_butt.setGeometry(QtCore.QRect(172, 191, 46, 9))
        self.Deuce_TLine9_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Deuce_TLine9_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Deuce_TLine9_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine9_butt.setStyleSheet("#Deuce_TLine9_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine9_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine9_butt.setText("")
        self.Deuce_TLine9_butt.setCheckable(True)
        self.Deuce_TLine9_butt.setObjectName("Deuce_TLine9_butt")
        self.label_21 = QtWidgets.QLabel(self.Deuce_groupBox)
        self.label_21.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_21.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.Deuce_TLine7_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine7_butt.setEnabled(False)
        self.Deuce_TLine7_butt.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.Deuce_TLine7_butt.setStyleSheet("#Deuce_TLine7_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine7_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine7_butt.setText("")
        self.Deuce_TLine7_butt.setCheckable(True)
        self.Deuce_TLine7_butt.setObjectName("Deuce_TLine7_butt")
        self.Deuce_TLine4_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine4_butt.setEnabled(False)
        self.Deuce_TLine4_butt.setGeometry(QtCore.QRect(128, 23, 99, 9))
        self.Deuce_TLine4_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Deuce_TLine4_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Deuce_TLine4_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine4_butt.setStyleSheet("#Deuce_TLine4_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine4_butt.setText("")
        self.Deuce_TLine4_butt.setCheckable(True)
        self.Deuce_TLine4_butt.setObjectName("Deuce_TLine4_butt")
        self.Deuce_Rel4_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_Rel4_butt.setGeometry(QtCore.QRect(10, 131, 31, 31))
        self.Deuce_Rel4_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel4_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel4_butt.setStyleSheet("#Deuce_Rel4_butt{\n"
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
"#Deuce_Rel4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_Rel4_butt.setText("")
        self.Deuce_Rel4_butt.setCheckable(True)
        self.Deuce_Rel4_butt.setObjectName("Deuce_Rel4_butt")
        self.Deuce_TLine12_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine12_butt.setEnabled(False)
        self.Deuce_TLine12_butt.setGeometry(QtCore.QRect(31, 191, 89, 9))
        self.Deuce_TLine12_butt.setMinimumSize(QtCore.QSize(26, 4))
        self.Deuce_TLine12_butt.setMaximumSize(QtCore.QSize(300, 40))
        self.Deuce_TLine12_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine12_butt.setStyleSheet("#Deuce_TLine12_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine12_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine12_butt.setText("")
        self.Deuce_TLine12_butt.setCheckable(True)
        self.Deuce_TLine12_butt.setObjectName("Deuce_TLine12_butt")
        self.Deuce_TLine18_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine18_butt.setEnabled(False)
        self.Deuce_TLine18_butt.setGeometry(QtCore.QRect(106, 23, 15, 9))
        self.Deuce_TLine18_butt.setMinimumSize(QtCore.QSize(15, 4))
        self.Deuce_TLine18_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Deuce_TLine18_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine18_butt.setStyleSheet("#Deuce_TLine18_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine18_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine18_butt.setText("")
        self.Deuce_TLine18_butt.setCheckable(True)
        self.Deuce_TLine18_butt.setObjectName("Deuce_TLine18_butt")
        self.Deuce_TLine3_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine3_butt.setEnabled(False)
        self.Deuce_TLine3_butt.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.Deuce_TLine3_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Deuce_TLine3_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Deuce_TLine3_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine3_butt.setStyleSheet("#Deuce_TLine3_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine3_butt.setText("")
        self.Deuce_TLine3_butt.setCheckable(True)
        self.Deuce_TLine3_butt.setObjectName("Deuce_TLine3_butt")
        self.Deuce_Rel2_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_Rel2_butt.setGeometry(QtCore.QRect(205, 67, 31, 31))
        self.Deuce_Rel2_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel2_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel2_butt.setStyleSheet("#Deuce_Rel2_butt{\n"
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
"#Deuce_Rel2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_Rel2_butt.setText("")
        self.Deuce_Rel2_butt.setCheckable(True)
        self.Deuce_Rel2_butt.setObjectName("Deuce_Rel2_butt")
        self.Deuce_TLine16_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine16_butt.setEnabled(False)
        self.Deuce_TLine16_butt.setGeometry(QtCore.QRect(22, 31, 9, 81))
        self.Deuce_TLine16_butt.setStyleSheet("#Deuce_TLine16_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine16_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine16_butt.setText("")
        self.Deuce_TLine16_butt.setCheckable(True)
        self.Deuce_TLine16_butt.setObjectName("Deuce_TLine16_butt")
        self.Deuce_TLine6_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine6_butt.setEnabled(False)
        self.Deuce_TLine6_butt.setGeometry(QtCore.QRect(218, 97, 9, 15))
        self.Deuce_TLine6_butt.setStyleSheet("#Deuce_TLine6_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine6_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine6_butt.setText("")
        self.Deuce_TLine6_butt.setCheckable(True)
        self.Deuce_TLine6_butt.setObjectName("Deuce_TLine6_butt")
        self.Deuce_Rel3_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_Rel3_butt.setGeometry(QtCore.QRect(142, 180, 31, 31))
        self.Deuce_Rel3_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel3_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel3_butt.setStyleSheet("#Deuce_Rel3_butt{\n"
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
"#Deuce_Rel3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_Rel3_butt.setText("")
        self.Deuce_Rel3_butt.setCheckable(True)
        self.Deuce_Rel3_butt.setObjectName("Deuce_Rel3_butt")
        self.Deuce_TLine15_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine15_butt.setEnabled(False)
        self.Deuce_TLine15_butt.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.Deuce_TLine15_butt.setStyleSheet("#Deuce_TLine15_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine15_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine15_butt.setText("")
        self.Deuce_TLine15_butt.setCheckable(True)
        self.Deuce_TLine15_butt.setObjectName("Deuce_TLine15_butt")
        self.Deuce_TLine11_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine11_butt.setEnabled(False)
        self.Deuce_TLine11_butt.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.Deuce_TLine11_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Deuce_TLine11_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Deuce_TLine11_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine11_butt.setStyleSheet("#Deuce_TLine11_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine11_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine11_butt.setText("")
        self.Deuce_TLine11_butt.setCheckable(True)
        self.Deuce_TLine11_butt.setObjectName("Deuce_TLine11_butt")
        self.Deuce_Rel5_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_Rel5_butt.setGeometry(QtCore.QRect(76, 12, 31, 31))
        self.Deuce_Rel5_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel5_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Deuce_Rel5_butt.setStyleSheet("#Deuce_Rel5_butt{\n"
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
"#Deuce_Rel5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_Rel5_butt.setText("")
        self.Deuce_Rel5_butt.setCheckable(True)
        self.Deuce_Rel5_butt.setObjectName("Deuce_Rel5_butt")
        self.Deuce_TLine8_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine8_butt.setEnabled(False)
        self.Deuce_TLine8_butt.setGeometry(QtCore.QRect(218, 121, 9, 79))
        self.Deuce_TLine8_butt.setStyleSheet("#Deuce_TLine8_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine8_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine8_butt.setText("")
        self.Deuce_TLine8_butt.setCheckable(True)
        self.Deuce_TLine8_butt.setObjectName("Deuce_TLine8_butt")
        self.Deuce_TLine5_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine5_butt.setEnabled(False)
        self.Deuce_TLine5_butt.setGeometry(QtCore.QRect(218, 23, 9, 45))
        self.Deuce_TLine5_butt.setStyleSheet("#Deuce_TLine5_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine5_butt.setText("")
        self.Deuce_TLine5_butt.setCheckable(True)
        self.Deuce_TLine5_butt.setObjectName("Deuce_TLine5_butt")
        self.Deuce_TLine13_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine13_butt.setEnabled(False)
        self.Deuce_TLine13_butt.setGeometry(QtCore.QRect(22, 161, 9, 39))
        self.Deuce_TLine13_butt.setStyleSheet("#Deuce_TLine13_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine13_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine13_butt.setText("")
        self.Deuce_TLine13_butt.setCheckable(True)
        self.Deuce_TLine13_butt.setObjectName("Deuce_TLine13_butt")
        self.Deuce_TLine10_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine10_butt.setEnabled(False)
        self.Deuce_TLine10_butt.setGeometry(QtCore.QRect(129, 191, 14, 9))
        self.Deuce_TLine10_butt.setMinimumSize(QtCore.QSize(12, 4))
        self.Deuce_TLine10_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Deuce_TLine10_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine10_butt.setStyleSheet("#Deuce_TLine10_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine10_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine10_butt.setText("")
        self.Deuce_TLine10_butt.setCheckable(True)
        self.Deuce_TLine10_butt.setObjectName("Deuce_TLine10_butt")
        self.Deuce_TLine17_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine17_butt.setEnabled(False)
        self.Deuce_TLine17_butt.setGeometry(QtCore.QRect(22, 23, 55, 9))
        self.Deuce_TLine17_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Deuce_TLine17_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Deuce_TLine17_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine17_butt.setStyleSheet("#Deuce_TLine17_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine17_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine17_butt.setText("")
        self.Deuce_TLine17_butt.setCheckable(True)
        self.Deuce_TLine17_butt.setObjectName("Deuce_TLine17_butt")
        self.Deuce_TLine14_butt = QtWidgets.QPushButton(self.Deuce_groupBox)
        self.Deuce_TLine14_butt.setEnabled(False)
        self.Deuce_TLine14_butt.setGeometry(QtCore.QRect(22, 120, 9, 13))
        self.Deuce_TLine14_butt.setStyleSheet("#Deuce_TLine14_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine14_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine14_butt.setText("")
        self.Deuce_TLine14_butt.setCheckable(True)
        self.Deuce_TLine14_butt.setObjectName("Deuce_TLine14_butt")
        self.Deuce_to_Joker_TLine_butt2 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Deuce_to_Joker_TLine_butt2.setEnabled(False)
        self.Deuce_to_Joker_TLine_butt2.setGeometry(QtCore.QRect(1358, 270, 9, 89))
        self.Deuce_to_Joker_TLine_butt2.setMinimumSize(QtCore.QSize(1, 1))
        self.Deuce_to_Joker_TLine_butt2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Deuce_to_Joker_TLine_butt2.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_to_Joker_TLine_butt2.setStyleSheet("#Deuce_to_Joker_TLine_butt2{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_to_Joker_TLine_butt2:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_to_Joker_TLine_butt2.setText("")
        self.Deuce_to_Joker_TLine_butt2.setCheckable(True)
        self.Deuce_to_Joker_TLine_butt2.setObjectName("Deuce_to_Joker_TLine_butt2")
        self.layoutWidget_4 = QtWidgets.QWidget(self.Window_groupBox)
        self.layoutWidget_4.setGeometry(QtCore.QRect(1520, 10, 86, 84))
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
        self.Deuce_Va_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Deuce_Va_label.setFont(font)
        self.Deuce_Va_label.setObjectName("Deuce_Va_label")
        self.verticalLayout_14.addWidget(self.Deuce_Va_label)
        self.Deuce_Ia_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Deuce_Ia_label.setFont(font)
        self.Deuce_Ia_label.setObjectName("Deuce_Ia_label")
        self.verticalLayout_14.addWidget(self.Deuce_Ia_label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.Deuce_live_Va_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Deuce_live_Va_label.setFont(font)
        self.Deuce_live_Va_label.setObjectName("Deuce_live_Va_label")
        self.verticalLayout_15.addWidget(self.Deuce_live_Va_label)
        self.Deuce_live_Ia_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Deuce_live_Ia_label.setFont(font)
        self.Deuce_live_Ia_label.setObjectName("Deuce_live_Ia_label")
        self.verticalLayout_15.addWidget(self.Deuce_live_Ia_label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_15)
        self.verticalLayout_13.addWidget(self.frame_4)
        self.Deuce_expand_butt = QtWidgets.QPushButton(self.layoutWidget_4)
        self.Deuce_expand_butt.setMinimumSize(QtCore.QSize(70, 20))
        self.Deuce_expand_butt.setMaximumSize(QtCore.QSize(80, 20))
        self.Deuce_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_expand_butt.setStyleSheet("#Deuce_expand_butt{\n"
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
"#Deuce_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.Deuce_expand_butt.setCheckable(True)
        self.Deuce_expand_butt.setObjectName("Deuce_expand_butt")
        self.verticalLayout_13.addWidget(self.Deuce_expand_butt)
        self.Joker_to_Queen_TLine_butt2 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Joker_to_Queen_TLine_butt2.setEnabled(False)
        self.Joker_to_Queen_TLine_butt2.setGeometry(QtCore.QRect(1358, 583, 9, 89))
        self.Joker_to_Queen_TLine_butt2.setMinimumSize(QtCore.QSize(1, 1))
        self.Joker_to_Queen_TLine_butt2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Joker_to_Queen_TLine_butt2.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_to_Queen_TLine_butt2.setStyleSheet("#Joker_to_Queen_TLine_butt2{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_to_Queen_TLine_butt2:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_to_Queen_TLine_butt2.setText("")
        self.Joker_to_Queen_TLine_butt2.setCheckable(True)
        self.Joker_to_Queen_TLine_butt2.setObjectName("Joker_to_Queen_TLine_butt2")
        self.layoutWidget_3 = QtWidgets.QWidget(self.Window_groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(1520, 700, 86, 84))
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
        self.Queen_Va_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Queen_Va_label.setFont(font)
        self.Queen_Va_label.setObjectName("Queen_Va_label")
        self.verticalLayout_11.addWidget(self.Queen_Va_label)
        self.Queen_Ia_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Queen_Ia_label.setFont(font)
        self.Queen_Ia_label.setObjectName("Queen_Ia_label")
        self.verticalLayout_11.addWidget(self.Queen_Ia_label)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Queen_live_Va_label = QtWidgets.QLabel(self.frame_3)
        self.Queen_live_Va_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Queen_live_Va_label.setFont(font)
        self.Queen_live_Va_label.setObjectName("Queen_live_Va_label")
        self.verticalLayout_12.addWidget(self.Queen_live_Va_label)
        self.Queen_live_Ia_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Queen_live_Ia_label.setFont(font)
        self.Queen_live_Ia_label.setObjectName("Queen_live_Ia_label")
        self.verticalLayout_12.addWidget(self.Queen_live_Ia_label)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_10.addWidget(self.frame_3)
        self.Queen_expand_butt = QtWidgets.QPushButton(self.layoutWidget_3)
        self.Queen_expand_butt.setMinimumSize(QtCore.QSize(70, 20))
        self.Queen_expand_butt.setMaximumSize(QtCore.QSize(80, 20))
        self.Queen_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_expand_butt.setStyleSheet("#Queen_expand_butt{\n"
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
"#Queen_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.Queen_expand_butt.setCheckable(True)
        self.Queen_expand_butt.setObjectName("Queen_expand_butt")
        self.verticalLayout_10.addWidget(self.Queen_expand_butt)
        self.groupBox = QtWidgets.QGroupBox(self.Window_groupBox)
        self.groupBox.setGeometry(QtCore.QRect(670, 600, 151, 151))
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.PV_Image_label = QtWidgets.QLabel(self.groupBox)
        self.PV_Image_label.setGeometry(QtCore.QRect(10, 11, 132, 130))
        self.PV_Image_label.setStyleSheet("border-image: url(:/img/Solar_energy128px.png);\n"
"")
        self.PV_Image_label.setText("")
        self.PV_Image_label.setObjectName("PV_Image_label")
        self.Poker_to_PV_TLine_butt3 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_to_PV_TLine_butt3.setEnabled(False)
        self.Poker_to_PV_TLine_butt3.setGeometry(QtCore.QRect(746, 578, 9, 23))
        self.Poker_to_PV_TLine_butt3.setMinimumSize(QtCore.QSize(1, 1))
        self.Poker_to_PV_TLine_butt3.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Poker_to_PV_TLine_butt3.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_to_PV_TLine_butt3.setStyleSheet("#Poker_to_PV_TLine_butt3{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_to_PV_TLine_butt3:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_to_PV_TLine_butt3.setText("")
        self.Poker_to_PV_TLine_butt3.setCheckable(True)
        self.Poker_to_PV_TLine_butt3.setObjectName("Poker_to_PV_TLine_butt3")
        self.Poker_groupBox = QtWidgets.QGroupBox(self.Window_groupBox)
        self.Poker_groupBox.setGeometry(QtCore.QRect(420, 359, 251, 224))
        self.Poker_groupBox.setTitle("")
        self.Poker_groupBox.setObjectName("Poker_groupBox")
        self.label_18 = QtWidgets.QLabel(self.Poker_groupBox)
        self.label_18.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.Poker_TLine11_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine11_butt.setEnabled(False)
        self.Poker_TLine11_butt.setGeometry(QtCore.QRect(31, 191, 46, 9))
        self.Poker_TLine11_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Poker_TLine11_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Poker_TLine11_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_TLine11_butt.setStyleSheet("#Poker_TLine11_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine11_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine11_butt.setText("")
        self.Poker_TLine11_butt.setCheckable(True)
        self.Poker_TLine11_butt.setObjectName("Poker_TLine11_butt")
        self.label_19 = QtWidgets.QLabel(self.Poker_groupBox)
        self.label_19.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_19.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.Poker_TLine5_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine5_butt.setEnabled(False)
        self.Poker_TLine5_butt.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.Poker_TLine5_butt.setStyleSheet("#Poker_TLine5_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine5_butt.setText("")
        self.Poker_TLine5_butt.setCheckable(True)
        self.Poker_TLine5_butt.setObjectName("Poker_TLine5_butt")
        self.Poker_TLine16_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine16_butt.setEnabled(False)
        self.Poker_TLine16_butt.setGeometry(QtCore.QRect(31, 23, 89, 9))
        self.Poker_TLine16_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Poker_TLine16_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Poker_TLine16_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_TLine16_butt.setStyleSheet("#Poker_TLine16_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine16_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine16_butt.setText("")
        self.Poker_TLine16_butt.setCheckable(True)
        self.Poker_TLine16_butt.setObjectName("Poker_TLine16_butt")
        self.Poker_Rel4_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_Rel4_butt.setGeometry(QtCore.QRect(10, 67, 31, 31))
        self.Poker_Rel4_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Poker_Rel4_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Poker_Rel4_butt.setStyleSheet("#Poker_Rel4_butt{\n"
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
"#Poker_Rel4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_Rel4_butt.setText("")
        self.Poker_Rel4_butt.setCheckable(True)
        self.Poker_Rel4_butt.setObjectName("Poker_Rel4_butt")
        self.Poker_TLine8_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine8_butt.setEnabled(False)
        self.Poker_TLine8_butt.setGeometry(QtCore.QRect(129, 191, 89, 9))
        self.Poker_TLine8_butt.setMinimumSize(QtCore.QSize(26, 4))
        self.Poker_TLine8_butt.setMaximumSize(QtCore.QSize(300, 40))
        self.Poker_TLine8_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_TLine8_butt.setStyleSheet("#Poker_TLine8_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine8_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine8_butt.setText("")
        self.Poker_TLine8_butt.setCheckable(True)
        self.Poker_TLine8_butt.setObjectName("Poker_TLine8_butt")
        self.Poker_TLine2_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine2_butt.setEnabled(False)
        self.Poker_TLine2_butt.setGeometry(QtCore.QRect(129, 23, 15, 9))
        self.Poker_TLine2_butt.setMinimumSize(QtCore.QSize(15, 4))
        self.Poker_TLine2_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Poker_TLine2_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_TLine2_butt.setStyleSheet("#Poker_TLine2_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine2_butt.setText("")
        self.Poker_TLine2_butt.setCheckable(True)
        self.Poker_TLine2_butt.setObjectName("Poker_TLine2_butt")
        self.Poker_TLine1_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine1_butt.setEnabled(False)
        self.Poker_TLine1_butt.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.Poker_TLine1_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Poker_TLine1_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Poker_TLine1_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_TLine1_butt.setStyleSheet("#Poker_TLine1_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine1_butt.setText("")
        self.Poker_TLine1_butt.setCheckable(True)
        self.Poker_TLine1_butt.setObjectName("Poker_TLine1_butt")
        self.Poker_Rel2_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_Rel2_butt.setGeometry(QtCore.QRect(205, 135, 31, 31))
        self.Poker_Rel2_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Poker_Rel2_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Poker_Rel2_butt.setStyleSheet("#Poker_Rel2_butt{\n"
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
"#Poker_Rel2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_Rel2_butt.setText("")
        self.Poker_Rel2_butt.setCheckable(True)
        self.Poker_Rel2_butt.setObjectName("Poker_Rel2_butt")
        self.Poker_TLine12_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine12_butt.setEnabled(False)
        self.Poker_TLine12_butt.setGeometry(QtCore.QRect(22, 120, 9, 80))
        self.Poker_TLine12_butt.setStyleSheet("#Poker_TLine12_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine12_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine12_butt.setText("")
        self.Poker_TLine12_butt.setCheckable(True)
        self.Poker_TLine12_butt.setObjectName("Poker_TLine12_butt")
        self.Poker_TLine6_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine6_butt.setEnabled(False)
        self.Poker_TLine6_butt.setGeometry(QtCore.QRect(218, 121, 9, 15))
        self.Poker_TLine6_butt.setStyleSheet("#Poker_TLine6_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine6_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine6_butt.setText("")
        self.Poker_TLine6_butt.setCheckable(True)
        self.Poker_TLine6_butt.setObjectName("Poker_TLine6_butt")
        self.Poker_Rel3_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_Rel3_butt.setEnabled(True)
        self.Poker_Rel3_butt.setGeometry(QtCore.QRect(76, 180, 31, 31))
        self.Poker_Rel3_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Poker_Rel3_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Poker_Rel3_butt.setStyleSheet("#Poker_Rel3_butt{\n"
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
"#Poker_Rel3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_Rel3_butt.setText("")
        self.Poker_Rel3_butt.setCheckable(True)
        self.Poker_Rel3_butt.setObjectName("Poker_Rel3_butt")
        self.Poker_TLine13_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine13_butt.setEnabled(False)
        self.Poker_TLine13_butt.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.Poker_TLine13_butt.setStyleSheet("#Poker_TLine13_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine13_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine13_butt.setText("")
        self.Poker_TLine13_butt.setCheckable(True)
        self.Poker_TLine13_butt.setObjectName("Poker_TLine13_butt")
        self.Poker_TLine9_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine9_butt.setEnabled(False)
        self.Poker_TLine9_butt.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.Poker_TLine9_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Poker_TLine9_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Poker_TLine9_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_TLine9_butt.setStyleSheet("#Poker_TLine9_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine9_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine9_butt.setText("")
        self.Poker_TLine9_butt.setCheckable(True)
        self.Poker_TLine9_butt.setObjectName("Poker_TLine9_butt")
        self.Poker_Rel1_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_Rel1_butt.setGeometry(QtCore.QRect(143, 12, 31, 31))
        self.Poker_Rel1_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Poker_Rel1_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Poker_Rel1_butt.setStyleSheet("#Poker_Rel1_butt{\n"
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
"#Poker_Rel1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_Rel1_butt.setText("")
        self.Poker_Rel1_butt.setCheckable(True)
        self.Poker_Rel1_butt.setObjectName("Poker_Rel1_butt")
        self.Poker_TLine4_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine4_butt.setEnabled(False)
        self.Poker_TLine4_butt.setGeometry(QtCore.QRect(218, 32, 9, 80))
        self.Poker_TLine4_butt.setStyleSheet("#Poker_TLine4_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine4_butt.setText("")
        self.Poker_TLine4_butt.setCheckable(True)
        self.Poker_TLine4_butt.setObjectName("Poker_TLine4_butt")
        self.Poker_TLine7_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine7_butt.setEnabled(False)
        self.Poker_TLine7_butt.setGeometry(QtCore.QRect(218, 165, 9, 35))
        self.Poker_TLine7_butt.setStyleSheet("#Poker_TLine7_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine7_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine7_butt.setText("")
        self.Poker_TLine7_butt.setCheckable(True)
        self.Poker_TLine7_butt.setObjectName("Poker_TLine7_butt")
        self.Poker_TLine15_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine15_butt.setEnabled(False)
        self.Poker_TLine15_butt.setGeometry(QtCore.QRect(22, 23, 9, 45))
        self.Poker_TLine15_butt.setStyleSheet("#Poker_TLine15_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine15_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine15_butt.setText("")
        self.Poker_TLine15_butt.setCheckable(True)
        self.Poker_TLine15_butt.setObjectName("Poker_TLine15_butt")
        self.Poker_TLine10_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine10_butt.setEnabled(False)
        self.Poker_TLine10_butt.setGeometry(QtCore.QRect(106, 191, 14, 9))
        self.Poker_TLine10_butt.setMinimumSize(QtCore.QSize(12, 4))
        self.Poker_TLine10_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Poker_TLine10_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_TLine10_butt.setStyleSheet("#Poker_TLine10_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine10_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine10_butt.setText("")
        self.Poker_TLine10_butt.setCheckable(True)
        self.Poker_TLine10_butt.setObjectName("Poker_TLine10_butt")
        self.Poker_TLine3_butt = QtWidgets.QPushButton(self.Poker_groupBox)
        self.Poker_TLine3_butt.setEnabled(False)
        self.Poker_TLine3_butt.setGeometry(QtCore.QRect(173, 23, 54, 9))
        self.Poker_TLine3_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Poker_TLine3_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Poker_TLine3_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_TLine3_butt.setStyleSheet("#Poker_TLine3_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine3_butt.setText("")
        self.Poker_TLine3_butt.setCheckable(True)
        self.Poker_TLine3_butt.setObjectName("Poker_TLine3_butt")
        self.King_groupBox = QtWidgets.QGroupBox(self.Window_groupBox)
        self.King_groupBox.setGeometry(QtCore.QRect(60, 680, 251, 224))
        self.King_groupBox.setTitle("")
        self.King_groupBox.setObjectName("King_groupBox")
        self.label_17 = QtWidgets.QLabel(self.King_groupBox)
        self.label_17.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.King_TLine5_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine5_butt.setEnabled(False)
        self.King_TLine5_butt.setGeometry(QtCore.QRect(31, 191, 46, 9))
        self.King_TLine5_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.King_TLine5_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.King_TLine5_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine5_butt.setStyleSheet("#King_TLine5_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine5_butt.setText("")
        self.King_TLine5_butt.setCheckable(True)
        self.King_TLine5_butt.setObjectName("King_TLine5_butt")
        self.label_15 = QtWidgets.QLabel(self.King_groupBox)
        self.label_15.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_15.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.King_TLine15_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine15_butt.setEnabled(False)
        self.King_TLine15_butt.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.King_TLine15_butt.setStyleSheet("#King_TLine15_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine15_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine15_butt.setText("")
        self.King_TLine15_butt.setCheckable(True)
        self.King_TLine15_butt.setObjectName("King_TLine15_butt")
        self.King_TLine10_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine10_butt.setEnabled(False)
        self.King_TLine10_butt.setGeometry(QtCore.QRect(31, 23, 89, 9))
        self.King_TLine10_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.King_TLine10_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.King_TLine10_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine10_butt.setStyleSheet("#King_TLine10_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine10_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine10_butt.setText("")
        self.King_TLine10_butt.setCheckable(True)
        self.King_TLine10_butt.setObjectName("King_TLine10_butt")
        self.King_Rel3_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_Rel3_butt.setGeometry(QtCore.QRect(10, 67, 31, 31))
        self.King_Rel3_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.King_Rel3_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.King_Rel3_butt.setStyleSheet("#King_Rel3_butt{\n"
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
"#King_Rel3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_Rel3_butt.setText("")
        self.King_Rel3_butt.setCheckable(True)
        self.King_Rel3_butt.setObjectName("King_Rel3_butt")
        self.King_TLine18_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine18_butt.setEnabled(False)
        self.King_TLine18_butt.setGeometry(QtCore.QRect(129, 191, 89, 9))
        self.King_TLine18_butt.setMinimumSize(QtCore.QSize(26, 4))
        self.King_TLine18_butt.setMaximumSize(QtCore.QSize(300, 40))
        self.King_TLine18_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine18_butt.setStyleSheet("#King_TLine18_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine18_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine18_butt.setText("")
        self.King_TLine18_butt.setCheckable(True)
        self.King_TLine18_butt.setObjectName("King_TLine18_butt")
        self.King_TLine12_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine12_butt.setEnabled(False)
        self.King_TLine12_butt.setGeometry(QtCore.QRect(129, 23, 15, 9))
        self.King_TLine12_butt.setMinimumSize(QtCore.QSize(15, 4))
        self.King_TLine12_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.King_TLine12_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine12_butt.setStyleSheet("#King_TLine12_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine12_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine12_butt.setText("")
        self.King_TLine12_butt.setCheckable(True)
        self.King_TLine12_butt.setObjectName("King_TLine12_butt")
        self.King_TLine11_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine11_butt.setEnabled(False)
        self.King_TLine11_butt.setGeometry(QtCore.QRect(120, 0, 9, 32))
        self.King_TLine11_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.King_TLine11_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.King_TLine11_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine11_butt.setStyleSheet("#King_TLine11_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine11_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine11_butt.setText("")
        self.King_TLine11_butt.setCheckable(True)
        self.King_TLine11_butt.setObjectName("King_TLine11_butt")
        self.King_Rel5_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_Rel5_butt.setGeometry(QtCore.QRect(205, 135, 31, 31))
        self.King_Rel5_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.King_Rel5_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.King_Rel5_butt.setStyleSheet("#King_Rel5_butt{\n"
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
"#King_Rel5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_Rel5_butt.setText("")
        self.King_Rel5_butt.setCheckable(True)
        self.King_Rel5_butt.setObjectName("King_Rel5_butt")
        self.King_TLine6_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine6_butt.setEnabled(False)
        self.King_TLine6_butt.setGeometry(QtCore.QRect(22, 120, 9, 80))
        self.King_TLine6_butt.setStyleSheet("#King_TLine6_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine6_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine6_butt.setText("")
        self.King_TLine6_butt.setCheckable(True)
        self.King_TLine6_butt.setObjectName("King_TLine6_butt")
        self.King_TLine16_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine16_butt.setEnabled(False)
        self.King_TLine16_butt.setGeometry(QtCore.QRect(218, 121, 9, 15))
        self.King_TLine16_butt.setStyleSheet("#King_TLine16_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine16_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine16_butt.setText("")
        self.King_TLine16_butt.setCheckable(True)
        self.King_TLine16_butt.setObjectName("King_TLine16_butt")
        self.King_Rel2_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_Rel2_butt.setGeometry(QtCore.QRect(76, 180, 31, 31))
        self.King_Rel2_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.King_Rel2_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.King_Rel2_butt.setStyleSheet("#King_Rel2_butt{\n"
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
"#King_Rel2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_Rel2_butt.setText("")
        self.King_Rel2_butt.setCheckable(True)
        self.King_Rel2_butt.setObjectName("King_Rel2_butt")
        self.King_TLine7_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine7_butt.setEnabled(False)
        self.King_TLine7_butt.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.King_TLine7_butt.setStyleSheet("#King_TLine7_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine7_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine7_butt.setText("")
        self.King_TLine7_butt.setCheckable(True)
        self.King_TLine7_butt.setObjectName("King_TLine7_butt")
        self.King_TLine3_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine3_butt.setEnabled(False)
        self.King_TLine3_butt.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.King_TLine3_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.King_TLine3_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.King_TLine3_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine3_butt.setStyleSheet("#King_TLine3_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine3_butt.setText("")
        self.King_TLine3_butt.setCheckable(True)
        self.King_TLine3_butt.setObjectName("King_TLine3_butt")
        self.King_Rel4_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_Rel4_butt.setGeometry(QtCore.QRect(143, 12, 31, 31))
        self.King_Rel4_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.King_Rel4_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.King_Rel4_butt.setStyleSheet("#King_Rel4_butt{\n"
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
"#King_Rel4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_Rel4_butt.setText("")
        self.King_Rel4_butt.setCheckable(True)
        self.King_Rel4_butt.setObjectName("King_Rel4_butt")
        self.King_TLine14_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine14_butt.setEnabled(False)
        self.King_TLine14_butt.setGeometry(QtCore.QRect(218, 32, 9, 80))
        self.King_TLine14_butt.setStyleSheet("#King_TLine14_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine14_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine14_butt.setText("")
        self.King_TLine14_butt.setCheckable(True)
        self.King_TLine14_butt.setObjectName("King_TLine14_butt")
        self.King_TLine17_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine17_butt.setEnabled(False)
        self.King_TLine17_butt.setGeometry(QtCore.QRect(218, 165, 9, 35))
        self.King_TLine17_butt.setStyleSheet("#King_TLine17_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine17_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine17_butt.setText("")
        self.King_TLine17_butt.setCheckable(True)
        self.King_TLine17_butt.setObjectName("King_TLine17_butt")
        self.King_TLine9_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine9_butt.setEnabled(False)
        self.King_TLine9_butt.setGeometry(QtCore.QRect(22, 23, 9, 45))
        self.King_TLine9_butt.setStyleSheet("#King_TLine9_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine9_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine9_butt.setText("")
        self.King_TLine9_butt.setCheckable(True)
        self.King_TLine9_butt.setObjectName("King_TLine9_butt")
        self.King_TLine4_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine4_butt.setEnabled(False)
        self.King_TLine4_butt.setGeometry(QtCore.QRect(106, 191, 14, 9))
        self.King_TLine4_butt.setMinimumSize(QtCore.QSize(12, 4))
        self.King_TLine4_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.King_TLine4_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine4_butt.setStyleSheet("#King_TLine4_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine4_butt.setText("")
        self.King_TLine4_butt.setCheckable(True)
        self.King_TLine4_butt.setObjectName("King_TLine4_butt")
        self.King_TLine13_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine13_butt.setEnabled(False)
        self.King_TLine13_butt.setGeometry(QtCore.QRect(173, 23, 54, 9))
        self.King_TLine13_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.King_TLine13_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.King_TLine13_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine13_butt.setStyleSheet("#King_TLine13_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine13_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine13_butt.setText("")
        self.King_TLine13_butt.setCheckable(True)
        self.King_TLine13_butt.setObjectName("King_TLine13_butt")
        self.King_TLine8_butt = QtWidgets.QPushButton(self.King_groupBox)
        self.King_TLine8_butt.setEnabled(False)
        self.King_TLine8_butt.setGeometry(QtCore.QRect(22, 97, 9, 15))
        self.King_TLine8_butt.setStyleSheet("#King_TLine8_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine8_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine8_butt.setText("")
        self.King_TLine8_butt.setCheckable(True)
        self.King_TLine8_butt.setObjectName("King_TLine8_butt")
        self.Ace_Rel1_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Ace_Rel1_butt.setGeometry(QtCore.QRect(74, 19, 31, 31))
        self.Ace_Rel1_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Ace_Rel1_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Ace_Rel1_butt.setStyleSheet("#Ace_Rel1_butt{\n"
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
"#Ace_Rel1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_Rel1_butt.setText("")
        self.Ace_Rel1_butt.setCheckable(True)
        self.Ace_Rel1_butt.setObjectName("Ace_Rel1_butt")
        self.Poker_to_PV_TLine_butt1 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_to_PV_TLine_butt1.setEnabled(False)
        self.Poker_to_PV_TLine_butt1.setGeometry(QtCore.QRect(670, 471, 85, 9))
        self.Poker_to_PV_TLine_butt1.setMinimumSize(QtCore.QSize(20, 4))
        self.Poker_to_PV_TLine_butt1.setMaximumSize(QtCore.QSize(100, 20))
        self.Poker_to_PV_TLine_butt1.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_to_PV_TLine_butt1.setStyleSheet("#Poker_to_PV_TLine_butt1{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_to_PV_TLine_butt1:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_to_PV_TLine_butt1.setText("")
        self.Poker_to_PV_TLine_butt1.setCheckable(True)
        self.Poker_to_PV_TLine_butt1.setObjectName("Poker_to_PV_TLine_butt1")
        self.King_to_Ace_TLine_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.King_to_Ace_TLine_butt.setEnabled(False)
        self.King_to_Ace_TLine_butt.setGeometry(QtCore.QRect(51, 150, 9, 651))
        self.King_to_Ace_TLine_butt.setMinimumSize(QtCore.QSize(1, 500))
        self.King_to_Ace_TLine_butt.setMaximumSize(QtCore.QSize(32, 700))
        self.King_to_Ace_TLine_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_to_Ace_TLine_butt.setStyleSheet("#King_to_Ace_TLine_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"\n"
"\n"
"}\n"
"#King_to_Ace_TLine_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_to_Ace_TLine_butt.setText("")
        self.King_to_Ace_TLine_butt.setCheckable(True)
        self.King_to_Ace_TLine_butt.setObjectName("King_to_Ace_TLine_butt")
        self.layoutWidget1 = QtWidgets.QWidget(self.Window_groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(310, 700, 86, 84))
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
        self.King_Va_label = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.King_Va_label.setFont(font)
        self.King_Va_label.setObjectName("King_Va_label")
        self.verticalLayout_5.addWidget(self.King_Va_label)
        self.King_Ia_label = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.King_Ia_label.setFont(font)
        self.King_Ia_label.setObjectName("King_Ia_label")
        self.verticalLayout_5.addWidget(self.King_Ia_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.King_live_Va_label = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.King_live_Va_label.setFont(font)
        self.King_live_Va_label.setObjectName("King_live_Va_label")
        self.verticalLayout_6.addWidget(self.King_live_Va_label)
        self.King_live_Ia_label = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.King_live_Ia_label.setFont(font)
        self.King_live_Ia_label.setObjectName("King_live_Ia_label")
        self.verticalLayout_6.addWidget(self.King_live_Ia_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addWidget(self.frame1)
        self.King_expand_butt = QtWidgets.QPushButton(self.layoutWidget1)
        self.King_expand_butt.setMinimumSize(QtCore.QSize(70, 20))
        self.King_expand_butt.setMaximumSize(QtCore.QSize(80, 20))
        self.King_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_expand_butt.setStyleSheet("#King_expand_butt{\n"
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
"#King_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.King_expand_butt.setCheckable(True)
        self.King_expand_butt.setObjectName("King_expand_butt")
        self.verticalLayout_4.addWidget(self.King_expand_butt)
        self.Deuce_LoadBulbButton = QtWidgets.QPushButton(self.Window_groupBox)
        self.Deuce_LoadBulbButton.setEnabled(False)
        self.Deuce_LoadBulbButton.setGeometry(QtCore.QRect(1850, 6, 53, 53))
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
        self.Ace_TLine2_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Ace_TLine2_butt.setEnabled(False)
        self.Ace_TLine2_butt.setGeometry(QtCore.QRect(104, 30, 85, 9))
        self.Ace_TLine2_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Ace_TLine2_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Ace_TLine2_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_TLine2_butt.setStyleSheet("#Ace_TLine2_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine2_butt.setText("")
        self.Ace_TLine2_butt.setCheckable(True)
        self.Ace_TLine2_butt.setObjectName("Ace_TLine2_butt")
        self.Ace_TLine16_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Ace_TLine16_butt.setEnabled(False)
        self.Ace_TLine16_butt.setGeometry(QtCore.QRect(82, 135, 9, 15))
        self.Ace_TLine16_butt.setStyleSheet("#Ace_TLine16_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine16_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine16_butt.setText("")
        self.Ace_TLine16_butt.setCheckable(True)
        self.Ace_TLine16_butt.setObjectName("Ace_TLine16_butt")
        self.groupBox_9 = QtWidgets.QGroupBox(self.Window_groupBox)
        self.groupBox_9.setGeometry(QtCore.QRect(1600, 680, 251, 224))
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
        self.Ace_groupBox = QtWidgets.QGroupBox(self.Window_groupBox)
        self.Ace_groupBox.setGeometry(QtCore.QRect(60, 38, 251, 224))
        self.Ace_groupBox.setTitle("")
        self.Ace_groupBox.setObjectName("Ace_groupBox")
        self.label_16 = QtWidgets.QLabel(self.Ace_groupBox)
        self.label_16.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.Ace_TLine13_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine13_butt.setEnabled(False)
        self.Ace_TLine13_butt.setGeometry(QtCore.QRect(31, 191, 46, 9))
        self.Ace_TLine13_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Ace_TLine13_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Ace_TLine13_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_TLine13_butt.setStyleSheet("#Ace_TLine13_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine13_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine13_butt.setText("")
        self.Ace_TLine13_butt.setCheckable(True)
        self.Ace_TLine13_butt.setObjectName("Ace_TLine13_butt")
        self.label_14 = QtWidgets.QLabel(self.Ace_groupBox)
        self.label_14.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_14.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.Ace_TLine7_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine7_butt.setEnabled(False)
        self.Ace_TLine7_butt.setGeometry(QtCore.QRect(218, 112, 42, 9))
        self.Ace_TLine7_butt.setStyleSheet("#Ace_TLine7_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine7_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine7_butt.setText("")
        self.Ace_TLine7_butt.setCheckable(True)
        self.Ace_TLine7_butt.setObjectName("Ace_TLine7_butt")
        self.Ace_TLine18_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine18_butt.setEnabled(False)
        self.Ace_TLine18_butt.setGeometry(QtCore.QRect(31, 23, 89, 9))
        self.Ace_TLine18_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Ace_TLine18_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Ace_TLine18_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_TLine18_butt.setStyleSheet("#Ace_TLine18_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine18_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine18_butt.setText("")
        self.Ace_TLine18_butt.setCheckable(True)
        self.Ace_TLine18_butt.setObjectName("Ace_TLine18_butt")
        self.Ace_Rel5_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_Rel5_butt.setGeometry(QtCore.QRect(10, 67, 31, 31))
        self.Ace_Rel5_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Ace_Rel5_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Ace_Rel5_butt.setStyleSheet("#Ace_Rel5_butt{\n"
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
"#Ace_Rel5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_Rel5_butt.setText("")
        self.Ace_Rel5_butt.setCheckable(True)
        self.Ace_Rel5_butt.setObjectName("Ace_Rel5_butt")
        self.Ace_TLine10_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine10_butt.setEnabled(False)
        self.Ace_TLine10_butt.setGeometry(QtCore.QRect(129, 191, 89, 9))
        self.Ace_TLine10_butt.setMinimumSize(QtCore.QSize(26, 4))
        self.Ace_TLine10_butt.setMaximumSize(QtCore.QSize(300, 40))
        self.Ace_TLine10_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_TLine10_butt.setStyleSheet("#Ace_TLine10_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine10_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine10_butt.setText("")
        self.Ace_TLine10_butt.setCheckable(True)
        self.Ace_TLine10_butt.setObjectName("Ace_TLine10_butt")
        self.Ace_TLine4_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine4_butt.setEnabled(False)
        self.Ace_TLine4_butt.setGeometry(QtCore.QRect(129, 23, 16, 9))
        self.Ace_TLine4_butt.setMinimumSize(QtCore.QSize(15, 4))
        self.Ace_TLine4_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Ace_TLine4_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_TLine4_butt.setStyleSheet("#Ace_TLine4_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine4_butt.setText("")
        self.Ace_TLine4_butt.setCheckable(True)
        self.Ace_TLine4_butt.setObjectName("Ace_TLine4_butt")
        self.Ace_TLine3_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine3_butt.setEnabled(False)
        self.Ace_TLine3_butt.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.Ace_TLine3_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Ace_TLine3_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Ace_TLine3_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_TLine3_butt.setStyleSheet("#Ace_TLine3_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine3_butt.setText("")
        self.Ace_TLine3_butt.setCheckable(True)
        self.Ace_TLine3_butt.setObjectName("Ace_TLine3_butt")
        self.Ace_Rel3_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_Rel3_butt.setGeometry(QtCore.QRect(205, 135, 31, 31))
        self.Ace_Rel3_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Ace_Rel3_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Ace_Rel3_butt.setStyleSheet("#Ace_Rel3_butt{\n"
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
"#Ace_Rel3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_Rel3_butt.setText("")
        self.Ace_Rel3_butt.setCheckable(True)
        self.Ace_Rel3_butt.setObjectName("Ace_Rel3_butt")
        self.Ace_TLine14_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine14_butt.setEnabled(False)
        self.Ace_TLine14_butt.setGeometry(QtCore.QRect(22, 120, 9, 80))
        self.Ace_TLine14_butt.setStyleSheet("#Ace_TLine14_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine14_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine14_butt.setText("")
        self.Ace_TLine14_butt.setCheckable(True)
        self.Ace_TLine14_butt.setObjectName("Ace_TLine14_butt")
        self.Ace_TLine8_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine8_butt.setEnabled(False)
        self.Ace_TLine8_butt.setGeometry(QtCore.QRect(218, 121, 9, 15))
        self.Ace_TLine8_butt.setStyleSheet("#Ace_TLine8_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine8_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine8_butt.setText("")
        self.Ace_TLine8_butt.setCheckable(True)
        self.Ace_TLine8_butt.setObjectName("Ace_TLine8_butt")
        self.Ace_Rel4_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_Rel4_butt.setGeometry(QtCore.QRect(76, 180, 31, 31))
        self.Ace_Rel4_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Ace_Rel4_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Ace_Rel4_butt.setStyleSheet("#Ace_Rel4_butt{\n"
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
"#Ace_Rel4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_Rel4_butt.setText("")
        self.Ace_Rel4_butt.setCheckable(True)
        self.Ace_Rel4_butt.setObjectName("Ace_Rel4_butt")
        self.Ace_TLine15_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine15_butt.setEnabled(False)
        self.Ace_TLine15_butt.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.Ace_TLine15_butt.setStyleSheet("#Ace_TLine15_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine15_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine15_butt.setText("")
        self.Ace_TLine15_butt.setCheckable(True)
        self.Ace_TLine15_butt.setObjectName("Ace_TLine15_butt")
        self.Ace_TLine11_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine11_butt.setEnabled(False)
        self.Ace_TLine11_butt.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.Ace_TLine11_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Ace_TLine11_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Ace_TLine11_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_TLine11_butt.setStyleSheet("#Ace_TLine11_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine11_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine11_butt.setText("")
        self.Ace_TLine11_butt.setCheckable(True)
        self.Ace_TLine11_butt.setObjectName("Ace_TLine11_butt")
        self.Ace_Rel2_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_Rel2_butt.setGeometry(QtCore.QRect(143, 12, 31, 31))
        self.Ace_Rel2_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Ace_Rel2_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Ace_Rel2_butt.setStyleSheet("#Ace_Rel2_butt{\n"
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
"#Ace_Rel2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_Rel2_butt.setText("")
        self.Ace_Rel2_butt.setCheckable(True)
        self.Ace_Rel2_butt.setObjectName("Ace_Rel2_butt")
        self.Ace_TLine6_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine6_butt.setEnabled(False)
        self.Ace_TLine6_butt.setGeometry(QtCore.QRect(218, 32, 9, 80))
        self.Ace_TLine6_butt.setStyleSheet("#Ace_TLine6_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine6_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine6_butt.setText("")
        self.Ace_TLine6_butt.setCheckable(True)
        self.Ace_TLine6_butt.setObjectName("Ace_TLine6_butt")
        self.Ace_TLine9_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine9_butt.setEnabled(False)
        self.Ace_TLine9_butt.setGeometry(QtCore.QRect(218, 165, 9, 35))
        self.Ace_TLine9_butt.setStyleSheet("#Ace_TLine9_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine9_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine9_butt.setText("")
        self.Ace_TLine9_butt.setCheckable(True)
        self.Ace_TLine9_butt.setObjectName("Ace_TLine9_butt")
        self.Ace_TLine17_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine17_butt.setEnabled(False)
        self.Ace_TLine17_butt.setGeometry(QtCore.QRect(22, 23, 9, 45))
        self.Ace_TLine17_butt.setStyleSheet("#Ace_TLine17_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine17_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine17_butt.setText("")
        self.Ace_TLine17_butt.setCheckable(True)
        self.Ace_TLine17_butt.setObjectName("Ace_TLine17_butt")
        self.Ace_TLine12_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine12_butt.setEnabled(False)
        self.Ace_TLine12_butt.setGeometry(QtCore.QRect(106, 191, 14, 9))
        self.Ace_TLine12_butt.setMinimumSize(QtCore.QSize(13, 4))
        self.Ace_TLine12_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Ace_TLine12_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_TLine12_butt.setStyleSheet("#Ace_TLine12_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine12_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine12_butt.setText("")
        self.Ace_TLine12_butt.setCheckable(True)
        self.Ace_TLine12_butt.setObjectName("Ace_TLine12_butt")
        self.Ace_TLine5_butt = QtWidgets.QPushButton(self.Ace_groupBox)
        self.Ace_TLine5_butt.setEnabled(False)
        self.Ace_TLine5_butt.setGeometry(QtCore.QRect(173, 23, 54, 9))
        self.Ace_TLine5_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Ace_TLine5_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Ace_TLine5_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ace_TLine5_butt.setStyleSheet("#Ace_TLine5_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Ace_TLine5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Ace_TLine5_butt.setText("")
        self.Ace_TLine5_butt.setCheckable(True)
        self.Ace_TLine5_butt.setObjectName("Ace_TLine5_butt")
        self.Deuce_TLine2_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Deuce_TLine2_butt.setEnabled(False)
        self.Deuce_TLine2_butt.setGeometry(QtCore.QRect(1720, 30, 85, 9))
        self.Deuce_TLine2_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Deuce_TLine2_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Deuce_TLine2_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Deuce_TLine2_butt.setStyleSheet("#Deuce_TLine2_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Deuce_TLine2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Deuce_TLine2_butt.setText("")
        self.Deuce_TLine2_butt.setCheckable(True)
        self.Deuce_TLine2_butt.setObjectName("Deuce_TLine2_butt")
        self.King_TLine2_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.King_TLine2_butt.setEnabled(False)
        self.King_TLine2_butt.setGeometry(QtCore.QRect(104, 900, 85, 9))
        self.King_TLine2_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.King_TLine2_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.King_TLine2_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine2_butt.setStyleSheet("#King_TLine2_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine2_butt.setText("")
        self.King_TLine2_butt.setCheckable(True)
        self.King_TLine2_butt.setObjectName("King_TLine2_butt")
        self.King_TLine1_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.King_TLine1_butt.setEnabled(False)
        self.King_TLine1_butt.setGeometry(QtCore.QRect(60, 900, 15, 9))
        self.King_TLine1_butt.setMinimumSize(QtCore.QSize(15, 4))
        self.King_TLine1_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.King_TLine1_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.King_TLine1_butt.setStyleSheet("#King_TLine1_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#King_TLine1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_TLine1_butt.setText("")
        self.King_TLine1_butt.setCheckable(True)
        self.King_TLine1_butt.setObjectName("King_TLine1_butt")
        self.King_LoadBulbButton = QtWidgets.QPushButton(self.Window_groupBox)
        self.King_LoadBulbButton.setEnabled(False)
        self.King_LoadBulbButton.setGeometry(QtCore.QRect(8, 870, 53, 53))
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
        self.King_Rel1_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.King_Rel1_butt.setGeometry(QtCore.QRect(74, 890, 31, 31))
        self.King_Rel1_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.King_Rel1_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.King_Rel1_butt.setStyleSheet("#King_Rel1_butt{\n"
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
"#King_Rel1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.King_Rel1_butt.setText("")
        self.King_Rel1_butt.setCheckable(True)
        self.King_Rel1_butt.setObjectName("King_Rel1_butt")
        self.Queen_TLine1_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Queen_TLine1_butt.setEnabled(False)
        self.Queen_TLine1_butt.setGeometry(QtCore.QRect(1831, 900, 20, 9))
        self.Queen_TLine1_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Queen_TLine1_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Queen_TLine1_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine1_butt.setStyleSheet("#Queen_TLine1_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine1_butt.setText("")
        self.Queen_TLine1_butt.setCheckable(True)
        self.Queen_TLine1_butt.setObjectName("Queen_TLine1_butt")
        self.Queen_Rel1_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Queen_Rel1_butt.setGeometry(QtCore.QRect(1801, 890, 31, 31))
        self.Queen_Rel1_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Queen_Rel1_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Queen_Rel1_butt.setStyleSheet("#Queen_Rel1_butt{\n"
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
"#Queen_Rel1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_Rel1_butt.setText("")
        self.Queen_Rel1_butt.setCheckable(True)
        self.Queen_Rel1_butt.setObjectName("Queen_Rel1_butt")
        self.Queen_LoadBulbButton = QtWidgets.QPushButton(self.Window_groupBox)
        self.Queen_LoadBulbButton.setEnabled(False)
        self.Queen_LoadBulbButton.setGeometry(QtCore.QRect(1850, 870, 53, 53))
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
        self.Queen_TLine2_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Queen_TLine2_butt.setEnabled(False)
        self.Queen_TLine2_butt.setGeometry(QtCore.QRect(1720, 900, 85, 9))
        self.Queen_TLine2_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Queen_TLine2_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Queen_TLine2_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Queen_TLine2_butt.setStyleSheet("#Queen_TLine2_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Queen_TLine2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Queen_TLine2_butt.setText("")
        self.Queen_TLine2_butt.setCheckable(True)
        self.Queen_TLine2_butt.setObjectName("Queen_TLine2_butt")
        self.Poker_to_King_TLine_butt2 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_to_King_TLine_butt2.setEnabled(False)
        self.Poker_to_King_TLine_butt2.setGeometry(QtCore.QRect(540, 583, 9, 89))
        self.Poker_to_King_TLine_butt2.setMinimumSize(QtCore.QSize(1, 1))
        self.Poker_to_King_TLine_butt2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Poker_to_King_TLine_butt2.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_to_King_TLine_butt2.setStyleSheet("#Poker_to_King_TLine_butt2{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_to_King_TLine_butt2:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_to_King_TLine_butt2.setText("")
        self.Poker_to_King_TLine_butt2.setCheckable(True)
        self.Poker_to_King_TLine_butt2.setObjectName("Poker_to_King_TLine_butt2")
        self.Joker_groupBox = QtWidgets.QGroupBox(self.Window_groupBox)
        self.Joker_groupBox.setGeometry(QtCore.QRect(1238, 359, 251, 224))
        self.Joker_groupBox.setStyleSheet("")
        self.Joker_groupBox.setTitle("")
        self.Joker_groupBox.setObjectName("Joker_groupBox")
        self.label_42 = QtWidgets.QLabel(self.Joker_groupBox)
        self.label_42.setGeometry(QtCore.QRect(100, 35, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.Joker_TLine7_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine7_butt.setEnabled(False)
        self.Joker_TLine7_butt.setGeometry(QtCore.QRect(172, 191, 46, 9))
        self.Joker_TLine7_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Joker_TLine7_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Joker_TLine7_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_TLine7_butt.setStyleSheet("#Joker_TLine7_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine7_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine7_butt.setText("")
        self.Joker_TLine7_butt.setCheckable(True)
        self.Joker_TLine7_butt.setObjectName("Joker_TLine7_butt")
        self.label_43 = QtWidgets.QLabel(self.Joker_groupBox)
        self.label_43.setGeometry(QtCore.QRect(44, 56, 158, 111))
        self.label_43.setStyleSheet("border-image: url(:/img/powSub.jpg);")
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.Joker_TLine5_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine5_butt.setEnabled(False)
        self.Joker_TLine5_butt.setGeometry(QtCore.QRect(218, 112, 32, 9))
        self.Joker_TLine5_butt.setStyleSheet("#Joker_TLine5_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine5_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine5_butt.setText("")
        self.Joker_TLine5_butt.setCheckable(True)
        self.Joker_TLine5_butt.setObjectName("Joker_TLine5_butt")
        self.Joker_TLine2_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine2_butt.setEnabled(False)
        self.Joker_TLine2_butt.setGeometry(QtCore.QRect(128, 23, 99, 9))
        self.Joker_TLine2_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Joker_TLine2_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Joker_TLine2_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_TLine2_butt.setStyleSheet("#Joker_TLine2_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine2_butt.setText("")
        self.Joker_TLine2_butt.setCheckable(True)
        self.Joker_TLine2_butt.setObjectName("Joker_TLine2_butt")
        self.Joker_Rel3_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_Rel3_butt.setGeometry(QtCore.QRect(10, 131, 31, 31))
        self.Joker_Rel3_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Joker_Rel3_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Joker_Rel3_butt.setStyleSheet("#Joker_Rel3_butt{\n"
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
"#Joker_Rel3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_Rel3_butt.setText("")
        self.Joker_Rel3_butt.setCheckable(True)
        self.Joker_Rel3_butt.setObjectName("Joker_Rel3_butt")
        self.Joker_TLine10_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine10_butt.setEnabled(False)
        self.Joker_TLine10_butt.setGeometry(QtCore.QRect(31, 191, 89, 9))
        self.Joker_TLine10_butt.setMinimumSize(QtCore.QSize(26, 4))
        self.Joker_TLine10_butt.setMaximumSize(QtCore.QSize(300, 40))
        self.Joker_TLine10_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_TLine10_butt.setStyleSheet("#Joker_TLine10_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine10_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine10_butt.setText("")
        self.Joker_TLine10_butt.setCheckable(True)
        self.Joker_TLine10_butt.setObjectName("Joker_TLine10_butt")
        self.Joker_TLine16_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine16_butt.setEnabled(False)
        self.Joker_TLine16_butt.setGeometry(QtCore.QRect(106, 23, 15, 9))
        self.Joker_TLine16_butt.setMinimumSize(QtCore.QSize(15, 4))
        self.Joker_TLine16_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Joker_TLine16_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_TLine16_butt.setStyleSheet("#Joker_TLine16_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine16_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine16_butt.setText("")
        self.Joker_TLine16_butt.setCheckable(True)
        self.Joker_TLine16_butt.setObjectName("Joker_TLine16_butt")
        self.Joker_TLine1_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine1_butt.setEnabled(False)
        self.Joker_TLine1_butt.setGeometry(QtCore.QRect(120, -1, 9, 33))
        self.Joker_TLine1_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Joker_TLine1_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Joker_TLine1_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_TLine1_butt.setStyleSheet("#Joker_TLine1_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine1_butt.setText("")
        self.Joker_TLine1_butt.setCheckable(True)
        self.Joker_TLine1_butt.setObjectName("Joker_TLine1_butt")
        self.Joker_Rel1_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_Rel1_butt.setGeometry(QtCore.QRect(205, 67, 31, 31))
        self.Joker_Rel1_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Joker_Rel1_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Joker_Rel1_butt.setStyleSheet("#Joker_Rel1_butt{\n"
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
"#Joker_Rel1_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_Rel1_butt.setText("")
        self.Joker_Rel1_butt.setCheckable(True)
        self.Joker_Rel1_butt.setObjectName("Joker_Rel1_butt")
        self.Joker_TLine14_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine14_butt.setEnabled(False)
        self.Joker_TLine14_butt.setGeometry(QtCore.QRect(22, 31, 9, 81))
        self.Joker_TLine14_butt.setStyleSheet("#Joker_TLine14_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine14_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine14_butt.setText("")
        self.Joker_TLine14_butt.setCheckable(True)
        self.Joker_TLine14_butt.setObjectName("Joker_TLine14_butt")
        self.Joker_TLine4_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine4_butt.setEnabled(False)
        self.Joker_TLine4_butt.setGeometry(QtCore.QRect(218, 97, 9, 15))
        self.Joker_TLine4_butt.setStyleSheet("#Joker_TLine4_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine4_butt.setText("")
        self.Joker_TLine4_butt.setCheckable(True)
        self.Joker_TLine4_butt.setObjectName("Joker_TLine4_butt")
        self.Joker_Rel2_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_Rel2_butt.setGeometry(QtCore.QRect(142, 180, 31, 31))
        self.Joker_Rel2_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Joker_Rel2_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Joker_Rel2_butt.setStyleSheet("#Joker_Rel2_butt{\n"
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
"#Joker_Rel2_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_Rel2_butt.setText("")
        self.Joker_Rel2_butt.setCheckable(True)
        self.Joker_Rel2_butt.setObjectName("Joker_Rel2_butt")
        self.Joker_TLine13_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine13_butt.setEnabled(False)
        self.Joker_TLine13_butt.setGeometry(QtCore.QRect(-2, 112, 33, 9))
        self.Joker_TLine13_butt.setStyleSheet("#Joker_TLine13_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine13_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine13_butt.setText("")
        self.Joker_TLine13_butt.setCheckable(True)
        self.Joker_TLine13_butt.setObjectName("Joker_TLine13_butt")
        self.Joker_TLine9_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine9_butt.setEnabled(False)
        self.Joker_TLine9_butt.setGeometry(QtCore.QRect(120, 191, 9, 33))
        self.Joker_TLine9_butt.setMinimumSize(QtCore.QSize(1, 1))
        self.Joker_TLine9_butt.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Joker_TLine9_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_TLine9_butt.setStyleSheet("#Joker_TLine9_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine9_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine9_butt.setText("")
        self.Joker_TLine9_butt.setCheckable(True)
        self.Joker_TLine9_butt.setObjectName("Joker_TLine9_butt")
        self.Joker_Rel4_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_Rel4_butt.setGeometry(QtCore.QRect(76, 12, 31, 31))
        self.Joker_Rel4_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Joker_Rel4_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Joker_Rel4_butt.setStyleSheet("#Joker_Rel4_butt{\n"
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
"#Joker_Rel4_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_Rel4_butt.setText("")
        self.Joker_Rel4_butt.setCheckable(True)
        self.Joker_Rel4_butt.setObjectName("Joker_Rel4_butt")
        self.Joker_TLine6_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine6_butt.setEnabled(False)
        self.Joker_TLine6_butt.setGeometry(QtCore.QRect(218, 121, 9, 79))
        self.Joker_TLine6_butt.setStyleSheet("#Joker_TLine6_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine6_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine6_butt.setText("")
        self.Joker_TLine6_butt.setCheckable(True)
        self.Joker_TLine6_butt.setObjectName("Joker_TLine6_butt")
        self.Joker_TLine3_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine3_butt.setEnabled(False)
        self.Joker_TLine3_butt.setGeometry(QtCore.QRect(218, 23, 9, 45))
        self.Joker_TLine3_butt.setStyleSheet("#Joker_TLine3_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine3_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine3_butt.setText("")
        self.Joker_TLine3_butt.setCheckable(True)
        self.Joker_TLine3_butt.setObjectName("Joker_TLine3_butt")
        self.Joker_TLine11_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine11_butt.setEnabled(False)
        self.Joker_TLine11_butt.setGeometry(QtCore.QRect(22, 161, 9, 39))
        self.Joker_TLine11_butt.setStyleSheet("#Joker_TLine11_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine11_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine11_butt.setText("")
        self.Joker_TLine11_butt.setCheckable(True)
        self.Joker_TLine11_butt.setObjectName("Joker_TLine11_butt")
        self.Joker_TLine8_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine8_butt.setEnabled(False)
        self.Joker_TLine8_butt.setGeometry(QtCore.QRect(129, 191, 14, 9))
        self.Joker_TLine8_butt.setMinimumSize(QtCore.QSize(12, 4))
        self.Joker_TLine8_butt.setMaximumSize(QtCore.QSize(100, 40))
        self.Joker_TLine8_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_TLine8_butt.setStyleSheet("#Joker_TLine8_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine8_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine8_butt.setText("")
        self.Joker_TLine8_butt.setCheckable(True)
        self.Joker_TLine8_butt.setObjectName("Joker_TLine8_butt")
        self.Joker_TLine15_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine15_butt.setEnabled(False)
        self.Joker_TLine15_butt.setGeometry(QtCore.QRect(22, 23, 55, 9))
        self.Joker_TLine15_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Joker_TLine15_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Joker_TLine15_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_TLine15_butt.setStyleSheet("#Joker_TLine15_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine15_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine15_butt.setText("")
        self.Joker_TLine15_butt.setCheckable(True)
        self.Joker_TLine15_butt.setObjectName("Joker_TLine15_butt")
        self.Joker_TLine12_butt = QtWidgets.QPushButton(self.Joker_groupBox)
        self.Joker_TLine12_butt.setEnabled(False)
        self.Joker_TLine12_butt.setGeometry(QtCore.QRect(22, 120, 9, 12))
        self.Joker_TLine12_butt.setStyleSheet("#Joker_TLine12_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_TLine12_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_TLine12_butt.setText("")
        self.Joker_TLine12_butt.setCheckable(True)
        self.Joker_TLine12_butt.setObjectName("Joker_TLine12_butt")
        self.NMSU_Logo_Label = QtWidgets.QLabel(self.Window_groupBox)
        self.NMSU_Logo_Label.setGeometry(QtCore.QRect(953, 20, 101, 111))
        self.NMSU_Logo_Label.setStyleSheet("border-image: url(:/img/NM_State_University_logo.png);")
        self.NMSU_Logo_Label.setText("")
        self.NMSU_Logo_Label.setObjectName("NMSU_Logo_Label")
        self.label_45 = QtWidgets.QLabel(self.Window_groupBox)
        self.label_45.setGeometry(QtCore.QRect(19, 60, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.Window_groupBox)
        self.label_46.setGeometry(QtCore.QRect(19, 840, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.Window_groupBox)
        self.label_47.setGeometry(QtCore.QRect(1863, 840, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.Window_groupBox)
        self.label_48.setGeometry(QtCore.QRect(1863, 60, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.Poker_TLine14_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_TLine14_butt.setEnabled(False)
        self.Poker_TLine14_butt.setGeometry(QtCore.QRect(442, 456, 9, 15))
        self.Poker_TLine14_butt.setStyleSheet("#Poker_TLine14_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_TLine14_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_TLine14_butt.setText("")
        self.Poker_TLine14_butt.setCheckable(True)
        self.Poker_TLine14_butt.setObjectName("Poker_TLine14_butt")
        self.Poker_L_or_G_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_L_or_G_butt.setEnabled(False)
        self.Poker_L_or_G_butt.setGeometry(QtCore.QRect(300, 450, 53, 53))
        self.Poker_L_or_G_butt.setStyleSheet("#Poker_L_or_G_butt{\n"
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
"#Poker_L_or_G_butt:checked{\n"
"border-color: rgb(255, 0, 0);\n"
"border-image: url(:/img/lightBulb.svg);\n"
"}")
        self.Poker_L_or_G_butt.setText("")
        self.Poker_L_or_G_butt.setCheckable(True)
        self.Poker_L_or_G_butt.setObjectName("Poker_L_or_G_butt")
        self.label_49 = QtWidgets.QLabel(self.Window_groupBox)
        self.label_49.setGeometry(QtCore.QRect(354, 502, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.Poker_L_or_G_TLine_butt2 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_L_or_G_TLine_butt2.setEnabled(False)
        self.Poker_L_or_G_TLine_butt2.setGeometry(QtCore.QRect(395, 471, 25, 9))
        self.Poker_L_or_G_TLine_butt2.setMinimumSize(QtCore.QSize(20, 4))
        self.Poker_L_or_G_TLine_butt2.setMaximumSize(QtCore.QSize(100, 20))
        self.Poker_L_or_G_TLine_butt2.setSizeIncrement(QtCore.QSize(1, 1))
        self.Poker_L_or_G_TLine_butt2.setStyleSheet("#Poker_L_or_G_TLine_butt2{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_L_or_G_TLine_butt2:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_L_or_G_TLine_butt2.setText("")
        self.Poker_L_or_G_TLine_butt2.setCheckable(True)
        self.Poker_L_or_G_TLine_butt2.setObjectName("Poker_L_or_G_TLine_butt2")
        self.Joker_L_or_G_TLine_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Joker_L_or_G_TLine_butt.setEnabled(False)
        self.Joker_L_or_G_TLine_butt.setGeometry(QtCore.QRect(1488, 471, 25, 9))
        self.Joker_L_or_G_TLine_butt.setMinimumSize(QtCore.QSize(20, 4))
        self.Joker_L_or_G_TLine_butt.setMaximumSize(QtCore.QSize(100, 20))
        self.Joker_L_or_G_TLine_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Joker_L_or_G_TLine_butt.setStyleSheet("#Joker_L_or_G_TLine_butt{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_L_or_G_TLine_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_L_or_G_TLine_butt.setText("")
        self.Joker_L_or_G_TLine_butt.setCheckable(True)
        self.Joker_L_or_G_TLine_butt.setObjectName("Joker_L_or_G_TLine_butt")
        self.Joker_L_or_G_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Joker_L_or_G_butt.setEnabled(False)
        self.Joker_L_or_G_butt.setGeometry(QtCore.QRect(1556, 450, 53, 53))
        self.Joker_L_or_G_butt.setStyleSheet("#Joker_L_or_G_butt{\n"
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
"#Joker_L_or_G_butt:checked{\n"
"border-color: rgb(255, 0, 0);\n"
"border-image: url(:/img/lightBulb.svg);\n"
"}")
        self.Joker_L_or_G_butt.setText("")
        self.Joker_L_or_G_butt.setCheckable(True)
        self.Joker_L_or_G_butt.setObjectName("Joker_L_or_G_butt")
        self.Poker_Rel_to_L_or_G_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_Rel_to_L_or_G_butt.setGeometry(QtCore.QRect(365, 460, 31, 31))
        self.Poker_Rel_to_L_or_G_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Poker_Rel_to_L_or_G_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Poker_Rel_to_L_or_G_butt.setStyleSheet("#Poker_Rel_to_L_or_G_butt{\n"
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
"#Poker_Rel_to_L_or_G_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_Rel_to_L_or_G_butt.setText("")
        self.Poker_Rel_to_L_or_G_butt.setCheckable(True)
        self.Poker_Rel_to_L_or_G_butt.setObjectName("Poker_Rel_to_L_or_G_butt")
        self.Poker_L_or_G_TLine_butt1 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Poker_L_or_G_TLine_butt1.setEnabled(False)
        self.Poker_L_or_G_TLine_butt1.setGeometry(QtCore.QRect(352, 471, 14, 9))
        self.Poker_L_or_G_TLine_butt1.setMinimumSize(QtCore.QSize(12, 9))
        self.Poker_L_or_G_TLine_butt1.setStyleSheet("#Poker_L_or_G_TLine_butt1{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Poker_L_or_G_TLine_butt1:checked{\n"
"    background-color: red;\n"
"}")
        self.Poker_L_or_G_TLine_butt1.setText("")
        self.Poker_L_or_G_TLine_butt1.setCheckable(True)
        self.Poker_L_or_G_TLine_butt1.setObjectName("Poker_L_or_G_TLine_butt1")
        self.Joker_Rel_to_L_or_G_butt = QtWidgets.QPushButton(self.Window_groupBox)
        self.Joker_Rel_to_L_or_G_butt.setGeometry(QtCore.QRect(1512, 460, 31, 31))
        self.Joker_Rel_to_L_or_G_butt.setMinimumSize(QtCore.QSize(31, 31))
        self.Joker_Rel_to_L_or_G_butt.setMaximumSize(QtCore.QSize(31, 31))
        self.Joker_Rel_to_L_or_G_butt.setStyleSheet("#Joker_Rel_to_L_or_G_butt{\n"
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
"#Joker_Rel_to_L_or_G_butt:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_Rel_to_L_or_G_butt.setText("")
        self.Joker_Rel_to_L_or_G_butt.setCheckable(True)
        self.Joker_Rel_to_L_or_G_butt.setObjectName("Joker_Rel_to_L_or_G_butt")
        self.Joker_L_or_G_TLine_butt1 = QtWidgets.QPushButton(self.Window_groupBox)
        self.Joker_L_or_G_TLine_butt1.setEnabled(False)
        self.Joker_L_or_G_TLine_butt1.setGeometry(QtCore.QRect(1542, 471, 15, 9))
        self.Joker_L_or_G_TLine_butt1.setMinimumSize(QtCore.QSize(15, 9))
        self.Joker_L_or_G_TLine_butt1.setStyleSheet("#Joker_L_or_G_TLine_butt1{\n"
"background-color: green;\n"
"border-style: outset;\n"
"}\n"
"#Joker_L_or_G_TLine_butt1:checked{\n"
"    background-color: red;\n"
"}")
        self.Joker_L_or_G_TLine_butt1.setText("")
        self.Joker_L_or_G_TLine_butt1.setCheckable(True)
        self.Joker_L_or_G_TLine_butt1.setObjectName("Joker_L_or_G_TLine_butt1")
        self.King_groupBox.raise_()
        self.Joker_groupBox.raise_()
        self.groupBox_9.raise_()
        self.groupBox.raise_()
        self.Poker_groupBox.raise_()
        self.Ace_groupBox.raise_()
        self.Joker_to_Queen_TLine_butt1.raise_()
        self.Ace_L_or_G_butt.raise_()
        self.Ace_to_Deuce_TLine_butt.raise_()
        self.Queen_groupBox.raise_()
        self.layoutWidget_6.raise_()
        self.Poker_to_PV_Rel_butt.raise_()
        self.Ace_TLine1_butt.raise_()
        self.Ace_to_Poker_TLine_butt1.raise_()
        self.Poker_to_PV_TLine_butt2.raise_()
        self.Ace_to_Poker_TLine_butt2.raise_()
        self.layoutWidget_5.raise_()
        self.Deuce_to_Queen_TLine_butt.raise_()
        self.layoutWidget_2.raise_()
        self.Poker_to_King_TLine_butt1.raise_()
        self.layoutWidget.raise_()
        self.Queen_to_King_TLine_butt.raise_()
        self.Deuce_groupBox.raise_()
        self.Deuce_to_Joker_TLine_butt2.raise_()
        self.layoutWidget_4.raise_()
        self.Joker_to_Queen_TLine_butt2.raise_()
        self.layoutWidget_3.raise_()
        self.Poker_to_PV_TLine_butt3.raise_()
        self.Ace_Rel1_butt.raise_()
        self.Poker_to_PV_TLine_butt1.raise_()
        self.King_to_Ace_TLine_butt.raise_()
        self.layoutWidget.raise_()
        self.Deuce_LoadBulbButton.raise_()
        self.Ace_TLine2_butt.raise_()
        self.Ace_TLine16_butt.raise_()
        self.Deuce_TLine2_butt.raise_()
        self.King_TLine2_butt.raise_()
        self.King_TLine1_butt.raise_()
        self.King_LoadBulbButton.raise_()
        self.King_Rel1_butt.raise_()
        self.Queen_TLine1_butt.raise_()
        self.Queen_LoadBulbButton.raise_()
        self.Queen_TLine2_butt.raise_()
        self.Deuce_Rel1_butt.raise_()
        self.Deuce_TLine1_butt.raise_()
        self.Poker_to_King_TLine_butt2.raise_()
        self.Deuce_to_Joker_TLine_butt1.raise_()
        self.Queen_Rel1_butt.raise_()
        self.NMSU_Logo_Label.raise_()
        self.label_45.raise_()
        self.label_46.raise_()
        self.label_47.raise_()
        self.label_48.raise_()
        self.Poker_TLine14_butt.raise_()
        self.Poker_L_or_G_butt.raise_()
        self.label_49.raise_()
        self.Poker_L_or_G_TLine_butt2.raise_()
        self.Joker_L_or_G_TLine_butt.raise_()
        self.Joker_L_or_G_butt.raise_()
        self.Poker_Rel_to_L_or_G_butt.raise_()
        self.Poker_L_or_G_TLine_butt1.raise_()
        self.Joker_Rel_to_L_or_G_butt.raise_()
        self.Joker_L_or_G_TLine_butt1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1909, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuPresets = QtWidgets.QMenu(self.menuEdit)
        self.menuPresets.setObjectName("menuPresets")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDemo = QtWidgets.QAction(MainWindow)
        self.actionDemo.setObjectName("actionDemo")
        self.actionPreset1 = QtWidgets.QAction(MainWindow)
        self.actionPreset1.setObjectName("actionPreset1")
        self.actionPreset_2 = QtWidgets.QAction(MainWindow)
        self.actionPreset_2.setObjectName("actionPreset_2")
        self.menuPresets.addAction(self.actionDemo)
        self.menuPresets.addAction(self.actionPreset1)
        self.menuPresets.addAction(self.actionPreset_2)
        self.menuEdit.addAction(self.menuPresets.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_22.setText(_translate("MainWindow", "Queen"))
        self.PV_Va_label.setText(_translate("MainWindow", " V ="))
        self.PV_Ia_label.setText(_translate("MainWindow", "  I ="))
        self.PV_live_Va_label.setText(_translate("MainWindow", " 000.0 "))
        self.PV_live_Ia_label.setText(_translate("MainWindow", " 00.00 "))
        self.PV_expand_butt.setText(_translate("MainWindow", "Expand"))
        self.Joker_Va_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">V</span><span style=\" font-weight:600; vertical-align:sub;\">A</span><span style=\" font-weight:600;\"> =</span></p></body></html>"))
        self.Joker_Ia_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">  I</span><span style=\" font-weight:600; vertical-align:sub;\">A</span><span style=\" font-weight:600;\"> =</span></p></body></html>"))
        self.Joker_live_Va_label.setText(_translate("MainWindow", " 000.0 "))
        self.Joker_live_Ia_label.setText(_translate("MainWindow", " 00.00 "))
        self.Joker_expand_butt.setText(_translate("MainWindow", "Expand"))
        self.Poker_Va_label.setText(_translate("MainWindow", "<html><head/><body><p> V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Poker_Ia_label.setText(_translate("MainWindow", "<html><head/><body><p>  I<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Poker_live_Va_label.setText(_translate("MainWindow", " 000.0 "))
        self.Poker_live_Ia_label.setText(_translate("MainWindow", " 00.00 "))
        self.Poker_expand_butt.setText(_translate("MainWindow", "Expand"))
        self.Ace_Va_label.setText(_translate("MainWindow", "<html><head/><body><p> V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Ace_Ia_label.setText(_translate("MainWindow", "<html><head/><body><p> I<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Ace_live_Va_label.setText(_translate("MainWindow", " 000.0 "))
        self.Ace_live_Ia_label.setText(_translate("MainWindow", " 00.00 "))
        self.Ace_expand_butt.setText(_translate("MainWindow", "Expand"))
        self.label_20.setText(_translate("MainWindow", "Deuce"))
        self.Deuce_Va_label.setText(_translate("MainWindow", "<html><head/><body><p> V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Deuce_Ia_label.setText(_translate("MainWindow", "<html><head/><body><p>  I<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Deuce_live_Va_label.setText(_translate("MainWindow", " 000.0 "))
        self.Deuce_live_Ia_label.setText(_translate("MainWindow", " 00.00 "))
        self.Deuce_expand_butt.setText(_translate("MainWindow", "Expand"))
        self.Queen_Va_label.setText(_translate("MainWindow", "<html><head/><body><p> V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Queen_Ia_label.setText(_translate("MainWindow", "<html><head/><body><p>  I<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Queen_live_Va_label.setText(_translate("MainWindow", " 000.0 "))
        self.Queen_live_Ia_label.setText(_translate("MainWindow", " 00.00 "))
        self.Queen_expand_butt.setText(_translate("MainWindow", "Expand"))
        self.label_18.setText(_translate("MainWindow", "Poker"))
        self.label_17.setText(_translate("MainWindow", "King"))
        self.King_Va_label.setText(_translate("MainWindow", "<html><head/><body><p> V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.King_Ia_label.setText(_translate("MainWindow", "<html><head/><body><p>  I<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.King_live_Va_label.setText(_translate("MainWindow", " 000.0 "))
        self.King_live_Ia_label.setText(_translate("MainWindow", " 00.00 "))
        self.King_expand_butt.setText(_translate("MainWindow", "Expand"))
        self.label_37.setText(_translate("MainWindow", "Joker"))
        self.label_16.setText(_translate("MainWindow", "Ace"))
        self.label_42.setText(_translate("MainWindow", "Joker"))
        self.label_45.setText(_translate("MainWindow", "G/L"))
        self.label_46.setText(_translate("MainWindow", "G/L"))
        self.label_47.setText(_translate("MainWindow", "G/L"))
        self.label_48.setText(_translate("MainWindow", "G/L"))
        self.label_49.setText(_translate("MainWindow", "G/L"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuPresets.setTitle(_translate("MainWindow", "Presets"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionDemo.setText(_translate("MainWindow", "Demo"))
        self.actionPreset1.setText(_translate("MainWindow", "Preset 1"))
        self.actionPreset_2.setText(_translate("MainWindow", "Preset 2"))

import resources_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.showMaximized()
    sys.exit(app.exec_())

