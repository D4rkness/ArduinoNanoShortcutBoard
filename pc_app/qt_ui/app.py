# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui',
# licensing of 'app.ui' applies.
#
# Created: Sat Sep 14 22:28:17 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.combobox_comport = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_comport.setMaximumSize(QtCore.QSize(100, 16777215))
        self.combobox_comport.setObjectName("combobox_comport")
        self.horizontalLayout.addWidget(self.combobox_comport)
        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout.addWidget(self.btn_connect)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_connected = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_connected.setFont(font)
        self.label_connected.setObjectName("label_connected")
        self.horizontalLayout_14.addWidget(self.label_connected)
        self.horizontalLayout.addLayout(self.horizontalLayout_14)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.f1_layout = QtWidgets.QHBoxLayout()
        self.f1_layout.setObjectName("f1_layout")
        self.f1_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f1_label.setFont(font)
        self.f1_label.setObjectName("f1_label")
        self.f1_layout.addWidget(self.f1_label)
        self.f1_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f1_shortcut_field.setObjectName("f1_shortcut_field")
        self.f1_layout.addWidget(self.f1_shortcut_field)
        self.btn_f1_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f1_set.setObjectName("btn_f1_set")
        self.f1_layout.addWidget(self.btn_f1_set)
        self.btn_f1_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f1_delete.setObjectName("btn_f1_delete")
        self.f1_layout.addWidget(self.btn_f1_delete)
        self.btn_debug_f1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f1.setObjectName("btn_debug_f1")
        self.f1_layout.addWidget(self.btn_debug_f1)
        self.verticalLayout.addLayout(self.f1_layout)
        self.f2_layout = QtWidgets.QHBoxLayout()
        self.f2_layout.setObjectName("f2_layout")
        self.f2_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f2_label.setFont(font)
        self.f2_label.setObjectName("f2_label")
        self.f2_layout.addWidget(self.f2_label)
        self.f2_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f2_shortcut_field.setObjectName("f2_shortcut_field")
        self.f2_layout.addWidget(self.f2_shortcut_field)
        self.btn_f2_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f2_set.setObjectName("btn_f2_set")
        self.f2_layout.addWidget(self.btn_f2_set)
        self.btn_f2_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f2_delete.setObjectName("btn_f2_delete")
        self.f2_layout.addWidget(self.btn_f2_delete)
        self.btn_debug_f2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f2.setObjectName("btn_debug_f2")
        self.f2_layout.addWidget(self.btn_debug_f2)
        self.verticalLayout.addLayout(self.f2_layout)
        self.f3_layout = QtWidgets.QHBoxLayout()
        self.f3_layout.setObjectName("f3_layout")
        self.f3_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f3_label.setFont(font)
        self.f3_label.setObjectName("f3_label")
        self.f3_layout.addWidget(self.f3_label)
        self.f3_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f3_shortcut_field.setObjectName("f3_shortcut_field")
        self.f3_layout.addWidget(self.f3_shortcut_field)
        self.btn_f3_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f3_set.setObjectName("btn_f3_set")
        self.f3_layout.addWidget(self.btn_f3_set)
        self.btn_f3_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f3_delete.setObjectName("btn_f3_delete")
        self.f3_layout.addWidget(self.btn_f3_delete)
        self.btn_debug_f3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f3.setObjectName("btn_debug_f3")
        self.f3_layout.addWidget(self.btn_debug_f3)
        self.verticalLayout.addLayout(self.f3_layout)
        self.f4_layout = QtWidgets.QHBoxLayout()
        self.f4_layout.setObjectName("f4_layout")
        self.f4_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f4_label.setFont(font)
        self.f4_label.setObjectName("f4_label")
        self.f4_layout.addWidget(self.f4_label)
        self.f4_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f4_shortcut_field.setObjectName("f4_shortcut_field")
        self.f4_layout.addWidget(self.f4_shortcut_field)
        self.btn_f4_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f4_set.setObjectName("btn_f4_set")
        self.f4_layout.addWidget(self.btn_f4_set)
        self.btn_f4_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f4_delete.setObjectName("btn_f4_delete")
        self.f4_layout.addWidget(self.btn_f4_delete)
        self.btn_debug_f4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f4.setObjectName("btn_debug_f4")
        self.f4_layout.addWidget(self.btn_debug_f4)
        self.verticalLayout.addLayout(self.f4_layout)
        self.f5_layout = QtWidgets.QHBoxLayout()
        self.f5_layout.setObjectName("f5_layout")
        self.f5_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f5_label.setFont(font)
        self.f5_label.setObjectName("f5_label")
        self.f5_layout.addWidget(self.f5_label)
        self.f5_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f5_shortcut_field.setObjectName("f5_shortcut_field")
        self.f5_layout.addWidget(self.f5_shortcut_field)
        self.btn_f5_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f5_set.setObjectName("btn_f5_set")
        self.f5_layout.addWidget(self.btn_f5_set)
        self.btn_f5_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f5_delete.setObjectName("btn_f5_delete")
        self.f5_layout.addWidget(self.btn_f5_delete)
        self.btn_debug_f5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f5.setObjectName("btn_debug_f5")
        self.f5_layout.addWidget(self.btn_debug_f5)
        self.verticalLayout.addLayout(self.f5_layout)
        self.f6_layout = QtWidgets.QHBoxLayout()
        self.f6_layout.setObjectName("f6_layout")
        self.f6_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f6_label.setFont(font)
        self.f6_label.setObjectName("f6_label")
        self.f6_layout.addWidget(self.f6_label)
        self.f6_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f6_shortcut_field.setObjectName("f6_shortcut_field")
        self.f6_layout.addWidget(self.f6_shortcut_field)
        self.btn_f6_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f6_set.setObjectName("btn_f6_set")
        self.f6_layout.addWidget(self.btn_f6_set)
        self.btn_f6_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f6_delete.setObjectName("btn_f6_delete")
        self.f6_layout.addWidget(self.btn_f6_delete)
        self.btn_debug_f6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f6.setObjectName("btn_debug_f6")
        self.f6_layout.addWidget(self.btn_debug_f6)
        self.verticalLayout.addLayout(self.f6_layout)
        self.f7_layout = QtWidgets.QHBoxLayout()
        self.f7_layout.setObjectName("f7_layout")
        self.f7_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f7_label.setFont(font)
        self.f7_label.setObjectName("f7_label")
        self.f7_layout.addWidget(self.f7_label)
        self.f7_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f7_shortcut_field.setObjectName("f7_shortcut_field")
        self.f7_layout.addWidget(self.f7_shortcut_field)
        self.btn_f7_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f7_set.setObjectName("btn_f7_set")
        self.f7_layout.addWidget(self.btn_f7_set)
        self.btn_f7_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f7_delete.setObjectName("btn_f7_delete")
        self.f7_layout.addWidget(self.btn_f7_delete)
        self.btn_debug_f7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f7.setObjectName("btn_debug_f7")
        self.f7_layout.addWidget(self.btn_debug_f7)
        self.verticalLayout.addLayout(self.f7_layout)
        self.f8_layout = QtWidgets.QHBoxLayout()
        self.f8_layout.setObjectName("f8_layout")
        self.f8_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f8_label.setFont(font)
        self.f8_label.setObjectName("f8_label")
        self.f8_layout.addWidget(self.f8_label)
        self.f8_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f8_shortcut_field.setObjectName("f8_shortcut_field")
        self.f8_layout.addWidget(self.f8_shortcut_field)
        self.btn_f8_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f8_set.setObjectName("btn_f8_set")
        self.f8_layout.addWidget(self.btn_f8_set)
        self.btn_f8_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f8_delete.setObjectName("btn_f8_delete")
        self.f8_layout.addWidget(self.btn_f8_delete)
        self.btn_debug_f8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f8.setObjectName("btn_debug_f8")
        self.f8_layout.addWidget(self.btn_debug_f8)
        self.verticalLayout.addLayout(self.f8_layout)
        self.f9_layout = QtWidgets.QHBoxLayout()
        self.f9_layout.setObjectName("f9_layout")
        self.f9_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f9_label.setFont(font)
        self.f9_label.setObjectName("f9_label")
        self.f9_layout.addWidget(self.f9_label)
        self.f9_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f9_shortcut_field.setObjectName("f9_shortcut_field")
        self.f9_layout.addWidget(self.f9_shortcut_field)
        self.btn_f9_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f9_set.setObjectName("btn_f9_set")
        self.f9_layout.addWidget(self.btn_f9_set)
        self.btn_f9_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f9_delete.setObjectName("btn_f9_delete")
        self.f9_layout.addWidget(self.btn_f9_delete)
        self.btn_debug_f9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f9.setObjectName("btn_debug_f9")
        self.f9_layout.addWidget(self.btn_debug_f9)
        self.verticalLayout.addLayout(self.f9_layout)
        self.f10_layout = QtWidgets.QHBoxLayout()
        self.f10_layout.setObjectName("f10_layout")
        self.f10_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f10_label.setFont(font)
        self.f10_label.setObjectName("f10_label")
        self.f10_layout.addWidget(self.f10_label)
        self.f10_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f10_shortcut_field.setObjectName("f10_shortcut_field")
        self.f10_layout.addWidget(self.f10_shortcut_field)
        self.btn_f10_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f10_set.setObjectName("btn_f10_set")
        self.f10_layout.addWidget(self.btn_f10_set)
        self.btn_f10_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f10_delete.setObjectName("btn_f10_delete")
        self.f10_layout.addWidget(self.btn_f10_delete)
        self.btn_debug_f10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f10.setObjectName("btn_debug_f10")
        self.f10_layout.addWidget(self.btn_debug_f10)
        self.verticalLayout.addLayout(self.f10_layout)
        self.f11_layout = QtWidgets.QHBoxLayout()
        self.f11_layout.setObjectName("f11_layout")
        self.f11_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f11_label.setFont(font)
        self.f11_label.setObjectName("f11_label")
        self.f11_layout.addWidget(self.f11_label)
        self.f11_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f11_shortcut_field.setObjectName("f11_shortcut_field")
        self.f11_layout.addWidget(self.f11_shortcut_field)
        self.btn_f11_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f11_set.setObjectName("btn_f11_set")
        self.f11_layout.addWidget(self.btn_f11_set)
        self.btn_f11_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f11_delete.setObjectName("btn_f11_delete")
        self.f11_layout.addWidget(self.btn_f11_delete)
        self.btn_debug_f11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f11.setObjectName("btn_debug_f11")
        self.f11_layout.addWidget(self.btn_debug_f11)
        self.verticalLayout.addLayout(self.f11_layout)
        self.f12_layout = QtWidgets.QHBoxLayout()
        self.f12_layout.setObjectName("f12_layout")
        self.f12_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f12_label.setFont(font)
        self.f12_label.setObjectName("f12_label")
        self.f12_layout.addWidget(self.f12_label)
        self.f12_shortcut_field = QtWidgets.QLineEdit(self.centralwidget)
        self.f12_shortcut_field.setObjectName("f12_shortcut_field")
        self.f12_layout.addWidget(self.f12_shortcut_field)
        self.btn_f12_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f12_set.setObjectName("btn_f12_set")
        self.f12_layout.addWidget(self.btn_f12_set)
        self.btn_f12_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f12_delete.setObjectName("btn_f12_delete")
        self.f12_layout.addWidget(self.btn_f12_delete)
        self.btn_debug_f12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug_f12.setObjectName("btn_debug_f12")
        self.f12_layout.addWidget(self.btn_debug_f12)
        self.verticalLayout.addLayout(self.f12_layout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.btn_setcolor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setcolor.setObjectName("btn_setcolor")
        self.verticalLayout.addWidget(self.btn_setcolor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 579, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.menu_bar = QtWidgets.QMenu(self.menuMenu)
        self.menu_bar.setObjectName("menu_bar")
        MainWindow.setMenuBar(self.menuBar)
        self.actionEnable_debug = QtWidgets.QAction(MainWindow)
        self.actionEnable_debug.setObjectName("actionEnable_debug")
        self.actiondefault = QtWidgets.QAction(MainWindow)
        self.actiondefault.setObjectName("actiondefault")
        self.menu_bar.addAction(self.actiondefault)
        self.menuMenu.addAction(self.menu_bar.menuAction())
        self.menuMenu.addAction(self.actionEnable_debug)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Select COM-Port", None, -1))
        self.btn_connect.setText(QtWidgets.QApplication.translate("MainWindow", "Connect", None, -1))
        self.label_connected.setText(QtWidgets.QApplication.translate("MainWindow", "Disconnected", None, -1))
        self.f1_label.setText(QtWidgets.QApplication.translate("MainWindow", "F1 Shortcut:  ", None, -1))
        self.btn_f1_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f1_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f1.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f2_label.setText(QtWidgets.QApplication.translate("MainWindow", "F2 Shortcut:  ", None, -1))
        self.btn_f2_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f2_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f2.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f3_label.setText(QtWidgets.QApplication.translate("MainWindow", "F3 Shortcut:  ", None, -1))
        self.btn_f3_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f3_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f3.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f4_label.setText(QtWidgets.QApplication.translate("MainWindow", "F4 Shortcut:  ", None, -1))
        self.btn_f4_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f4_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f4.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f5_label.setText(QtWidgets.QApplication.translate("MainWindow", "F5 Shortcut:  ", None, -1))
        self.btn_f5_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f5_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f5.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f6_label.setText(QtWidgets.QApplication.translate("MainWindow", "F6 Shortcut:  ", None, -1))
        self.btn_f6_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f6_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f6.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f7_label.setText(QtWidgets.QApplication.translate("MainWindow", "F7 Shortcut:  ", None, -1))
        self.btn_f7_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f7_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f7.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f8_label.setText(QtWidgets.QApplication.translate("MainWindow", "F8 Shortcut:  ", None, -1))
        self.btn_f8_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f8_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f8.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f9_label.setText(QtWidgets.QApplication.translate("MainWindow", "F9 Shortcut:  ", None, -1))
        self.btn_f9_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f9_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f9.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f10_label.setText(QtWidgets.QApplication.translate("MainWindow", "F10 Shortcut:", None, -1))
        self.btn_f10_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f10_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f10.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f11_label.setText(QtWidgets.QApplication.translate("MainWindow", "F11 Shortcut:", None, -1))
        self.btn_f11_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f11_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f11.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.f12_label.setText(QtWidgets.QApplication.translate("MainWindow", "F12 Shortcut:", None, -1))
        self.btn_f12_set.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.btn_f12_delete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.btn_debug_f12.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.btn_setcolor.setText(QtWidgets.QApplication.translate("MainWindow", "Set Color", None, -1))
        self.menuMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Menu", None, -1))
        self.menu_bar.setTitle(QtWidgets.QApplication.translate("MainWindow", "Select config", None, -1))
        self.actionEnable_debug.setText(QtWidgets.QApplication.translate("MainWindow", "debug: false", None, -1))
        self.actiondefault.setText(QtWidgets.QApplication.translate("MainWindow", "default", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

