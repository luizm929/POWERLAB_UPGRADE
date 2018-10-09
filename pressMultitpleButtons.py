#from PyQt5.QtCore import SIGNAL
##from PyQt5.QtGui import QApplication, QLabel, QWidget
##from PyQt5.QtGui import QPushButton, QVBoxLayout

#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtGui import QPixmap

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QMessageBox, QWidget, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)
########################################################################
class MultiButtonDemo(QWidget):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(MultiButtonDemo, self).__init__()

        layout = QVBoxLayout()

        self.label = QLabel("You haven't pressed a button!")
        layout.addWidget(self.label)
        labels = ["One", "Two", "Three", "Four"]
        for label in labels:
            btn = QPushButton(label)
            btn.clicked.connect(self.clicked)
            layout.addWidget(btn)

        self.setLayout(layout)

        self.setWindowTitle("PySide Signals / Slots Demo")

    # ----------------------------------------------------------------------
    def clicked(self):
        """
        Change label based on what button was pressed
        """
        button = self.sender()
        if isinstance(button, QPushButton):
            self.label.setText("You pressed %s!" % button.text())


# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication([])
    form = MultiButtonDemo()
    form.show()
    app.exec_()