# -*- coding: utf-8 -*-

import sys, os
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QSyntaxHighlighter

from PyQt5.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QApplication, 
    QMenu, 
    QFileDialog, 
    qApp
    )

from ui.Ui_start import Ui_startWindow
from highlight import highlightEditor
from ui import Ui_easy, Ui_hard


root = os.path.split(os.path.abspath(__file__))[0]


class startWindow(QWidget, Ui_startWindow):
    """
    初始窗口逻辑\n
    用于选择课程和模式
    """

    def __init__(self, parent=None):
        super(startWindow, self).__init__(parent)
        self.setupUi(self)

        self.mode = 0
        self.course = 0

        self.easyButton.clicked.connect(self.updateIntro)
        self.hardButton.clicked.connect(self.updateIntro)
        self.easyButton.clicked.connect(self.enableYesBtn)
        self.hardButton.clicked.connect(self.enableYesBtn)
        self.comboBox.currentIndexChanged.connect(self.updateCourse)
        self.comboBox.currentIndexChanged.connect(self.enableYesBtn)
        self.yesButton.clicked.connect(self.changeWindow)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)


    def updateIntro(self):
        """
        更新介绍框内容
        """

        sender = self.sender()
        _translate = QtCore.QCoreApplication.translate
        if sender == self.easyButton:
            self.introductionBox.setPlainText(
                _translate(
                    "Form", 
                    "选择题模式介绍：\n\n"
                    "简单模式\n"
                    "只需要选择给出的代码块\n"
                    "点击确认进入选择题模式"))
            self.mode = 1
        elif sender == self.hardButton:
            self.introductionBox.setPlainText(
                _translate(
                    "Form", 
                    "填空题模式介绍：\n\n"
                    "较难模式\n"
                    "需要自己完成程序中缺失的代码\n"
                    "点击确认进入填空题模式"))
            self.mode = 2
        else:
            self.yesButton.setEnabled(False)
            self.introductionBox.setPlainText(_translate("Form", "模式介绍"))
            self.mode = 0


    def updateCourse(self, event):
        """
        将课程参数同步为下拉菜单内所选内容
        """

        self.course = self.comboBox.currentIndex()
        # print(self.course)


    def changeWindow(self, event):
        """
        切换窗口
        """

        mode = self.mode
        course = self.course
        if mode == 1:
            self.mainWindow = easyWindow()
        elif mode == 2:
            self.mainWindow = hardWindow()
        
        self.loadText(course)
        self.mainWindow.menu = menu(self.mainWindow)       
        self.mainWindow.menu.mode = mode 
        self.mainWindow.back2HomeBtn.clicked.connect(self.show)

        self.hide()  # close
        self.mainWindow.showFirstQuestion()
        # print(11111111)
        self.mainWindow.show()
        


    def loadText(self, course):
        """
        载入代码文本
        """

        rsc = root + '/CourseCode'
        f1 = open(rsc + '/test'+str(course)+'.py')
        f2 = open(rsc + '/answer'+str(course)+'.py')
        f3 = open(rsc + '/divide'+str(course)+'.txt')
        temp3 = f1.readlines()
        temp1 = f2.read()
        temp2 = f3.readline()
        f1.close()
        f2.close() 
        f3.close()

        # print('test file open condition')
        
        # print('test1')
        answerSet = []
        tmpList = temp1.split('@')
        for i in range(int(len(tmpList)/3)):
            tmp = tmpList[3*i+2]
            tmp = tmp[:-1]
            answerSet.append([tmpList[3*i], tmpList[3*i+1], tmp])

        # print('test2')
         
        divideSet = []
        divideSet = temp2.split('@')
        # print('test3')

        questionCount = 0
        questionSet = []
        lineIndex = 0
        for i in range(len(temp3)):
            if temp3[i].find('___') != -1:
                questionCount += 1
        for i in range(questionCount):
            text = ''
            linesNumber = int( divideSet[i] )
            for lines in temp3[lineIndex: lineIndex + linesNumber]:
                text += lines
            lineIndex += linesNumber
            questionSet.append(text)

        self.mainWindow.questionSet = questionSet
        self.mainWindow.questionCount = questionCount
        self.mainWindow.answerSet = answerSet
        # self.mainWindow.divideSet = divideSet


    def enableYesBtn(self, event):
        """
        启用/禁用“确认”按钮
        """

        if (self.mode != 0) and (self.course != 0):
            self.yesButton.setEnabled(True)
            self.yesButton.setStyleSheet("background-color: rgb(108, 0, 255);\n color: rgb(255, 255, 255);\nborder-radius: 5px;\npadding: 6px 24px 6px 24px;")
        else:
            self.yesButton.setEnabled(False)
            self.yesButton.setStyleSheet("background-color: rgb(207, 200, 187);\n color: rgb(255, 255, 255);\nborder-radius: 5px;\npadding: 6px 24px 6px 24px;")










