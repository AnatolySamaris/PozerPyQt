from PyQt5.QtWidgets import QDialog, QPushButton, QGroupBox, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QGridLayout, QFormLayout, QSpacerItem, QSizePolicy, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class SetDialog(QDialog):
    def __init__(self, parent, x: int, y: int, current_node):
        super().__init__(parent)
        self.current_node = current_node
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(x, y, 230, 150)
        self.setStyleSheet("QDialog {background-color: #e5e5e5; border: 1px solid black;}")

        font = QFont("Arial", 12)
        
        self.label = QLabel("Введите выигрыши:")
        #label.setStyleSheet("border: none;")

        self.spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.hlayout = QHBoxLayout()

        self.opening_bracket = QLabel("(")
        self.opening_bracket.setFont(font)
        self.hlayout.addWidget(self.opening_bracket)

        self.input_1 = QLineEdit()
        # input_1.setFixedSize(70, 20)
        self.input_1.setPlaceholderText("А")
        self.input_1.setFont(font)
        self.hlayout.addWidget(self.input_1)

        self.comma = QLabel(";")
        self.comma.setFont(font)
        self.hlayout.addWidget(self.comma)

        self.input_2 = QLineEdit()
        # input_2.setFixedSize(70, 20)
        self.input_2.setPlaceholderText("B")
        self.input_2.setFont(font)
        self.hlayout.addWidget(self.input_2)

        self.closing_bracket = QLabel(")")
        self.closing_bracket.setFont(font)
        self.hlayout.addWidget(self.closing_bracket)

        self.spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet("width: 70px;")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = SetDialog(None, 600, 350, None)
    window.show()
    sys.exit(App.exec())
