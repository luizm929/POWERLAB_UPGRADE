# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(577, 204)
        Dialog.setMaximumSize(QtCore.QSize(577, 204))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 160, 571, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        #School's Logo
        self.label_Logo = QtWidgets.QLabel(Dialog)
        self.label_Logo.setGeometry(QtCore.QRect(10, 20, 141, 151))
        #Next lines fix the logo not showing up on a Qlabel
        NMSU_logo_pix = QPixmap('img/NM_State_University_logo.png')
        self.label_Logo.setScaledContents(True)
        self.label_Logo.setPixmap(NMSU_logo_pix)


        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 80, 291, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 121, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Access"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.label_3.setText(_translate("Dialog", "Max Length: 20 char"))

import resources_rc
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PasswordDialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(PasswordDialog)
    PasswordDialog.show()
    sys.exit(app.exec_())

