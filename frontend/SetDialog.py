from PyQt5.QtCore import QSize, QMetaObject, Qt, QRect
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtWidgets import (
    QMainWindow, QDialog, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QSpacerItem, QSizePolicy, QHBoxLayout, QLayout
)

from backend.Node import Node


class SetDialog(QDialog):
    """
    Диалоговое окно установки выигрышей. При вводе выигрышей сразу проверяет их правильность
    и окрашивает соответствующее поле ввода в красный цвет в случае ошибки.
    """
    def __init__(self, parent: QMainWindow, current_node: Node):
        super().__init__(parent)

        self.current_node = current_node
        self.error_counter = 0

        #######################
        # === DIALOG DESIGN ===
        #######################

        self.setObjectName("Dialog")
        self.resize(230, 150)
        self.setMinimumSize(QSize(230, 150))
        self.setMaximumSize(QSize(230, 150))
        self.setStyleSheet("QDialog {\n"
        "    background-color: #e5e5e5;\n"
        "    border: 1px solid black;\n"
        "}")
        self.int_validator = QIntValidator(-1000, 1000, self)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 211, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)

        self.label = QLabel(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QLabel(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QSize(100, 25))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(self.int_validator)
        self.lineEdit.setPlaceholderText("A")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMaximumSize(QSize(100, 25))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(self.int_validator)
        self.lineEdit_2.setPlaceholderText("B")
        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.check_and_set_costs)
        self.lineEdit.editingFinished.connect(self.change_costs)
        self.lineEdit_2.editingFinished.connect(self.change_costs)
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setModal(True)

        self.label.setText("Введите выигрыши:")
        self.label_2.setText("(")
        self.label_3.setText(";")
        self.label_4.setText(")")
        self.pushButton.setText("OK")

        self.lineEdit.setFocus()
        QMetaObject.connectSlotsByName(self)

    def keyPressEvent(self, event) -> None:
        """
        Обработчик нажатия на клавиши во время открытого окна.
        Обрабатывает Enter, стрелки вверх-вниз, Escape.
        """
        if event.key() == Qt.Key_Return:
            self.check_and_set_costs()
        elif event.key() == Qt.Key_Up:
            self.lineEdit_2.setFocus()
        elif event.key() == Qt.Key_Down:
            self.lineEdit.setFocus()
        elif event.key() == Qt.Key_Escape:
            self.close()

    def set_position(self, x: int, y: int) -> None:
        """
        Внешняя функция, вызывается из родительского окна.
        Устанавливает позицию диалогового окна относительно родительского.
        """
        self.x = x
        self.y = y
        self.move(x, y)

    def change_costs(self) -> None:
        """
        Проверка введенных выигрышей и изменение стилей полей ввода в случае ошибок
        и после исправления ошибок.
        """
        a, b = self.lineEdit.text(), self.lineEdit_2.text()

        if (self.current_node.getChildren()
            and self.current_node.checkChildrenCosts()
            and (a, b) not in self.current_node.findBestCosts()):

            a_is_valid = a != '' and any(tup[0] == int(a) for tup in self.current_node.findBestCosts())
            b_is_valid = b != '' and any(tup[1] == int(b) for tup in self.current_node.findBestCosts())

            previous_a = self.lineEdit.property('previousText')
            previous_b = self.lineEdit_2.property('previousText')

            if a_is_valid:
                self.lineEdit.setStyleSheet('background-color:  #ffffff;')
            elif a != '' and any(int(tup[0]) != int(a) for tup in self.current_node.findBestCosts()):
                self.lineEdit.setStyleSheet('background-color:  #d9746c;')
                if a != previous_a:
                    self.error_counter += 1
                self.lineEdit.setProperty('previousText', a)

            if b_is_valid:
                self.lineEdit_2.setStyleSheet('background-color:  #ffffff;')
            elif b != '' and any(int(tup[1]) != int(b) for tup in self.current_node.findBestCosts()):
                self.lineEdit_2.setStyleSheet('background-color:  #d9746c;')
                if b != previous_b:
                    self.error_counter += 1
                self.lineEdit_2.setProperty('previousText', b)

    def check_and_set_costs(self) -> None:
        """
        Устанавливает введенные выигрыши и рисует их в родительском окне, если
        значения были введены верно. После установки выигрышей окно закрывается.
        """
        a, b = self.lineEdit.text(), self.lineEdit_2.text()
        if a != '' and a != '+' and a != '-' and b != '' and b != '+' and b != '-':
            a, b = int(a), int(b)
            if (not self.current_node.getChildren()
                or not self.current_node.checkChildrenCosts()
                or (a, b) in self.current_node.findBestCosts()):
                    self.parent().set_node_cost(self.current_node, (a, b))
                    self.parent().increment_counter(self.error_counter)
                    self.parent().update()
                    self.close()
