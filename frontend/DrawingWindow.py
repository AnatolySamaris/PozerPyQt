from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QLabel, QApplication

from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

from .HelpWindow import HelpWindow
#from .ModeWindow import ModeWindow
from .test import ModeWindow

import sys


class DrawingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ########################
        # === WINDOW CONFIG ===
        ########################
        self.title = "Позиционные игры"
        self.top= 150
        self.left= 150
        self.width = 1500
        self.height = 800

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.center()

        ########################
        # === MENU BAR ===
        ########################
        helpAction = QAction("&Справка", self)
        helpAction.triggered.connect(self.showHelpMenu)

        modeAction = QAction("&Режим работы", self)
        modeAction.triggered.connect(self.showModeActionMenu)

        clearFieldAction = QAction("&Очистить поле", self)
        clearFieldAction.triggered.connect(self.clearField)

        startSolution = QAction("&Начать решение", self)
        startSolution.triggered.connect(self.startSolution)

        self.menubar = self.menuBar()
        self.menubar.addAction(helpAction)
        self.menubar.addAction(modeAction)
        self.menubar.addAction(clearFieldAction)
        self.menubar.addAction(startSolution)

        self.number_label = QLabel('Nothing')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2))

    def showHelpMenu(self):
        helpWindow = HelpWindow(self)
        helpWindow.show()

    def showModeActionMenu(self):
        pass
        #modeWindow = ModeWindow()
        #modeWindow.show()
        #app = QApplication(sys.argv)
        #MainWindow = QMainWindow()
        #ui = ModeWindow()
        #MainWindow.show()

    def clearField(self):
        print(3)

    def startSolution(self):
        print(4)

    def redraw(self):
        self.update()
