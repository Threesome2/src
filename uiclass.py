# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(939, 558)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(90, 350, 75, 41))
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 161, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(270, 10, 648, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 591, 481))
        self.tableView.setObjectName("tableView")
        self.pushButton8 = QtWidgets.QPushButton(self.widget)
        self.pushButton8.setGeometry(QtCore.QRect(590, 430, 51, 41))
        self.pushButton8.setObjectName("pushButton8")
        self.tabWidget.addTab(self.widget, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser1 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser1.setGeometry(QtCore.QRect(30, 30, 601, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser1.setFont(font)
        self.textBrowser1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser1.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser1.setObjectName("textBrowser1")
        self.pushButton2 = QtWidgets.QPushButton(self.tab)
        self.pushButton2.setGeometry(QtCore.QRect(130, 440, 75, 41))
        self.pushButton2.setObjectName("pushButton2")
        self.comboBox3 = QtWidgets.QComboBox(self.tab)
        self.comboBox3.setGeometry(QtCore.QRect(60, 440, 69, 22))
        self.comboBox3.setObjectName("comboBox3")
        self.pushButton3 = QtWidgets.QPushButton(self.tab)
        self.pushButton3.setGeometry(QtCore.QRect(220, 440, 75, 41))
        self.pushButton3.setObjectName("pushButton3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton4.setGeometry(QtCore.QRect(150, 440, 75, 41))
        self.pushButton4.setObjectName("pushButton4")
        self.textBrowser2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser2.setGeometry(QtCore.QRect(30, 20, 591, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser2.setFont(font)
        self.textBrowser2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser2.setObjectName("textBrowser2")
        self.comboBox4 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox4.setGeometry(QtCore.QRect(60, 450, 69, 22))
        self.comboBox4.setObjectName("comboBox4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton7.setGeometry(QtCore.QRect(180, 70, 75, 41))
        self.pushButton7.setObjectName("pushButton7")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton6.setGeometry(QtCore.QRect(180, 10, 71, 41))
        self.pushButton6.setObjectName("pushButton6")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(10, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.pushButton11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton11.setGeometry(QtCore.QRect(180, 140, 75, 41))
        self.pushButton11.setObjectName("pushButton11")
        self.comboBox7 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox7.setGeometry(QtCore.QRect(130, 150, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox7.setFont(font)
        self.comboBox7.setObjectName("comboBox7")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(10, 220, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.pushButton12 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton12.setGeometry(QtCore.QRect(180, 210, 75, 41))
        self.pushButton12.setObjectName("pushButton12")
        self.comboBox8 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox8.setGeometry(QtCore.QRect(130, 220, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox8.setFont(font)
        self.comboBox8.setObjectName("comboBox8")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.pushButton13 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton13.setGeometry(QtCore.QRect(180, 280, 75, 41))
        self.pushButton13.setObjectName("pushButton13")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(10, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableView_2 = QtWidgets.QTableView(self.tab_4)
        self.tableView_2.setGeometry(QtCore.QRect(0, 150, 561, 341))
        self.tableView_2.setObjectName("tableView_2")
        self.comboBox6 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox6.setGeometry(QtCore.QRect(420, 30, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox6.setFont(font)
        self.comboBox6.setObjectName("comboBox6")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(320, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton9 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton9.setGeometry(QtCore.QRect(430, 70, 75, 41))
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 271, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(190, 110, 75, 41))
        self.pushButton5.setObjectName("pushButton5")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 170, 201, 170))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox1 = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox1.setFont(font)
        self.comboBox1.setObjectName("comboBox1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox2 = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox2.setFont(font)
        self.comboBox2.setObjectName("comboBox2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox2)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comboBox5 = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox5.setFont(font)
        self.comboBox5.setObjectName("comboBox5")
        self.comboBox5.addItem("")
        self.comboBox5.addItem("")
        self.comboBox5.addItem("")
        self.comboBox5.addItem("")
        self.comboBox5.addItem("")
        self.comboBox5.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox5)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox9 = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox9.setFont(font)
        self.comboBox9.setObjectName("comboBox9")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAppend_offer = QtWidgets.QAction(MainWindow)
        self.actionAppend_offer.setObjectName("actionAppend_offer")
        self.actionDB = QtWidgets.QAction(MainWindow)
        self.actionDB.setObjectName("actionDB")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "Add"))
        self.label_4.setText(_translate("MainWindow", "Delay(up)"))
        self.label_6.setText(_translate("MainWindow", "threads"))
        self.label_5.setText(_translate("MainWindow", "Delay(Down)"))
        self.lineEdit_3.setText(_translate("MainWindow", "10"))
        self.lineEdit_4.setText(_translate("MainWindow", "5"))
        self.lineEdit_2.setText(_translate("MainWindow", "3"))
        self.pushButton8.setText(_translate("MainWindow", "Import"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Mission_Info"))
        self.pushButton2.setText(_translate("MainWindow", "Move"))
        self.pushButton3.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "All_links"))
        self.pushButton4.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Working_links"))
        self.label_10.setText(_translate("MainWindow", "Data Import"))
        self.pushButton7.setText(_translate("MainWindow", "Delete"))
        self.label_11.setText(_translate("MainWindow", "Emails clean"))
        self.pushButton6.setText(_translate("MainWindow", "Import"))
        self.label_16.setText(_translate("MainWindow", "Upload plan"))
        self.pushButton11.setText(_translate("MainWindow", "Start"))
        self.comboBox7.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox7.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox7.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox7.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox7.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox7.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox7.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox7.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox7.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox7.setItemText(9, _translate("MainWindow", "10"))
        self.label_17.setText(_translate("MainWindow", "Delete All ports"))
        self.pushButton12.setText(_translate("MainWindow", "Delete"))
        self.comboBox8.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox8.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox8.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox8.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox8.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox8.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox8.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox8.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox8.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox8.setItemText(9, _translate("MainWindow", "10"))
        self.pushButton13.setText(_translate("MainWindow", "Test"))
        self.label_18.setText(_translate("MainWindow", "Test"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Some funcs"))
        self.label_12.setText(_translate("MainWindow", "Account Lists"))
        self.pushButton9.setText(_translate("MainWindow", "Login"))
        self.label_14.setText(_translate("MainWindow", "Roboform pwd"))
        self.label_13.setText(_translate("MainWindow", "Roboform name"))
        self.label_15.setText(_translate("MainWindow", "Country"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Alliance_login"))
        self.pushButton5.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Alliances"))
        self.label_2.setText(_translate("MainWindow", "Offer"))
        self.label_9.setText(_translate("MainWindow", "Country"))
        self.comboBox5.setItemText(0, _translate("MainWindow", "US"))
        self.comboBox5.setItemText(1, _translate("MainWindow", "CA"))
        self.comboBox5.setItemText(2, _translate("MainWindow", "GB"))
        self.comboBox5.setItemText(3, _translate("MainWindow", "AU"))
        self.comboBox5.setItemText(4, _translate("MainWindow", "FR"))
        self.comboBox5.setItemText(5, _translate("MainWindow", "DE"))
        self.label_3.setText(_translate("MainWindow", "Url_link"))
        self.label_7.setText(_translate("MainWindow", "Account"))
        self.comboBox9.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox9.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox9.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox9.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox9.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox9.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox9.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox9.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox9.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox9.setItemText(9, _translate("MainWindow", "10"))
        self.actionAppend_offer.setText(_translate("MainWindow", "delete email"))
        self.actionDB.setText(_translate("MainWindow", "DB"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))

