from PyQt5.QtWidgets import QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt

from backend.Node import Node


class AddDialog(QDialog):
    """
    Диалоговое окно добавления потомков. Помимо добавления потомка (обычной или конечной вершины),
    позволяет удалить выбранную вершину. После действия с вершиной не пропадает, позволяя, например,
    добавить ещё потомков к выбранной вершине, не открывая окно ещё раз.
    """
    def __init__(self, parent: QMainWindow, current_node: Node):
        super().__init__(parent)
        self.current_node = current_node

        #######################
        # === DIALOG DESIGN ===
        #######################

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 170, 130)
        self.setStyleSheet("background-color: #e5e5e5; border: 1px solid black;")
        btn_add_child = QPushButton('Добавить потомка', self)
        btn_add_child.setGeometry(10, 10, 150, 30)

        btn_add_leaf = QPushButton('Добавить исход', self)
        btn_add_leaf.setGeometry(10, 50, 150, 30)

        btn_remove_child = QPushButton('Удалить вершину', self)
        btn_remove_child.setGeometry(10, 90, 150, 30)

        if not self.current_node.getEndNode():
            btn_add_child.setStyleSheet("background-color: white; border: 1px solid black;")
            btn_add_leaf.setStyleSheet("background-color: white; border: 1px solid black;")
        btn_remove_child.setStyleSheet("background-color: white; border: 1px solid black;")

        btn_add_child.clicked.connect(self.add_child)
        btn_add_leaf.clicked.connect(self.add_leaf)
        btn_remove_child.clicked.connect(self.remove_child)
    
    def set_position(self, x: int, y: int) -> None:
        """
        Внешняя функция, вызывается из родительского окна.
        Устанавливает позицию диалогового окна относительно родительского.
        """
        self.x = x
        self.y = y
        self.move(x, y)
    
    def add_child(self) -> None:
        """
        Добавляет потомка (обычную вершину) к выбранной вершине.
        """
        if not self.current_node.getEndNode():
            self.parent().create_node(self.current_node)
            self.parent().update()

    def add_leaf(self) -> None:
        """
        Добавляет потомка (конечную вершину) к выбранной вершине.
        """
        if not self.current_node.getEndNode():
            self.parent().create_node(self.current_node, leaf=True)
            self.parent().update()

    def remove_child(self) -> None:
        """
        Удаляет выбранную вершину.
        """
        if self.current_node != self.parent().get_root():
            parent = self.current_node.getParent()
            parent.removeChild(self.current_node)
            self.parent().update_nodes_pos()
            self.parent().update()
