# -*- coding: utf-8 -*-

# Form2 implementation generated from reading ui file 'Enter_stock.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(591, 680)
        self.pushButton = QtWidgets.QPushButton(Form2)
        self.pushButton.setGeometry(QtCore.QRect(30, 590, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form2)
        self.label.setGeometry(QtCore.QRect(50, 420, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form2)
        self.label_2.setGeometry(QtCore.QRect(50, 490, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form2)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, 490, 341, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(Form2)
        self.label_3.setGeometry(QtCore.QRect(100, 420, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.tableView = QtWidgets.QTableView(Form2)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 571, 401))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "登入庫存"))
        self.pushButton.setText(_translate("Form2", "確定"))
        self.label.setText(_translate("Form2", "品項:"))
        self.label_2.setText(_translate("Form2", "數量:"))
