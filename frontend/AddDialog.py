from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtCore import Qt


class AddDialog(QDialog):
    def __init__(self, parent, current_node):
        super().__init__(parent)
        self.current_node = current_node
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 170, 130)
        self.setStyleSheet("background-color: #e5e5e5; border: 1px solid black;")
        btn_add_child = QPushButton('Добавить потомка', self)
        btn_add_child.setGeometry(10, 10, 150, 30)

        btn_add_leaf = QPushButton('Добавить исход', self)
        btn_add_leaf.setGeometry(10, 50, 150, 30)

        btn_remove_child = QPushButton('Удалить потомка', self)
        btn_remove_child.setGeometry(10, 90, 150, 30)

        if not self.current_node.getEndNode():
            btn_add_child.setStyleSheet("background-color: white; border: 1px solid black;")
            btn_add_leaf.setStyleSheet("background-color: white; border: 1px solid black;")
        btn_remove_child.setStyleSheet("background-color: white; border: 1px solid black;")

        btn_add_child.clicked.connect(self.add_child)
        btn_add_leaf.clicked.connect(self.add_leaf)
        btn_remove_child.clicked.connect(self.remove_child)
    
    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.move(x, y)
    
    def add_child(self):
        if not self.current_node.getEndNode():
            self.parent().create_node(self.current_node)
            self.parent().update()

    def add_leaf(self):
        if not self.current_node.getEndNode():
            self.parent().create_node(self.current_node, leaf=True)
            self.parent().update()

    def remove_child(self):
        if self.current_node != self.parent().get_root():
            parent = self.current_node.getParent()
            parent.removeChild(self.current_node)
            self.parent().update()
