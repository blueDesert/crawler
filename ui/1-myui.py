#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from ui import Ui_Dialog


class MainWindow(QMainWindow,Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.ui = Ui_Dialog()
        #self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

