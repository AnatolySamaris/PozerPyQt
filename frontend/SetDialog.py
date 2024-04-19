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
        
        layout = QVBoxLayout()
        
        label = QLabel("Введите выигрыши:")
        #label.setStyleSheet("border: none;")
        layout.addWidget(label)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        hlayout = QHBoxLayout()
        layout.addLayout(hlayout)

        opening_bracket = QLabel("(")
        opening_bracket.setFont(font)
        hlayout.addWidget(opening_bracket)

        input_1 = QLineEdit()
        # input_1.setFixedSize(70, 20)
        input_1.setPlaceholderText("А")
        input_1.setFont(font)
        hlayout.addWidget(input_1)

        comma = QLabel(";")
        comma.setFont(font)
        hlayout.addWidget(comma)

        input_2 = QLineEdit()
        # input_2.setFixedSize(70, 20)
        input_2.setPlaceholderText("B")
        input_2.setFont(font)
        hlayout.addWidget(input_2)

        closing_bracket = QLabel(")")
        closing_bracket.setFont(font)
        hlayout.addWidget(closing_bracket)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        ok_button = QPushButton("OK")
        ok_button.setStyleSheet("width: 70px;")
        layout.addWidget(ok_button, alignment=Qt.AlignRight)

        self.setLayout(layout)


    def check_and_set_costs(self):
        a, b = int(self.input_1.text()), int(self.input_2.text)
        if a and b:
            if (a, b) == self.current_node.findBestCosts():
                self.parent().set_node_cost(self.current_node, (a, b))
                self.close()
            else:
                pass    # Обработка неправильных значений
        else:
            pass    # Обработка пустых значений


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = SetDialog(None, 600, 350, None)
    window.show()
    sys.exit(App.exec())