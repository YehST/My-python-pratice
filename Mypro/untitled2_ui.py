# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untutled2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 598)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.catchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.catchbutton.setGeometry(QtCore.QRect(370, 100, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.catchbutton.setFont(font)
        self.catchbutton.setAutoRepeatDelay(3000)
        self.catchbutton.setAutoRepeatInterval(1000)
        self.catchbutton.setObjectName("catchbutton")
        self.locatebutton = QtWidgets.QPushButton(self.centralwidget)
        self.locatebutton.setGeometry(QtCore.QRect(370, 200, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.locatebutton.setFont(font)
        self.locatebutton.setObjectName("locatebutton")
        self.locate = QtWidgets.QLabel(self.centralwidget)
        self.locate.setGeometry(QtCore.QRect(20, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.locate.setFont(font)
        self.locate.setText("定位座標")
        self.locate.setObjectName("locate")
        self.locate_x_value = QtWidgets.QLabel(self.centralwidget)
        self.locate_x_value.setGeometry(QtCore.QRect(60, 140, 71, 16))
        self.locate_x_value.setObjectName("locate_x_value")
        self.locate_x = QtWidgets.QLabel(self.centralwidget)
        self.locate_x.setGeometry(QtCore.QRect(20, 140, 58, 15))
        self.locate_x.setText("X軸：")
        self.locate_x.setObjectName("locate_x")
        self.locate_y = QtWidgets.QLabel(self.centralwidget)
        self.locate_y.setGeometry(QtCore.QRect(160, 140, 58, 15))
        self.locate_y.setText("Ｙ軸：")
        self.locate_y.setObjectName("locate_y")
        self.locate_y_value = QtWidgets.QLabel(self.centralwidget)
        self.locate_y_value.setGeometry(QtCore.QRect(210, 140, 71, 16))
        self.locate_y_value.setObjectName("locate_y_value")
        self.now = QtWidgets.QLabel(self.centralwidget)
        self.now.setGeometry(QtCore.QRect(20, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.now.setFont(font)
        self.now.setText("當前座標")
        self.now.setObjectName("now")
        self.now_y_value = QtWidgets.QLabel(self.centralwidget)
        self.now_y_value.setGeometry(QtCore.QRect(210, 240, 71, 16))
        self.now_y_value.setObjectName("now_y_value")
        self.now_x_value = QtWidgets.QLabel(self.centralwidget)
        self.now_x_value.setGeometry(QtCore.QRect(60, 240, 71, 16))
        self.now_x_value.setObjectName("now_x_value")
        self.now_x = QtWidgets.QLabel(self.centralwidget)
        self.now_x.setGeometry(QtCore.QRect(20, 240, 58, 15))
        self.now_x.setText("X軸：")
        self.now_x.setObjectName("now_x")
        self.now_y = QtWidgets.QLabel(self.centralwidget)
        self.now_y.setGeometry(QtCore.QRect(160, 240, 58, 15))
        self.now_y.setText("Ｙ軸：")
        self.now_y.setObjectName("now_y")
        self.mistake = QtWidgets.QLabel(self.centralwidget)
        self.mistake.setGeometry(QtCore.QRect(20, 300, 58, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mistake.setFont(font)
        self.mistake.setText("誤差")
        self.mistake.setObjectName("mistake")
        self.mistake_x = QtWidgets.QLabel(self.centralwidget)
        self.mistake_x.setGeometry(QtCore.QRect(20, 340, 58, 15))
        self.mistake_x.setText("X軸：")
        self.mistake_x.setObjectName("mistake_x")
        self.mistake_y_value = QtWidgets.QLabel(self.centralwidget)
        self.mistake_y_value.setGeometry(QtCore.QRect(210, 340, 71, 16))
        self.mistake_y_value.setObjectName("mistake_y_value")
        self.mistake_x_value = QtWidgets.QLabel(self.centralwidget)
        self.mistake_x_value.setGeometry(QtCore.QRect(60, 340, 71, 16))
        self.mistake_x_value.setObjectName("mistake_x_value")
        self.mistake_y = QtWidgets.QLabel(self.centralwidget)
        self.mistake_y.setGeometry(QtCore.QRect(160, 340, 58, 15))
        self.mistake_y.setText("Ｙ軸：")
        self.mistake_y.setObjectName("mistake_y")
        self.servobutton = QtWidgets.QPushButton(self.centralwidget)
        self.servobutton.setGeometry(QtCore.QRect(370, 300, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.servobutton.setFont(font)
        self.servobutton.setObjectName("servobutton")
        self.servo_x_CW = QtWidgets.QPushButton(self.centralwidget)
        self.servo_x_CW.setGeometry(QtCore.QRect(300, 420, 61, 51))
        self.servo_x_CW.setObjectName("servo_x_CW")
        self.servo_y_CW = QtWidgets.QPushButton(self.centralwidget)
        self.servo_y_CW.setGeometry(QtCore.QRect(300, 480, 61, 51))
        self.servo_y_CW.setObjectName("servo_y_CW")
        self.servo_x_CCW = QtWidgets.QPushButton(self.centralwidget)
        self.servo_x_CCW.setGeometry(QtCore.QRect(460, 420, 61, 51))
        self.servo_x_CCW.setObjectName("servo_x_CCW")
        self.servo_y_CCW = QtWidgets.QPushButton(self.centralwidget)
        self.servo_y_CCW.setGeometry(QtCore.QRect(460, 480, 61, 51))
        self.servo_y_CCW.setObjectName("servo_y_CCW")
        self.servo_x_STOP = QtWidgets.QPushButton(self.centralwidget)
        self.servo_x_STOP.setGeometry(QtCore.QRect(380, 420, 61, 51))
        self.servo_x_STOP.setObjectName("servo_x_STOP")
        self.servo_y_STOP = QtWidgets.QPushButton(self.centralwidget)
        self.servo_y_STOP.setGeometry(QtCore.QRect(380, 480, 61, 51))
        self.servo_y_STOP.setObjectName("servo_y_STOP")
        self.AutoMode = QtWidgets.QRadioButton(self.centralwidget)
        self.AutoMode.setGeometry(QtCore.QRect(30, 20, 98, 19))
        self.AutoMode.setObjectName("AutoMode")
        self.ManualMode = QtWidgets.QRadioButton(self.centralwidget)
        self.ManualMode.setGeometry(QtCore.QRect(150, 20, 121, 19))
        self.ManualMode.setObjectName("ManualMode")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 501, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.descriptionlayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.descriptionlayout.setContentsMargins(0, 0, 0, 0)
        self.descriptionlayout.setObjectName("descriptionlayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setObjectName("addWinAction")
        self.menu.addSeparator()
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.catchbutton.setText(_translate("MainWindow", "擷取"))
        self.locatebutton.setText(_translate("MainWindow", "定位"))
        self.locate_x_value.setText(_translate("MainWindow", "TextLabel"))
        self.locate_y_value.setText(_translate("MainWindow", "TextLabel"))
        self.now_y_value.setText(_translate("MainWindow", "TextLabel"))
        self.now_x_value.setText(_translate("MainWindow", "TextLabel"))
        self.mistake_y_value.setText(_translate("MainWindow", "TextLabel"))
        self.mistake_x_value.setText(_translate("MainWindow", "TextLabel"))
        self.servobutton.setText(_translate("MainWindow", "校正"))
        self.servo_x_CW.setText(_translate("MainWindow", "xCW"))
        self.servo_y_CW.setText(_translate("MainWindow", "yCW"))
        self.servo_x_CCW.setText(_translate("MainWindow", "xCCW"))
        self.servo_y_CCW.setText(_translate("MainWindow", "yCCW"))
        self.servo_x_STOP.setText(_translate("MainWindow", "xSTOP"))
        self.servo_y_STOP.setText(_translate("MainWindow", "ySTOP"))
        self.AutoMode.setText(_translate("MainWindow", "AutoMode"))
        self.ManualMode.setText(_translate("MainWindow", "ManualMode"))
        self.menu.setTitle(_translate("MainWindow", "關於"))
        self.addWinAction.setText(_translate("MainWindow", "關於"))
        self.addWinAction.setToolTip(_translate("MainWindow", "關於"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
