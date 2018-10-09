import random, sys, traceback, socket, time, sched
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon, QPicture, QStandardItemModel
from PyQt5.QtWidgets import QAction, qApp, QApplication, QTableWidgetItem
from PyQt5.QtCore import (QObject, QRunnable,QProcess, QThread, QThreadPool, pyqtSignal)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QMessageBox, QWidget, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QToolButton, QTableWidget)
import os

''' This is a test to spawn qprocesses everytime commj(not included in this repository) tries to make a connection 
    to a node. '''

class runcommands(QWidget):
    def __init__(self, parent=None):
        super(runcommands, self).__init__(parent)

        layout = QFormLayout()
        self.commandlist = QComboBox()
        self.param = QLineEdit()
        self.runit = QToolButton()
        self.runit.setText('run')
        self.runit.clicked.connect(self.runcommand)
        self.commandlist.addItems(['simplerun.py', 'simplerun2.py'])
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.model = QStandardItemModel()
        self.table.setHorizontalHeaderLabels(['Process', 'Parameter', 'STDOut', 'Status', 'Kill'])
        self.rowcount = 0

        layout.addRow(self.commandlist)
        layout.addRow(self.param)
        layout.addRow(self.runit)

        layout.addRow(self.table)

        self.setLayout(layout)
        self.setWindowTitle("Run & Monitor")
        #self.commandrunning="0"
        self.mylistofprocesses=[]



    def runcommand(self):
        # add a record in the QTableWidget
        # updating its row number at each run
        self.rowcount = self.rowcount + 1
        self.table.setRowCount(self.rowcount)

        # add column 0: command string
        self.c1 = QTableWidgetItem()
        self.c1.setText("%s" % os.path.join(os.getcwd(), self.commandlist.currentText()))
        self.table.setItem(self.rowcount - 1, 0, self.c1)

        # add column 1: parameter string
        self.c2 = QTableWidgetItem()
        self.c2.setText("%s" % self.param.text())
        self.table.setItem(self.rowcount - 1, 1, self.c2)

        # add column 2 to store the  Process StandardOutput
        stdout_item = QTableWidgetItem()
        self.table.setItem(self.rowcount - 1, 2, stdout_item)

        # add column 3: index to store the process status (0: Not Running, 1: Starting, 2: Running)
        status_item = QTableWidgetItem()
        self.table.setItem(self.rowcount - 1, 3, status_item)

        # add column 4: kill button to kill the relative process
        killbtn = QPushButton(self.table)
        killbtn.setText('Kill')
        self.table.setCellWidget(self.rowcount - 1, 4, killbtn)

        # Initiate a QProcess running a system command
        process = QtCore.QProcess()
        command = 'python' + ' ' + os.getcwd() + '/' + self.commandlist.currentText() + ' ' + self.param.text()
        process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        # connect the stdout_item to the Process StandardOutput
        # it gets constantly update as the process emit std output
        process.readyReadStandardOutput.connect(lambda: stdout_item.setText(str(process.readAllStandardOutput().data().decode('utf-8'))))
        # start the process
        process.start(command)

        # # this was supposed to add the process status in the relative column ... BUT it DOESN'T do it
        status_item.setText(str(process.ProcessState()))
        # # connect the kill button to the process.kill method, to stop the process
        killbtn.clicked.connect(process.kill)
        killbtn.clicked.connect(lambda: killbtn.setText('Killed'))
        # # this was supposed to 'UPDATE' the process status (from running to stoppted) in the relative column ... BUT it DOESN'T do it
        killbtn.clicked.connect(lambda: status_item.setText(str(process.ProcessState())))
        # append the process to a list so that it doesn't get destroyed at each run
        self.mylistofprocesses.append(process)

        status = {QProcess.Starting: "Starting",
                    QProcess.Running: "Running",
                  QProcess.NotRunning: "Not Running"}

        print(status)
        process.stateChanged.connect(lambda state: status_item.setText(status[state]))



def main():
    app = QApplication(sys.argv)
    ex = runcommands()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()