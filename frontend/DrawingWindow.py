from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QDialog, QPushButton

from PyQt5.QtGui import QPaintEvent, QPainter, QBrush, QPen, QColor, QFont, QResizeEvent
from PyQt5.QtCore import Qt, QPoint, QEvent

from .HelpWindow import HelpWindow
from .ModeWindow import ModeWindow

from backend.Node import Node
from backend.TaskParser import TaskParser

def log(*args):
    print('=' * 20)
    print(*args, sep=' ')
    print('=' * 20)


class AddDialog(QDialog):
    def __init__(self, parent: QMainWindow, x: int, y: int, current_node: Node):
        super().__init__(parent)
        self.current_node = current_node
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(x, y, 150, 90)
        self.setStyleSheet("background-color: #e5e5e5; border: 1px solid black;")
        btn_add_child = QPushButton('Добавить потомка', self)
        btn_add_child.setGeometry(10, 10, 130, 30)
        btn_add_leaf = QPushButton('Добавить лист', self)
        btn_add_leaf.setGeometry(10, 50, 130, 30)
        btn_add_child.setStyleSheet("background-color: white; border: 1px solid black;")
        btn_add_leaf.setStyleSheet("background-color: white; border: 1px solid black;")

        btn_add_child.clicked.connect(self.add_child)
        btn_add_leaf.clicked.connect(self.add_leaf)
    
    def add_child(self):
        self.parent().create_node(self.current_node)
        self.parent().update()
        
    
    def add_leaf(self):
        self.parent().create_node(self.current_node, leaf=True)
        self.parent().update()


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

        self.installEventFilter(self)

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

        ########################
        # === VARIABLES ===
        ########################
        self.task_number = -1
        self.node_size = 40
        self.letter_size = 16
        self.x_letter_position = int(self.node_size * 0.3)
        self.y_letter_position = int(self.node_size * 0.7)
        self.x_paint_zero = 0
        self.y_paint_zero = 30

        self.root_x = self.x_paint_zero + self.width // 2 - self.node_size
        self.root_y = self.y_paint_zero

        self.add_dialog_opened = False

        ##############################
        # === TREE INITIALIZATION ===
        ##############################
        self.tree_height = 1
        self.root = Node(1, None, self.root_x, self.root_y)

    def get_root(self):
        return self.root

    def resizeEvent(self, event):
        new_size = event.size()
        self.width, self.height = new_size.width(), new_size.height()
        
        # Update coordinates of all the nodes
        self.root.graphTraverse(
            lambda node: node.recalculateNode(
                self.root, self.height, self.width,
                self.y_paint_zero, self.x_paint_zero,
                self.node_size, self.tree_height
            )
        )

        self.update()
    
    def create_node(self, parent: Node|None, leaf=False):
        if parent is None:
            self.root = Node(1)
        else:
            child = Node(parent.getLevel() + 1, parent)
            if leaf: child.setEndNode(True)
            parent.addChild(child)
        self.tree_height = self.root.updateTreeHeight(self.tree_height)
        self.root.graphTraverse(
            lambda node: node.recalculateNode(
                self.root, self.height, self.width,
                self.y_paint_zero, self.x_paint_zero,
                self.node_size, self.tree_height
            )
        )
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(QFont('Arial', self.letter_size))
        painter.setPen(QPen(QColor(Qt.black), 2))
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.draw_tree(painter)

        painter.end()
    
    def draw_node(self, painter: QPainter, node: Node):
        if node.getEndNode() == False:
            painter.drawEllipse(*node.getPosition(), self.node_size, self.node_size)
            painter.drawText(
                node.getX() + self.x_letter_position,
                node.getY() + self.y_letter_position,
                'A' if node.getLevel() % 2 else 'B'
            )
        else:
            painter.setBrush(QColor(Qt.black))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(
                node.getX() + self.node_size // 4,
                node.getY(),
                self.node_size // 2,
                self.node_size // 2
            )
            painter.setBrush(Qt.NoBrush)
            painter.setPen(QPen(QColor(Qt.black), 2))

    def draw_tree(self, painter: QPainter):
        self.root.graphTraverse(
            lambda node: self.draw_node(painter, node)
        )
        self.root.graphTraverse(
            lambda node: self.connect_nodes(painter, node.getParent(), node)
        )

    def connect_nodes(self, painter: QPainter, from_node: Node, to_node: Node):
        if not from_node:
            return
        from_x, from_y = from_node.getPosition()
        #if to_node.getEndNode():
        #    to_x, to_y = to_node.getX() + self.node_size, to_node.getY()
        #else:
        to_x, to_y = to_node.getPosition()
        painter.drawLine(
            from_x + self.node_size // 2,
            from_y + self.node_size,
            to_x + self.node_size // 2,
            to_y
        )

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if self.add_dialog_opened and not self.dialog.geometry().contains(event.globalPos()):
                self.dialog.close()
                self.add_dialog_opened = False
        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        if event.button() == 2:  # Правая кнопка мыши
            click_pos = [event.x(), event.y()]
            clicked_node = self.root.graphTraverse(
                lambda node: node.findNode(click_pos, self.node_size)
            )
            if clicked_node:
                self.dialog = AddDialog(
                    self,
                    clicked_node.getX() + self.node_size,
                    clicked_node.getY() + self.node_size // 2,
                    clicked_node
                )
                self.add_dialog_opened = True
                self.dialog.show()

    def get_task_tree(self):
        parser = TaskParser(self.task_number)
        parser.createSchema(self.root)
        self.tree_height = self.root.updateTreeHeight(self.tree_height)
        log(self.root.getChildren())
        log(self.tree_height)
        self.root.graphTraverse(
            lambda node: node.recalculateNode(
                self.root, self.height, self.width,
                self.y_paint_zero, self.x_paint_zero,
                self.node_size, self.tree_height
            )
        )
        self.update()
        #parser.setCosts(self.root)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showHelpMenu(self):
        help_window = HelpWindow(self)
        help_window.show()

    def showModeActionMenu(self):
        mode_window = ModeWindow(self)
        mode_window.show()

    def clearField(self):
        self.root.deleteChildren()
        self.tree_height = 1
        self.update()

    def startSolution(self):
        pass

    def set_task_number(self, num: int):
        self.task_number = num

    def redraw(self):
        self.update()
