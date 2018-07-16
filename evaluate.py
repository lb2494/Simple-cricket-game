# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EvaluateWindow(object):
    def setupUi(self, EvaluateWindow):
        EvaluateWindow.setObjectName("EvaluateWindow")
        EvaluateWindow.resize(699, 509)
        self.centralwidget = QtWidgets.QWidget(EvaluateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 180, 521, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.listView_2 = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.listView_2.setObjectName("listView_2")
        self.horizontalLayout.addWidget(self.listView_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 110, 501, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Players = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Players.setFont(font)
        self.Players.setAlignment(QtCore.Qt.AlignCenter)
        self.Players.setIndent(10)
        self.Players.setObjectName("Players")
        self.horizontalLayout_2.addWidget(self.Players)
        self.Points = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Points.setFont(font)
        self.Points.setAlignment(QtCore.Qt.AlignCenter)
        self.Points.setIndent(10)
        self.Points.setObjectName("Points")
        self.horizontalLayout_2.addWidget(self.Points)
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(300, 440, 93, 28))
        self.Calculate.setObjectName("Calculate")
        self.SelectTeam = QtWidgets.QComboBox(self.centralwidget)
        self.SelectTeam.setGeometry(QtCore.QRect(150, 50, 141, 22))
        self.SelectTeam.setObjectName("SelectTeam")
        self.Selectmatch = QtWidgets.QComboBox(self.centralwidget)
        self.Selectmatch.setGeometry(QtCore.QRect(400, 50, 141, 22))
        self.Selectmatch.setObjectName("Selectmatch")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 80, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        EvaluateWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EvaluateWindow)
        self.statusbar.setObjectName("statusbar")
        EvaluateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EvaluateWindow)
        QtCore.QMetaObject.connectSlotsByName(EvaluateWindow)

    def retranslateUi(self, EvaluateWindow):
        _translate = QtCore.QCoreApplication.translate
        EvaluateWindow.setWindowTitle(_translate("EvaluateWindow", "MainWindow"))
        self.Players.setText(_translate("EvaluateWindow", "Players"))
        self.Points.setText(_translate("EvaluateWindow", "Points"))
        self.Calculate.setText(_translate("EvaluateWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvaluateWindow = QtWidgets.QMainWindow()
    ui = Ui_EvaluateWindow()
    ui.setupUi(EvaluateWindow)
    EvaluateWindow.show()
    sys.exit(app.exec_())

