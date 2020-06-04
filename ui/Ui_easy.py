# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\OneDrive - CUHK-ShenZhen\Code\Lab\Lab\Code\GUI\final3\CourseGUI\ui\easy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 374)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/badge2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setObjectName("importBtn")
        self.horizontalLayout_5.addWidget(self.importBtn)
        self.exportCodeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportCodeBtn.setObjectName("exportCodeBtn")
        self.horizontalLayout_5.addWidget(self.exportCodeBtn)
        self.exportAnswerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportAnswerBtn.setObjectName("exportAnswerBtn")
        self.horizontalLayout_5.addWidget(self.exportAnswerBtn)
        self.back2HomeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.back2HomeBtn.setObjectName("back2HomeBtn")
        self.horizontalLayout_5.addWidget(self.back2HomeBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("#groupContent {\n"
"    background-image: url(:/img/badge4.png);\n"
"    background-repeat: no-repeat;\n"
"    background-attachment: fixed;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.groupContent = QtWidgets.QWidget()
        self.groupContent.setGeometry(QtCore.QRect(0, 0, 508, 298))
        self.groupContent.setStyleSheet("")
        self.groupContent.setObjectName("groupContent")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupContent)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.groupContent)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.importAction = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.importAction.setFont(font)
        self.importAction.setIconVisibleInMenu(False)
        self.importAction.setObjectName("importAction")
        self.exportAction = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exportAction.setFont(font)
        self.exportAction.setIconVisibleInMenu(False)
        self.exportAction.setObjectName("exportAction")
        self.quitAction = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quitAction.setFont(font)
        self.quitAction.setIconVisibleInMenu(False)
        self.quitAction.setObjectName("quitAction")
        self.saveAction = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saveAction.setFont(font)
        self.saveAction.setIconVisibleInMenu(False)
        self.saveAction.setShortcutVisibleInContextMenu(True)
        self.saveAction.setObjectName("saveAction")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人工智能课程代码编辑器-选择题模式"))
        self.importBtn.setText(_translate("MainWindow", "导入答案"))
        self.exportCodeBtn.setText(_translate("MainWindow", "导出代码"))
        self.exportAnswerBtn.setText(_translate("MainWindow", "导出答案"))
        self.back2HomeBtn.setText(_translate("MainWindow", "返回主菜单"))
        self.importAction.setText(_translate("MainWindow", "导入"))
        self.importAction.setStatusTip(_translate("MainWindow", "导入python文件"))
        self.exportAction.setText(_translate("MainWindow", "导出"))
        self.exportAction.setStatusTip(_translate("MainWindow", "另存为python文件"))
        self.quitAction.setText(_translate("MainWindow", "退出"))
        self.quitAction.setStatusTip(_translate("MainWindow", "退出程序"))
        self.saveAction.setText(_translate("MainWindow", "保存"))
        self.saveAction.setStatusTip(_translate("MainWindow", "保存为python文件"))
        self.saveAction.setShortcut(_translate("MainWindow", "Ctrl+S"))

import ui.rsc_rc