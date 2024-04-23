from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtCore import Qt


class AddDialog(QDialog):
    def __init__(self, parent, current_node):
        super().__init__(parent)
        self.current_node = current_node
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 170, 90)
        self.setStyleSheet("background-color: #e5e5e5; border: 1px solid black;")
        btn_add_child = QPushButton('Добавить потомка', self)
        btn_add_child.setGeometry(10, 10, 150, 30)
        btn_add_leaf = QPushButton('Добавить лист', self)
        btn_add_leaf.setGeometry(10, 50, 150, 30)
        btn_add_child.setStyleSheet("background-color: white; border: 1px solid black;")
        btn_add_leaf.setStyleSheet("background-color: white; border: 1px solid black;")

        btn_add_child.clicked.connect(self.add_child)
        btn_add_leaf.clicked.connect(self.add_leaf)
    
    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.move(x, y)
    
    def add_child(self):
        self.parent().create_node(self.current_node)
        self.parent().update()

    def add_leaf(self):
        self.parent().create_node(self.current_node, leaf=True)
        self.parent().update()
