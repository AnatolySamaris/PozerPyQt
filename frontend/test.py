from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class ModeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(320, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 350))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 291, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(3)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(180, 120, 120, 28))
        self.ok.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowTitle("Режим ввода")
        MainWindow.setGeometry(300, 300, 320, 180)
        self.center()
        self.radioButton.setText("Ввод из файла")
        self.radioButton_2.setText("Ввод вручную")
        self.ok.setText("OK")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getNum(self):
        return 10005000
    
    def print(self):
        pass

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ModeWindow()
    MainWindow.show()
    sys.exit(app.exec())
"""