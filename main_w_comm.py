#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# #----------------------------------------------------------------------------------------
# Software Written for the NMSU ECE department
# Written by Luis Martinez : luizmartines@gmail.com
#                          : luizm929@nmsu.edu
#
#----------------------------------------------------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QMessageBox, QWidget, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)
import serial

# Mac serial port
#ser = serial.Serial('/dev/cu.usbserial-AI05B96M', 9600)
# Windows serial port
#ser = serial.Serial('COM3', 9600)
# Linux Serial port
#ser = serial.Serial('/dev/tty0', 9600)

############################ Open/Close Prompt Breaker 1 #############################
class WindowA1(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Ace 1", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerA1)
        self.button2.clicked.connect(self.CloseBreakerA1)
        self.button3.clicked.connect(self.StatusA1)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerA1(self):
        self.parent().brkr1_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening A1')
        ser.write('on,1;'.encode())
        self.close()

    def CloseBreakerA1(self):
        print('Closing A1')
        ser.write('off,1;'.encode())
        self.parent().brkr1_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()

    def StatusA1(self):
        print('Status A1')
        stA1 = ser.write('st,1;'.encode().strip())
        st_A1 = ser.readline(stA1).strip()
        print(st_A1.decode())


##############################################################################################
############################ Open/Close Prompt Breaker 2 #############################
class WindowA2(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("Ace 2", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerA2)
        self.button2.clicked.connect(self.CloseBreakerA2)
        self.button3.clicked.connect(self.StatusA2)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerA2(self):
        self.parent().brkr2_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening A2')
        ser.write('on,2;'.encode())
        self.close()

    def CloseBreakerA2(self):
        ser.write('off,2;'.encode())
        self.parent().brkr2_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing A2')

    def StatusA2(self):
        print('Status A2')
        stA2 = ser.write('st,2;'.encode().strip())
        st_A2 = ser.readline(stA2).strip()
        print(st_A2)


##############################################################################################
############################ Open/Close Prompt Breaker 3 #############################
class WindowA3(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Ace 3", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerA3)
        self.button2.clicked.connect(self.CloseBreakerA3)
        self.button3.clicked.connect(self.StatusA3)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerA3(self):
        self.parent().brkr3_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening A3')
        ser.write('on,3;'.encode())
        self.close()

    def CloseBreakerA3(self):
        self.parent().brkr3_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing A3')
        ser.write('off,3;'.encode())

    def StatusA3(self):
        print('Status A3')
        stA3 = ser.write('st,3;'.encode().strip())
        st_A3 = ser.readline(stA3).strip()
        print(st_A3)


##############################################################################################
############################ Open/Close Prompt Breaker 4 #############################
class WindowA4(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Ace 4", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerA4)
        self.button2.clicked.connect(self.CloseBreakerA4)
        self.button3.clicked.connect(self.StatusA4)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerA4(self):
        self.parent().brkr4_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening A4')
        ser.write('on,4'.encode())
        self.close()

    def CloseBreakerA4(self):
        self.parent().brkr4_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        ser.write('off,4'.encode())
        self.close()
        print('Closing A4')

    def StatusA4(self):
        print('Status A4')
        stA4 = ser.write('st,4'.encode().strip())
        st_A4 = ser.readline(stA4).strip()
        print(st_A4)


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowA5(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Ace 5", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerA5)
        self.button2.clicked.connect(self.CloseBreakerA5)
        self.button3.clicked.connect(self.StatusA5)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerA5(self):
        self.parent().mother_ace.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening A5')
        ser.write('on,5'.encode())
        self.close()

    def CloseBreakerA5(self):
        print('Closing A5')
        ser.write('off,5'.encode())
        self.parent().mother_ace.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()

    def StatusA5(self):
        print('Status A5')
        stA5 = ser.write('st,5'.encode().strip())
        st_A5 = ser.readline(stA5).strip()
        print(st_A5)


##############################################################################################



############################ Open/Close Prompt Breaker 1 #############################
class WindowJ1(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Joker 1", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerJ1)
        self.button2.clicked.connect(self.CloseBreakerJ1)
        self.button3.clicked.connect(self.StatusJ1)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerJ1(self):
        self.parent().brkr1_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening J1')
        # ser.write('on,;'.encode())
        self.close()

    def CloseBreakerJ1(self):
        # ser.write('off,;'.encode())
        self.parent().brkr1_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing J1')

    def StatusJ1(self):
        print('Status J1')
        # stJ1=ser.write('st,;'.encode().strip())
        # st_J1=ser.readline(stJ1).strip()
        print(st_J1)


##############################################################################################
############################ Open/Close Prompt Breaker 2 #############################
class WindowJ2(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("Joker 2", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerJ2)
        self.button2.clicked.connect(self.CloseBreakerJ2)
        self.button3.clicked.connect(self.StatusJ2)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerJ2(self):
        self.parent().brkr2_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening J2')
        self.close()

    def CloseBreakerJ2(self):
        self.parent().brkr2_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing J2')

    def StatusJ2(self):
        print('Status J2')


##############################################################################################
############################ Open/Close Prompt Breaker 3 #############################
class WindowJ3(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Joker 3", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerJ3)
        self.button2.clicked.connect(self.CloseBreakerJ3)
        self.button3.clicked.connect(self.StatusJ3)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerJ3(self):
        self.parent().brkr3_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening J3')
        self.close()

    def CloseBreakerJ3(self):
        self.parent().brkr3_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing J3')

    def StatusJ3(self):
        print('Status J3')


##############################################################################################
############################ Open/Close Prompt Breaker 4 #############################
class WindowJ4(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Joker 4", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerJ4)
        self.button2.clicked.connect(self.CloseBreakerJ4)
        self.button3.clicked.connect(self.StatusJ4)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerJ4(self):
        self.parent().brkr4_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening J4')
        self.close()

    def CloseBreakerJ4(self):
        self.parent().brkr4_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing J4')

    def StatusJ4(self):
        print('Status J4')


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowJ5(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Joker 5", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerJ5)
        self.button2.clicked.connect(self.CloseBreakerJ5)
        self.button3.clicked.connect(self.StatusJ5)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerJ5(self):
        self.parent().mother_joker.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening J5')
        self.close()

    def CloseBreakerJ5(self):
        self.parent().mother_joker.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing J5')

    def StatusJ5(self):
        print('Status J5')


##############################################################################################




############################ Open/Close Prompt Breaker 1 #############################
class WindowP1(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Poker 1", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerP1)
        self.button2.clicked.connect(self.CloseBreakerP1)
        self.button3.clicked.connect(self.StatusP1)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerP1(self):
        self.parent().brkr1_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening P1')
        self.close()

    def CloseBreakerP1(self):
        self.parent().brkr1_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing P1')

    def StatusP1(self):
        print('Status P1')


##############################################################################################
############################ Open/Close Prompt Breaker 2 #############################
class WindowP2(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("Poker 2", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerP2)
        self.button2.clicked.connect(self.CloseBreakerP2)
        self.button3.clicked.connect(self.StatusP2)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerP2(self):
        self.parent().brkr2_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening P2')
        self.close()

    def CloseBreakerP2(self):
        self.parent().brkr2_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing P2')

    def StatusP2(self):
        print('Status P2')


##############################################################################################
############################ Open/Close Prompt Breaker 3 #############################
class WindowP3(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Poker 3", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerP3)
        self.button2.clicked.connect(self.CloseBreakerP3)
        self.button3.clicked.connect(self.StatusP3)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerP3(self):
        self.parent().brkr3_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening P3')
        self.close()

    def CloseBreakerP3(self):
        self.parent().brkr3_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing P3')

    def StatusP3(self):
        print('status P3')


##############################################################################################
############################ Open/Close Prompt Breaker 4 #############################
class WindowP4(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Poker 4", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerP4)
        self.button2.clicked.connect(self.CloseBreakerP4)
        self.button3.clicked.connect(self.StatusP4)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerP4(self):
        self.parent().brkr4_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening P4')
        self.close()

    def CloseBreakerP4(self):
        self.parent().brkr4_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing P4')

    def StatusP4(self):
        print('Status P4')


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowP5(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Poker 5", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerP5)
        self.button2.clicked.connect(self.CloseBreakerP5)
        self.button3.clicked.connect(self.StatusP5)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerP5(self):
        self.parent().mother_poker.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening P5')
        self.close()

    def CloseBreakerP5(self):
        self.parent().mother_poker.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing P5')

    def StatusP5(self):
        print('Status P5')


##############################################################################################




############################ Open/Close Prompt Breaker 1 #############################
class WindowK1(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("King 1", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerK1)
        self.button2.clicked.connect(self.CloseBreakerK1)
        self.button3.clicked.connect(self.StatusK1)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerK1(self):
        self.parent().brkr1_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening K1')
        ser.write('on,6'.encode())
        self.close()

    def CloseBreakerK1(self):
        self.parent().brkr1_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing K1')
        ser.write('off,6'.encode())

    def StatusK1(self):
        print('Status K1')
        stK1 = ser.write('st,6'.encode().strip())
        st_K1 = ser.readline(stK1).strip()
        print(st_K1)


##############################################################################################
############################ Open/Close Prompt Breaker 2 #############################
class WindowK2(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("King 2", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerK2)
        self.button2.clicked.connect(self.CloseBreakerK2)
        self.button3.clicked.connect(self.StatusK2)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerK2(self):
        self.parent().brkr2_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening K2')
        ser.write('on,7'.encode())
        self.close()

    def CloseBreakerK2(self):
        self.parent().brkr2_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,7'.encode())
        print('Closing K2')

    def StatusK2(self):
        print('Status K2')
        stK2 = ser.write('st,7'.encode().strip())
        st_K2 = ser.readline(stK2).strip()
        print(st_K2)


##############################################################################################
############################ Open/Close Prompt Breaker 3 #############################
class WindowK3(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("King 3", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerK3)
        self.button2.clicked.connect(self.CloseBreakerK3)
        self.button3.clicked.connect(self.StatusK3)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerK3(self):
        self.parent().brkr3_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening K3')
        self.close()
        ser.write('on,8'.encode())

    def CloseBreakerK3(self):
        self.parent().brkr3_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,8'.encode())
        print('Closing K3')

    def StatusK3(self):
        print('Status K3')
        stK3 = ser.write('st,8'.encode().strip())
        st_K3 = ser.readline(stK3).strip()
        print(st_K3)


##############################################################################################
############################ Open/Close Prompt Breaker 4 #############################
class WindowK4(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("King 4", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerK4)
        self.button2.clicked.connect(self.CloseBreakerK4)
        self.button3.clicked.connect(self.StatusK4)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerK4(self):
        self.parent().brkr4_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening K4')
        ser.write('on,9'.encode())
        self.close()

    def CloseBreakerK4(self):
        self.parent().brkr4_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,9'.encode())
        print('Closing K4')

    def StatusK4(self):
        print('Status K4')
        stK4 = ser.write('st,9'.encode().strip())
        st_K4 = ser.readline(stK4).encode()
        print(st_k4)


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowK5(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("King Breaker", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerK5)
        self.button2.clicked.connect(self.CloseBreakerK5)
        self.button3.clicked.connect(self.StatusK5)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerK5(self):
        self.parent().mother_king.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening K5')
        ser.write('on,10;'.encode())
        self.close()

    def CloseBreakerK5(self):
        self.parent().mother_king.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,10;'.encode())
        print('Closing K5')

    def StatusK5(self):
        print('Status K5')
        stK5 = ser.write('st,10;'.encode().strip())
        st_K5 = ser.readline(stK5).encode()
        print(st_K5)


##############################################################################################




############################ Open/Close Prompt Breaker 1 #############################
class WindowQ1(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Queen 1", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerQ1)
        self.button2.clicked.connect(self.CloseBreakerQ1)
        self.button3.clicked.connect(self.StatusQ1)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerQ1(self):
        self.parent().brkr1_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening Q1')
        ser.write('on,6'.encode())
        self.close()

    def CloseBreakerQ1(self):
        self.parent().brkr1_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,6'.encode())
        print('Closing Q1')

    def StatusQ1(self):
        print('Status Q1')
        stQ1 = ser.write('st,6'.encode().strip())
        st_Q1 = ser.readline(stQ1).strip()
        print(st_Q1.decode())


##############################################################################################
############################ Open/Close Prompt Breaker 2 #############################
class WindowQ2(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("Queen 2", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerQ2)
        self.button2.clicked.connect(self.CloseBreakerQ2)
        self.button3.clicked.connect(self.StatusQ2)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerQ2(self):
        self.parent().brkr2_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening Q2')
        ser.write('on,7'.encode())
        self.close()

    def CloseBreakerQ2(self):
        self.parent().brkr2_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,7'.encode())
        print('Closing Q2')

    def StatusQ2(self):
        print('Status Q2')
        stQ2 = ser.write('st,7'.encode().strip())
        st_Q2 = ser.readline(stQ2).strip()
        print(st_Q2.decode())


##############################################################################################
############################ Open/Close Prompt Breaker 3 #############################
class WindowQ3(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Queen 3", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerQ3)
        self.button2.clicked.connect(self.CloseBreakerQ3)
        self.button3.clicked.connect(self.StatusQ3)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerQ3(self):
        self.parent().brkr3_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening Q3')
        ser.write('on,8'.encode())
        self.close()

    def CloseBreakerQ3(self):
        self.parent().brkr3_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,8'.encode())
        print('Closing Q3')

    def StatusQ3(self):
        print('Status Q3')
        stQ3 = ser.write('st,8'.encode().strip())
        st_Q3 = ser.readline(stQ3).strip()
        print(st_Q3.decode().strip())


##############################################################################################
############################ Open/Close Prompt Breaker 4 #############################
class WindowQ4(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Queen 4", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerQ4)
        self.button2.clicked.connect(self.CloseBreakerQ4)
        self.button3.clicked.connect(self.StatusQ4)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerQ4(self):
        self.parent().brkr4_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening Q4')
        ser.write('on,9'.encode())
        self.close()

    def CloseBreakerQ4(self):
        self.parent().brkr4_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,9'.encode())
        print('Closing Q4')

    def StatusQ4(self):
        print('Status Q4')
        stQ4 = ser.write('st,9'.encode().strip())
        st_Q4 = ser.readline(stQ4).strip()
        print(st_Q4.decode().strip())


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowQ5(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Queen 5", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerQ5)
        self.button2.clicked.connect(self.CloseBreakerQ5)
        self.button3.clicked.connect(self.StatusQ5)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerQ5(self):
        self.parent().mother_queen.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening Q5')
        ser.write('on,10'.encode())
        self.close()

    def CloseBreakerQ5(self):
        self.parent().mother_queen.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,10'.encode())
        print('Closing Q5')

    def StatusQ5(self):
        print('Status Q5')
        stQ5 = ser.write('st,10'.encode().strip())
        st_Q5 = ser.readline(stQ5).strip()
        print(st_Q5.decode().strip())


##############################################################################################



############################ Open/Close Prompt Breaker 1 #############################
class WindowD1(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Deuce 1", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerD1)
        self.button2.clicked.connect(self.CloseBreakerD1)
        self.button3.clicked.connect(self.StatusD1)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerD1(self):
        self.parent().brkr1_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        ser.write('on,1;'.encode())
        print('Opening D1')
        self.close()

    def CloseBreakerD1(self):
        self.parent().brkr1_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        ser.write('off,1'.encode())
        self.close()
        print('Closing D1')

    def StatusD1(self):
        print('Status D1')
        stD1 = ser.write('st,1'.encode().strip())
        st_D1 = ser.readline(stD1).strip()
        print(st_D1.decode())


##############################################################################################
############################ Open/Close Prompt Breaker 2 #############################
class WindowD2(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("Deuce 2", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerD2)
        self.button2.clicked.connect(self.CloseBreakerD2)
        self.button3.clicked.connect(self.StatusD2)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerD2(self):
        self.parent().brkr2_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening D2')
        ser.write('on,2;'.encode())
        self.close()

    def CloseBreakerD2(self):
        self.parent().brkr2_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        ser.write('off,2;'.encode())
        self.close()
        print('Closing D2')

    def StatusD2(self):
        print('Stauts D2')
        stD2 = ser.write('st,2'.encode().strip())
        st_D2 = ser.readline(stD2).strip()
        print(st_D2.decode())


##############################################################################################
############################ Open/Close Prompt Breaker 3 #############################
class WindowD3(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Deuce 3", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerD3)
        self.button2.clicked.connect(self.CloseBreakerD3)
        self.button3.clicked.connect(self.StatusD3)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerD3(self):
        self.parent().brkr3_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening D3')
        ser.write('on,3'.encode())
        self.close()

    def CloseBreakerD3(self):
        self.parent().brkr3_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,3'.encode())
        print('Closing D3')

    def StatusD3(self):
        print('Stauts D3')
        stD3 = ser.write('st,3'.encode().strip())
        st_D3 = ser.readline(stD3).strip()
        print(st_D3.decode())


##############################################################################################
############################ Open/Close Prompt Breaker 4 #############################
class WindowD4(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Deuce 4", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerD4)
        self.button2.clicked.connect(self.CloseBreakerD4)
        self.button3.clicked.connect(self.StatusD4)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerD4(self):
        self.parent().brkr4_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening D4')
        ser.write('on,4'.encode())
        self.close()

    def CloseBreakerD4(self):
        self.parent().brkr4_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        ser.write('off,4')
        self.close()
        print('Closing D4')

    def StatusD4(self):
        print('Status D4')
        stD4 = ser.write('st,4'.encode().strip())
        st_D4 = ser.readline(stD4).strip()
        print(st_D4.decode())


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowD5(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Deuce 5", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerD5)
        self.button2.clicked.connect(self.CloseBreakerD5)
        self.button3.clicked.connect(self.StatusD5)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerD5(self):
        self.parent().mother_deuce.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening D5')
        ser.write('on,5'.encode())
        self.close()

    def CloseBreakerD5(self):
        self.parent().mother_deuce.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        ser.write('off,5'.encode())
        print('Closing D5')

    def StatusD5(self):
        print('Status D5')
        stD5 = ser.write('st,5'.encode().strip())
        st_D5 = ser.readline(stD5).strip()
        print(st_D5.decode())


##############################################################################################
############################ Open/Close Prompt Breaker 1 #############################
class WindowS1(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Solar 1", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerS1)
        self.button2.clicked.connect(self.CloseBreakerS1)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerS1(self):
        self.parent().brkr1_S.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening S1')
        self.close()

    def CloseBreakerS1(self):
        self.parent().brkr1_S.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing S1')


##############################################################################################
############################ Open/Close Prompt Breaker 2 #############################
class WindowS2(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("Solar 2", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerS2)
        self.button2.clicked.connect(self.CloseBreakerS2)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerS2(self):
        self.parent().mother_solar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  S2')
        self.close()

    def CloseBreakerS2(self):
        self.parent().mother_solar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing S2')


##############################################################################################


############################ Open/Close Prompt ATL #############################
class WindowATL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Transmission Line A", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerATL)
        self.button2.clicked.connect(self.CloseBreakerATL)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerATL(self):
        self.parent().A_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening ATL')
        self.close()

    def CloseBreakerATL(self):
        self.parent().A_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Closing ATL')
        self.close()


##############################################################################################
############################ Open/Close Prompt Breaker 2 #############################
class WindowBTL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("Transmission Line B", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.button3 = QPushButton("Status", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 2, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerBTL)
        self.button2.clicked.connect(self.CloseBreakerBTL)
        self.button3.clicked.connect(self.StatusBTL)
        ######################################################
        # OpenBreaker is where you will communicate with arduino

    def OpenBreakerBTL(self):
        self.parent().B_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  BTL')
        self.close()

    def CloseBreakerBTL(self):
        self.parent().B_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing BTL')

    def StatusBTL(self):
        print('Status BTL')


##############################################################################################
############################ Open/Close Prompt Breaker 3 #############################
class WindowCTL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Transmission Line C", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerCTL)
        self.button2.clicked.connect(self.CloseBreakerCTL)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerCTL(self):
        self.parent().C_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  CTL')
        self.close()

    def CloseBreakerCTL(self):
        self.parent().C_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing CTL')


##############################################################################################
############################ Open/Close Prompt Breaker 4 #############################
class WindowDTL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Transmission Line D", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerDTL)
        self.button2.clicked.connect(self.CloseBreakerDTL)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerDTL(self):
        self.parent().D_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  DTL')
        self.close()

    def CloseBreakerDTL(self):
        self.parent().D_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing DTL')


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowETL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Transmission Line E", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerETL)
        self.button2.clicked.connect(self.CloseBreakerETL)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerETL(self):
        self.parent().E_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  ETL')
        self.close()

    def CloseBreakerETL(self):
        self.parent().E_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing ETL')


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowFTL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Transmission Line F", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerFTL)
        self.button2.clicked.connect(self.CloseBreakerFTL)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerFTL(self):
        self.parent().F_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  FTL')
        self.close()

    def CloseBreakerFTL(self):
        self.parent().F_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing FTL')


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowGTL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Transmission Line G", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerGTL)
        self.button2.clicked.connect(self.CloseBreakerGTL)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerGTL(self):
        self.parent().G_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  GTL')
        self.close()

    def CloseBreakerGTL(self):
        self.parent().G_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing GTL')


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowHTL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Transmission Line H", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerHTL)
        self.button2.clicked.connect(self.CloseBreakerHTL)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerHTL(self):
        self.parent().H_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  HTL')
        self.close()

    def CloseBreakerHTL(self):
        self.parent().H_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing HTL')


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowITL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Transmission Line I", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerITL)
        self.button2.clicked.connect(self.CloseBreakerITL)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerITL(self):
        self.parent().I_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  ITL')
        self.close()

    def CloseBreakerITL(self):
        self.parent().I_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing ITL')


##############################################################################################
############################ Open/Close Prompt Breaker 5 #############################
class WindowJTL(QDialog):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.
        self.label = QLabel("Transmission Line J", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button = QPushButton("Open", self)
        self.button2 = QPushButton("Close", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.button2, 1, 1)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Power Lab 4.0")
        self.setLayout(self.layout)
        self.show()
        ################# Button Events #################
        self.button.clicked.connect(self.OpenBreakerJTL)
        self.button2.clicked.connect(self.CloseBreakerJTL)
        ######################################################

    # OpenBreaker is where you will communicate with arduino
    def OpenBreakerJTL(self):
        self.parent().J_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(0, 100, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        print('Opening  JTL')
        self.close()

    def CloseBreakerJTL(self):
        self.parent().J_TL.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close()
        print('Closing JTL')


##############################################################################################





class Ui_MainWindow(QWidget):
    ################ Solar #############
    def clickS1(self):
        if not hasattr(self, 'dialogS1'):
            self.dialogS1 = WindowS1(self)
        self.dialogS1.show()
        print("S1 Clicked")

    def clickS2(self):
        if not hasattr(self, 'dialogS2'):
            self.dialogS2 = WindowS2(self)
        self.dialogS2.show()
        print("S2 Clicked")

    ################ Ace ###############
    def clickA1(self):
        if not hasattr(self, 'dialogA1'):
            self.dialogA1 = WindowA1(self)
        self.dialogA1.show()
        print("A1 Clicked")

    def clickA2(self):
        if not hasattr(self, 'dialogA2'):
            self.dialogA2 = WindowA2(self)
        self.dialogA2.show()
        print("A2 Clicked")

    def clickA3(self):
        if not hasattr(self, 'dialogA3'):
            self.dialogA3 = WindowA3(self)
        self.dialogA3.show()
        print("A3 Clicked")

    def clickA4(self):
        if not hasattr(self, 'dialogA4'):
            self.dialogA4 = WindowA4(self)
        self.dialogA4.show()
        print("A4 Clicked")

    def clickA5(self):
        if not hasattr(self, 'dialogA5'):
            self.dialogA5 = WindowA5(self)
        self.dialogA5.show()
        print("A5 Clicked")

    ################Joker ###############
    def clickJ1(self):
        if not hasattr(self, 'dialogJ1'):
            self.dialogJ1 = WindowJ1(self)
        self.dialogJ1.show()
        print("J1 Clicked")

    def clickJ2(self):
        if not hasattr(self, 'dialogJ2'):
            self.dialogJ2 = WindowJ2(self)
        self.dialogJ2.show()
        print("J2 Clicked")

    def clickJ3(self):
        if not hasattr(self, 'dialogJ3'):
            self.dialogJ3 = WindowJ3(self)
        self.dialogJ3.show()
        print("J3 Clicked")

    def clickJ4(self):
        if not hasattr(self, 'dialogJ4'):
            self.dialogJ4 = WindowJ4(self)
        self.dialogJ4.show()
        print("J4 Clicked")

    def clickJ5(self):
        if not hasattr(self, 'dialogJ5'):
            self.dialogJ5 = WindowJ5(self)
        self.dialogJ5.show()
        print("J5 Clicked")

    ################Poker ###############
    def clickP1(self):
        if not hasattr(self, 'dialogP1'):
            self.dialogP1 = WindowP1(self)
        self.dialogP1.show()
        print("P1 Clicked")

    def clickP2(self):
        if not hasattr(self, 'dialogP2'):
            self.dialogP2 = WindowP2(self)
        self.dialogP2.show()
        print("P2 Clicked")

    def clickP3(self):
        if not hasattr(self, 'dialogP3'):
            self.dialogP3 = WindowP3(self)
        self.dialogP3.show()
        print("P3 Clicked")

    def clickP4(self):
        if not hasattr(self, 'dialogP4'):
            self.dialogP4 = WindowP4(self)
        self.dialogP4.show()
        print("P4 Clicked")

    def clickP5(self):
        if not hasattr(self, 'dialogP5'):
            self.dialogP5 = WindowP5(self)
        self.dialogP5.show()
        print("P5 Clicked")

    ################King ###############
    def clickK1(self):
        if not hasattr(self, 'dialogK1'):
            self.dialogK1 = WindowK1(self)
        self.dialogK1.show()
        print("K1 Clicked")

    def clickK2(self):
        if not hasattr(self, 'dialogK2'):
            self.dialogK2 = WindowK2(self)
        self.dialogK2.show()
        print("K2 Clicked")

    def clickK3(self):
        if not hasattr(self, 'dialogK3'):
            self.dialogK3 = WindowK3(self)
        self.dialogK3.show()
        print("K3 Clicked")

    def clickK4(self):
        if not hasattr(self, 'dialogK4'):
            self.dialogK4 = WindowK4(self)
        self.dialogK4.show()
        print("K4 Clicked")

    def clickK5(self):
        if not hasattr(self, 'dialogK5'):
            self.dialogK5 = WindowK5(self)
        self.dialogK5.show()
        print("K5 Clicked")

    ################ Queen ###############
    def clickQ1(self):
        if not hasattr(self, 'dialogQ1'):
            self.dialogQ1 = WindowQ1(self)
        self.dialogQ1.show()
        print("Q1 Clicked")

    def clickQ2(self):
        if not hasattr(self, 'dialogQ2'):
            self.dialogQ2 = WindowQ2(self)
        self.dialogQ2.show()
        print("Q2 Clicked")

    def clickQ3(self):
        if not hasattr(self, 'dialogQ3'):
            self.dialogQ3 = WindowQ3(self)
        self.dialogQ3.show()
        print("Q3 Clicked")

    def clickQ4(self):
        if not hasattr(self, 'dialogQ4'):
            self.dialogQ4 = WindowQ4(self)
        self.dialogQ4.show()
        print("Q4 Clicked")

    def clickQ5(self):
        if not hasattr(self, 'dialogQ5'):
            self.dialogQ5 = WindowQ5(self)
        self.dialogQ5.show()
        print("Q5 Clicked")

    ################## Deuce #################
    def clickD1(self):
        if not hasattr(self, 'dialogD1'):
            self.dialogD1 = WindowD1(self)
        self.dialogD1.show()
        print("D1 Clicked")

    def clickD2(self):
        if not hasattr(self, 'dialogD2'):
            self.dialogD2 = WindowD2(self)
        self.dialogD2.show()
        print("D2 Clicked")

    def clickD3(self):
        if not hasattr(self, 'dialoD3'):
            self.dialogD3 = WindowD3(self)
        self.dialogD3.show()
        print("D3 Clicked")

    def clickD4(self):
        if not hasattr(self, 'dialogD4'):
            self.dialogD4 = WindowD4(self)
        self.dialogD4.show()
        print("D4 Clicked")

    def clickD5(self):
        if not hasattr(self, 'dialogQ5'):
            self.dialogD5 = WindowD5(self)
        self.dialogD5.show()
        print("D5 Clicked")

    ########### Transmission Lines #################
    def ATL(self):
        if not hasattr(self, 'dialogATL'):
            self.dialogATL = WindowATL(self)
        self.dialogATL.show()
        print("ATL Clicked")

    def BTL(self):
        if not hasattr(self, 'dialogBTL'):
            self.dialogBTL = WindowBTL(self)
        self.dialogBTL.show()
        print("BTL Clicked")

    def CTL(self):
        if not hasattr(self, 'dialogCTL'):
            self.dialogCTL = WindowCTL(self)
        self.dialogCTL.show()
        print("CTL Clicked")

    def DTL(self):
        if not hasattr(self, 'dialogDTL'):
            self.dialogDTL = WindowDTL(self)
        self.dialogDTL.show()
        print("DTL Clicked")

    def ETL(self):
        if not hasattr(self, 'dialogETL'):
            self.dialogETL = WindowETL(self)
        self.dialogETL.show()
        print("ETL Clicked")

    def FTL(self):
        if not hasattr(self, 'dialogFTL'):
            self.dialogFTL = WindowFTL(self)
        self.dialogFTL.show()
        print("FTL Clicked")

    def GTL(self):
        if not hasattr(self, 'dialogGTL'):
            self.dialogGTL = WindowGTL(self)
        self.dialogGTL.show()
        print("GTL Clicked")

    def HTL(self):
        if not hasattr(self, 'dialogHTL'):
            self.dialogHTL = WindowHTL(self)
        self.dialogHTL.show()
        print("HTL Clicked")

    def ITL(self):
        if not hasattr(self, 'dialogITL'):
            self.dialogITL = WindowITL(self)
        self.dialogITL.show()
        print("ITL Clicked")

    def JTL(self):
        if not hasattr(self, 'dialogJTL'):
            self.dialogJTL = WindowJTL(self)
        self.dialogJTL.show()
        print("JTL Clicked")

    #######################################################
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1300, 700)
        MainWindow.showMaximized()
        MainWindow.setMinimumSize(QtCore.QSize(1300, 900))
        #MainWindow.setMaximumSize(QtCore.QSize(1300, 700))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(128, 128, 128);")
        # self.logo = Qt
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.brkr3_A = QtWidgets.QPushButton(self.centralwidget)
        self.brkr3_A.setGeometry(QtCore.QRect(160, 110, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr3_A.setFont(font)
        self.brkr3_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr3_A.setObjectName("brkr3_A")
        ############ Button Event ##############
        self.brkr3_A.clicked.connect(self.clickA3)
        ########################################
        self.brkr2_A = QtWidgets.QPushButton(self.centralwidget)
        self.brkr2_A.setGeometry(QtCore.QRect(80, 110, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr2_A.setFont(font)
        self.brkr2_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr2_A.setObjectName("brkr2_A")
        ############ Button Event ##############
        self.brkr2_A.clicked.connect(self.clickA2)
        ########################################
        self.brkr1_A = QtWidgets.QPushButton(self.centralwidget)
        self.brkr1_A.setGeometry(QtCore.QRect(120, 70, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr1_A.setFont(font)
        self.brkr1_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr1_A.setObjectName("brkr1_A")
        ############ Button Event ##############
        self.brkr1_A.clicked.connect(self.clickA1)
        ########################################
        self.brkr4_A = QtWidgets.QPushButton(self.centralwidget)
        self.brkr4_A.setGeometry(QtCore.QRect(120, 150, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr4_A.setFont(font)
        self.brkr4_A.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr4_A.setObjectName("brkr4_A")
        ############ Button Event ##############
        self.brkr4_A.clicked.connect(self.clickA4)
        ########################################
        self.mother_ace = QtWidgets.QPushButton(self.centralwidget)
        self.mother_ace.setGeometry(QtCore.QRect(30, 30, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.mother_ace.setFont(font)
        self.mother_ace.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mother_ace.setObjectName("mother_ace")
        ############ Button Event ##############
        self.mother_ace.clicked.connect(self.clickA5)
        ########################################
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(100, 170, 81, 3))
        self.line_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "selection-color: rgb(255, 0, 0);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(170, 90, 20, 81))
        self.line_4.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "selection-color: rgb(255, 0, 0);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(100, 80, 81, 16))
        self.line_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "selection-color: rgb(255, 0, 0);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(90, 90, 20, 81))
        self.line_5.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "selection-color: rgb(255, 0, 0);")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.brkr2_K = QtWidgets.QPushButton(self.centralwidget)
        self.brkr2_K.setGeometry(QtCore.QRect(80, 430, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr2_K.setFont(font)
        self.brkr2_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr2_K.setObjectName("brkr2_K")
        ############ Button Event ##############
        self.brkr2_K.clicked.connect(self.clickK2)
        ########################################
        self.mother_king = QtWidgets.QPushButton(self.centralwidget)
        self.mother_king.setGeometry(QtCore.QRect(30, 500, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.mother_king.setFont(font)
        self.mother_king.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mother_king.setObjectName("mother_king")
        ############ Button Event ##############
        self.mother_king.clicked.connect(self.clickK5)
        ########################################
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(170, 410, 20, 81))
        self.line_6.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "selection-color: rgb(255, 0, 0);")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(100, 410, 81, 3))
        self.line_7.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "selection-color: rgb(255, 0, 0);")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(100, 490, 81, 3))
        self.line_8.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "selection-color: rgb(255, 0, 0);")
        self.line_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.brkr4_K = QtWidgets.QPushButton(self.centralwidget)
        self.brkr4_K.setGeometry(QtCore.QRect(120, 470, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr4_K.setFont(font)
        self.brkr4_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr4_K.setObjectName("brkr4_K")
        ################ Button Event ##############
        self.brkr4_K.clicked.connect(self.clickK4)
        ############################################
        self.brkr3_K = QtWidgets.QPushButton(self.centralwidget)
        self.brkr3_K.setGeometry(QtCore.QRect(160, 430, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr3_K.setFont(font)
        self.brkr3_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr3_K.setObjectName("brkr3_K")
        ############ Button Event ##############
        self.brkr3_K.clicked.connect(self.clickK3)
        ########################################
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(90, 410, 20, 81))
        self.line_9.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "selection-color: rgb(255, 0, 0);")
        self.line_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.brkr1_K = QtWidgets.QPushButton(self.centralwidget)
        self.brkr1_K.setGeometry(QtCore.QRect(120, 390, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr1_K.setFont(font)
        self.brkr1_K.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr1_K.setObjectName("brkr1_K")
        ############ Button Event ##############
        self.brkr1_K.clicked.connect(self.clickK1)
        ########################################
        self.brkr2_J = QtWidgets.QPushButton(self.centralwidget)
        self.brkr2_J.setGeometry(QtCore.QRect(230, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr2_J.setFont(font)
        self.brkr2_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr2_J.setObjectName("brkr2_J")
        ############ Button Event ##############
        self.brkr2_J.clicked.connect(self.clickJ2)
        ########################################
        self.mother_joker = QtWidgets.QPushButton(self.centralwidget)
        self.mother_joker.setGeometry(QtCore.QRect(350, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.mother_joker.setFont(font)
        self.mother_joker.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mother_joker.setObjectName("mother_joker")
        ############ Button Event ##############
        self.mother_joker.clicked.connect(self.clickJ5)
        ########################################
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(320, 190, 20, 81))
        self.line_10.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(250, 190, 81, 3))
        self.line_11.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_11.setLineWidth(2)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(250, 270, 81, 3))
        self.line_12.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_12.setLineWidth(2)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.brkr4_J = QtWidgets.QPushButton(self.centralwidget)
        self.brkr4_J.setGeometry(QtCore.QRect(270, 250, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr4_J.setFont(font)
        self.brkr4_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr4_J.setObjectName("brkr4_J")
        ############ Button Event ##############
        self.brkr4_J.clicked.connect(self.clickJ4)
        ########################################
        self.brkr3_J = QtWidgets.QPushButton(self.centralwidget)
        self.brkr3_J.setGeometry(QtCore.QRect(310, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr3_J.setFont(font)
        self.brkr3_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr3_J.setObjectName("brkr3_J")
        ############ Button Event ##############
        self.brkr3_J.clicked.connect(self.clickJ3)
        ########################################
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(240, 190, 20, 81))
        self.line_13.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_13.setLineWidth(2)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setObjectName("line_13")
        self.brkr1_J = QtWidgets.QPushButton(self.centralwidget)
        self.brkr1_J.setGeometry(QtCore.QRect(270, 170, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr1_J.setFont(font)
        self.brkr1_J.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr1_J.setObjectName("brkr1_J")
        ############ Button Event ##############
        self.brkr1_J.clicked.connect(self.clickJ1)
        ########################################
        self.brkr2_D = QtWidgets.QPushButton(self.centralwidget)
        self.brkr2_D.setGeometry(QtCore.QRect(730, 110, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr2_D.setFont(font)
        self.brkr2_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr2_D.setObjectName("brkr2_D")
        ############ Button Event ##############
        self.brkr2_D.clicked.connect(self.clickD2)
        ########################################
        self.mother_deuce = QtWidgets.QPushButton(self.centralwidget)
        self.mother_deuce.setGeometry(QtCore.QRect(840, 30, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.mother_deuce.setFont(font)
        self.mother_deuce.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mother_deuce.setObjectName("mother_deuce")
        ############ Button Event ##############
        self.mother_deuce.clicked.connect(self.clickD5)
        ########################################
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(820, 90, 20, 81))
        self.line_14.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_14.setLineWidth(2)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(750, 90, 81, 3))
        self.line_15.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_15.setLineWidth(2)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(750, 170, 81, 3))
        self.line_16.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_16.setLineWidth(2)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setObjectName("line_16")
        self.brkr4_D = QtWidgets.QPushButton(self.centralwidget)
        self.brkr4_D.setGeometry(QtCore.QRect(770, 150, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr4_D.setFont(font)
        self.brkr4_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr4_D.setObjectName("brkr4_D")
        ############ Button Event ##############
        self.brkr4_D.clicked.connect(self.clickD4)
        ########################################
        self.brkr3_D = QtWidgets.QPushButton(self.centralwidget)
        self.brkr3_D.setGeometry(QtCore.QRect(810, 110, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr3_D.setFont(font)
        self.brkr3_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr3_D.setObjectName("brkr3_D")
        ############ Button Event ##############
        self.brkr3_D.clicked.connect(self.clickD3)
        ########################################
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(740, 90, 20, 81))
        self.line_17.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_17.setLineWidth(2)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setObjectName("line_17")
        self.brkr1_D = QtWidgets.QPushButton(self.centralwidget)
        self.brkr1_D.setGeometry(QtCore.QRect(770, 70, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr1_D.setFont(font)
        self.brkr1_D.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr1_D.setObjectName("brkr1_D")
        ############ Button Event ##############
        self.brkr1_D.clicked.connect(self.clickD1)
        ########################################
        self.brkr2_P = QtWidgets.QPushButton(self.centralwidget)
        self.brkr2_P.setGeometry(QtCore.QRect(590, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr2_P.setFont(font)
        self.brkr2_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr2_P.setObjectName("brkr2_P")
        ############ Button Event ##############
        self.brkr2_P.clicked.connect(self.clickP2)
        ########################################
        self.mother_poker = QtWidgets.QPushButton(self.centralwidget)
        self.mother_poker.setGeometry(QtCore.QRect(550, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.mother_poker.setFont(font)
        self.mother_poker.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mother_poker.setObjectName("mother_poker")
        ############ Button Event ##############
        self.mother_poker.clicked.connect(self.clickP5)
        ########################################
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(680, 190, 20, 81))
        self.line_18.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_18.setLineWidth(2)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(610, 190, 81, 3))
        self.line_19.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_19.setLineWidth(2)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(610, 270, 81, 3))
        self.line_20.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_20.setLineWidth(2)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setObjectName("line_20")
        self.brkr4_P = QtWidgets.QPushButton(self.centralwidget)
        self.brkr4_P.setGeometry(QtCore.QRect(630, 250, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr4_P.setFont(font)
        self.brkr4_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr4_P.setObjectName("brkr4_P")
        ############ Button Event ##############
        self.brkr4_P.clicked.connect(self.clickP4)
        ########################################
        self.brkr3_P = QtWidgets.QPushButton(self.centralwidget)
        self.brkr3_P.setGeometry(QtCore.QRect(670, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr3_P.setFont(font)
        self.brkr3_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr3_P.setObjectName("brkr3_P")
        ############ Button Event ##############
        self.brkr3_P.clicked.connect(self.clickP3)
        ########################################
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setGeometry(QtCore.QRect(600, 190, 20, 81))
        self.line_21.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_21.setLineWidth(2)
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setObjectName("line_21")
        self.brkr1_P = QtWidgets.QPushButton(self.centralwidget)
        self.brkr1_P.setGeometry(QtCore.QRect(630, 170, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr1_P.setFont(font)
        self.brkr1_P.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr1_P.setObjectName("brkr1_P")
        ############ Button Event ##############
        self.brkr1_P.clicked.connect(self.clickP1)
        ########################################
        self.brkr2_Q = QtWidgets.QPushButton(self.centralwidget)
        self.brkr2_Q.setGeometry(QtCore.QRect(730, 430, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr2_Q.setFont(font)
        self.brkr2_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr2_Q.setObjectName("brkr2_Q")
        ############ Button Event ##############
        self.brkr2_Q.clicked.connect(self.clickQ2)
        ########################################
        self.mother_queen = QtWidgets.QPushButton(self.centralwidget)
        self.mother_queen.setGeometry(QtCore.QRect(840, 510, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.mother_queen.setFont(font)
        self.mother_queen.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mother_queen.setObjectName("mother_queen")
        ############ Button Event ##############
        self.mother_queen.clicked.connect(self.clickQ5)
        ########################################
        self.line_22 = QtWidgets.QFrame(self.centralwidget)
        self.line_22.setGeometry(QtCore.QRect(820, 410, 20, 81))
        self.line_22.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_22.setLineWidth(2)
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.centralwidget)
        self.line_23.setGeometry(QtCore.QRect(750, 410, 81, 3))
        self.line_23.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_23.setLineWidth(2)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(self.centralwidget)
        self.line_24.setGeometry(QtCore.QRect(750, 490, 81, 3))
        self.line_24.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_24.setLineWidth(2)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setObjectName("line_24")
        self.brkr4_Q = QtWidgets.QPushButton(self.centralwidget)
        self.brkr4_Q.setGeometry(QtCore.QRect(770, 470, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr4_Q.setFont(font)
        self.brkr4_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr4_Q.setObjectName("brkr4_Q")
        ############ Button Event ##############
        self.brkr4_Q.clicked.connect(self.clickQ4)
        ########################################
        self.brkr3_Q = QtWidgets.QPushButton(self.centralwidget)
        self.brkr3_Q.setGeometry(QtCore.QRect(810, 430, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr3_Q.setFont(font)
        self.brkr3_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr3_Q.setObjectName("brkr3_Q")
        ############ Button Event ##############
        self.brkr3_Q.clicked.connect(self.clickQ3)
        ########################################
        self.line_25 = QtWidgets.QFrame(self.centralwidget)
        self.line_25.setGeometry(QtCore.QRect(740, 410, 20, 81))
        self.line_25.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_25.setLineWidth(2)
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setObjectName("line_25")
        self.brkr1_Q = QtWidgets.QPushButton(self.centralwidget)
        self.brkr1_Q.setGeometry(QtCore.QRect(770, 390, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr1_Q.setFont(font)
        self.brkr1_Q.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr1_Q.setObjectName("brkr1_Q")
        ############ Button Event ##############
        self.brkr1_Q.clicked.connect(self.clickQ1)
        ########################################
        self.mother_solar = QtWidgets.QPushButton(self.centralwidget)
        self.mother_solar.setGeometry(QtCore.QRect(350, 420, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.mother_solar.setFont(font)
        self.mother_solar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mother_solar.setObjectName("mother_solar")
        ############ Button Event ##############
        self.mother_solar.clicked.connect(self.clickS2)
        ########################################
        self.line_26 = QtWidgets.QFrame(self.centralwidget)
        self.line_26.setGeometry(QtCore.QRect(500, 340, 20, 81))
        self.line_26.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_26.setLineWidth(2)
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.centralwidget)
        self.line_27.setGeometry(QtCore.QRect(430, 340, 81, 3))
        self.line_27.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_27.setLineWidth(2)
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.centralwidget)
        self.line_28.setGeometry(QtCore.QRect(430, 420, 81, 3))
        self.line_28.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_28.setLineWidth(2)
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setObjectName("line_28")
        self.line_29 = QtWidgets.QFrame(self.centralwidget)
        self.line_29.setGeometry(QtCore.QRect(420, 340, 20, 81))
        self.line_29.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_29.setLineWidth(2)
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setObjectName("line_29")
        self.brkr1_S = QtWidgets.QPushButton(self.centralwidget)
        self.brkr1_S.setGeometry(QtCore.QRect(450, 320, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.brkr1_S.setFont(font)
        self.brkr1_S.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.brkr1_S.setObjectName("brkr1_S")
        ############ Button Event ##############
        self.brkr1_S.clicked.connect(self.clickS1)
        ########################################
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 50, 20, 41))
        self.line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                "selection-color: rgb(255, 0, 0);")
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_30 = QtWidgets.QFrame(self.centralwidget)
        self.line_30.setGeometry(QtCore.QRect(70, 40, 31, 16))
        self.line_30.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_30.setLineWidth(2)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setObjectName("line_30")
        self.line_33 = QtWidgets.QFrame(self.centralwidget)
        self.line_33.setGeometry(QtCore.QRect(90, 490, 16, 41))
        self.line_33.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_33.setLineWidth(2)
        self.line_33.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_33.setObjectName("line_33")
        self.line_34 = QtWidgets.QFrame(self.centralwidget)
        self.line_34.setGeometry(QtCore.QRect(70, 520, 31, 16))
        self.line_34.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_34.setLineWidth(2)
        self.line_34.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_34.setObjectName("line_34")
        self.line_37 = QtWidgets.QFrame(self.centralwidget)
        self.line_37.setGeometry(QtCore.QRect(830, 480, 31, 20))
        self.line_37.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_37.setLineWidth(2)
        self.line_37.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_37.setObjectName("line_37")
        self.line_38 = QtWidgets.QFrame(self.centralwidget)
        self.line_38.setGeometry(QtCore.QRect(850, 490, 20, 21))
        self.line_38.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_38.setLineWidth(2)
        self.line_38.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_38.setObjectName("line_38")
        self.line_39 = QtWidgets.QFrame(self.centralwidget)
        self.line_39.setGeometry(QtCore.QRect(850, 70, 20, 21))
        self.line_39.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_39.setLineWidth(2)
        self.line_39.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_39.setObjectName("line_39")
        self.line_40 = QtWidgets.QFrame(self.centralwidget)
        self.line_40.setGeometry(QtCore.QRect(830, 80, 31, 20))
        self.line_40.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_40.setLineWidth(2)
        self.line_40.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_40.setObjectName("line_40")
        self.c1_line = QtWidgets.QFrame(self.centralwidget)
        self.c1_line.setGeometry(QtCore.QRect(170, 170, 20, 21))
        self.c1_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.c1_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c1_line.setLineWidth(2)
        self.c1_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.c1_line.setObjectName("c1_line")
        self.d2_line = QtWidgets.QFrame(self.centralwidget)
        self.d2_line.setGeometry(QtCore.QRect(680, 170, 20, 21))
        self.d2_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.d2_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d2_line.setLineWidth(2)
        self.d2_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.d2_line.setObjectName("d2_line")
        self.line_45 = QtWidgets.QFrame(self.centralwidget)
        self.line_45.setGeometry(QtCore.QRect(330, 290, 21, 20))
        self.line_45.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_45.setLineWidth(2)
        self.line_45.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_45.setObjectName("line_45")
        self.line_46 = QtWidgets.QFrame(self.centralwidget)
        self.line_46.setGeometry(QtCore.QRect(320, 270, 20, 31))
        self.line_46.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_46.setLineWidth(2)
        self.line_46.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_46.setObjectName("line_46")
        self.line_48 = QtWidgets.QFrame(self.centralwidget)
        self.line_48.setGeometry(QtCore.QRect(590, 290, 21, 20))
        self.line_48.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_48.setLineWidth(2)
        self.line_48.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_48.setObjectName("line_48")
        self.line_49 = QtWidgets.QFrame(self.centralwidget)
        self.line_49.setGeometry(QtCore.QRect(600, 260, 20, 41))
        self.line_49.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_49.setLineWidth(2)
        self.line_49.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_49.setObjectName("line_49")
        self.b1_line = QtWidgets.QFrame(self.centralwidget)
        self.b1_line.setGeometry(QtCore.QRect(320, 260, 110, 20))
        self.b1_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.b1_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.b1_line.setLineWidth(2)
        self.b1_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.b1_line.setObjectName("b1_line")
        self.line_52 = QtWidgets.QFrame(self.centralwidget)
        self.line_52.setGeometry(QtCore.QRect(380, 420, 50, 3))
        self.line_52.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.line_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_52.setLineWidth(2)
        self.line_52.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_52.setObjectName("line_52")
        self.ace_label = QtWidgets.QLabel(self.centralwidget)
        self.ace_label.setGeometry(QtCore.QRect(170, 42, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ace_label.setFont(font)
        self.ace_label.setObjectName("ace_label")
        self.joker_label = QtWidgets.QLabel(self.centralwidget)
        self.joker_label.setGeometry(QtCore.QRect(260, 132, 47, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.joker_label.setFont(font)
        self.joker_label.setObjectName("joker_label")
        self.deuce_label = QtWidgets.QLabel(self.centralwidget)
        self.deuce_label.setGeometry(QtCore.QRect(710, 50, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.deuce_label.setFont(font)
        self.deuce_label.setObjectName("deuce_label")
        self.king_label = QtWidgets.QLabel(self.centralwidget)
        self.king_label.setGeometry(QtCore.QRect(120, 350, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.king_label.setFont(font)
        self.king_label.setObjectName("king_label")
        self.queen_label = QtWidgets.QLabel(self.centralwidget)
        self.queen_label.setGeometry(QtCore.QRect(670, 395, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.queen_label.setFont(font)
        self.queen_label.setObjectName("queen_label")
        self.poker_label = QtWidgets.QLabel(self.centralwidget)
        self.poker_label.setGeometry(QtCore.QRect(590, 143, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.poker_label.setFont(font)
        self.poker_label.setObjectName("poker_label")
        self.solar_label = QtWidgets.QLabel(self.centralwidget)
        self.solar_label.setGeometry(QtCore.QRect(520, 370, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.solar_label.setFont(font)
        self.solar_label.setObjectName("solar_label")
        self.h2_line = QtWidgets.QFrame(self.centralwidget)
        self.h2_line.setGeometry(QtCore.QRect(177, 260, 91, 20))
        self.h2_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.h2_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.h2_line.setLineWidth(2)
        self.h2_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.h2_line.setObjectName("h2_line")
        self.k1_line = QtWidgets.QFrame(self.centralwidget)
        self.k1_line.setGeometry(QtCore.QRect(690, 260, 61, 20))
        self.k1_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "selection-color: rgb(255, 0, 0);")
        self.k1_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.k1_line.setLineWidth(2)
        self.k1_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.k1_line.setObjectName("k1_line")
        self.A_TL = QtWidgets.QPushButton(self.centralwidget)
        self.A_TL.setGeometry(QtCore.QRect(180, 80, 571, 16))
        self.A_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.A_TL.setObjectName("A_TL")
        ############ Button Event ##############
        self.A_TL.clicked.connect(self.ATL)
        ########################################
        self.J_TL = QtWidgets.QPushButton(self.centralwidget)
        self.J_TL.setGeometry(QtCore.QRect(180, 490, 571, 16))
        self.J_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.J_TL.setObjectName("J_TL")
        ############ Button Event ##############
        self.J_TL.clicked.connect(self.JTL)
        ########################################
        self.D_TL = QtWidgets.QPushButton(self.centralwidget)
        self.D_TL.setGeometry(QtCore.QRect(330, 180, 281, 16))
        self.D_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.D_TL.setObjectName("D_TL")
        ############ Button Event ##############
        self.D_TL.clicked.connect(self.DTL)
        ########################################
        self.F_TL = QtWidgets.QPushButton(self.centralwidget)
        self.F_TL.setGeometry(QtCore.QRect(826, 170, 16, 241))
        self.F_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.F_TL.setObjectName("F_TL")
        ############ Button Event ##############
        self.F_TL.clicked.connect(self.FTL)
        ########################################
        self.B_TL = QtWidgets.QPushButton(self.centralwidget)
        self.B_TL.setGeometry(QtCore.QRect(90, 170, 16, 241))
        self.B_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.B_TL.setObjectName("B_TL")
        ############ Button Event ##############
        self.B_TL.clicked.connect(self.BTL)
        ########################################
        self.C_TL = QtWidgets.QPushButton(self.centralwidget)
        self.C_TL.setGeometry(QtCore.QRect(180, 176, 71, 16))
        self.C_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.C_TL.setObjectName("C_TL")
        ############ Button Event ##############
        self.C_TL.clicked.connect(self.CTL)
        ########################################
        self.E_TL = QtWidgets.QPushButton(self.centralwidget)
        self.E_TL.setGeometry(QtCore.QRect(680, 160, 71, 16))
        self.E_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.E_TL.setObjectName("E_TL")
        ############ Button Event ##############
        self.E_TL.clicked.connect(self.ETL)
        ########################################
        self.G_TL = QtWidgets.QPushButton(self.centralwidget)
        self.G_TL.setGeometry(QtCore.QRect(170, 270, 16, 141))
        self.G_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.G_TL.setObjectName("G_TL")
        ############ Button Event ##############
        self.G_TL.clicked.connect(self.GTL)
        ########################################
        self.H_TL = QtWidgets.QPushButton(self.centralwidget)
        self.H_TL.setGeometry(QtCore.QRect(416, 270, 16, 71))
        self.H_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.H_TL.setObjectName("pushButton_9")
        ############ Button Event ##############
        self.H_TL.clicked.connect(self.HTL)
        ########################################
        self.I_TL = QtWidgets.QPushButton(self.centralwidget)
        self.I_TL.setGeometry(QtCore.QRect(740, 270, 16, 141))
        self.I_TL.setStyleSheet("background-color:rgb(170, 0, 0)\n"
                                "")
        self.I_TL.setObjectName("I_TL")
        ############ Button Event ##############
        self.I_TL.clicked.connect(self.ITL)
        ########################################
        self.line_4.raise_()
        self.mother_ace.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_5.raise_()
        self.brkr1_A.raise_()
        self.brkr4_A.raise_()
        self.mother_king.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.brkr4_K.raise_()
        self.line_9.raise_()
        self.brkr1_K.raise_()
        self.mother_joker.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.line_12.raise_()
        self.brkr4_J.raise_()
        self.line_13.raise_()
        self.brkr1_J.raise_()
        self.mother_deuce.raise_()
        self.line_14.raise_()
        self.line_16.raise_()
        self.brkr4_D.raise_()
        self.line_17.raise_()
        self.mother_poker.raise_()
        self.line_18.raise_()
        self.line_21.raise_()
        self.mother_queen.raise_()
        self.line_22.raise_()
        self.line_23.raise_()
        self.line_24.raise_()
        self.brkr4_Q.raise_()
        self.line_25.raise_()
        self.brkr1_Q.raise_()
        self.brkr2_P.raise_()
        self.line_26.raise_()
        self.line_27.raise_()
        self.line_28.raise_()
        self.line_29.raise_()
        self.brkr1_S.raise_()
        self.line.raise_()
        self.line_30.raise_()
        self.line_33.raise_()
        self.line_34.raise_()
        self.line_37.raise_()
        self.line_38.raise_()
        self.line_39.raise_()
        self.line_40.raise_()
        self.c1_line.raise_()
        self.d2_line.raise_()
        self.line_45.raise_()
        self.line_46.raise_()
        self.line_48.raise_()
        self.line_49.raise_()
        self.b1_line.raise_()
        self.line_52.raise_()
        self.mother_solar.raise_()
        self.ace_label.raise_()
        self.joker_label.raise_()
        self.deuce_label.raise_()
        self.king_label.raise_()
        self.queen_label.raise_()
        self.poker_label.raise_()
        self.solar_label.raise_()
        self.h2_line.raise_()
        self.k1_line.raise_()
        self.brkr3_P.raise_()
        self.brkr2_K.raise_()
        self.brkr2_J.raise_()
        self.brkr3_K.raise_()
        self.brkr2_A.raise_()
        self.brkr2_Q.raise_()
        self.brkr3_D.raise_()
        self.brkr2_D.raise_()
        self.brkr3_J.raise_()
        self.brkr3_A.raise_()
        self.brkr3_Q.raise_()
        self.A_TL.raise_()
        self.J_TL.raise_()
        self.D_TL.raise_()
        self.line_19.raise_()
        self.line_20.raise_()
        self.brkr4_P.raise_()
        self.brkr1_P.raise_()
        self.line_15.raise_()
        self.brkr1_D.raise_()
        self.F_TL.raise_()
        self.B_TL.raise_()
        self.C_TL.raise_()
        self.E_TL.raise_()
        self.G_TL.raise_()
        self.H_TL.raise_()
        self.I_TL.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 21))
        self.menubar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.164, y1:0.193636, x2:0.954545, y2:0.937, stop:0.176136 rgba(170, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionGraphs = QtWidgets.QAction(MainWindow)
        self.actionGraphs.setObjectName("actionGraphs")
        self.menuFile.addAction(self.actionSave)
        self.menuView.addAction(self.actionGraphs)
        self.menuAdmin.addAction(self.actionLogin)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Power Lab 4.0"))
        self.brkr3_A.setText(_translate("MainWindow", "3"))
        self.brkr2_A.setText(_translate("MainWindow", "2"))
        self.brkr1_A.setText(_translate("MainWindow", "1"))
        self.brkr4_A.setText(_translate("MainWindow", "4"))
        self.mother_ace.setText(_translate("MainWindow", "5"))
        self.brkr2_K.setText(_translate("MainWindow", "2"))
        self.mother_king.setText(_translate("MainWindow", "5"))
        self.brkr4_K.setText(_translate("MainWindow", "4"))
        self.brkr3_K.setText(_translate("MainWindow", "3"))
        self.brkr1_K.setText(_translate("MainWindow", "1"))
        self.brkr2_J.setText(_translate("MainWindow", "2"))
        self.mother_joker.setText(_translate("MainWindow", "5"))
        self.brkr4_J.setText(_translate("MainWindow", "4"))
        self.brkr3_J.setText(_translate("MainWindow", "3"))
        self.brkr1_J.setText(_translate("MainWindow", "1"))
        self.brkr2_D.setText(_translate("MainWindow", "2"))
        self.mother_deuce.setText(_translate("MainWindow", "5"))
        self.brkr4_D.setText(_translate("MainWindow", "4"))
        self.brkr3_D.setText(_translate("MainWindow", "3"))
        self.brkr1_D.setText(_translate("MainWindow", "1"))
        self.brkr2_P.setText(_translate("MainWindow", "2"))
        self.mother_poker.setText(_translate("MainWindow", "5"))
        self.brkr4_P.setText(_translate("MainWindow", "4"))
        self.brkr3_P.setText(_translate("MainWindow", "3"))
        self.brkr1_P.setText(_translate("MainWindow", "1"))
        self.brkr2_Q.setText(_translate("MainWindow", "2"))
        self.mother_queen.setText(_translate("MainWindow", "5"))
        self.brkr4_Q.setText(_translate("MainWindow", "4"))
        self.brkr3_Q.setText(_translate("MainWindow", "3"))
        self.brkr1_Q.setText(_translate("MainWindow", "1"))
        self.mother_solar.setText(_translate("MainWindow", "2"))
        self.brkr1_S.setText(_translate("MainWindow", "1"))
        self.ace_label.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" color:#ffffff;\">Ace</span></p></body></html>"))
        self.joker_label.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" color:#ffffff;\">Joker</span></p></body></html>"))
        self.deuce_label.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" color:#ffffff;\">Deuce</span></p></body></html>"))
        self.king_label.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" color:#ffffff;\">King</span></p></body></html>"))
        self.queen_label.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" color:#ffffff;\">Queen</span></p></body></html>"))
        self.poker_label.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" color:#ffffff;\">Poker</span></p></body></html>"))
        self.solar_label.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" color:#ffffff;\">Solar</span></p></body></html>"))
        self.A_TL.setText(_translate("MainWindow", "A"))
        self.J_TL.setText(_translate("MainWindow", "J"))
        self.D_TL.setText(_translate("MainWindow", "D"))
        self.F_TL.setText(_translate("MainWindow", "F"))
        self.B_TL.setText(_translate("MainWindow", "B"))
        self.C_TL.setText(_translate("MainWindow", "C"))
        self.E_TL.setText(_translate("MainWindow", "E"))
        self.G_TL.setText(_translate("MainWindow", "G"))
        self.H_TL.setText(_translate("MainWindow", "H"))
        self.I_TL.setText(_translate("MainWindow", "I"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionGraphs.setText(_translate("MainWindow", "Graphs"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
