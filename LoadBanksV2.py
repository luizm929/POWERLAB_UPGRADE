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


#TODO Clean all unused libraries
import random, sys, traceback, socket, time, sched
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon, QPicture
from PyQt5.QtWidgets import QAction, qApp, QApplication
from PyQt5.QtCore import (QObject, QRunnable, QThread, QThreadPool, pyqtSignal)
device_ip = ('192.168.1.3', 2000)
name = 'LoadBox001'
from commj import *

# Button colors


class GetReadingsThread(QThread):
    def __init__(self, Readings):
        QThread.__init__(self)
        self.Readings = Readings


    def __del__(self):
        self.wait()


    def run(self):
        command = 'Get Meas ACK'
        err = SetCMD(command, device_ip, name)
        print('Success, thread running')


# class WorkerSignals(QObject):
#     finished = pyqtSignal()
#     error = pyqtSignal(tuple)
#     result = pyqtSignal(object)
#     progress = pyqtSignal(int)
#
# class Worker(QRunnable):
#     # This is a worker
#     def __init__(self,*args, **kwargs ):
#         super(Worker, self).__init__()
#         self.args = args
#         self.kwargs = kwargs
#         self.signals = WorkerSignals()
#         self.kwargs['progress_callback'] = self.signals.progress
#
#     def run(self):
#         command = 'Get Meas ACK'
#         err = SetCMD(command, device_ip, name)
#         print('Success, thread running')


