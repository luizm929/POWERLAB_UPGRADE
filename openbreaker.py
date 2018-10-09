# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 255)
        self.open_breaker = QtWidgets.QLabel(Dialog)
        self.open_breaker.setGeometry(QtCore.QRect(30, 50, 431, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.open_breaker.setFont(font)
        self.open_breaker.setObjectName("open_breaker")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(110, 190, 248, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes_btn = QtWidgets.QPushButton(self.widget)
        self.yes_btn.setObjectName("yes_btn")
        self.horizontalLayout.addWidget(self.yes_btn)
        self.no_btn = QtWidgets.QPushButton(self.widget)
        self.no_btn.setObjectName("no_btn")
        self.horizontalLayout.addWidget(self.no_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.open_breaker.setText(_translate("Dialog", "Are you sure you want to open this breaker?"))
        self.yes_btn.setText(_translate("Dialog", "Yes"))
        self.no_btn.setText(_translate("Dialog", "No"))

