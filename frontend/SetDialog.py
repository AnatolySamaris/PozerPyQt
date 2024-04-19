from PyQt5.QtWidgets import QDialog, QPushButton, QGroupBox, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QGridLayout, QFormLayout, QSpacerItem, QSizePolicy, QApplication, QTextBrowser
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class SetDialog(QDialog):
    def __init__(self, parent, x: int, y: int, current_node):
        super().__init__(parent)
        self.current_node = current_node
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(x, y, 330, 180)
        self.setStyleSheet("QDialog {background-color: #e5e5e5; border: 1px solid black;}")

        font = QFont("Arial", 12)

        layout = QVBoxLayout()

        label = QTextBrowser()
        label.setPlainText("Введите выигрыши:")
        layout.addWidget(label)
        label.setFont(font)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        hlayout = QHBoxLayout()
        hlayout.setAlignment(Qt.AlignVCenter)
        layout.addLayout(hlayout)

        opening_bracket = QTextBrowser()
        opening_bracket.setPlainText("(")
        opening_bracket.setFont(font)

        input_1 = QLineEdit()
        input_1.setPlaceholderText("A")
        input_1.setFixedWidth(70)
        input_1.setFont(font)
        # input_1.setGeometry(130, 20, 10, 10)

        comma = QTextBrowser()
        comma.setPlainText(";")
        comma.setFont(font)

        input_2 = QLineEdit()
        input_2.setPlaceholderText("B")
        input_2.setFixedWidth(70)
        input_2.setFont(font)
        # input_2.setGeometry(130, 20, 110, 10)

        closing_bracket = QTextBrowser()
        closing_bracket.setPlainText(")")
        closing_bracket.setFont(font)

        opening_bracket.setFixedWidth(20)
        closing_bracket.setFixedWidth(25)
        comma.setFixedWidth(15)

        # opening_bracket.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # closing_bracket.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # comma.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        spacer1 = QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Fixed)
        spacer2 = QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Fixed)
        spacer3 = QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Fixed)
        spacer4 = QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Fixed)

        hlayout.addWidget(opening_bracket)
        hlayout.addItem(spacer1)
        hlayout.addWidget(input_1)
        hlayout.addItem(spacer2)
        hlayout.addWidget(comma)
        hlayout.addItem(spacer3)
        hlayout.addWidget(input_2)
        hlayout.addItem(spacer4)
        hlayout.addWidget(closing_bracket)

        # hlayout.addWidget(opening_bracket)
        # hlayout.addSpacing(10)
        # hlayout.addWidget(input_1)
        # hlayout.addSpacing(10)
        # hlayout.addWidget(comma)
        # hlayout.addSpacing(10)
        # hlayout.addWidget(input_2)
        # hlayout.addSpacing(10)
        # hlayout.addWidget(closing_bracket)

        # opening_bracket = QLabel(" (")
        # opening_bracket.setFont(font)
        # opening_bracket.setFixedWidth(20)
        # hlayout.addWidget(opening_bracket)

        # input_1 = QLineEdit()
        # input_1.setPlaceholderText("А")
        # input_1.setFont(font)
        # input_1.setFixedWidth(70)
        # hlayout.addWidget(input_1)

        # comma = QLabel(";")
        # comma.setFont(font)
        # comma.setFixedWidth(10)
        # hlayout.addWidget(comma)

        # input_2 = QLineEdit()
        # input_2.setPlaceholderText("B")
        # input_2.setFont(font)
        # input_2.setFixedWidth(70)
        # hlayout.addWidget(input_2)

        # closing_bracket = QLabel(") ")
        # closing_bracket.setFont(font)
        # closing_bracket.setFixedWidth(20)
        # hlayout.addWidget(closing_bracket)


        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        ok_button = QPushButton("OK")
        ok_button.setStyleSheet("width: 70px;")
        layout.addWidget(ok_button, alignment=Qt.AlignRight)

        labels = [label, opening_bracket, comma, closing_bracket]
        for lbl in labels:
            lbl.setStyleSheet("border: none; background-color: transparent;")
        for lb in [opening_bracket, comma, closing_bracket]:
            lb.setAlignment(Qt.AlignCenter)

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