class Ui_LoadBanksWindow(object):

    def setupUi(self, LoadBanksWindow):
        #--------------Initial values of live updates labels---
        # These values here are just for reference they may not be needed
        init_mag_Pa = init_mag_Ib = init_mag_Ic = 0.0
        init_ang_Ia = init_ang_Ib = init_ang_Ic = 0.0
        init_mag_Va = init_mag_Vb = init_mag_Vc = 0.0
        init_ang_Va = init_ang_Vb = init_ang_Vc = 0.0
        init_mag_Pa = init_mag_Pb = init_mag_Pc = 0.0
        init_ang_Pa = init_ang_Pb = init_ang_Pc = 0.0
        LoadBanksWindow.setObjectName("LoadBanksWindow")
        #LoadBanksWindow.resize(1388, 916)
        LoadBanksWindow.setFixedSize(1360, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadBanksWindow.sizePolicy().hasHeightForWidth())
        LoadBanksWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(LoadBanksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1350, 751))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.ResistiveLoads = QtWidgets.QWidget()
        self.ResistiveLoads.setObjectName("ResistiveLoads")
        self.label = QtWidgets.QLabel(self.ResistiveLoads)
        self.label.setGeometry(QtCore.QRect(0, 0, 1351, 721))

        #resistive_pix = QPixmap('img/Resistive.png')
        #self.label.setScaledContents(True)
        self.label.setPixmap(QPixmap('img/Resistive.png'))
        self.label.setScaledContents(True)

        #self.label.setStyleSheet("border-image: url(:/img/Resistive.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnR1 = QtWidgets.QPushButton(self.ResistiveLoads)
        self.btnR1.setGeometry(QtCore.QRect(132, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnR1.sizePolicy().hasHeightForWidth())
        self.btnR1.setSizePolicy(sizePolicy)
        self.btnR1.setMinimumSize(QtCore.QSize(70, 70))
        self.btnR1.setMaximumSize(QtCore.QSize(70, 70))
        self.btnR1.setStyleSheet("#btnR1{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnR1:checked{\n"
"    background-color: red;\n"
"}")
        self.btnR1.setCheckable(True)
        self.btnR1.setObjectName("btnR1")
        # ---------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR1.clicked.connect(self.btn_r1)
        # ----------------------------------------


        self.btnR2 = QtWidgets.QPushButton(self.ResistiveLoads)
        self.btnR2.setGeometry(QtCore.QRect(240, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnR2.sizePolicy().hasHeightForWidth())
        self.btnR2.setSizePolicy(sizePolicy)
        self.btnR2.setMinimumSize(QtCore.QSize(70, 70))
        self.btnR2.setMaximumSize(QtCore.QSize(70, 70))
        self.btnR2.setStyleSheet("#btnR2{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnR2:checked{\n"
"    background-color: red;\n"
"}")
        self.btnR2.setCheckable(True)
        self.btnR2.setObjectName("btnR2")
        # -------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR2.clicked.connect(self.btn_r2)
        # -------------------------------------------------------------

        self.btnR3 = QtWidgets.QPushButton(self.ResistiveLoads)
        self.btnR3.setGeometry(QtCore.QRect(349, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnR3.sizePolicy().hasHeightForWidth())
        self.btnR3.setSizePolicy(sizePolicy)
        self.btnR3.setMinimumSize(QtCore.QSize(70, 70))
        self.btnR3.setMaximumSize(QtCore.QSize(70, 70))
        self.btnR3.setStyleSheet("#btnR3{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnR3:checked{\n"
"    background-color: red;\n"
"}")
        self.btnR3.setCheckable(True)
        self.btnR3.setObjectName("btnR3")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR3.clicked.connect(self.btn_r3)

        self.btnR4 = QtWidgets.QPushButton(self.ResistiveLoads)
        self.btnR4.setGeometry(QtCore.QRect(523, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnR4.sizePolicy().hasHeightForWidth())
        self.btnR4.setSizePolicy(sizePolicy)
        self.btnR4.setMinimumSize(QtCore.QSize(70, 70))
        self.btnR4.setMaximumSize(QtCore.QSize(70, 70))
        self.btnR4.setStyleSheet("#btnR4{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnR4:checked{\n"
"    background-color: red;\n"
"}")
        self.btnR4.setCheckable(True)
        self.btnR4.setObjectName("btnR4")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR4.clicked.connect(self.btn_r4)

        self.btnR5 = QtWidgets.QPushButton(self.ResistiveLoads)
        self.btnR5.setGeometry(QtCore.QRect(630, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnR5.sizePolicy().hasHeightForWidth())
        self.btnR5.setSizePolicy(sizePolicy)
        self.btnR5.setMinimumSize(QtCore.QSize(70, 70))
        self.btnR5.setMaximumSize(QtCore.QSize(70, 70))
        self.btnR5.setStyleSheet("#btnR5{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnR5:checked{\n"
"    background-color: red;\n"
"}")
        self.btnR5.setCheckable(True)
        self.btnR5.setObjectName("btnR5")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR5.clicked.connect(self.btn_r5)

        self.btnR6 = QtWidgets.QPushButton(self.ResistiveLoads)
        self.btnR6.setGeometry(QtCore.QRect(740, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnR6.sizePolicy().hasHeightForWidth())
        self.btnR6.setSizePolicy(sizePolicy)
        self.btnR6.setMinimumSize(QtCore.QSize(70, 70))
        self.btnR6.setMaximumSize(QtCore.QSize(70, 70))
        self.btnR6.setStyleSheet("#btnR6{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnR6:checked{\n"
"    background-color: red;\n"
"}")
        self.btnR6.setCheckable(True)
        self.btnR6.setObjectName("btnR6")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR6.clicked.connect(self.btn_r6)

        self.btnR7 = QtWidgets.QPushButton(self.ResistiveLoads)
        self.btnR7.setGeometry(QtCore.QRect(910, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnR7.sizePolicy().hasHeightForWidth())
        self.btnR7.setSizePolicy(sizePolicy)
        self.btnR7.setMinimumSize(QtCore.QSize(70, 70))
        self.btnR7.setMaximumSize(QtCore.QSize(70, 70))
        self.btnR7.setStyleSheet("#btnR7{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnR7:checked{\n"
"    background-color: red;\n"
"}")
        self.btnR7.setCheckable(True)
        self.btnR7.setObjectName("btnR7")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR7.clicked.connect(self.btn_r7)

        self.btnR8 = QtWidgets.QPushButton(self.ResistiveLoads)
        self.btnR8.setGeometry(QtCore.QRect(1020, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnR8.sizePolicy().hasHeightForWidth())
        self.btnR8.setSizePolicy(sizePolicy)
        self.btnR8.setMinimumSize(QtCore.QSize(70, 70))
        self.btnR8.setMaximumSize(QtCore.QSize(70, 70))
        self.btnR8.setStyleSheet("#btnR8{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnR8:checked{\n"
"    background-color: red;\n"
"}")
        self.btnR8.setCheckable(True)
        self.btnR8.setObjectName("btnR8")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR8.clicked.connect(self.btn_r8)

        self.btnR9 = QtWidgets.QPushButton(self.ResistiveLoads)
        self.btnR9.setGeometry(QtCore.QRect(1135, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnR9.sizePolicy().hasHeightForWidth())
        self.btnR9.setSizePolicy(sizePolicy)
        self.btnR9.setMinimumSize(QtCore.QSize(70, 70))
        self.btnR9.setMaximumSize(QtCore.QSize(70, 70))
        self.btnR9.setStyleSheet("#btnR9{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnR9:checked{\n"
"    background-color: red;\n"
"}")
        self.btnR9.setCheckable(True)
        self.btnR9.setObjectName("btnR9")

        # -------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnR9.clicked.connect(self.btn_r9)
        # -------------------------------------------------------------

        self.widget = QtWidgets.QWidget(self.ResistiveLoads)
        self.widget.setGeometry(QtCore.QRect(0, 0, 149, 72))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnAllOn_R = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAllOn_R.sizePolicy().hasHeightForWidth())
        self.btnAllOn_R.setSizePolicy(sizePolicy)
        self.btnAllOn_R.setMinimumSize(QtCore.QSize(70, 70))
        self.btnAllOn_R.setMaximumSize(QtCore.QSize(70, 70))
        self.btnAllOn_R.setStyleSheet("#btnAllOn_R{\n"
"background-color: red;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnAllOn_R:pressed{\n"
"    background-color: #F1948A;\n"
"}")
        self.btnAllOn_R.setCheckable(True)
        self.btnAllOn_R.setObjectName("btnAllOn_R")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOn_R.clicked.connect(self.all_on_res)

        self.horizontalLayout_3.addWidget(self.btnAllOn_R)
        self.btnAllOff_R = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAllOff_R.sizePolicy().hasHeightForWidth())
        self.btnAllOff_R.setSizePolicy(sizePolicy)
        self.btnAllOff_R.setMinimumSize(QtCore.QSize(70, 70))
        self.btnAllOff_R.setMaximumSize(QtCore.QSize(70, 70))
        self.btnAllOff_R.setStyleSheet("#btnAllOff_R{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnAllOff_R:pressed{\n"
"    background-color: #28B463;\n" # #28B463
"}")
        self.btnAllOff_R.setCheckable(True)
        self.btnAllOff_R.setObjectName("btnAllOff_R")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOff_R.clicked.connect(self.all_off_res)

        self.horizontalLayout_3.addWidget(self.btnAllOff_R)
        self.frame_8 = QtWidgets.QFrame(self.ResistiveLoads)
        self.frame_8.setGeometry(QtCore.QRect(229, 81, 84, 55))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.Pa_label_left_ResLoad = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_label_left_ResLoad.sizePolicy().hasHeightForWidth())
        self.Pa_label_left_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Pa_label_left_ResLoad.setFont(font)
        self.Pa_label_left_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_label_left_ResLoad.setObjectName("Pa_label_left_ResLoad")
        self.verticalLayout_23.addWidget(self.Pa_label_left_ResLoad)
        self.Va_label_left_ResLoad = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_label_left_ResLoad.sizePolicy().hasHeightForWidth())
        self.Va_label_left_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Va_label_left_ResLoad.setFont(font)
        self.Va_label_left_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_label_left_ResLoad.setObjectName("Va_label_left_ResLoad")
        self.verticalLayout_23.addWidget(self.Va_label_left_ResLoad)
        self.horizontalLayout_14.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")

        # This is how we assign the initial value to the QLabel
        self.Pa_live_label_left_ResLoad = QtWidgets.QLabel(str(init_mag_Pa), self.frame_8)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_live_label_left_ResLoad.sizePolicy().hasHeightForWidth())
        self.Pa_live_label_left_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Pa_live_label_left_ResLoad.setFont(font)
        self.Pa_live_label_left_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_live_label_left_ResLoad.setObjectName("Pa_live_label_left_ResLoad")
        self.verticalLayout_24.addWidget(self.Pa_live_label_left_ResLoad)
        self.Va_live_label_left_ResLoad = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_live_label_left_ResLoad.sizePolicy().hasHeightForWidth())
        self.Va_live_label_left_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Va_live_label_left_ResLoad.setFont(font)
        self.Va_live_label_left_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_live_label_left_ResLoad.setObjectName("Va_live_label_left_ResLoad")
        self.verticalLayout_24.addWidget(self.Va_live_label_left_ResLoad)
        self.horizontalLayout_14.addLayout(self.verticalLayout_24)
        self.frame_9 = QtWidgets.QFrame(self.ResistiveLoads)
        self.frame_9.setGeometry(QtCore.QRect(622, 81, 84, 55))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.Pa_label_middle_ResLoad = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_label_middle_ResLoad.sizePolicy().hasHeightForWidth())
        self.Pa_label_middle_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Pa_label_middle_ResLoad.setFont(font)
        self.Pa_label_middle_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_label_middle_ResLoad.setObjectName("Pa_label_middle_ResLoad")
        self.verticalLayout_26.addWidget(self.Pa_label_middle_ResLoad)
        self.Va_label_middle_ResLoad = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_label_middle_ResLoad.sizePolicy().hasHeightForWidth())
        self.Va_label_middle_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Va_label_middle_ResLoad.setFont(font)
        self.Va_label_middle_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_label_middle_ResLoad.setObjectName("Va_label_middle_ResLoad")
        self.verticalLayout_26.addWidget(self.Va_label_middle_ResLoad)
        self.horizontalLayout_16.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")

        #-------------------------------------------------------------------------------
        self.Pa_live_label_middle_ResLoad = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_live_label_middle_ResLoad.sizePolicy().hasHeightForWidth())
        self.Pa_live_label_middle_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Pa_live_label_middle_ResLoad.setFont(font)
        self.Pa_live_label_middle_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_live_label_middle_ResLoad.setObjectName("Pa_live_label_middle_ResLoad")
        self.verticalLayout_27.addWidget(self.Pa_live_label_middle_ResLoad)
        # -------------------------------------------------------------------------------
        self.Va_live_label_middle_ResLoad = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_live_label_middle_ResLoad.sizePolicy().hasHeightForWidth())
        self.Va_live_label_middle_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Va_live_label_middle_ResLoad.setFont(font)
        self.Va_live_label_middle_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_live_label_middle_ResLoad.setObjectName("Va_live_label_middle_ResLoad")
        self.verticalLayout_27.addWidget(self.Va_live_label_middle_ResLoad)
        # -------------------------------------------------------------------------------
        self.horizontalLayout_16.addLayout(self.verticalLayout_27)
        self.frame_10 = QtWidgets.QFrame(self.ResistiveLoads)
        self.frame_10.setGeometry(QtCore.QRect(1016, 81, 84, 55))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        # -------------------------------------------------------------------------------
        self.Pa_label_right_ResLoad = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_label_right_ResLoad.sizePolicy().hasHeightForWidth())
        self.Pa_label_right_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Pa_label_right_ResLoad.setFont(font)
        self.Pa_label_right_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_label_right_ResLoad.setObjectName("Pa_label_right_ResLoad")
        self.verticalLayout_29.addWidget(self.Pa_label_right_ResLoad)
        # -------------------------------------------------------------------------------
        self.Va_label_right_ResLoad = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_label_right_ResLoad.sizePolicy().hasHeightForWidth())
        self.Va_label_right_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Va_label_right_ResLoad.setFont(font)
        self.Va_label_right_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_label_right_ResLoad.setObjectName("Va_label_right_ResLoad")
        self.verticalLayout_29.addWidget(self.Va_label_right_ResLoad)
        # -------------------------------------------------------------------------------
        self.horizontalLayout_18.addLayout(self.verticalLayout_29)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")

        self.Pa_live_label_right_ResLoad = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_live_label_right_ResLoad.sizePolicy().hasHeightForWidth())
        self.Pa_live_label_right_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Pa_live_label_right_ResLoad.setFont(font)
        self.Pa_live_label_right_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_live_label_right_ResLoad.setObjectName("Pa_live_label_right_ResLoad")
        self.verticalLayout_30.addWidget(self.Pa_live_label_right_ResLoad)
        # -------------------------------------------------------------------------------
        self.Va_live_label_right_ResLoad = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_live_label_right_ResLoad.sizePolicy().hasHeightForWidth())
        self.Va_live_label_right_ResLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Va_live_label_right_ResLoad.setFont(font)
        self.Va_live_label_right_ResLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_live_label_right_ResLoad.setObjectName("Va_live_label_right_ResLoad")
        self.verticalLayout_30.addWidget(self.Va_live_label_right_ResLoad)
        self.horizontalLayout_18.addLayout(self.verticalLayout_30)
        # ----------------------------- expand button
        self.Res_right_expand_butt = QtWidgets.QPushButton(self.ResistiveLoads)
        self.Res_right_expand_butt.setGeometry(QtCore.QRect(1210, 90, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Res_right_expand_butt.sizePolicy().hasHeightForWidth())
        self.Res_right_expand_butt.setSizePolicy(sizePolicy)
        self.Res_right_expand_butt.setMinimumSize(QtCore.QSize(10, 10))
        self.Res_right_expand_butt.setMaximumSize(QtCore.QSize(80, 80))
        self.Res_right_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Res_right_expand_butt.setStyleSheet("#Res_right_expand_butt{\n"
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
"#Res_right_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.Res_right_expand_butt.setCheckable(True)
        self.Res_right_expand_butt.setObjectName("Res_right_expand_butt")
        self.tabWidget.addTab(self.ResistiveLoads, "")
        self.InductiveLoads = QtWidgets.QWidget()
        self.InductiveLoads.setObjectName("InductiveLoads")
        self.label_2 = QtWidgets.QLabel(self.InductiveLoads)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1351, 721))

        #Here we map a QPixmap out of the image
        inductive_pix = QPixmap('img/Ind.png')
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(inductive_pix)

        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        #------------------------ Inductive loads buttons start here
        self.btnL1 = QtWidgets.QPushButton(self.InductiveLoads)
        self.btnL1.setGeometry(QtCore.QRect(133, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnL1.sizePolicy().hasHeightForWidth())
        self.btnL1.setSizePolicy(sizePolicy)
        self.btnL1.setMinimumSize(QtCore.QSize(70, 70))
        self.btnL1.setMaximumSize(QtCore.QSize(70, 70))
        self.btnL1.setStyleSheet("#btnL1{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnL1:checked{\n"
"    background-color: red;\n"
"}")
        self.btnL1.setCheckable(True)
        self.btnL1.setObjectName("btnL1")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL1.clicked.connect(self.btn_L1)

        self.btnL2 = QtWidgets.QPushButton(self.InductiveLoads)
        self.btnL2.setGeometry(QtCore.QRect(241, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnL2.sizePolicy().hasHeightForWidth())
        self.btnL2.setSizePolicy(sizePolicy)
        self.btnL2.setMinimumSize(QtCore.QSize(70, 70))
        self.btnL2.setMaximumSize(QtCore.QSize(70, 70))
        self.btnL2.setStyleSheet("#btnL2{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnL2:checked{\n"
"    background-color: red;\n"
"}")
        self.btnL2.setCheckable(True)
        self.btnL2.setObjectName("btnL2")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL2.clicked.connect(self.btn_L2)

        self.btnL3 = QtWidgets.QPushButton(self.InductiveLoads)
        self.btnL3.setGeometry(QtCore.QRect(350, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnL3.sizePolicy().hasHeightForWidth())
        self.btnL3.setSizePolicy(sizePolicy)
        self.btnL3.setMinimumSize(QtCore.QSize(70, 70))
        self.btnL3.setMaximumSize(QtCore.QSize(70, 70))
        self.btnL3.setStyleSheet("#btnL3{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnL3:checked{\n"
"    background-color: red;\n"
"}")
        self.btnL3.setCheckable(True)
        self.btnL3.setObjectName("btnL3")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL3.clicked.connect(self.btn_L3)

        self.btnL4 = QtWidgets.QPushButton(self.InductiveLoads)
        self.btnL4.setGeometry(QtCore.QRect(521, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnL4.sizePolicy().hasHeightForWidth())
        self.btnL4.setSizePolicy(sizePolicy)
        self.btnL4.setMinimumSize(QtCore.QSize(70, 70))
        self.btnL4.setMaximumSize(QtCore.QSize(70, 70))
        self.btnL4.setStyleSheet("#btnL4{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnL4:checked{\n"
"    background-color: red;\n"
"}")
        self.btnL4.setCheckable(True)
        self.btnL4.setObjectName("btnL4")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL4.clicked.connect(self.btn_L4)

        self.btnL5 = QtWidgets.QPushButton(self.InductiveLoads)
        self.btnL5.setGeometry(QtCore.QRect(628, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnL5.sizePolicy().hasHeightForWidth())
        self.btnL5.setSizePolicy(sizePolicy)
        self.btnL5.setMinimumSize(QtCore.QSize(70, 70))
        self.btnL5.setMaximumSize(QtCore.QSize(70, 70))
        self.btnL5.setStyleSheet("#btnL5{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnL5:checked{\n"
"    background-color: red;\n"
"}")
        self.btnL5.setCheckable(True)
        self.btnL5.setObjectName("btnL5")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL5.clicked.connect(self.btn_L5)

        self.btnL6 = QtWidgets.QPushButton(self.InductiveLoads)
        self.btnL6.setGeometry(QtCore.QRect(735, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnL6.sizePolicy().hasHeightForWidth())
        self.btnL6.setSizePolicy(sizePolicy)
        self.btnL6.setMinimumSize(QtCore.QSize(70, 70))
        self.btnL6.setMaximumSize(QtCore.QSize(70, 70))
        self.btnL6.setStyleSheet("#btnL6{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnL6:checked{\n"
"    background-color: red;\n"
"}")
        self.btnL6.setCheckable(True)
        self.btnL6.setObjectName("btnL6")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL6.clicked.connect(self.btn_L6)

        self.btnL7 = QtWidgets.QPushButton(self.InductiveLoads)
        self.btnL7.setGeometry(QtCore.QRect(910, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnL7.sizePolicy().hasHeightForWidth())
        self.btnL7.setSizePolicy(sizePolicy)
        self.btnL7.setMinimumSize(QtCore.QSize(70, 70))
        self.btnL7.setMaximumSize(QtCore.QSize(70, 70))
        self.btnL7.setStyleSheet("#btnL7{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnL7:checked{\n"
"    background-color: red;\n"
"}")
        self.btnL7.setCheckable(True)
        self.btnL7.setObjectName("btnL7")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL7.clicked.connect(self.btn_L7)

        self.btnL8 = QtWidgets.QPushButton(self.InductiveLoads)
        self.btnL8.setGeometry(QtCore.QRect(1020, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnL8.sizePolicy().hasHeightForWidth())
        self.btnL8.setSizePolicy(sizePolicy)
        self.btnL8.setMinimumSize(QtCore.QSize(70, 70))
        self.btnL8.setMaximumSize(QtCore.QSize(70, 70))
        self.btnL8.setStyleSheet("#btnL8{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnL8:checked{\n"
"    background-color: red;\n"
"}")
        self.btnL8.setCheckable(True)
        self.btnL8.setObjectName("btnL8")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL8.clicked.connect(self.btn_L8)

        self.btnL9 = QtWidgets.QPushButton(self.InductiveLoads)
        self.btnL9.setGeometry(QtCore.QRect(1132, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnL9.sizePolicy().hasHeightForWidth())
        self.btnL9.setSizePolicy(sizePolicy)
        self.btnL9.setMinimumSize(QtCore.QSize(70, 70))
        self.btnL9.setMaximumSize(QtCore.QSize(70, 70))
        self.btnL9.setStyleSheet("#btnL9{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnL9:checked{\n"
"    background-color: red;\n"
"}")
        self.btnL9.setCheckable(True)
        self.btnL9.setObjectName("btnL9")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnL9.clicked.connect(self.btn_L9)

        self.frame_6 = QtWidgets.QFrame(self.InductiveLoads)
        self.frame_6.setGeometry(QtCore.QRect(622, 81, 84, 55))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.Pa_label_middle_IndLoad = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_label_middle_IndLoad.sizePolicy().hasHeightForWidth())
        self.Pa_label_middle_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Pa_label_middle_IndLoad.setFont(font)
        self.Pa_label_middle_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_label_middle_IndLoad.setObjectName("Pa_label_middle_IndLoad")
        self.verticalLayout_17.addWidget(self.Pa_label_middle_IndLoad)
        self.Va_label_middle_IndLoad = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_label_middle_IndLoad.sizePolicy().hasHeightForWidth())
        self.Va_label_middle_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Va_label_middle_IndLoad.setFont(font)
        self.Va_label_middle_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_label_middle_IndLoad.setObjectName("Va_label_middle_IndLoad")
        self.verticalLayout_17.addWidget(self.Va_label_middle_IndLoad)
        self.horizontalLayout_10.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.Pa_live_label_middle_IndLoad = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_live_label_middle_IndLoad.sizePolicy().hasHeightForWidth())
        self.Pa_live_label_middle_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Pa_live_label_middle_IndLoad.setFont(font)
        self.Pa_live_label_middle_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_live_label_middle_IndLoad.setObjectName("Pa_live_label_middle_IndLoad")
        self.verticalLayout_18.addWidget(self.Pa_live_label_middle_IndLoad)
        self.Va_live_label_middle_IndLoad = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_live_label_middle_IndLoad.sizePolicy().hasHeightForWidth())
        self.Va_live_label_middle_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Va_live_label_middle_IndLoad.setFont(font)
        self.Va_live_label_middle_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_live_label_middle_IndLoad.setObjectName("Va_live_label_middle_IndLoad")
        self.verticalLayout_18.addWidget(self.Va_live_label_middle_IndLoad)
        self.horizontalLayout_10.addLayout(self.verticalLayout_18)
        self.widget1 = QtWidgets.QWidget(self.InductiveLoads)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 149, 72))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnAllOn_L = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAllOn_L.sizePolicy().hasHeightForWidth())
        self.btnAllOn_L.setSizePolicy(sizePolicy)
        self.btnAllOn_L.setMinimumSize(QtCore.QSize(70, 70))
        self.btnAllOn_L.setMaximumSize(QtCore.QSize(70, 70))
        self.btnAllOn_L.setStyleSheet("#btnAllOn_L{\n"
"background-color: red;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnAllOn_L:pressed{\n"
"    background-color: #F1948A;\n"
"}")
        self.btnAllOn_L.setCheckable(True)
        self.btnAllOn_L.setObjectName("btnAllOn_L")

        # --------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOn_L.clicked.connect(self.all_on_ind)
        # --------------------------------------------------------------

        self.horizontalLayout_5.addWidget(self.btnAllOn_L)
        self.btnAllOff_L = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAllOff_L.sizePolicy().hasHeightForWidth())
        self.btnAllOff_L.setSizePolicy(sizePolicy)
        self.btnAllOff_L.setMinimumSize(QtCore.QSize(70, 70))
        self.btnAllOff_L.setMaximumSize(QtCore.QSize(70, 70))
        self.btnAllOff_L.setStyleSheet("#btnAllOff_L{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnAllOff_L:pressed{\n"
"    background-color: #28B463;\n" # 
"}")
        self.btnAllOff_L.setCheckable(True)
        self.btnAllOff_L.setObjectName("btnAllOff_L")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOff_L.clicked.connect(self.all_off_ind)

        self.horizontalLayout_5.addWidget(self.btnAllOff_L)
        self.Ind_left_expand_butt = QtWidgets.QPushButton(self.InductiveLoads)
        self.Ind_left_expand_butt.setGeometry(QtCore.QRect(1210, 90, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ind_left_expand_butt.sizePolicy().hasHeightForWidth())
        self.Ind_left_expand_butt.setSizePolicy(sizePolicy)
        self.Ind_left_expand_butt.setMinimumSize(QtCore.QSize(10, 10))
        self.Ind_left_expand_butt.setMaximumSize(QtCore.QSize(80, 80))
        self.Ind_left_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Ind_left_expand_butt.setStyleSheet("#Ind_left_expand_butt{\n"
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
"#Ind_left_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.Ind_left_expand_butt.setCheckable(True)
        self.Ind_left_expand_butt.setObjectName("Ind_left_expand_butt")
        self.frame_5 = QtWidgets.QFrame(self.InductiveLoads)
        self.frame_5.setGeometry(QtCore.QRect(229, 81, 84, 55))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.Pa_label_left_IndLoad = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_label_left_IndLoad.sizePolicy().hasHeightForWidth())
        self.Pa_label_left_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Pa_label_left_IndLoad.setFont(font)
        self.Pa_label_left_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_label_left_IndLoad.setObjectName("Pa_label_left_IndLoad")
        self.verticalLayout_14.addWidget(self.Pa_label_left_IndLoad)
        self.Va_label_left_IndLoad = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_label_left_IndLoad.sizePolicy().hasHeightForWidth())
        self.Va_label_left_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Va_label_left_IndLoad.setFont(font)
        self.Va_label_left_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_label_left_IndLoad.setObjectName("Va_label_left_IndLoad")
        self.verticalLayout_14.addWidget(self.Va_label_left_IndLoad)
        self.horizontalLayout_8.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.Pa_live_label_left_IndLoad = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_live_label_left_IndLoad.sizePolicy().hasHeightForWidth())
        self.Pa_live_label_left_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Pa_live_label_left_IndLoad.setFont(font)
        self.Pa_live_label_left_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_live_label_left_IndLoad.setObjectName("Pa_live_label_left_IndLoad")
        self.verticalLayout_15.addWidget(self.Pa_live_label_left_IndLoad)
        self.Va_live_label_left_IndLoad = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_live_label_left_IndLoad.sizePolicy().hasHeightForWidth())
        self.Va_live_label_left_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Va_live_label_left_IndLoad.setFont(font)
        self.Va_live_label_left_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_live_label_left_IndLoad.setObjectName("Va_live_label_left_IndLoad")
        self.verticalLayout_15.addWidget(self.Va_live_label_left_IndLoad)
        self.horizontalLayout_8.addLayout(self.verticalLayout_15)
        self.frame_7 = QtWidgets.QFrame(self.InductiveLoads)
        self.frame_7.setGeometry(QtCore.QRect(1016, 81, 84, 55))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.Pa_label_right_IndLoad = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_label_right_IndLoad.sizePolicy().hasHeightForWidth())
        self.Pa_label_right_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Pa_label_right_IndLoad.setFont(font)
        self.Pa_label_right_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_label_right_IndLoad.setObjectName("Pa_label_right_IndLoad")
        self.verticalLayout_20.addWidget(self.Pa_label_right_IndLoad)
        self.Va_label_right_IndLoad = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_label_right_IndLoad.sizePolicy().hasHeightForWidth())
        self.Va_label_right_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Va_label_right_IndLoad.setFont(font)
        self.Va_label_right_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_label_right_IndLoad.setObjectName("Va_label_right_IndLoad")
        self.verticalLayout_20.addWidget(self.Va_label_right_IndLoad)
        self.horizontalLayout_12.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.Pa_live_label_right_IndLoad = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_live_label_right_IndLoad.sizePolicy().hasHeightForWidth())
        self.Pa_live_label_right_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Pa_live_label_right_IndLoad.setFont(font)
        self.Pa_live_label_right_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_live_label_right_IndLoad.setObjectName("Pa_live_label_right_IndLoad")
        self.verticalLayout_21.addWidget(self.Pa_live_label_right_IndLoad)
        self.Va_live_label_right_IndLoad = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_live_label_right_IndLoad.sizePolicy().hasHeightForWidth())
        self.Va_live_label_right_IndLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Va_live_label_right_IndLoad.setFont(font)
        self.Va_live_label_right_IndLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_live_label_right_IndLoad.setObjectName("Va_live_label_right_IndLoad")
        self.verticalLayout_21.addWidget(self.Va_live_label_right_IndLoad)
        self.horizontalLayout_12.addLayout(self.verticalLayout_21)
        self.tabWidget.addTab(self.InductiveLoads, "")
        self.CapacitiveLoads = QtWidgets.QWidget()
        self.CapacitiveLoads.setObjectName("CapacitiveLoads")
        self.label_3 = QtWidgets.QLabel(self.CapacitiveLoads)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1351, 721))

        # Create a QPixMap of the cap image
        capacitive_pix = QPixmap('img/Cap.png')
        self.label_3.setScaledContents(True)
        self.label_3.setPixmap(capacitive_pix)


        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.btnC1 = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.btnC1.setGeometry(QtCore.QRect(136, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC1.sizePolicy().hasHeightForWidth())
        self.btnC1.setSizePolicy(sizePolicy)
        self.btnC1.setMinimumSize(QtCore.QSize(70, 70))
        self.btnC1.setMaximumSize(QtCore.QSize(70, 70))
        self.btnC1.setStyleSheet("#btnC1{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnC1:checked{\n"
"    background-color: red;\n"
"}")
        self.btnC1.setCheckable(True)
        self.btnC1.setObjectName("btnC1")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnC1.clicked.connect(self.btn_c1)

        self.btnC2 = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.btnC2.setGeometry(QtCore.QRect(244, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC2.sizePolicy().hasHeightForWidth())
        self.btnC2.setSizePolicy(sizePolicy)
        self.btnC2.setMinimumSize(QtCore.QSize(70, 70))
        self.btnC2.setMaximumSize(QtCore.QSize(70, 70))
        self.btnC2.setStyleSheet("#btnC2{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnC2:checked{\n"
"    background-color: red;\n"
"}")
        self.btnC2.setCheckable(True)
        self.btnC2.setObjectName("btnC2")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnC2.clicked.connect(self.btn_c2)

        self.btnC3 = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.btnC3.setGeometry(QtCore.QRect(352, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC3.sizePolicy().hasHeightForWidth())
        self.btnC3.setSizePolicy(sizePolicy)
        self.btnC3.setMinimumSize(QtCore.QSize(70, 70))
        self.btnC3.setMaximumSize(QtCore.QSize(70, 70))
        self.btnC3.setStyleSheet("#btnC3{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnC3:checked{\n"
"    background-color: red;\n"
"}")
        self.btnC3.setCheckable(True)
        self.btnC3.setObjectName("btnC3")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnC3.clicked.connect(self.btn_c3)

        self.btnC4 = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.btnC4.setGeometry(QtCore.QRect(525, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC4.sizePolicy().hasHeightForWidth())
        self.btnC4.setSizePolicy(sizePolicy)
        self.btnC4.setMinimumSize(QtCore.QSize(70, 70))
        self.btnC4.setMaximumSize(QtCore.QSize(70, 70))
        self.btnC4.setStyleSheet("#btnC4{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnC4:checked{\n"
"    background-color: red;\n"
"}")
        self.btnC4.setCheckable(True)
        self.btnC4.setObjectName("btnC4")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnC4.clicked.connect(self.btn_c4)

        self.btnC5 = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.btnC5.setGeometry(QtCore.QRect(633, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC5.sizePolicy().hasHeightForWidth())
        self.btnC5.setSizePolicy(sizePolicy)
        self.btnC5.setMinimumSize(QtCore.QSize(70, 70))
        self.btnC5.setMaximumSize(QtCore.QSize(70, 70))
        self.btnC5.setStyleSheet("#btnC5{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnC5:checked{\n"
"    background-color: red;\n"
"}")
        self.btnC5.setCheckable(True)
        self.btnC5.setObjectName("btnC5")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnC5.clicked.connect(self.btn_c5)

        self.btnC6 = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.btnC6.setGeometry(QtCore.QRect(741, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC6.sizePolicy().hasHeightForWidth())
        self.btnC6.setSizePolicy(sizePolicy)
        self.btnC6.setMinimumSize(QtCore.QSize(70, 70))
        self.btnC6.setMaximumSize(QtCore.QSize(70, 70))
        self.btnC6.setStyleSheet("#btnC6{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnC6:checked{\n"
"    background-color: red;\n"
"}")
        self.btnC6.setCheckable(True)
        self.btnC6.setObjectName("btnC6")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnC6.clicked.connect(self.btn_c6)

        self.btnC7 = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.btnC7.setGeometry(QtCore.QRect(917, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC7.sizePolicy().hasHeightForWidth())
        self.btnC7.setSizePolicy(sizePolicy)
        self.btnC7.setMinimumSize(QtCore.QSize(70, 70))
        self.btnC7.setMaximumSize(QtCore.QSize(70, 70))
        self.btnC7.setStyleSheet("#btnC7{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnC7:checked{\n"
"    background-color: red;\n"
"}")
        self.btnC7.setCheckable(True)
        self.btnC7.setObjectName("btnC7")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnC7.clicked.connect(self.btn_c7)

        self.btnC8 = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.btnC8.setGeometry(QtCore.QRect(1028, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC8.sizePolicy().hasHeightForWidth())
        self.btnC8.setSizePolicy(sizePolicy)
        self.btnC8.setMinimumSize(QtCore.QSize(70, 70))
        self.btnC8.setMaximumSize(QtCore.QSize(70, 70))
        self.btnC8.setStyleSheet("#btnC8{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnC8:checked{\n"
"    background-color: red;\n"
"}")
        self.btnC8.setCheckable(True)
        self.btnC8.setObjectName("btnC8")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnC8.clicked.connect(self.btn_c8)

        self.btnC9 = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.btnC9.setGeometry(QtCore.QRect(1140, 286, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC9.sizePolicy().hasHeightForWidth())
        self.btnC9.setSizePolicy(sizePolicy)
        self.btnC9.setMinimumSize(QtCore.QSize(70, 70))
        self.btnC9.setMaximumSize(QtCore.QSize(70, 70))
        self.btnC9.setStyleSheet("#btnC9{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnC9:checked{\n"
"    background-color: red;\n"
"}")
        self.btnC9.setCheckable(True)
        self.btnC9.setObjectName("btnC9")

        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnC9.clicked.connect(self.btn_c9)

        self.widget2 = QtWidgets.QWidget(self.CapacitiveLoads)
        self.widget2.setGeometry(QtCore.QRect(0, 0, 149, 72))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnAllOn_C = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAllOn_C.sizePolicy().hasHeightForWidth())
        self.btnAllOn_C.setSizePolicy(sizePolicy)
        self.btnAllOn_C.setMinimumSize(QtCore.QSize(70, 70))
        self.btnAllOn_C.setMaximumSize(QtCore.QSize(70, 70))
        self.btnAllOn_C.setStyleSheet("#btnAllOn_C{\n"
"background-color: red;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnAllOn_C:pressed{\n"
"    background-color: #F1948A;\n" 
"}")
        self.btnAllOn_C.setCheckable(True)
        self.btnAllOn_C.setObjectName("btnAllOn_C")

        # --------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOn_C.clicked.connect(self.all_on_cap)
        # ----------------------------------------------------------------

        self.horizontalLayout_7.addWidget(self.btnAllOn_C)
        self.btnAllOff_C = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAllOff_C.sizePolicy().hasHeightForWidth())
        self.btnAllOff_C.setSizePolicy(sizePolicy)
        self.btnAllOff_C.setMinimumSize(QtCore.QSize(70, 70))
        self.btnAllOff_C.setMaximumSize(QtCore.QSize(70, 70))
        self.btnAllOff_C.setStyleSheet("#btnAllOff_C{\n"
"background-color: green;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"padding: 3px;\n"
"max-width:60px;\n"
"max-height:60px;\n"
"min-width:60px;\n"
"min-height:60px;\n"
"font-size:16px;\n"
"font-weight:300;\n"
"color: white;\n"
"text-align:center;\n"
"}\n"
"#btnAllOff_C:pressed{\n"
"    background-color: #28B463;\n" # 
"}")
        self.btnAllOff_C.setCheckable(True)
        self.btnAllOff_C.setObjectName("btnAllOff_C")

        # -------------------------------------------------------------
        """Enables calling function btn_r1 when buttons is pressed."""
        self.btnAllOff_C.clicked.connect(self.all_off_cap)
        # -------------------------------------------------------------

        self.horizontalLayout_7.addWidget(self.btnAllOff_C)
        self.frame = QtWidgets.QFrame(self.CapacitiveLoads)
        self.frame.setGeometry(QtCore.QRect(229, 81, 84, 55))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Pa_label_left_CapLoad = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_label_left_CapLoad.sizePolicy().hasHeightForWidth())
        self.Pa_label_left_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Pa_label_left_CapLoad.setFont(font)
        self.Pa_label_left_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_label_left_CapLoad.setObjectName("Pa_label_left_CapLoad")
        self.verticalLayout.addWidget(self.Pa_label_left_CapLoad)
        self.Va_label_left_CapLoad = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_label_left_CapLoad.sizePolicy().hasHeightForWidth())
        self.Va_label_left_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Va_label_left_CapLoad.setFont(font)
        self.Va_label_left_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_label_left_CapLoad.setObjectName("Va_label_left_CapLoad")
        self.verticalLayout.addWidget(self.Va_label_left_CapLoad)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Pa_live_label_left_CapLoad = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_live_label_left_CapLoad.sizePolicy().hasHeightForWidth())
        self.Pa_live_label_left_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Pa_live_label_left_CapLoad.setFont(font)
        self.Pa_live_label_left_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_live_label_left_CapLoad.setObjectName("Pa_live_label_left_CapLoad")
        self.verticalLayout_2.addWidget(self.Pa_live_label_left_CapLoad)
        self.Va_live_label_left_CapLoad = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_live_label_left_CapLoad.sizePolicy().hasHeightForWidth())
        self.Va_live_label_left_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Va_live_label_left_CapLoad.setFont(font)
        self.Va_live_label_left_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_live_label_left_CapLoad.setObjectName("Va_live_label_left_CapLoad")
        self.verticalLayout_2.addWidget(self.Va_live_label_left_CapLoad)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.frame_3 = QtWidgets.QFrame(self.CapacitiveLoads)
        self.frame_3.setGeometry(QtCore.QRect(622, 81, 84, 55))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Pa_label_middle_CapLoad = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_label_middle_CapLoad.sizePolicy().hasHeightForWidth())
        self.Pa_label_middle_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Pa_label_middle_CapLoad.setFont(font)
        self.Pa_label_middle_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_label_middle_CapLoad.setObjectName("Pa_label_middle_CapLoad")
        self.verticalLayout_8.addWidget(self.Pa_label_middle_CapLoad)
        self.Va_label_middle_CapLoad = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_label_middle_CapLoad.sizePolicy().hasHeightForWidth())
        self.Va_label_middle_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Va_label_middle_CapLoad.setFont(font)
        self.Va_label_middle_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_label_middle_CapLoad.setObjectName("Va_label_middle_CapLoad")
        self.verticalLayout_8.addWidget(self.Va_label_middle_CapLoad)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Pa_live_label_middle_CapLoad = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_live_label_middle_CapLoad.sizePolicy().hasHeightForWidth())
        self.Pa_live_label_middle_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Pa_live_label_middle_CapLoad.setFont(font)
        self.Pa_live_label_middle_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_live_label_middle_CapLoad.setObjectName("Pa_live_label_middle_CapLoad")
        self.verticalLayout_9.addWidget(self.Pa_live_label_middle_CapLoad)
        self.Va_live_label_middle_CapLoad = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_live_label_middle_CapLoad.sizePolicy().hasHeightForWidth())
        self.Va_live_label_middle_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Va_live_label_middle_CapLoad.setFont(font)
        self.Va_live_label_middle_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_live_label_middle_CapLoad.setObjectName("Va_live_label_middle_CapLoad")
        self.verticalLayout_9.addWidget(self.Va_live_label_middle_CapLoad)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.frame_4 = QtWidgets.QFrame(self.CapacitiveLoads)
        self.frame_4.setGeometry(QtCore.QRect(1016, 81, 84, 55))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Pa_label_right_CapLoad = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_label_right_CapLoad.sizePolicy().hasHeightForWidth())
        self.Pa_label_right_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Pa_label_right_CapLoad.setFont(font)
        self.Pa_label_right_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_label_right_CapLoad.setObjectName("Pa_label_right_CapLoad")
        self.verticalLayout_11.addWidget(self.Pa_label_right_CapLoad)
        self.Va_label_right_CapLoad = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_label_right_CapLoad.sizePolicy().hasHeightForWidth())
        self.Va_label_right_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Va_label_right_CapLoad.setFont(font)
        self.Va_label_right_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_label_right_CapLoad.setObjectName("Va_label_right_CapLoad")
        self.verticalLayout_11.addWidget(self.Va_label_right_CapLoad)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Pa_live_label_right_CapLoad = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pa_live_label_right_CapLoad.sizePolicy().hasHeightForWidth())
        self.Pa_live_label_right_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Pa_live_label_right_CapLoad.setFont(font)
        self.Pa_live_label_right_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pa_live_label_right_CapLoad.setObjectName("Pa_live_label_right_CapLoad")
        self.verticalLayout_12.addWidget(self.Pa_live_label_right_CapLoad)
        self.Va_live_label_right_CapLoad = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Va_live_label_right_CapLoad.sizePolicy().hasHeightForWidth())
        self.Va_live_label_right_CapLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter UI Medium")
        font.setPointSize(9)
        self.Va_live_label_right_CapLoad.setFont(font)
        self.Va_live_label_right_CapLoad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va_live_label_right_CapLoad.setObjectName("Va_live_label_right_CapLoad")
        self.verticalLayout_12.addWidget(self.Va_live_label_right_CapLoad)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.Cap_expand_butt = QtWidgets.QPushButton(self.CapacitiveLoads)
        self.Cap_expand_butt.setGeometry(QtCore.QRect(1210, 90, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cap_expand_butt.sizePolicy().hasHeightForWidth())
        self.Cap_expand_butt.setSizePolicy(sizePolicy)
        self.Cap_expand_butt.setMinimumSize(QtCore.QSize(10, 10))
        self.Cap_expand_butt.setMaximumSize(QtCore.QSize(80, 80))
        self.Cap_expand_butt.setSizeIncrement(QtCore.QSize(1, 1))
        self.Cap_expand_butt.setStyleSheet("#Cap_expand_butt{\n"
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
"#Cap_expand_butt:pressed{\n"
"    background-color: #ff8c00;\n"
"}")
        self.Cap_expand_butt.setCheckable(True)
        self.Cap_expand_butt.setObjectName("Cap_expand_butt")
        self.tabWidget.addTab(self.CapacitiveLoads, "")
        self.ExtraControls = QtWidgets.QWidget()
        self.ExtraControls.setObjectName("ExtraControls")
        self.tabWidget.addTab(self.ExtraControls, "")
        LoadBanksWindow.setCentralWidget(self.centralwidget)

        # --------Menu bar--------------------------------
        # create the menu bar on main window
        self.menubar = QtWidgets.QMenuBar(LoadBanksWindow)

        # set menubar size
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1388, 26))

        # set object name
        self.menubar.setObjectName("menubar")

        # Create the first entry namely "File" and place it on menubar and set object name
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        # create the sub-entry under File
        self.menuLabs = QtWidgets.QMenu(self.menuFile)
        self.menuLabs.setObjectName("menuLabs")

        # Create second entry of menubar
        self.menuRemotee_Load_Boxes = QtWidgets.QMenu(self.menubar)
        self.menuRemotee_Load_Boxes.setObjectName("menuRemotee_Load_Boxes")

        # Create third entry of the menubar and set its object name
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        # Place the menubar on LoadBanksWindow
        LoadBanksWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(LoadBanksWindow)
        self.statusbar.setObjectName("statusbar")
        LoadBanksWindow.setStatusBar(self.statusbar)
        self.actionDemo = QtWidgets.QAction(LoadBanksWindow)
        self.actionDemo.setObjectName("actionDemo")
        self.actionLab_1 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLab_1.setObjectName("actionLab_1")
        self.actionLab_2 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLab_2.setObjectName("actionLab_2")
        self.actionLab_3 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLab_3.setObjectName("actionLab_3")
        self.actionLab_4 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLab_4.setObjectName("actionLab_4")
        self.actionLab_5 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLab_5.setObjectName("actionLab_5")
        self.actionLab_6 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLab_6.setObjectName("actionLab_6")
        self.actionLab_7 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLab_7.setObjectName("actionLab_7")
        self.actionLab_8 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLab_8.setObjectName("actionLab_8")
        self.actionDemo_2 = QtWidgets.QAction(LoadBanksWindow)
        self.actionDemo_2.setObjectName("actionDemo_2")
        self.actionLoadBox001 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLoadBox001.setObjectName("actionLoadBox001")
        self.actionLoadBox002 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLoadBox002.setObjectName("actionLoadBox002")
        self.actionLoadBox003 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLoadBox003.setObjectName("actionLoadBox003")
        self.actionLoadBox004 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLoadBox004.setObjectName("actionLoadBox004")
        self.actionLoadBox005 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLoadBox005.setObjectName("actionLoadBox005")
        self.actionLoadBox006 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLoadBox006.setObjectName("actionLoadBox006")
        self.actionLoadBox007 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLoadBox007.setObjectName("actionLoadBox007")
        self.actionLoadBox008 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLoadBox008.setObjectName("actionLoadBox008")
        self.actionLoadBox009 = QtWidgets.QAction(LoadBanksWindow)
        self.actionLoadBox009.setObjectName("actionLoadBox009")
        self.actionAttribution_Page = QtWidgets.QAction(LoadBanksWindow)
        self.actionAttribution_Page.setObjectName("actionAttribution_Page")
        self.menuLabs.addAction(self.actionLab_1)
        self.menuLabs.addAction(self.actionLab_2)
        self.menuLabs.addAction(self.actionLab_3)
        self.menuLabs.addAction(self.actionLab_4)
        self.menuLabs.addAction(self.actionLab_5)
        self.menuLabs.addAction(self.actionLab_6)
        self.menuLabs.addAction(self.actionLab_7)
        self.menuLabs.addAction(self.actionLab_8)
        self.menuFile.addAction(self.menuLabs.menuAction())
        self.menuFile.addAction(self.actionDemo_2)
        self.menuRemotee_Load_Boxes.addAction(self.actionLoadBox001)
        self.menuRemotee_Load_Boxes.addAction(self.actionLoadBox002)
        self.menuRemotee_Load_Boxes.addAction(self.actionLoadBox003)
        self.menuRemotee_Load_Boxes.addAction(self.actionLoadBox004)
        self.menuRemotee_Load_Boxes.addAction(self.actionLoadBox005)
        self.menuRemotee_Load_Boxes.addAction(self.actionLoadBox006)
        self.menuAbout.addAction(self.actionAttribution_Page)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRemotee_Load_Boxes.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(LoadBanksWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(LoadBanksWindow)

        #self.statusBar().showMessage('Message in statusbar.')

        # TODO Replace this function with the function to turn ON all inductive relays.
        # OFF_all_Relays()

        # comment out this line to avoid output on terminal
        # print('All inductive loads off')

        # -------------------------------------------PART 2 to Update QLabels ( V,I etc readings)-------------------------------------------
        # after 1 second (1000 milliseconds), call self.updateLabel. This is a trigger that gets current value of QLabes
        # from the updateLabel function
        QtCore.QTimer.singleShot(1000, lambda: self.updateLabel(self.Pa_live_label_left_ResLoad,
                                                                self.Va_live_label_left_ResLoad,
                                                                self.Pa_live_label_middle_ResLoad,
                                                                self.Va_live_label_middle_ResLoad,
                                                                self.Pa_live_label_right_ResLoad,
                                                                self.Va_live_label_right_ResLoad,
                                                                self.Pa_live_label_left_IndLoad,
                                                                self.Va_live_label_left_IndLoad,
                                                                self.Pa_live_label_middle_IndLoad,
                                                                self.Va_live_label_middle_IndLoad,
                                                                self.Pa_live_label_right_IndLoad,
                                                                self.Va_live_label_right_IndLoad,
                                                                self.Pa_live_label_left_CapLoad,
                                                                self.Va_live_label_left_CapLoad,
                                                                self.Pa_live_label_middle_CapLoad,
                                                                self.Va_live_label_middle_CapLoad,
                                                                self.Pa_live_label_right_CapLoad,
                                                                self.Va_live_label_right_CapLoad))
        # ---------------------------------------------------------------------------------------------------------------



    def updateLabel(self, Present_mag_Pa_left_Rload, Present_mag_Va_left_Rload,
                    Present_mag_Pa_middle_Rload, Present_mag_Va_middle_Rload,
                    Present_mag_Pa_right_Rload, Present_mag_Va_right_Rload,

                    Present_mag_Pa_left_Indload, Present_mag_Va_left_Indload,
                    Present_mag_Pa_middle_Indload, Present_mag_Va_middle_Indload,
                    Present_mag_Pa_right_Indload, Present_mag_Va_right_Indload,

                    Present_mag_Pa_left_Capload, Present_mag_Va_left_Capload,
                    Present_mag_Pa_middle_Capload, Present_mag_Va_middle_Capload,
                    Present_mag_Pa_right_Capload, Present_mag_Va_right_Capload):

        # -------------------Resistive Loads
        Pa_live_label_left_ResLoad = Pa_live_label_middle_ResLoad = Pa_live_label_right_ResLoad = random.gauss(1200.0, 2.0)

        # Here we define a thread

        #worker = Worker()
        #self.start(worker)
        #read = str()
        #self.Readings = GetReadingsThread(read)
        #self.Readings.start()

        Va_live_label_left_ResLoad = Va_live_label_middle_ResLoad = Va_live_label_right_ResLoad = random.gauss(120.0,
                                                                                                               2.0)
        # -------------------Resistive Loads----------------------
        new_mag_Pa_left_ResLoad = float('%.1f' % Pa_live_label_left_ResLoad)
        new_mag_Pa_middle_ResLoad = float('%.1f' % Pa_live_label_middle_ResLoad)
        new_mag_Pa_right_ResLoad = float('%.1f' % Pa_live_label_right_ResLoad)

        new_mag_Va_left = float('%.1f' % Va_live_label_left_ResLoad)
        new_mag_Va_middle = float('%.1f' % Va_live_label_middle_ResLoad)
        new_mag_Va_right = float('%.1f' % Va_live_label_right_ResLoad)

        Present_mag_Pa_left_Rload.setText(str(new_mag_Pa_left_ResLoad))
        Present_mag_Pa_middle_Rload.setText(str(new_mag_Pa_middle_ResLoad))
        Present_mag_Pa_right_Rload.setText(str(new_mag_Pa_right_ResLoad))

        Present_mag_Va_left_Rload.setText(str(new_mag_Va_left))
        Present_mag_Va_middle_Rload.setText(str(new_mag_Va_middle))
        Present_mag_Va_right_Rload.setText(str(new_mag_Va_right))



        # ----------------Induction Loads--------------------
        Pa_live_label_left_IndLoad = Pa_live_label_middle_IndLoad = Pa_live_label_right_IndLoad = random.gauss(1200.0,
                                                                                                               2.0)
        Va_live_label_left_IndLoad = Va_live_label_middle_IndLoad = Va_live_label_right_IndLoad = random.gauss(120.0,
                                                                                                               2.0)
        new_mag_Pa_left_IndLoad = float('%.1f' % Pa_live_label_left_IndLoad)
        new_mag_Pa_middle_IndLoad = float('%.1f' % Pa_live_label_middle_IndLoad)
        new_mag_Pa_right_IndLoad = float('%.1f' % Pa_live_label_right_IndLoad)

        new_mag_Va_left_IndLoad = float('%.1f' % Va_live_label_left_IndLoad)
        new_mag_Va_middle_IndLoad = float('%.1f' % Va_live_label_middle_IndLoad)
        new_mag_Va_right_IndLoad = float('%.1f' % Va_live_label_right_IndLoad)

        Present_mag_Pa_left_Indload.setText(str(new_mag_Pa_left_IndLoad))
        Present_mag_Pa_middle_Indload.setText(str(new_mag_Pa_middle_IndLoad))
        Present_mag_Pa_right_Indload.setText(str(new_mag_Pa_right_IndLoad))

        Present_mag_Va_left_Indload.setText(str(new_mag_Va_left_IndLoad))
        Present_mag_Va_middle_Indload.setText(str(new_mag_Va_middle_IndLoad))
        Present_mag_Va_right_Indload.setText(str(new_mag_Va_right_IndLoad))

        # -----------------Capacitive Loads -----------------------
        Pa_live_label_left_CapLoad = Pa_live_label_middle_CapLoad = Pa_live_label_right_CapLoad = random.gauss(1200.0,
                                                                                                               2.0)
        Va_live_label_left_CapLoad = Va_live_label_middle_CapLoad = Va_live_label_right_CapLoad = random.gauss(120.0,
                                                                                                               2.0)

        new_mag_Pa_left_CapLoad = float('%.1f' % Pa_live_label_left_CapLoad)
        new_mag_Pa_middle_CapLoad = float('%.1f' % Pa_live_label_middle_CapLoad)
        new_mag_Pa_right_CapLoad = float('%.1f' % Pa_live_label_right_CapLoad)

        new_mag_Va_left_CapLoad = float('%.1f' % Va_live_label_left_CapLoad)
        new_mag_Va_middle_CapLoad = float('%.1f' % Va_live_label_middle_CapLoad)
        new_mag_Va_right_CapLoad = float('%.1f' % Va_live_label_right_CapLoad)

        Present_mag_Pa_left_Capload.setText(str(new_mag_Pa_left_CapLoad))
        Present_mag_Pa_middle_Capload.setText(str(new_mag_Pa_middle_CapLoad))
        Present_mag_Pa_right_Capload.setText(str(new_mag_Pa_right_CapLoad))

        Present_mag_Va_left_Capload.setText(str(new_mag_Va_left_CapLoad))
        Present_mag_Va_middle_Capload.setText(str(new_mag_Va_middle_CapLoad))
        Present_mag_Va_right_Capload.setText(str(new_mag_Va_right_CapLoad))

        QtCore.QTimer.singleShot(1000, lambda: self.updateLabel(Present_mag_Pa_left_Rload,
                                                                Present_mag_Va_left_Rload,
                                                                Present_mag_Pa_middle_Rload,
                                                                Present_mag_Va_middle_Rload,
                                                                Present_mag_Pa_right_Rload,
                                                                Present_mag_Va_right_Rload,
                                                                Present_mag_Pa_left_Indload,
                                                                Present_mag_Va_left_Indload,
                                                                Present_mag_Pa_middle_Indload,
                                                                Present_mag_Va_middle_Indload,
                                                                Present_mag_Pa_right_Indload,
                                                                Present_mag_Va_right_Indload,
                                                                Present_mag_Pa_left_Capload,
                                                                Present_mag_Va_left_Capload,
                                                                Present_mag_Pa_middle_Capload,
                                                                Present_mag_Va_middle_Capload,
                                                                Present_mag_Pa_right_Capload,
                                                                Present_mag_Va_right_Capload))


        """These functions receive the signal from the load bank buttons."""


    def btn_r1(self):
        read = str()
        self.Readings = GetReadingsThread(read)
        self.Readings.start()
        print(self.Readings)
        # if self.btnR1.isChecked():
        #         command = 'Set Open 1 ACK'
        #         #print('R1 in load bank On')
        #         # ON_Relay0()
        # else:
        #         command = 'Set Close 1 ACK'
        #
        #         # OFF_Relay0()
        #         #print('R1 in load bank Off')
        # err = SetCMD(command, device_ip, name)
        # count = 0
        # while err:
        #         err = SetCMD(command, device_ip, name)
        #         count = count + 1
        #         if count == 10:
        #                 err = False

    def btn_r2(self):
        if self.btnR2.isChecked():
                command = 'Set Open 2 ACK'
                print('R2 in load bank is On')
                # ON_Relay1()
        else:
                command = 'Set Close 2 ACK'
                print('R2 in load bank is off')
                # OFF_Relay1()
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
                # ON_Relay2()
        else:
                command = 'Set Close 3 ACK'
                print('R3 in load bank is off')
                # OFF_Relay2()
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
                # ON_Relay3()
        else:
                command = 'Set Close 4 ACK'
                print('R3 in load bank is off')
                # OFF_Relay3()
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
                # ON_Relay4()
        else:
                command = 'Set Close 5 ACK'
                print('R4 in load bank is On')
                # OFF_Relay4()
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
                # ON_Relay5()
        else:
                command = 'Set Close 6 ACK'
                print('R5 in load bank is On')
                # OFF_Relay5()
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
                # ON_Relay6()
        else:
                command = 'Set Close 7 ACK'
                print('R6 in load bank is On')
                # OFF_Relay6()
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
                # print('R7 in load bank pressed')
                # ON_Relay7()
        else:
                command = 'Set Close 8 ACK'
                # print('R7 in load bank is On')
                # OFF_Relay7()
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
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                print('R8 in load bank is On')
                # OFF_Relay8()
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

        # ON_all_Relays()

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

        # OFF_all_Relays()

    # Inductive loads buttons

    # TODO Add inductive and capacitive button actions.
    def btn_L1(self):
        if self.btnL1.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('L1 in load bank pressed')

    def btn_L2(self):
        if self.btnL2.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('L2 in load bank pressed')

    def btn_L3(self):
        if self.btnL3.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('L3 in load bank pressed')

    def btn_L4(self):
        if self.btnL4.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('L4 in load bank pressed')

    def btn_L5(self):
        if self.btnL5.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('L5 in load bank pressed')

    def btn_L6(self):
        if self.btnL6.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('L6 in load bank pressed')

    def btn_L7(self):
        if self.btnL7.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('L7 in load bank pressed')

    def btn_L8(self):
        if self.btnL8.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('L8 in load bank pressed')

    def btn_L9(self):
        if self.btnL9.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('L9 in load bank pressed')

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

        # TODO Replace this function with the function to turn ON all inductive relays.
        # ON_all_Relays()

        # comment out this line to avoid output on terminal
        # print('All inductive loads on')

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
        # OFF_all_Relays()

        # comment out this line to avoid output on terminal
        print('All inductive loads off')

    # All cap buttons

    def btn_c1(self):
        if self.btnC1.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('c1 in load bank pressed')

    def btn_c2(self):
        if self.btnC2.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('c2 in load bank pressed')

    def btn_c3(self):
        if self.btnC3.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('c3 in load bank pressed')

    def btn_c4(self):
        if self.btnC4.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('c4 in load bank pressed')

    def btn_c5(self):
        if self.btnC5.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('c5 in load bank pressed')

    def btn_c6(self):
        if self.btnC6.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('c6 in load bank pressed')

    def btn_c7(self):
        if self.btnC7.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('c7 in load bank pressed')

    def btn_c8(self):
        if self.btnC8.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('c8 in load bank pressed')

    def btn_c9(self):
        if self.btnC9.isChecked():
                command = 'Set Open 1 ACK'
                # print('L1 in load bank pressed')
                # ON_Relay8()
        else:
                command = 'Set Close 9 ACK'
                # print('L1 in load bank is On')
                # OFF_Relay8()
        err = SetCMD(command, device_ip, name)
        count = 0
        while err:
                err = SetCMD(command, device_ip, name)
                count = count + 1
                if count == 10:
                        err = False
        # print('c9 in load bank pressed')

    def all_on_cap(self):
        """ This function turns all buttons to ON but it will not do anything else
        we need to call the function that is actually gonna do something. """
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



    def retranslateUi(self, LoadBanksWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadBanksWindow.setWindowTitle(_translate("LoadBanksWindow", "Load Boxes Window"))
        self.btnR1.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnR2.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnR3.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnR4.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnR5.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnR6.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnR7.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnR8.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnR9.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnAllOn_R.setText(_translate("LoadBanksWindow", "All On"))
        self.btnAllOff_R.setText(_translate("LoadBanksWindow", "All Off"))
        self.Pa_label_left_ResLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Va_label_left_ResLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Pa_live_label_left_ResLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Va_live_label_left_ResLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Pa_label_middle_ResLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Va_label_middle_ResLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Pa_live_label_middle_ResLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Va_live_label_middle_ResLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Pa_label_right_ResLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Va_label_right_ResLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Pa_live_label_right_ResLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Va_live_label_right_ResLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Res_right_expand_butt.setToolTip(_translate("LoadBanksWindow", "<html><head/><body><p>Opens a window with data from all 3 phases.</p></body></html>"))
        self.Res_right_expand_butt.setText(_translate("LoadBanksWindow", "Expand"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ResistiveLoads), _translate("LoadBanksWindow", "ResistiveLoads"))
        self.btnL1.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnL2.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnL3.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnL4.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnL5.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnL6.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnL7.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnL8.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnL9.setText(_translate("LoadBanksWindow", "On|Off"))
        self.Pa_label_middle_IndLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Va_label_middle_IndLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Pa_live_label_middle_IndLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Va_live_label_middle_IndLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.btnAllOn_L.setText(_translate("LoadBanksWindow", "All On"))
        self.btnAllOff_L.setText(_translate("LoadBanksWindow", "All Off"))
        self.Ind_left_expand_butt.setToolTip(_translate("LoadBanksWindow", "<html><head/><body><p>Opens a window with data from all 3 phases.</p></body></html>"))
        self.Ind_left_expand_butt.setText(_translate("LoadBanksWindow", "Expand"))
        self.Pa_label_left_IndLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Va_label_left_IndLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Pa_live_label_left_IndLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Va_live_label_left_IndLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Pa_label_right_IndLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Va_label_right_IndLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Pa_live_label_right_IndLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Va_live_label_right_IndLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InductiveLoads), _translate("LoadBanksWindow", "Inductive Loads"))
        self.btnC1.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnC2.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnC3.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnC4.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnC5.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnC6.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnC7.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnC8.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnC9.setText(_translate("LoadBanksWindow", "On|Off"))
        self.btnAllOn_C.setText(_translate("LoadBanksWindow", "All On"))
        self.btnAllOff_C.setText(_translate("LoadBanksWindow", "All Off"))
        self.Pa_label_left_CapLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Va_label_left_CapLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Pa_live_label_left_CapLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Va_live_label_left_CapLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Pa_label_middle_CapLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Va_label_middle_CapLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Pa_live_label_middle_CapLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Va_live_label_middle_CapLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Pa_label_right_CapLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Va_label_right_CapLoad.setText(_translate("LoadBanksWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">A</span> =</p></body></html>"))
        self.Pa_live_label_right_CapLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Va_live_label_right_CapLoad.setText(_translate("LoadBanksWindow", " 000.0 "))
        self.Cap_expand_butt.setToolTip(_translate("LoadBanksWindow", "<html><head/><body><p>Opens a window with data from all 3 phases.</p></body></html>"))
        self.Cap_expand_butt.setText(_translate("LoadBanksWindow", "Expand"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CapacitiveLoads), _translate("LoadBanksWindow", "Capacitive Loads"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ExtraControls), _translate("LoadBanksWindow", "Extra Controls"))
        self.menuFile.setTitle(_translate("LoadBanksWindow", "File"))
        self.menuLabs.setTitle(_translate("LoadBanksWindow", "Loadable Labs"))
        self.menuRemotee_Load_Boxes.setTitle(_translate("LoadBanksWindow", "Remote Load Boxes"))
        self.menuAbout.setTitle(_translate("LoadBanksWindow", "About"))
        self.actionDemo.setText(_translate("LoadBanksWindow", "Demo"))
        self.actionLab_1.setText(_translate("LoadBanksWindow", "Lab 1"))
        self.actionLab_2.setText(_translate("LoadBanksWindow", "Lab 2"))
        self.actionLab_3.setText(_translate("LoadBanksWindow", "Lab 3"))
        self.actionLab_4.setText(_translate("LoadBanksWindow", "Lab 4"))
        self.actionLab_5.setText(_translate("LoadBanksWindow", "Lab 5"))
        self.actionLab_6.setText(_translate("LoadBanksWindow", "Lab 6"))
        self.actionLab_7.setText(_translate("LoadBanksWindow", "Lab 7"))
        self.actionLab_8.setText(_translate("LoadBanksWindow", "Lab 8"))
        self.actionDemo_2.setText(_translate("LoadBanksWindow", "Demo"))
        self.actionLoadBox001.setText(_translate("LoadBanksWindow", "LoadBox001"))
        self.actionLoadBox002.setText(_translate("LoadBanksWindow", "LoadBox002"))
        self.actionLoadBox003.setText(_translate("LoadBanksWindow", "LoadBox003"))
        self.actionLoadBox004.setText(_translate("LoadBanksWindow", "LoadBox004"))
        self.actionLoadBox005.setText(_translate("LoadBanksWindow", "LoadBox005"))
        self.actionLoadBox006.setText(_translate("LoadBanksWindow", "LoadBox006"))
        self.actionLoadBox007.setText(_translate("LoadBanksWindow", "LoadBox007"))
        self.actionLoadBox008.setText(_translate("LoadBanksWindow", "LoadBox008"))
        self.actionLoadBox009.setText(_translate("LoadBanksWindow", "LoadBox009"))
        self.actionAttribution_Page.setText(_translate("LoadBanksWindow", "Attribution Page"))

import resources_rc


if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoadBanksWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



