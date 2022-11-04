#!/usr/bin/env python3
# coding=utf-8

# Вариант 9
# В тексте пропущены некоторые слова и словосочетания. Эти слова и словосочетания представлены отдельным
# списком в том порядке, в каком должны быть вставлены. Места вставки отмечены в тексте символом «$».
# Откорректировать текст

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('LDV9_LAB4.2')
        self.setWindowIcon(QtGui.QIcon('drawable/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.textEdit_text.insertPlainText("Клара $ у Карла $")

    def solve(self):
        s = ["украла", "коралл"]
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()
        for l in s:
            text = text.replace("$", l, 1)

        self.textEdit_words.insertPlainText(text)


    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
