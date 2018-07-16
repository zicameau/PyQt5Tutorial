#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

ZetCode PyQt5 tutorial

This example shows an icon in the titlebar of the window.

Author: Jan Bodnar
Edited by: Trevor O'Neil
Website: zetcode.com
Last Edited: July 2018

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

import os

scriptDir = os.path.dirname(os.path.realpath(__file__))

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # locates window on scren and sets the size
        self.setGeometry(300, 300, 300, 220)

        # Titles the window
        self.setWindowTitle('Icon')

        # Gets the path to the image and sets it as the icon.
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'web.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
