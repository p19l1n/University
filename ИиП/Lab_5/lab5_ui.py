# Form implementation generated from reading ui file 'lab5.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modeCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.modeCheckBox.setGeometry(QtCore.QRect(170, 100, 200, 500))
        self.modeCheckBox.setObjectName("modeCheckBox")
        self.modeCheckBox.setStyleSheet("color: blue")
        self.actionButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.actionButton.setGeometry(QtCore.QRect(200, 230, 115, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.actionButton.setFont(font)
        self.actionButton.setAutoFillBackground(False)
        self.actionButton.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.actionButton.setObjectName("actionButton")
        self.sizeSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.sizeSlider.setGeometry(QtCore.QRect(170, 430, 160, 22))
        self.sizeSlider.setMinimum(8)
        self.sizeSlider.setMaximum(16)
        self.sizeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sizeSlider.setObjectName("sizeSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.modeCheckBox.setText(_translate("MainWindow", "РђРєС‚РёРІРЅС‹Р№ СЂРµР¶РёРј"))
        self.actionButton.setText(_translate("MainWindow", "Р–РјРё"))
