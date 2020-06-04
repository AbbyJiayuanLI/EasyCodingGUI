# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\OneDrive - CUHK-ShenZhen\Code\Lab\Lab\Code\GUI\final3\final3\src\ui\start.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_startWindow(object):
    def setupUi(self, startWindow):
        startWindow.setObjectName("startWindow")
        startWindow.resize(364, 372)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(startWindow.sizePolicy().hasHeightForWidth())
        startWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        startWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/badge2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        startWindow.setWindowIcon(icon)
        startWindow.setStyleSheet("background-color: rgb(255, 200, 51);")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(startWindow)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.courseLable = QtWidgets.QLabel(startWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.courseLable.setFont(font)
        self.courseLable.setObjectName("courseLable")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.courseLable)
        self.comboBox = QtWidgets.QComboBox(startWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("selection-background-color: rgba(255, 255, 255, 125);\n"
"selection-color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 200);\n"
"\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding: 1px 2px 1px 2px;\n"
"min-width: 9em;\n"
"\n"
"down-arrow {\n"
"    image: url(:/img/arrow.png);\n"
"};\n"
"\n"
"drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol- position: top right;\n"
"     width: 20px;\n"
" \n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid;\n"
"     border-top-right-radius: 3px;\n"
"     border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.modeLabel = QtWidgets.QLabel(startWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.modeLabel.setFont(font)
        self.modeLabel.setObjectName("modeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.modeLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.easyButton = QtWidgets.QRadioButton(startWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.easyButton.sizePolicy().hasHeightForWidth())
        self.easyButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.easyButton.setFont(font)
        self.easyButton.setObjectName("easyButton")
        self.horizontalLayout.addWidget(self.easyButton)
        self.hardButton = QtWidgets.QRadioButton(startWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hardButton.setFont(font)
        self.hardButton.setObjectName("hardButton")
        self.horizontalLayout.addWidget(self.hardButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.introductionBox = QtWidgets.QPlainTextEdit(startWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.introductionBox.sizePolicy().hasHeightForWidth())
        self.introductionBox.setSizePolicy(sizePolicy)
        self.introductionBox.setMinimumSize(QtCore.QSize(114, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.introductionBox.setFont(font)
        self.introductionBox.setStyleSheet("border-image: url(:/img/badge3.png);\n"
"background-color: rgba(255, 255, 255, 200);\n"
"\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding: 1px 2px 1px 2px;\n"
"min-width: 12em;")
        self.introductionBox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.introductionBox.setObjectName("introductionBox")
        self.verticalLayout.addWidget(self.introductionBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.yesButton = QtWidgets.QPushButton(startWindow)
        self.yesButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.yesButton.setFont(font)
        self.yesButton.setStyleSheet("background-color: rgb(207, 200, 187);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"padding: 6px 24px 6px 24px;\n"
"")
        self.yesButton.setObjectName("yesButton")
        self.horizontalLayout_2.addWidget(self.yesButton)
        self.quitButton = QtWidgets.QPushButton(startWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.quitButton.setFont(font)
        self.quitButton.setToolTip("")
        self.quitButton.setStatusTip("")
        self.quitButton.setStyleSheet("background-color: rgb(108, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"padding: 6px 24px 6px 24px;")
        self.quitButton.setDefault(False)
        self.quitButton.setFlat(False)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout_2.addWidget(self.quitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)

        self.retranslateUi(startWindow)
        self.quitButton.clicked.connect(startWindow.close)
        QtCore.QMetaObject.connectSlotsByName(startWindow)

    def retranslateUi(self, startWindow):
        _translate = QtCore.QCoreApplication.translate
        startWindow.setWindowTitle(_translate("startWindow", "人工智能课程代码编辑器"))
        self.courseLable.setText(_translate("startWindow", "课程："))
        self.comboBox.setItemText(0, _translate("startWindow", "--请选择课程--"))
        self.comboBox.setItemText(1, _translate("startWindow", "人工智能课程1-基础入门"))
        self.comboBox.setItemText(2, _translate("startWindow", "人工智能课程2-创建并打印向量"))
        self.comboBox.setItemText(3, _translate("startWindow", "人工智能课程3-向量的运算"))
        self.comboBox.setItemText(4, _translate("startWindow", "人工智能课程4-矩阵的运算"))
        self.comboBox.setItemText(5, _translate("startWindow", "人工智能课程5-循环、判断结构求和"))
        self.modeLabel.setText(_translate("startWindow", "模式："))
        self.easyButton.setText(_translate("startWindow", "选择题模式"))
        self.hardButton.setText(_translate("startWindow", "填空题模式"))
        self.introductionBox.setPlainText(_translate("startWindow", "模式介绍"))
        self.yesButton.setText(_translate("startWindow", "确认"))
        self.quitButton.setText(_translate("startWindow", "退出"))

import ui.rsc_rc
