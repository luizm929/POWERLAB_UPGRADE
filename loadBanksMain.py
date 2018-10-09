#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------
#
# Written by Luis Martinez : luizmartines@gmail.com
#                          : luizm929@nmsu.edu
#------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from learn import *
device_ip = ('192.168.1.3', 2000)
name = 'LoadBox001'
from commj import *

class Ui_LoadBanksWindow(object):
    def __init__(self):
        super(Ui_LoadBanksWindow, self).__init__()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1388, 899)
        MainWindow.setFixedSize(1388, 899)
        #self.MainWindow.setFixedSize(self.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1350, 751))
        self.tabWidget.setMaximumSize(QtCore.QSize(1350, 1200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")


        self.Resistive = QtWidgets.QWidget()
        self.Resistive.setObjectName("Resistive")
        self.resistiveBackLabel = QtWidgets.QLabel(self.Resistive)
        self.resistiveBackLabel.setGeometry(QtCore.QRect(0, 0, 1351, 721))

        # A QLabel does not display images unless we make a QPixmap object of the image
        resistive_pix = QPixmap('img/Resistive.png')
        self.resistiveBackLabel.setScaledContents(True)
        self.resistiveBackLabel.setPixmap(resistive_pix)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.resistiveBackLabel.setSizePolicy(sizePolicy)
        # ------------------------------------------------------------------------

        self.resistiveBackLabel.setText("")
        self.resistiveBackLabel.setObjectName("resistiveBackLabel")
        self.btnR1 = QtWidgets.QPushButton(self.Resistive)
        # if we want to disable the button btnR1 we change next line to False
        self.btnR1.setEnabled(True)
        self.btnR1.setGeometry(QtCore.QRect(140, 290, 65, 65))
        self.btnR1.setMaximumSize(QtCore.QSize(65, 65))
        # self.btnR1.setAutoFillBackground(False)
        self.btnR1.setObjectName("btnR1")

        self.btnR1.setStyleSheet("#btnR1 {background-color: red;\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;\n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnR1:checked{\n"
                                 "    background-color: green;\n"
                                 "}")

        self.btnR1.setText("")
        self.btnR1.setCheckable(True)
        self.btnR1.setChecked(False)
        # ---------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR1.clicked.connect(self.btn_r1)
        #----------------------------------------

        self.btnR2 = QtWidgets.QPushButton(self.Resistive)
        # enable this button
        self.btnR2.setEnabled(True)
        self.btnR2.setGeometry(QtCore.QRect(240, 290, 65, 65))
        self.btnR2.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR2.setAutoFillBackground(False)
        self.btnR2.setStyleSheet("#btnR2 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnR2:checked\n"
                                 "{\n"
                                 "    background-color: green;\n"
                                 "}")
        self.btnR2.setText("")
        self.btnR2.setCheckable(True)

        #-------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR2.clicked.connect(self.btn_r2)
        #-------------------------------------------------------------

        self.btnR2.setAutoDefault(False)
        self.btnR2.setObjectName("btnR2")
        self.btnR3 = QtWidgets.QPushButton(self.Resistive)
        # enable buton R3
        self.btnR3.setEnabled(True)
        self.btnR3.setGeometry(QtCore.QRect(350, 290, 65, 65))
        self.btnR3.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR3.setAutoFillBackground(False)
        self.btnR3.setStyleSheet("#btnR3 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnR3:checked\n"
                                 "{\n"
                                 "    background-color: green;\n"
                                 "}")
        self.btnR3.setText("")
        self.btnR3.setCheckable(True)

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR3.clicked.connect(self.btn_r3)

        # self.btnR3.setAutoDefault(False)
        self.btnR3.setObjectName("btnR3")
        self.btnR4 = QtWidgets.QPushButton(self.Resistive)
        # enable button R4
        self.btnR4.setEnabled(True)
        self.btnR4.setGeometry(QtCore.QRect(520, 290, 65, 65))
        self.btnR4.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR4.setAutoFillBackground(False)
        self.btnR4.setStyleSheet("#btnR4 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnR4:checked\n"
                                 "{\n"
                                 "    background-color: green;\n"
                                 "}")
        self.btnR4.setText("")
        self.btnR4.setCheckable(True)

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR4.clicked.connect(self.btn_r4)

        # self.btnR4.setAutoDefault(False)
        self.btnR4.setObjectName("btnR4")
        self.btnR5 = QtWidgets.QPushButton(self.Resistive)
        self.btnR5.setEnabled(True)
        self.btnR5.setGeometry(QtCore.QRect(630, 290, 65, 65))
        self.btnR5.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR5.setAutoFillBackground(False)
        self.btnR5.setStyleSheet("#btnR5 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnR5:checked\n"
                                 "{\n"
                                 "    background-color: green;\n"
                                 "}")
        self.btnR5.setText("")
        self.btnR5.setCheckable(True)

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR5.clicked.connect(self.btn_r5)

        self.btnR5.setAutoDefault(False)
        self.btnR5.setObjectName("btnR5")
        self.btnR6 = QtWidgets.QPushButton(self.Resistive)
        # enable this button
        self.btnR6.setEnabled(True)
        self.btnR6.setGeometry(QtCore.QRect(740, 290, 65, 65))
        self.btnR6.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR6.setAutoFillBackground(False)
        self.btnR6.setStyleSheet("#btnR6 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnR6:checked\n"
                                 "{\n"
                                 "    background-color: green;\n"
                                 "}")
        self.btnR6.setText("")
        self.btnR6.setCheckable(True)

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR6.clicked.connect(self.btn_r6)

        self.btnR6.setAutoDefault(False)
        self.btnR6.setObjectName("btnR6")
        self.btnR7 = QtWidgets.QPushButton(self.Resistive)
        # enable this button
        self.btnR7.setEnabled(True)
        self.btnR7.setGeometry(QtCore.QRect(920, 290, 65, 65))
        self.btnR7.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR7.setAutoFillBackground(False)
        self.btnR7.setStyleSheet("#btnR7 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnR7:checked\n"
                                 "{\n"
                                 "    background-color: green;\n"
                                 "}")
        self.btnR7.setText("")
        self.btnR7.setCheckable(True)

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR7.clicked.connect(self.btn_r7)

        self.btnR7.setAutoDefault(False)
        self.btnR7.setObjectName("btnR7")
        self.btnR8 = QtWidgets.QPushButton(self.Resistive)
        # enable this button
        self.btnR8.setEnabled(True)
        self.btnR8.setGeometry(QtCore.QRect(1030, 290, 65, 65))
        self.btnR8.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR8.setAutoFillBackground(False)
        self.btnR8.setStyleSheet("#btnR8 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnR8:checked\n"
                                 "{\n"
                                 "    background-color: green;\n"
                                 "}")
        self.btnR8.setText("")
        self.btnR8.setCheckable(True)

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR8.clicked.connect(self.btn_r8)

        self.btnR8.setAutoDefault(False)
        self.btnR8.setObjectName("btnR8")

        #--------Button R9 Resistive load-----------------------------------------------------------------------------
        self.btnR9 = QtWidgets.QPushButton(self.Resistive)
        # enable this button. This could be used to disable buttons if user does not have permission.
        self.btnR9.setEnabled(True)
        self.btnR9.setGeometry(QtCore.QRect(1140, 290, 65, 65))
        self.btnR9.setMaximumSize(QtCore.QSize(65, 65))
        self.btnR9.setAutoFillBackground(False)
        self.btnR9.setStyleSheet("#btnR9 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                     "text-align:center;\n"
                                 "}\n"
                                 "#btnR9:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnR9.setText("")
        self.btnR9.setCheckable(True)

        #-------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR9.clicked.connect(self.btn_r9)
        #-------------------------------------------------------------

        self.btnR9.setAutoDefault(False)
        self.btnR9.setObjectName("btnR9")
        
        #----------------------Button R9 ends------------------------------
        
        self.btnAllOff_R = QtWidgets.QPushButton(self.Resistive)
        self.btnAllOff_R.setEnabled(True)
        self.btnAllOff_R.setGeometry(QtCore.QRect(130, 10, 80, 80))
        self.btnAllOff_R.setMaximumSize(QtCore.QSize(80, 80))
        self.btnAllOff_R.setAutoFillBackground(False)
        self.btnAllOff_R.setStyleSheet("QPushButton#btnAllOff_R {\n"
                                       "border-image: url(:/img/Power_off_icon.png);\n"
                                       "background-color: red;\n"
                                       "border-radius:30px;\n"
                                       "max-width:60px;\n"
                                       "max-height:60px;\n"
                                       "min-width:60px;\n"
                                       "min-height:60px;\n"
                                       "border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "padding: 3px;\n"
                                       "border-color: beige;    \n"
                                       "font-size:16px;\n"
                                       "font-weight:300;\n"
                                       "color: white;\n"
                                       "text-align:center;\n"
                                       "}\n"
                                       "QPushButton#btnAllOff_R:pressed\n"
                                       "{\n"
                                       "    background-color: #F1948A ;\n"
                                       "}")


        self.btnAllOff_R.setCheckable(True)

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOff_R.clicked.connect(self.all_off_res)

        self.btnAllOff_R.setAutoDefault(False)
        self.btnAllOff_R.setObjectName("btnAllOff_R")
        self.btnAllOn_R = QtWidgets.QPushButton(self.Resistive)
        self.btnAllOn_R.setEnabled(True)
        self.btnAllOn_R.setGeometry(QtCore.QRect(40, 10, 80, 80))
        self.btnAllOn_R.setMaximumSize(QtCore.QSize(80, 80))
        self.btnAllOn_R.setAutoFillBackground(False)
        self.btnAllOn_R.setStyleSheet("QPushButton#btnAllOn_R {\n"
                                      "border-image: url(:/img/Power_off_icon.png);\n"
                                      "background-color: green;\n"
                                      "border-radius:30px;\n"
                                      "max-width:60px;\n"
                                      "max-height:60px;\n"
                                      "min-width:60px;\n"
                                      "min-height:60px;\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "padding: 3px;\n"
                                      "border-color: beige;    \n"
                                      "font-size:16px;\n"
                                      "font-weight:300;\n"
                                      "color: white;\n"
                                      "text-align:center;\n"
                                      "}\n"
                                      "QPushButton#btnAllOn_R:pressed\n"
                                      "{\n"
                                      "\n"
                                      "    background-color: #28B463;\n"
                                      "}")
        self.btnAllOn_R.setCheckable(True)

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOn_R.clicked.connect(self.all_on_res)


        self.btnAllOn_R.setAutoDefault(False)
        self.btnAllOn_R.setObjectName("btnAllOn_R")
        self.tabWidget.addTab(self.Resistive, "")

        #------------------- Inductive -------------------------------------------
        self.Inductive = QtWidgets.QWidget()
        self.Inductive.setObjectName("Inductive")
        self.inductiveBackLabel = QtWidgets.QLabel(self.Inductive)
        self.inductiveBackLabel.setGeometry(QtCore.QRect(0, 0, 1341, 711))

        # This fixes the image not showing up in background
        inductive_pix = QPixmap('img/Ind.png')
        self.inductiveBackLabel.setScaledContents(True)
        self.inductiveBackLabel.setPixmap(inductive_pix)
        #--------------------------------------------------
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.inductiveBackLabel.setSizePolicy(sizePolicy)
        # ------------------------------------------------------------------------

        self.inductiveBackLabel.setText("")
        self.inductiveBackLabel.setObjectName("inductiveBackLabel")

        self.btnL2 = QtWidgets.QPushButton(self.Inductive)
        self.btnL2.setEnabled(True)
        self.btnL2.setGeometry(QtCore.QRect(140, 290, 65, 65))
        self.btnL2.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL2.setAutoFillBackground(False)
        self.btnL2.setStyleSheet("#btnL2 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnL2:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnL2.setText("")
        self.btnL2.setCheckable(True)
        # -------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL2.clicked.connect(self.btn_L2)
        # -------------------------------------------------------------
        self.btnL2.setAutoDefault(False)
        self.btnL2.setObjectName("btnL2")

        #------------------------------ Button L1-------------------
        self.btnL1 = QtWidgets.QPushButton(self.Inductive)
        self.btnL1.setEnabled(True)
        self.btnL1.setGeometry(QtCore.QRect(240, 290, 65, 65))
        self.btnL1.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL1.setAutoFillBackground(False)
        self.btnL1.setStyleSheet("#btnL1 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnL1:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnL1.setText("")
        self.btnL1.setCheckable(True)
        self.btnL1.setAutoDefault(False)
        self.btnL1.setObjectName("btnL1")
        self.btnL3 = QtWidgets.QPushButton(self.Inductive)
        self.btnL3.setEnabled(True)
        self.btnL3.setGeometry(QtCore.QRect(350, 290, 65, 65))
        self.btnL3.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL3.setAutoFillBackground(False)
        self.btnL3.setStyleSheet("#btnL3 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnL3:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnL3.setText("")
        self.btnL3.setCheckable(True)
        self.btnL3.setAutoDefault(False)
        self.btnL3.setObjectName("btnL3")
        self.btnL6 = QtWidgets.QPushButton(self.Inductive)
        self.btnL6.setEnabled(True)
        self.btnL6.setGeometry(QtCore.QRect(520, 290, 65, 65))
        self.btnL6.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL6.setAutoFillBackground(False)
        self.btnL6.setStyleSheet("#btnL6 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnL6:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnL6.setText("")
        self.btnL6.setCheckable(True)
        self.btnL6.setAutoDefault(False)
        self.btnL6.setObjectName("btnL6")
        self.btnL5 = QtWidgets.QPushButton(self.Inductive)
        self.btnL5.setEnabled(True)
        self.btnL5.setGeometry(QtCore.QRect(630, 290, 65, 65))
        self.btnL5.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL5.setAutoFillBackground(False)
        self.btnL5.setStyleSheet("#btnL5 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnL5:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnL5.setText("")
        self.btnL5.setCheckable(True)
        self.btnL5.setAutoDefault(False)
        self.btnL5.setObjectName("btnL5")
        self.btnL4 = QtWidgets.QPushButton(self.Inductive)
        self.btnL4.setEnabled(True)
        self.btnL4.setGeometry(QtCore.QRect(730, 290, 65, 65))
        self.btnL4.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL4.setAutoFillBackground(False)
        self.btnL4.setStyleSheet("#btnL4 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnL4:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnL4.setText("")
        self.btnL4.setCheckable(True)
        self.btnL4.setAutoDefault(False)
        self.btnL4.setObjectName("btnL4")
        self.btnL9 = QtWidgets.QPushButton(self.Inductive)
        self.btnL9.setEnabled(True)
        self.btnL9.setGeometry(QtCore.QRect(900, 290, 65, 65))
        self.btnL9.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL9.setAutoFillBackground(False)
        self.btnL9.setStyleSheet("#btnL9 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnL9:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnL9.setText("")
        self.btnL9.setCheckable(True)
        self.btnL9.setAutoDefault(False)
        self.btnL9.setObjectName("btnL9")
        self.btnL8 = QtWidgets.QPushButton(self.Inductive)
        self.btnL8.setEnabled(True)
        self.btnL8.setGeometry(QtCore.QRect(1020, 290, 65, 65))
        self.btnL8.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL8.setAutoFillBackground(False)
        self.btnL8.setStyleSheet("#btnL8 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnL8:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnL8.setText("")
        self.btnL8.setCheckable(True)
        self.btnL8.setAutoDefault(False)
        self.btnL8.setObjectName("btnL8")
        self.btnL7 = QtWidgets.QPushButton(self.Inductive)
        self.btnL7.setEnabled(True)
        self.btnL7.setGeometry(QtCore.QRect(1130, 290, 65, 65))
        self.btnL7.setMaximumSize(QtCore.QSize(65, 65))
        self.btnL7.setAutoFillBackground(False)
        self.btnL7.setStyleSheet("#btnL7 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnL7:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnL7.setText("")
        self.btnL7.setCheckable(True)
        self.btnL7.setAutoDefault(False)
        self.btnL7.setObjectName("btnL7")
        self.btnAllOn_L = QtWidgets.QPushButton(self.Inductive)
        self.btnAllOn_L.setEnabled(True)
        self.btnAllOn_L.setGeometry(QtCore.QRect(40, 10, 80, 80))
        self.btnAllOn_L.setMaximumSize(QtCore.QSize(80, 80))
        self.btnAllOn_L.setAutoFillBackground(False)
        self.btnAllOn_L.setStyleSheet("QPushButton#btnAllOn_L {\n"
                                      "border-image: url(:/img/Power_off_icon.png);\n"
                                      "background-color: green;\n"
                                      "border-radius:30px;\n"
                                      "max-width:60px;\n"
                                      "max-height:60px;\n"
                                      "min-width:60px;\n"
                                      "min-height:60px;\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "padding: 3px;\n"
                                      "border-color: beige;    \n"
                                      "font-size:16px;\n"
                                      "font-weight:300;\n"
                                      "color: white;\n"
                                      "text-align:center;\n"
                                      "}\n"
                                      "QPushButton#btnAllOn_L:pressed\n"
                                      "{\n"
                                      "    background-color: #28B463;\n"
                                      "}")
        self.btnAllOn_L.setCheckable(True)

        #--------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOn_L.clicked.connect(self.all_on_ind)
        #--------------------------------------------------------------
        self.btnAllOn_L.setAutoDefault(False)
        self.btnAllOn_L.setObjectName("btnAllOn_L")
        self.btnAllOff_L = QtWidgets.QPushButton(self.Inductive)
        self.btnAllOff_L.setEnabled(True)
        self.btnAllOff_L.setGeometry(QtCore.QRect(130, 10, 80, 80))
        self.btnAllOff_L.setMaximumSize(QtCore.QSize(80, 80))
        self.btnAllOff_L.setAutoFillBackground(False)
        self.btnAllOff_L.setStyleSheet("QPushButton#btnAllOff_L {\n"
                                       "border-image: url(:/img/Power_off_icon.png);\n"
                                       "background-color: red;\n"
                                       "border-radius:30px;\n"
                                       "max-width:60px;\n"
                                       "max-height:60px;\n"
                                       "min-width:60px;\n"
                                       "min-height:60px;\n"
                                       "border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "padding: 3px;\n"
                                       "border-color: beige;    \n"
                                       "font-size:16px;\n"
                                       "font-weight:300;\n"
                                       "color: white;\n"
                                       "text-align:center;\n"
                                       "}\n"
                                       "QPushButton#btnAllOff_L:pressed\n"
                                       "{\n"
                                       "    background-color: #F1948A;\n"
                                       "}")
        self.btnAllOff_L.setCheckable(True)
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOff_L.clicked.connect(self.all_off_ind)

        self.btnAllOff_L.setAutoDefault(False)
        self.btnAllOff_L.setObjectName("btnAllOff_L")
        self.tabWidget.addTab(self.Inductive, "")
        self.Capacitive = QtWidgets.QWidget()
        self.Capacitive.setObjectName("Capacitive")
        self.capacitiveBackLabel = QtWidgets.QLabel(self.Capacitive)
        self.capacitiveBackLabel.setGeometry(QtCore.QRect(0, 0, 1341, 721))

        #------------- Creates QPixMap
        capacitive_pix = QPixmap('img/Cap.png')
        self.capacitiveBackLabel.setScaledContents(True)
        self.capacitiveBackLabel.setPixmap(capacitive_pix)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.capacitiveBackLabel.setSizePolicy(sizePolicy)
        # ------------------------------------------------------------------------

        self.capacitiveBackLabel.setStyleSheet("border-image: url(:/img/Cap.png);")
        self.capacitiveBackLabel.setText("")
        self.capacitiveBackLabel.setObjectName("capacitiveBackLabel")
        self.btnC9 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC9.setEnabled(True)
        self.btnC9.setGeometry(QtCore.QRect(1130, 290, 65, 65))
        self.btnC9.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC9.setAutoFillBackground(False)
        self.btnC9.setStyleSheet("#btnC9 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnC9:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnC9.setText("")
        self.btnC9.setCheckable(True)
        self.btnC9.setAutoDefault(False)
        self.btnC9.setObjectName("btnC9")
        self.btnC8 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC8.setEnabled(True)
        self.btnC8.setGeometry(QtCore.QRect(1020, 290, 65, 65))
        self.btnC8.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC8.setAutoFillBackground(False)
        self.btnC8.setStyleSheet("#btnC8 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnC8:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnC8.setText("")
        self.btnC8.setCheckable(True)
        self.btnC8.setAutoDefault(False)
        self.btnC8.setObjectName("btnC8")
        self.btnC7 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC7.setEnabled(True)
        self.btnC7.setGeometry(QtCore.QRect(910, 290, 65, 65))
        self.btnC7.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC7.setAutoFillBackground(False)
        self.btnC7.setStyleSheet("#btnC7 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnC7:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnC7.setText("")
        self.btnC7.setCheckable(True)
        self.btnC7.setAutoDefault(False)
        self.btnC7.setObjectName("btnC7")
        self.btnC6 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC6.setEnabled(True)
        self.btnC6.setGeometry(QtCore.QRect(740, 290, 65, 65))
        self.btnC6.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC6.setAutoFillBackground(False)
        self.btnC6.setStyleSheet("#btnC6 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnC6:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnC6.setText("")
        self.btnC6.setCheckable(True)
        self.btnC6.setAutoDefault(False)
        self.btnC6.setObjectName("btnC6")
        self.btnC5 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC5.setEnabled(True)
        self.btnC5.setGeometry(QtCore.QRect(630, 290, 65, 65))
        self.btnC5.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC5.setAutoFillBackground(False)
        self.btnC5.setStyleSheet("#btnC5 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnC5:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnC5.setText("")
        self.btnC5.setCheckable(True)
        self.btnC5.setAutoDefault(False)
        self.btnC5.setObjectName("btnC5")
        self.btnC4 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC4.setEnabled(True)
        self.btnC4.setGeometry(QtCore.QRect(520, 290, 65, 65))
        self.btnC4.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC4.setAutoFillBackground(False)
        self.btnC4.setStyleSheet("#btnC4 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnC4:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnC4.setText("")
        self.btnC4.setCheckable(True)
        self.btnC4.setAutoDefault(False)
        self.btnC4.setObjectName("btnC4")
        self.btnC3 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC3.setEnabled(True)
        self.btnC3.setGeometry(QtCore.QRect(350, 290, 65, 65))
        self.btnC3.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC3.setAutoFillBackground(False)
        self.btnC3.setStyleSheet("#btnC3 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnC3:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnC3.setText("")
        self.btnC3.setCheckable(True)
        self.btnC3.setAutoDefault(False)
        self.btnC3.setObjectName("btnC3")
        self.btnC2 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC2.setEnabled(True)
        self.btnC2.setGeometry(QtCore.QRect(240, 290, 65, 65))
        self.btnC2.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC2.setAutoFillBackground(False)
        self.btnC2.setStyleSheet("#btnC2 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnC2:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnC2.setText("")
        self.btnC2.setCheckable(True)
        self.btnC2.setAutoDefault(False)
        self.btnC2.setObjectName("btnC2")
        self.btnC1 = QtWidgets.QPushButton(self.Capacitive)
        self.btnC1.setEnabled(True)
        self.btnC1.setGeometry(QtCore.QRect(140, 290, 65, 65))
        self.btnC1.setMaximumSize(QtCore.QSize(65, 65))
        self.btnC1.setAutoFillBackground(False)
        self.btnC1.setStyleSheet("#btnC1 {\n"
                                 "border-image: url(:/img/Power_off_icon.png);\n"
                                 "background-color: red;\n"
                                 "border-radius:30px;\n"
                                 "max-width:60px;\n"
                                 "max-height:60px;\n"
                                 "min-width:60px;\n"
                                 "min-height:60px;\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 3px;\n"
                                 "border-color: beige;    \n"
                                 "font-size:16px;\n"
                                 "font-weight:300;\n"
                                 "color: white;\n"
                                 "text-align:center;\n"
                                 "}\n"
                                 "#btnC1:checked {\n"
                                 "background-color: green;\n"
                                 "}")
        self.btnC1.setText("")
        self.btnC1.setCheckable(True)
        self.btnC1.setAutoDefault(False)
        self.btnC1.setObjectName("btnC1")
        self.btnAllOff_C = QtWidgets.QPushButton(self.Capacitive)
        self.btnAllOff_C.setEnabled(True)
        self.btnAllOff_C.setGeometry(QtCore.QRect(130, 10, 80, 80))
        self.btnAllOff_C.setMaximumSize(QtCore.QSize(80, 80))
        self.btnAllOff_C.setAutoFillBackground(False)
        self.btnAllOff_C.setStyleSheet("QPushButton#btnAllOff_C {\n"
                                       "border-image: url(:/img/Power_off_icon.png);\n"
                                       "background-color: red;\n"
                                       "border-radius:30px;\n"
                                       "max-width:60px;\n"
                                       "max-height:60px;\n"
                                       "min-width:60px;\n"
                                       "min-height:60px;\n"
                                       "border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "padding: 3px;\n"
                                       "border-color: beige;    \n"
                                       "font-size:16px;\n"
                                       "font-weight:300;\n"
                                       "color: white;\n"
                                       "text-align:center;\n"
                                       "}\n"
                                       "QPushButton#btnAllOff_C:pressed\n"
                                       "{\n"
                                       "    background-color: #F1948A;\n"
                                       "}")
        self.btnAllOff_C.setCheckable(True)

        #-------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOff_C.clicked.connect(self.all_off_cap)
        #-------------------------------------------------------------

        self.btnAllOff_C.setAutoDefault(False)
        self.btnAllOff_C.setObjectName("btnAllOff_C")
        self.btnAllOn_C = QtWidgets.QPushButton(self.Capacitive)
        self.btnAllOn_C.setEnabled(True)
        self.btnAllOn_C.setGeometry(QtCore.QRect(40, 10, 80, 80))
        self.btnAllOn_C.setMaximumSize(QtCore.QSize(80, 80))
        self.btnAllOn_C.setAutoFillBackground(False)
        self.btnAllOn_C.setStyleSheet("QPushButton#btnAllOn_C {\n"
                                      "border-image: url(:/img/Power_off_icon.png);\n"
                                      "background-color: green;\n"
                                      "border-radius:30px;\n"
                                      "max-width:60px;\n"
                                      "max-height:60px;\n"
                                      "min-width:60px;\n"
                                      "min-height:60px;\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "padding: 3px;\n"
                                      "border-color: beige;    \n"
                                      "font-size:16px;\n"
                                      "font-weight:300;\n"
                                      "color: white;\n"
                                      "text-align:center;\n"
                                      "}\n"
                                      "QPushButton#btnAllOn_C:pressed\n"
                                      "{\n"
                                      "    background-color: #28B463;\n"
                                      "}")
        self.btnAllOn_C.setCheckable(True)

        #--------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOn_C.clicked.connect(self.all_on_cap)
        #----------------------------------------------------------------

        self.btnAllOn_C.setAutoDefault(False)
        self.btnAllOn_C.setObjectName("btnAllOn_C")
        self.tabWidget.addTab(self.Capacitive, "")
        self.ExtraControls = QtWidgets.QWidget()
        self.ExtraControls.setObjectName("ExtraControls")
        self.tabWidget.addTab(self.ExtraControls, "")
        MainWindow.setCentralWidget(self.centralwidget)

        #--------Menu bar--------------------------------
        #create the menu bar on main window
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        # set size
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1388, 26))
        # set object name
        self.menubar.setObjectName("menubar")

        # Create the first entry namely "File" and place it on menubar
        self.menuFile = QtWidgets.QMenu(self.menubar)
        # Create object name of the first entry
        self.menuFile.setObjectName("menuFile")

        #------------------------------- Pre set Labs and Demos-----------------------------
        #TODO write a function that will set all loads automatically.
        # create a sub-item in menubar called AdministratorLogin and place it on the menu bar
        self.menuLab_1 = QtWidgets.QMenu(self.menuFile)
        # create the object name
        self.menuLab_1.setObjectName("Lab 1")

        # create a sub-item in menubar called AdministratorLogin and place it on the menu bar
        self.menuLab_2 = QtWidgets.QMenu(self.menuFile)
        # create the object name
        self.menuLab_2.setObjectName("Lab 2")
        #-----------------------------------------------------------------------------------

        #-------------------------List of remote boxes to load-----------------------------
        # Create the second entry namely "LoadBoxes" and place it on menubar
        #self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLoadBoxes = QtWidgets.QMenu(self.menubar)
        # set the object name
        #self.menuLogin.setObjectName("menuLogin")
        self.menuLoadBoxes.setObjectName("menuLoadBoxes")

        # create a sub-item in menubar called AdministratorLogin and place it on the menu bar
        self.menuLoadBox001 = QtWidgets.QMenu(self.menuLoadBoxes)
        # create the object name
        self.menuLoadBox001.setObjectName("LoadBox001")

        # create a sub-item in menubar called AdministratorLogin and place it on the menu bar
        self.menuLoadBox002 = QtWidgets.QMenu(self.menuLoadBoxes)
        # create the object name
        self.menuLoadBox002.setObjectName("LoadBox002")

        # create a sub-item in menubar called AdministratorLogin and place it on the menu bar
        self.menuLoadBox003 = QtWidgets.QMenu(self.menuLoadBoxes)
        # create the object name
        self.menuLoadBox003.setObjectName("LoadBox003")

        # create a sub-item in menubar called AdministratorLogin and place it on the menu bar
        self.menuLoadBox004 = QtWidgets.QMenu(self.menuLoadBoxes)
        # create the object name
        self.menuLoadBox004.setObjectName("LoadBox004")

        # create a sub-item in menubar called AdministratorLogin and place it on the menu bar
        self.menuLoadBox005 = QtWidgets.QMenu(self.menuLoadBoxes)
        # create the object name
        self.menuLoadBox005.setObjectName("LoadBox005")

        # create a sub-item in menubar called AdministratorLogin and place it on the menu bar
        self.menuLoadBox006 = QtWidgets.QMenu(self.menuLoadBoxes)
        # create the object name
        self.menuLoadBox006.setObjectName("LoadBox006")

        #------------------------------------------------------------------------------------

        # Create the third entry namely "About" and place it on menubar
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        # set the object name
        self.menuAbout.setObjectName("menuAbout")

        # create a sub-item in menubar called Attribution and place it on the menu bar
        self.menuAttribution = QtWidgets.QMenu(self.menuAbout)
        # create the object name
        self.menuAttribution.setObjectName("menuAttribution")

        # Place menu bar on main window
        MainWindow.setMenuBar(self.menubar)
        # Create status bar to be used on the main window
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # create the object name
        self.statusbar.setObjectName("statusbar")
        # place the status bar on the main window
        MainWindow.setStatusBar(self.statusbar)

        #---------------------------------------------------------------------------------------
        # TODO attach the menu item Login so tha the action is launch the password prompt window.
        self.menuFile.addAction(self.menuLab_1.menuAction())
        self.menuFile.addAction(self.menuLab_2.menuAction())
        #self.menuLogin.addAction(self.menuAdminlogin.menuAction())
        #------- Add LoadBox001 - 006 to main LoadBOxes object---------
        self.menuLoadBoxes.addAction(self.menuLoadBox001.menuAction())
        self.menuLoadBoxes.addAction(self.menuLoadBox002.menuAction())
        self.menuLoadBoxes.addAction(self.menuLoadBox003.menuAction())
        self.menuLoadBoxes.addAction(self.menuLoadBox004.menuAction())
        self.menuLoadBoxes.addAction(self.menuLoadBox005.menuAction())
        self.menuLoadBoxes.addAction(self.menuLoadBox006.menuAction())
        #------------------------------------------------------------
        self.menuAbout.addAction(self.menuAttribution.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        #self.menubar.addAction(self.menuLogin.menuAction())
        #--------- add LoadBoxes to menubar--------------
        self.menubar.addAction(self.menuLoadBoxes.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #-------------------------------------------------------------------------------------------
    """This functions receive the signal from the load bank buttons."""

    def btn_r1(self):
        if self.btnR1.isChecked():
            command = 'Set Open 1 ACK'
            print('R1 in load bank On')
            #ON_Relay0()
        else:
            command = 'Set Close 1 ACK'

            #OFF_Relay0()
            print('R1 in load bank Off')
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count+1
            if count == 10:
                err = False
                
    def btn_r2(self):
        if self.btnR2.isChecked():
            command = 'Set Open 2 ACK'
            print('R2 in load bank is On')
            #ON_Relay1()
        else:
            command = 'Set Close 2 ACK'
            print('R2 in load bank is off')
            #OFF_Relay1()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False

    def btn_r3(self):
        # print('R3 in load bank pressed')
        if self.btnR3.isChecked():
            command = 'Set Open 3 ACK'
            print('R3 in load bank is On')
            #ON_Relay2()
        else:
            command = 'Set Close 3 ACK'
            print('R3 in load bank is off')
            #OFF_Relay2()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False

    def btn_r4(self):
        # print('R4 in load bank pressed')
        if self.btnR4.isChecked():
            command = 'Set Open 4 ACK'
            print('R3 in load bank is On')
            #ON_Relay3()
        else:
            command = 'Set Close 4 ACK'
            print('R3 in load bank is off')
            #OFF_Relay3()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False

    def btn_r5(self):
        if self.btnR5.isChecked():
            command = 'Set Open 5 ACK'
            print('R4 in load bank pressed')
            #ON_Relay4()
        else:
            command = 'Set Close 5 ACK'
            print('R4 in load bank is On')
            #OFF_Relay4()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False

    def btn_r6(self):
        if self.btnR6.isChecked():
            command = 'Set Open 6 ACK'
            print('R5 in load bank pressed')
            #ON_Relay5()
        else:
            command = 'Set Close 6 ACK'
            print('R5 in load bank is On')
            #OFF_Relay5()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False

    def btn_r7(self):
        if self.btnR7.isChecked():
            command = 'Set Open 7 ACK'
            print('R6 in load bank pressed')
            #ON_Relay6()
        else:
            command = 'Set Close 7 ACK'
            print('R6 in load bank is On')
            #OFF_Relay6()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False

    def btn_r8(self):
        if self.btnR8.isChecked():
            command = 'Set Open 8 ACK'
            #print('R7 in load bank pressed')
            #ON_Relay7()
        else:
            command = 'Set Close 8 ACK'
            #print('R7 in load bank is On')
            #OFF_Relay7()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False

    def btn_r9(self):
        if self.btnR9.isChecked():
            command = 'Set Open 9 ACK'
            print('R8 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            print('R8 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False

    def all_on_res(self):
        # if self.btnAllOn_R.isChecked():
        #   print('loads bank pressed')
        self.btnR1.setChecked(True)
        self.btnR2.setChecked(True)
        self.btnR3.setChecked(True)
        self.btnR4.setChecked(True)
        self.btnR5.setChecked(True)
        self.btnR6.setChecked(True)
        self.btnR7.setChecked(True)
        self.btnR8.setChecked(True)
        self.btnR9.setChecked(True)

        #ON_all_Relays()

    def all_off_res(self):
        # if self.btnAllOff_R.isChecked():
        #    print('in load bank pressed')
        self.btnR1.setChecked(False)
        self.btnR2.setChecked(False)
        self.btnR3.setChecked(False)
        self.btnR4.setChecked(False)
        self.btnR5.setChecked(False)
        self.btnR6.setChecked(False)
        self.btnR7.setChecked(False)
        self.btnR8.setChecked(False)
        self.btnR9.setChecked(False)

        #OFF_all_Relays()

    # Inductive loads buttons

    # TODO Add inductive and capacitive button actions.
    def btn_L1(self):
        if self.btnL1.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('L1 in load bank pressed')

    def btn_L2(self):
        if self.btnL2.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('L2 in load bank pressed')

    def btn_L3(self):
        if self.btnL3.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('L3 in load bank pressed')

    def btn_L4(self):
        if self.btnL4.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('L4 in load bank pressed')

    def btn_L5(self):
        if self.btnL5.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('L5 in load bank pressed')

    def btn_L6(self):
        if self.btnL6.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('L6 in load bank pressed')

    def btn_L7(self):
        if self.btnL7.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('L7 in load bank pressed')

    def btn_L8(self):
        if self.btnL8.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('L8 in load bank pressed')

    def btn_L9(self):
        if self.btnL9.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('L9 in load bank pressed')

    def all_on_ind(self):
        """ This function turns all buttons to ON by forcing the state of the buttons"""
        self.btnL1.setChecked(True)
        self.btnL2.setChecked(True)
        self.btnL3.setChecked(True)
        self.btnL4.setChecked(True)
        self.btnL5.setChecked(True)
        self.btnL6.setChecked(True)
        self.btnL7.setChecked(True)
        self.btnL8.setChecked(True)
        self.btnL9.setChecked(True)

        #TODO Replace this function with the function to turn ON all inductive relays.
        #ON_all_Relays()

        # comment out this line to avoid output on terminal
        #print('All inductive loads on')

    def all_off_ind(self):
        """ This function turns all buttons to OFF by forcing the state of the buttons """
        self.btnL1.setChecked(False)
        self.btnL2.setChecked(False)
        self.btnL3.setChecked(False)
        self.btnL4.setChecked(False)
        self.btnL5.setChecked(False)
        self.btnL6.setChecked(False)
        self.btnL7.setChecked(False)
        self.btnL8.setChecked(False)
        self.btnL9.setChecked(False)

        # TODO Replace this function with the function to turn ON all inductive relays.
        #OFF_all_Relays()

        # comment out this line to avoid output on terminal
        print('All inductive loads off')



    # All cap buttons


    def btn_c1(self):
        if self.btnC1.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('c1 in load bank pressed')

    def btn_c2(self):
        if self.btnC2.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('c2 in load bank pressed')

    def btn_c3(self):
        if self.btnC3.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('c3 in load bank pressed')

    def btn_c4(self):
        if self.btnC4.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('c4 in load bank pressed')

    def btn_c5(self):
        if self.btnC5.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('c5 in load bank pressed')

    def btn_c6(self):
        if self.btnC6.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('c6 in load bank pressed')

    def btn_c7(self):
        if self.btnC7.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('c7 in load bank pressed')

    def btn_c8(self):
        if self.btnC8.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('c8 in load bank pressed')

    def btn_c9(self):
        if self.btnC9.isChecked():
            command = 'Set Open 1 ACK'
            #print('L1 in load bank pressed')
            #ON_Relay8()
        else:
            command = 'Set Close 9 ACK'
            #print('L1 in load bank is On')
            #OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
            err = SetCMD(command, device_ip, name)
            count = count + 1
            if count == 10:
                err = False
        #print('c9 in load bank pressed')

    def all_on_cap(self):
        """ This function turns all buttons to ON by forcing the state of the buttons"""
        self.btnC1.setChecked(True)
        self.btnC2.setChecked(True)
        self.btnC3.setChecked(True)
        self.btnC4.setChecked(True)
        self.btnC5.setChecked(True)
        self.btnC6.setChecked(True)
        self.btnC7.setChecked(True)
        self.btnC8.setChecked(True)
        self.btnC9.setChecked(True)

        # TODO Replace this function with the function to turn ON all inductive relays.
        # ON_all_Relays()

        # comment out this line to avoid output on terminal
        # print('All capacitive loads on')

    def all_off_cap(self):
        """ This function turns all buttons to OFF by forcing the state of the buttons """
        self.btnC1.setChecked(False)
        self.btnC2.setChecked(False)
        self.btnC3.setChecked(False)
        self.btnC4.setChecked(False)
        self.btnC5.setChecked(False)
        self.btnC6.setChecked(False)
        self.btnC7.setChecked(False)
        self.btnC8.setChecked(False)
        self.btnC9.setChecked(False)

        # TODO Replace this function with the function to turn ON all inductive relays.
        # OFF_all_Relays()

        # comment out this line to avoid output on terminal
        #print('All inductive loads off')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnR1.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR1.setText(_translate("MainWindow", "On|Off"))
        self.btnR2.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR2.setText(_translate("MainWindow", "On|Off"))
        self.btnR3.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR3.setText(_translate("MainWindow", "On|Off"))
        self.btnR4.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR4.setText(_translate("MainWindow", "On|Off"))
        self.btnR5.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR5.setText(_translate("MainWindow", "On|Off"))
        self.btnR6.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR6.setText(_translate("MainWindow", "On|Off"))
        self.btnR7.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR7.setText(_translate("MainWindow", "On|Off"))
        self.btnR8.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR8.setText(_translate("MainWindow", "On|Off"))
        self.btnR9.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnR9.setText(_translate("MainWindow", "On|Off"))
        self.btnAllOff_R.setToolTip(_translate("MainWindow", "Turn Off all resistive Loads."))
        self.btnAllOff_R.setText(_translate("MainWindow", "All Off"))
        self.btnAllOn_R.setToolTip(_translate("MainWindow", "Turn On all resistive loads."))
        self.btnAllOn_R.setText(_translate("MainWindow", "All On"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Resistive), _translate("MainWindow", "Resistive Loads"))
        self.btnL1.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL1.setText(_translate("MainWindow", "On|Off"))
        self.btnL2.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL2.setText(_translate("MainWindow", "On|Off"))
        self.btnL3.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL3.setText(_translate("MainWindow", "On|Off"))
        self.btnL6.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL6.setText(_translate("MainWindow", "On|Off"))
        self.btnL5.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL5.setText(_translate("MainWindow", "On|Off"))
        self.btnL4.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL4.setText(_translate("MainWindow", "On|Off"))
        self.btnL9.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL9.setText(_translate("MainWindow", "On|Off"))
        self.btnL8.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL8.setText(_translate("MainWindow", "On|Off"))
        self.btnL7.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnL7.setText(_translate("MainWindow", "On|Off"))
        self.btnAllOn_L.setToolTip(_translate("MainWindow", "Turn On all inductive loads."))
        self.btnAllOn_L.setText(_translate("MainWindow", "All On"))
        self.btnAllOff_L.setToolTip(_translate("MainWindow", "Turn Off all inductive loads."))
        self.btnAllOff_L.setText(_translate("MainWindow", "All Off"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inductive), _translate("MainWindow", "Inductive Loads"))
        self.btnC9.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC9.setText(_translate("MainWindow", "On|Off"))
        self.btnC8.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC8.setText(_translate("MainWindow", "On|Off"))
        self.btnC7.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC7.setText(_translate("MainWindow", "On|Off"))
        self.btnC6.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC6.setText(_translate("MainWindow", "On|Off"))
        self.btnC5.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC5.setText(_translate("MainWindow", "On|Off"))
        self.btnC4.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC4.setText(_translate("MainWindow", "On|Off"))
        self.btnC3.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC3.setText(_translate("MainWindow", "On|Off"))
        self.btnC2.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC2.setText(_translate("MainWindow", "On|Off"))
        self.btnC1.setToolTip(_translate("MainWindow", "Turn on/off this load."))
        self.btnC1.setText(_translate("MainWindow", "On|Off"))
        self.btnAllOff_C.setToolTip(_translate("MainWindow", "Turn Off all capacitive loads."))
        self.btnAllOff_C.setText(_translate("MainWindow", "All Off"))
        self.btnAllOn_C.setToolTip(_translate("MainWindow", "Turn On all capacitive loads."))
        self.btnAllOn_C.setText(_translate("MainWindow", "All On"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Capacitive), _translate("MainWindow", "Capacitive Loads"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ExtraControls),
                                  _translate("MainWindow", "Extra Controls"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLab_1.setTitle(_translate("MainWindow", "Lab 1"))
        self.menuLab_2.setTitle(_translate("MainWindow", "Demo"))
        #------------------ LoadBoxes list---------------------------------
        self.menuLoadBoxes.setTitle(_translate("MainWindow", "Remote Load Boxes"))
        self.menuLoadBox001.setTitle(_translate("MainWindow", "LoadBox001"))
        self.menuLoadBox002.setTitle(_translate("MainWindow", "LoadBox002"))
        self.menuLoadBox003.setTitle(_translate("MainWindow", "LoadBox003"))
        self.menuLoadBox004.setTitle(_translate("MainWindow", "LoadBox004"))
        self.menuLoadBox005.setTitle(_translate("MainWindow", "LoadBox005"))
        self.menuLoadBox006.setTitle(_translate("MainWindow", "LoadBox006"))
        #---------------------------------------------------------------------------
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuAttribution.setTitle(_translate("MainWindow", "Attribution"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoadBanksWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
