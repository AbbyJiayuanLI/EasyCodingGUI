#!/usr/bin/python3
#coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget

from action import startWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = startWindow()
    window.show()

    sys.exit(app.exec_())
