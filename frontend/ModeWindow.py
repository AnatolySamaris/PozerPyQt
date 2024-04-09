from PyQt5.QtWidgets import (
    QMainWindow, QDesktopWidget, QGroupBox, QGridLayout, QApplication,
    QVBoxLayout, QRadioButton, QLineEdit, QPushButton, QFormLayout, QLayout,
    QSizePolicy, QWidget
)
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtCore import Qt, QSize, QRect

import sys

class ModeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор режима")
        self.setGeometry(300, 300, 320, 180)
        self.center()

        self.gridLayout = QGridLayout()
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.setLayout(self.gridLayout)

        self.lineEdit = QLineEdit()
        self.lineEdit.setMaximumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(3)
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.radioButton = QRadioButton()
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton()
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.ok = QPushButton()
        self.ok.setGeometry(QRect(180, 120, 120, 28))
        self.ok.setMaximumSize(QSize(120, 30))
        font = QFont()
        font.setPointSize(8)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")

        self.setWindowTitle("Режим ввода")
        self.radioButton.setText("Ввод из файла")
        self.radioButton_2.setText("Ввод вручную")
        self.ok.setText("OK")



        """
        radio_file = QRadioButton('Ввод из файла', self)
        radio_file.toggled.connect(self.setFileMode)

        self.radio_manual = QRadioButton('Ввод вручную', self)
        self.radio_manual.toggled.connect(self.setManualMode)

        self.file_number = QLineEdit()
        self.file_number.setValidator(QIntValidator())
        self.file_number.setMaxLength(3)
        self.file_number.setAlignment(Qt.AlignRight)
        self.file_number.setFont(QFont("Arial", 8))

        self.ok_button = QPushButton('Ок', self)
        self.ok_button.clicked.connect(self.okButtonClicked)

        self.grid = QGridLayout()
        self.grid.addWidget(radio_file, 1, 1)
        self.grid.addWidget(self.radio_manual, 2, 1)
        self.grid.addWidget(self.file_number, 1, 2)
        self.grid.addWidget(self.ok_button, 2, 2)
        self.setLayout(self.grid)
        """


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setManualMode(self):
        self.input_file.setEnabled(False)

    def setFileMode(self):
        self.input_file.setEnabled(True)

    def okButtonClicked(self):
        if self.radio_file.isChecked():
            input_value = self.input_file.text()
            print('if', input_value)
        else:
            print('else', input_value)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowExample = ModeWindow()
    windowExample.show()
    sys.exit(app.exec_())