class easyWindow(QMainWindow, Ui_easy.Ui_MainWindow):
    """
    选择题模式窗口逻辑
    """

    questionSet = []
    answerSet = []
    # divideSet = []
    questionCount = 0
    selfAnswerSet = []
    # lineIndex = 0
    # answerText = ''

    def __init__(self):
        super(easyWindow, self).__init__()
        self.setupUi(self)
        
        # 加入文本框
        self.highlighter_1 = highlightEditor(self.centralwidget, True)
        self.codeBox = self.highlighter_1.editor
        # self.codeBox = QtWidgets.QTextEdit(self.centralwidget)
        self.horizontalLayout_3.addWidget(self.codeBox)

        # connection 按键
        # self.backButton.clicked.connect(self.close)
        # self.nextButton.clicked.connect(self.nextQuestion)
        # self.previousButton.clicked.connect(self.previousQuestion)
        # self.radioButton_a.clicked.connect(self.enableNextButton)
        # self.radioButton_b.clicked.connect(self.enableNextButton)
        # self.radioButton_c.clicked.connect(self.enableNextButton)
        # self.radioButton_d.clicked.connect(self.enableNextButton)
        self.back2HomeBtn.clicked.connect(self.close)

        
    def showFirstQuestion(self):       
        print(self.answerSet)
        # 根据题目数量加入指定数量button group
        self.addBtn()
        self.selfAnswerSet = [-1]*self.questionCount

        # get question
        questionText = ''
        # lineIndex = 0
        for i in range(self.questionCount):
            # linesNumber = int( self.divideSet[i] )
            # for lines in self.questionSet[lineIndex: lineIndex + linesNumber]:
            #     questionText += lines
            # lineIndex += linesNumber
            questionText += self.questionSet[i]

        # 显示文章
        _translate = QtCore.QCoreApplication.translate
        self.codeBox.setText(_translate("MainWindow", questionText))
        self.codeBox.setReadOnly(True)

        # 显示选项  
        for i in range(self.questionCount):
            # print(i)
            exec("self.choiceBox{0}.setTitle(_translate('MainWindow', '{0}'))".format(i+1))
            exec("self.radioButton{0}_a.setText(_translate('MainWindow', '{1}'))".format(i+1, self.answerSet[i][0]))
            exec("self.radioButton{0}_b.setText(_translate('MainWindow', '{1}'))".format(i+1, self.answerSet[i][1]))
            exec("self.radioButton{0}_c.setText(_translate('MainWindow', '{1}'))".format(i+1, self.answerSet[i][2]))
            # exec("self.radioButton{0}_d.setText(_translate('MainWindow', '{1}'))".format(i+1, self.answerSet[i][3]))

        # self.previousButton.setEnabled(False)   
        # self.nextButton.setEnabled(False)   


    def addBtn(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        # self.choiceBox1.setFont(font)
        for i in range(1, self.questionCount+1):
            exec("self.choiceGroup{} = QtWidgets.QButtonGroup(self.centralwidget)".format(i))
            exec("self.choiceBox{} = QtWidgets.QGroupBox(self.centralwidget)".format(i))
            exec("self.choiceBox{0}.setObjectName('choiceBox{0}')".format(i))
            exec("self.verticalLayout_4_{0} = QtWidgets.QVBoxLayout(self.choiceBox{0})".format(i))
            exec("self.verticalLayout_4_{0}.setObjectName('verticalLayout_4_{0}')".format(i))   
            exec("self.radioButton{1}_{0} = QtWidgets.QRadioButton(self.choiceBox{1})".format("a", i))
            exec("self.radioButton{1}_{0}.setObjectName('radioButton{1}_{0}')".format("a", i))
            exec("self.verticalLayout_4_{0}.addWidget(self.radioButton{0}_{1})".format(i, "a"))
            exec("self.choiceGroup{1}.addButton(self.radioButton{1}_{0}, 0)".format("a", i))
            exec("self.radioButton{1}_{0} = QtWidgets.QRadioButton(self.choiceBox{1})".format("b", i))
            exec("self.radioButton{1}_{0}.setObjectName('radioButton{1}_{0}')".format("b", i))
            exec("self.verticalLayout_4_{0}.addWidget(self.radioButton{0}_{1})".format(i, "b"))
            exec("self.choiceGroup{1}.addButton(self.radioButton{1}_{0}, 1)".format("b", i))
            exec("self.radioButton{1}_{0} = QtWidgets.QRadioButton(self.choiceBox{1})".format("c", i))
            exec("self.radioButton{1}_{0}.setObjectName('radioButton{1}_{0}')".format("c", i))
            exec("self.verticalLayout_4_{0}.addWidget(self.radioButton{0}_{1})".format(i, "c"))
            exec("self.choiceGroup{1}.addButton(self.radioButton{1}_{0}, 2)".format("c", i))
            # exec("self.radioButton{1}_{0} = QtWidgets.QRadioButton(self.choiceBox{1})".format("d", i))
            # exec("self.radioButton{1}_{0}.setObjectName('radioButton{1}_{0}')".format("d", i))
            # exec("self.verticalLayout_4_{0}.addWidget(self.radioButton{0}_{1})".format(i, "d"))
            # exec("self.choiceGroup{1}.addButton(self.radioButton{1}_{0}, 3)".format("d", i))
            exec("self.verticalLayout.addWidget(self.choiceBox{})".format(i))
            exec("self.radioButton{}_a.clicked.connect(self.updateAnswer)".format(i))
            exec("self.radioButton{}_b.clicked.connect(self.updateAnswer)".format(i))
            exec("self.radioButton{}_c.clicked.connect(self.updateAnswer)".format(i))
            # exec("self.radioButton{}_d.clicked.connect(self.updateAnswer)".format(i))



    def updateAnswer(self):
        # answerGoup = []
        # answerID = []
        for i in range(1, self.questionCount+1):
            tmp = eval("self.choiceGroup{}".format(i)).checkedId()
            if not tmp == -1:
                # answerGoup.append(i-1)
                # answerID.append(tmp)
                self.selfAnswerSet[i-1] = tmp

        questionText = ''
        # lineIndex = 0
        for i in range(self.questionCount):
            # tmpText = ''
            # linesNumber = int( self.divideSet[i] )
            # for lines in self.questionSet[lineIndex: lineIndex + linesNumber]:
            #     tmpText += lines
            tmpText = self.questionSet[i]

            if self.selfAnswerSet[i] != -1:
                tmpText = tmpText.replace('___', self.answerSet[i][(self.selfAnswerSet[i])])
            try: 
                tmpText = tmpText.replace('\\', '')
            finally:
                pass
            questionText += tmpText
            # lineIndex += linesNumber
    
        # print(self.selfAnswerSet)
        _translate = QtCore.QCoreApplication.translate
        self.codeBox.setText(_translate("MainWindow", questionText))
        


    # def nextQuestion(self):   
        # self.previousButton.setEnabled(True)
        # print(self.answerID)
        # print(self.questionIndex)

        # 更新上一题已作答代码内容
        # self.answerText = self.questionText
        # if self.answerText.find('___') != -1:
        #     self.answerText = self.answerText.replace('___', self.answerSet[self.questionIndex-1][self.answerID-1])
        
        # try:
        #     self.finishedText[self.questionIndex - 1] = self.answerText
        # except:
        #     self.finishedText.append(self.answerText)

        # # 更新所有已写代码
        # _translate = QtCore.QCoreApplication.translate
        # codes = ''
        # for code in self.finishedText:
        #     codes += code
        # code += self.questionText
        # self.codeBox.setPlainText(_translate("MainWindow", codes))

        # # print(self.answerText)
        # # print(self.finishedText)

        # self.questionIndex += 1  

        # # 更新按键   
        # # self.btnGroup.
        # self.radioButton_a.setChecked(False)
        # self.radioButton_b.setChecked(False)
        # self.radioButton_c.setChecked(False)
        # self.radioButton_d.setChecked(False)
        # # radiobutton 有点问题！！！！！！！！！！！！！

        # if self.questionIndex > self.questionCount:
        #     self.hide()
        #     # self.endWindow = endWindow(self)
        # else:
        #     if self.questionIndex == self.questionCount:
        #         self.nextButton.setText(_translate("MainWindow", "确定"))
        #     else:
        #         self.nextButton.setText(_translate("MainWindow", "下一题"))
            
        #     # 更新问题
        #     linesNumber = int(self.divideSet[self.questionIndex - 1])
        #     self.questionText = ''
        #     for lines in self.questionSet[self.lineIndex: self.lineIndex + linesNumber]:
        #         self.questionText += lines
        #     self.lineIndex += linesNumber
        #     self.questionBox.setPlainText(_translate("MainWindow", self.questionText))

        #     # 更新选项
        #     self.radioButton_a.setText(_translate("MainWindow", self.answerSet[self.questionIndex-1][0]))
        #     self.radioButton_b.setText(_translate("MainWindow", self.answerSet[self.questionIndex-1][1]))
        #     self.radioButton_c.setText(_translate("MainWindow", self.answerSet[self.questionIndex-1][2]))
        #     self.radioButton_d.setText(_translate("MainWindow", self.answerSet[self.questionIndex-1][3]))
            
            
    # def previousQuestion(self):
    #     print(self.questionIndex)
    #     self.questionIndex -= 1
    #     print(self.questionIndex)

        # # 更新按键
        # _translate = QtCore.QCoreApplication.translate
        # self.nextButton.setText(_translate("MainWindow", "下一题"))
        # if self.questionIndex == 1:
        #     self.previousButton.setEnabled(False)

        # # 更新问题
        # oldLinesNumber = int(self.divideSet[self.questionIndex])
        # self.lineIndex -= oldLinesNumber
        # linesNumber = int(self.divideSet[self.questionIndex-1])

        # self.questionText = ''
        # for lines in self.questionSet[self.lineIndex - linesNumber: self.lineIndex]:
        #     self.questionText += lines
        # self.questionBox.setPlainText(_translate("MainWindow", self.questionText))

        # # 更新选项
        # self.radioButton_a.setText(_translate("MainWindow", self.answerSet[self.questionIndex-1][0]))
        # self.radioButton_b.setText(_translate("MainWindow", self.answerSet[self.questionIndex-1][1]))
        # self.radioButton_c.setText(_translate("MainWindow", self.answerSet[self.questionIndex-1][2]))
        # self.radioButton_d.setText(_translate("MainWindow", self.answerSet[self.questionIndex-1][3]))
            

    # def enableNextButton(self):
    #     self.nextButton.setEnabled(True)












class hardWindow(QMainWindow, Ui_hard.Ui_MainWindow):
    """
    填空题模式窗口逻辑
    """

    questionSet = []
    answerSet = []
    # divideSet = []
    questionCount = 0
    # finishedText = []
    quesPosList = []
    selfAnswerSet = []
    # questionText = ''
    # answerText = ''

    def __init__(self):
        super(hardWindow, self).__init__()
        self.setupUi(self)


        # # 加入题目文本框
        self.highlighter_1 = highlightEditor(self.centralwidget, True)
        self.codeBox = self.highlighter_1.editor
        self.horizontalLayout_3.addWidget(self.codeBox)
        # self.codeBox = QtWidgets.QTextEdit(self.centralwidget)
        # self.horizontalLayout_3.addWidget(self.codeBox)

        # connection 按键
        # self.backButton.clicked.connect(self.close)
        # self.nextButton.clicked.connect(self.nextQuestion)
        # self.plainTextEdit.textChanged.connect(self.checkNextButton)
        # self.codeBox.cursorPositionChanged.connect(self.checkEdibility)
        self.back2HomeBtn.clicked.connect(self.close)


    def showFirstQuestion(self):
        # print(self.questionSet)
        # print(self.answerSet)
        # print(self.divideSet)

        self.addBox()
        self.selfAnswerSet = ["___"]*self.questionCount

        # get question
        questionText = ''
        # lineIndex = 0
        _translate = QtCore.QCoreApplication.translate
        for i in range(self.questionCount):
            # text = ''
            # linesNumber = int( self.divideSet[i] )
            # for lines in self.questionSet[lineIndex: lineIndex + linesNumber]:
            #     text += lines
            # lineIndex += linesNumber
            text = self.questionSet[i]
            questionText += text

            # quesBox显示
            exec("self.quesBox{0}.setText(_translate('MainWindow', text))".format(i+1))
            
        self.codeBox.setText(_translate("MainWindow", questionText))
        self.codeBox.setReadOnly(True)

        # 找到问题所在行和index
        # index = -1
        # line = -1 ？？？？？？？为什么不能加？？？？？？？？
        for i in range(self.questionCount):
            exec("doc = self.quesBox{}.text()".format(i+1))
            exec("index = doc.find('___')")
            exec("self.quesPosList.append(index)")
            exec("self.quesBox{}.cursorPositionChanged.connect(self.checkEdibility)".format(i+1))
        # print(self.quesPosList)


    def addBox(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        # self.choiceBox1.setFont(font)
        for i in range(1, self.questionCount+1):
            exec("highlighter_{} = highlightEditor(self.scrollAreaWidgetContents)".format(i))
            exec("self.quesBox{0} = highlighter_{0}.editor".format(i))
            exec("self.quesBox{0}.setObjectName('quesBox{0}')".format(i))
            exec("self.verticalLayout.addWidget(self.quesBox{})".format(i))   
            

    def checkEdibility(self):  #记得改成quesBox！！！
        # print(1)
        # beginPos = 0
        # quesPos = []
        # while not( doc.find("___", beginPos).isNull() ):
        #     pos = doc.find("___", beginPos).position()
        #     quesPos.append(pos)
        #     beginPos = pos
        # print(quesPos)

        # curPos = tc.position()
        # for pos in quesPos:
        #     if not (curPos < pos-3 or curPos > pos):
        #         self.codeBox.setReadOnly(False)
        #         return
        #     else:
        #         self.codeBox.setReadOnly(True)

        exec("text = ''")
        for i in range(self.questionCount):
            # exec("tc = self.quesBox{}.textCursor()".format(i+1))
            # exec("textLine = tc.block().firstLineNumber()")
            # exec("self.quesBox{0}.setReadOnly(False) if textLine == self.quesPosList[i][1] else self.quesBox{0}.setReadOnly(True) ".format(i+1))

            # refresh my answer
            exec("tmpText = self.quesBox{}.text()".format(i+1))
            exec("startIndex = self.quesPosList[i]")
            exec("endIndex = tmpText.find('\\n', startIndex)")
            # exec("print(startIndex)")
            # exec("print(endIndex)")
            exec("self.selfAnswerSet[i] = tmpText[startIndex: endIndex]")
            # exec("print(self.selfAnswerSet)")


            # new add: find answer by difflib of python !!!!!!!!!!!!!!!!!!!!!!!
            
            
            
            
            
            
            exec("text += tmpText")
            
        # refresh codeBox
        _translate = QtCore.QCoreApplication.translate
        exec("self.codeBox.setText(_translate('MainWindow', text))")
        




    # def checkNextButton(self):
    #     codes = self.plainTextEdit.toPlainText()
    #     if codes.find("__") == -1:
    #         self.nextButton.setEnabled(True)

    
    # def nextQuestion(self):   
    # 改为导出键？？





        

class menu():
    """
    菜单栏逻辑
    """

    def __init__(self, window):
        self.window = window
        self.workingDir = root + '/CourseCode'
        self.fileName = ""
        self.mode = 0

        self.window.importBtn.clicked.connect(self.openFile)
        self.window.exportCodeBtn.clicked.connect(self.exportCode)
        self.window.exportAnswerBtn.clicked.connect(self.exportAnswer)

    def openFile(self): 
        """
        导入文件
        """

        _translate = QtCore.QCoreApplication.translate
        fileName, fileType = QFileDialog.getOpenFileName(
            self.window, "选择文件", self.workingDir, f"Answer File (*.ans{self.mode});;All Files (*)")
        if fileName:
            fileHandle = open(fileName, 'r', encoding='utf-8')
            codes = fileHandle.read()
            fileHandle.close()
            tmpList = codes.split('@')
            # print(tmpList)

            # 选择题
            if isinstance(self.window, easyWindow):
                for i in range(len(tmpList)):
                    self.window.selfAnswerSet[i] = int(tmpList[i])


                # 显示
                questionText = ''
                # lineIndex = 0
                for i in range(self.window.questionCount):
                    # tmpText = ''
                    # linesNumber = int( self.window.divideSet[i] )
                    # for lines in self.window.questionSet[lineIndex: lineIndex + linesNumber]:
                    #     tmpText += lines
                    tmpText = self.window.questionSet[i]
                    if self.window.selfAnswerSet[i] != -1:
                        tmpText = tmpText.replace('___', self.window.answerSet[i][(self.window.selfAnswerSet[i])])
                    try: 
                        tmpText = tmpText.replace('\\', '')
                    finally:
                        pass
                    questionText += tmpText
                    # lineIndex += linesNumber
            
                # print(self.window.selfAnswerSet)
                _translate = QtCore.QCoreApplication.translate
                self.window.codeBox.setText(_translate("MainWindow", questionText))
                # self.window.codeBox.setText(_translate("MainWindow", codes))
            elif isinstance(self.window, hardWindow):
                # get question
                for i in range(len(tmpList)):
                    self.window.selfAnswerSet[i] = tmpList[i]
                for i in range(self.window.questionCount):
                    exec("self.window.quesBox{}.cursorPositionChanged.disconnect(self.window.checkEdibility)".format(i+1))
                # print(self.window.selfAnswerSet)
                exec("""questionText = ''
_translate = QtCore.QCoreApplication.translate
for i in range(self.window.questionCount):
    text = self.window.questionSet[i]
    print(text)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    startIndex = self.window.quesPosList[i]
    endIndex = text.find('\\n', startIndex)
    print(startIndex)
    print(endIndex)
    print(self.window.selfAnswerSet)

    text = text[:startIndex] + self.window.selfAnswerSet[i] + text[endIndex:] 
    print(text)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    exec("self.window.quesBox{}.setText(_translate('MainWindow', text))".format(i+1))
    questionText += text
    
self.window.codeBox.setText(_translate("MainWindow", questionText))
self.window.codeBox.setReadOnly(True)""")




            else:
                # 若用户关闭对话框或选择“取消”
                pass


    def exportCode(self):
        """
        导出代码
        """

        codes = self.window.codeBox.text()
        codes = codes.replace('\r', '')
        fileName = QFileDialog.getSaveFileName(
            self.window, "保存文件", self.workingDir, "Python File(*.py);;All Files (*)")[0]
        if fileName:
            self.fileName = fileName
            self.save(fileName, codes)
        else:
            # 若用户关闭对话框或选择“取消”
            pass


    def exportAnswer(self):
        """
        导出答案
        """

        answers = '@'.join(map(str, self.window.selfAnswerSet))     #TODO: answerSet替换成答案集
        fileName = QFileDialog.getSaveFileName(
            self.window, "保存文件", self.workingDir, f"Answer File(*.ans{self.mode});;All Files (*)")[0]
        if fileName:
            self.fileName = fileName
            self.save(fileName, answers)
        else:
            # 若用户关闭对话框或选择“取消”
            pass


    def save(self, fileName, content):
        """
        文件保存模块
        """

        fileHandle = open(fileName, 'w', encoding='utf-8')
        fileHandle.write(content)
        fileHandle.close()
        self.window.statusbar.showMessage("已保存", 2000)













# class menu(QMenu):
#     """
#     菜单栏逻辑
#     """

#     def __init__(self, window):
#         super(menu, self).__init__()
#         self.window = window
#         self.workingDir = os.path.split(os.path.abspath(__file__))[0]
#         self.fileName = ""

#         self.window.importAction.triggered.connect(self.openFile)
#         self.window.exportAction.triggered.connect(self.export)
#         self.window.saveAction.triggered.connect(self.saveFile)
#         self.window.quitAction.triggered.connect(qApp.quit)


#     def openFile(self):
#         """
#         导入文件
#         """

#         _translate = QtCore.QCoreApplication.translate
#         fileName, fileType = QFileDialog.getOpenFileName(
#             self, "选择文件", self.workingDir, "Python File (*.py);;All Files (*)")
#         if fileName:
#             fileHandle = open(fileName, 'r', encoding='utf-8')
#             codes = fileHandle.read()
#             fileHandle.close()
#             self.window.codeBox.setPlainText(_translate("MainWindow", codes))
#         else:
#             # 若用户关闭对话框或选择“取消”
#             pass


#     def export(self):
#         """
#         导出文件
#         """

#         fileName = QFileDialog.getSaveFileName(
#             self, "保存文件", self.workingDir, "Python File(*.py);;All Files (*)")[0]
#         if fileName:
#             self.fileName = fileName
#             self.save(fileName)
#         else:
#             # 若用户关闭对话框或选择“取消”
#             pass


#     def saveFile(self):
#         """
#         保存文件
#         """

#         if self.fileName:
#             self.save(self.fileName)
#         else:
#             self.export()


#     def save(self, fileName):
#         """
#         文件保存模块
#         """

#         codes = self.window.codeBox.toPlainText()
#         fileHandle = open(fileName, 'w', encoding='utf-8')
#         fileHandle.write(codes)
#         fileHandle.close()
#         self.window.statusbar.showMessage("已保存", 2000)
