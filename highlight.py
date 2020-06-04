# -*- coding: utf-8 -*-

import sys
import keyword
from PyQt5.Qsci import QsciScintilla, QsciAPIs, QsciLexerPython
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QFont, QColor


class highlight(QsciLexerPython):
    """
    语法高亮规则
    """

    def __init__(self,parent):
        super(highlight, self).__init__()
        font = QFont()
        font.setFamily('Consolas')
        font.setPointSize(12)
        font.setFixedPitch(True)
        self.setFont(font)
        self.setColor(QColor(0, 0, 0))
        self.setPaper(QColor(255, 255, 255))
        self.setColor(QColor("#0000FF"), QsciLexerPython.FunctionMethodName)
        self.setColor(QColor("#0000FF"), QsciLexerPython.ClassName)
        self.setColor(QColor("#0000FF"), QsciLexerPython.Decorator)
        self.setColor(QColor("#FF8C00"), QsciLexerPython.Keyword)
        self.setColor(QColor("#B5B5B5"), QsciLexerPython.Comment)
        self.setColor(QColor("#B5B5B5"), QsciLexerPython.CommentBlock)
        self.setColor(QColor("#00AB00"), QsciLexerPython.DoubleQuotedString)
        self.setColor(QColor("#00AB00"), QsciLexerPython.SingleQuotedString)
        self.setColor(QColor("#00AB00"), QsciLexerPython.TripleSingleQuotedString)
        self.setColor(QColor("#00AB00"), QsciLexerPython.TripleDoubleQuotedString)
        self.setColor(QColor("#000000"), QsciLexerPython.Number)
        self.setColor(QColor("#000000"), QsciLexerPython.Operator)
        self.setColor(QColor("#000000"), QsciLexerPython.Identifier)
        self.setColor(QColor("#000000"), QsciLexerPython.HighlightedIdentifier)
        self.setColor(QColor("#000000"), QsciLexerPython.UnclosedString)
        self.setFont(QFont('Consolas',12,weight=QFont.Bold),5)
        self.setFont(QFont('Consolas',12,italic=True),QsciLexerPython.Comment)

class highlightEditor(QMainWindow):
    """
    语法高亮代码框
    """
    
    def __init__(self, parent = None, lineNumberOn = False):
        super(highlightEditor, self).__init__()

        self.editor = QsciScintilla(parent)
        font = QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setFixedPitch(True)
        self.editor.setFont(font)
        self.editor.setObjectName("editor")

        self.editor.setUtf8(True)
        self.editor.setMarginsFont(font)
        if lineNumberOn:
            self.editor.setMarginWidth(0,len(str(len(self.editor.text().split('\n'))))*20)
        self.editor.setMarginLineNumbers(0, lineNumberOn)
 
        self.editor.setBraceMatching(QsciScintilla.StrictBraceMatch)
 
        self.editor.setIndentationsUseTabs(True)
        self.editor.setIndentationWidth(4)
        self.editor.setTabIndents(True)
        self.editor.setAutoIndent(True)
        self.editor.setBackspaceUnindents(True)
        self.editor.setTabWidth(4)
 
        self.editor.setCaretLineVisible(True)
        self.editor.setCaretLineBackgroundColor(QColor('#DCDCDC'))
 
        self.editor.setIndentationGuides(True)
 
        self.editor.setFolding(QsciScintilla.PlainFoldStyle)
        self.editor.setMarginWidth(2,12)
 
        self.editor.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        self.editor.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDER)
        self.editor.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.editor.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDEREND)
 
        self.editor.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        self.editor.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        self.editor.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.editor.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.editor.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.editor.setAutoCompletionCaseSensitivity(True)
        self.editor.setAutoCompletionReplaceWord(False)
        self.editor.setAutoCompletionThreshold(1)
        self.editor.setAutoCompletionUseSingle(QsciScintilla.AcusExplicit)
        self.lexer=highlight(self.editor)
        self.editor.setLexer(self.lexer)
        self.__api = QsciAPIs(self.lexer)
        autocompletions = keyword.kwlist+[]
        for ac in autocompletions:
            self.__api.add(ac)
        self.__api.prepare()
        self.editor.autoCompleteFromAll()

        self.editor.textChanged.connect(self.changed)
    
    def changed(self):
        self.editor.setMarginWidth(0, len(str(len(self.editor.text().split('\n')))) * 20)

# 参考代码：https://blog.csdn.net/Alan_Zhao_2007/article/details/84428664

import ui.rsc_rc