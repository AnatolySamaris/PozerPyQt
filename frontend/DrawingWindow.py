from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QDialog, QPushButton

from PyQt5.QtGui import QPaintEvent, QPainter, QBrush, QPen, QColor, QFont, QResizeEvent
from PyQt5.QtCore import Qt, QPoint

from .HelpWindow import HelpWindow
from .ModeWindow import ModeWindow

from backend.Node import Node


class CustomDialog(QDialog):
    def __init__(self, x, y):
        super().__init__()
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
        print('Добавлен потомок')
    
    def add_leaf(self):
        print('Добавлен лист')


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

        ##############################
        # === TREE INITIALIZATION ===
        ##############################
        Node.setup_static(
            self.width,
            self.height,
            self.x_paint_zero,
            self.y_paint_zero,
            self.node_size
        )

        self.tree_height = 1

        self.root = Node(1, None, self.root_x, self.root_y)

        n1 = Node(2, self.root, 100, 200)
        n2 = Node(2, self.root, 500, 200)

        self.root.addChild(n1)
        self.root.addChild(n2)

        #self.create_node(self.root)
        #self.create_node(self.root)


    def resizeEvent(self, event):
        new_size = event.size()
        self.width, self.height = new_size.width(), new_size.height()
        
        # Update coordinates of all the nodes


        #self.root.graphTraverse(
        #    self.root.recalculateNode(self.root, self.height, self.width, self.y_paint_zero, self.x_paint_zero, self.node_size, self.tree_height)
        #)

        #self.root.graphTraverse(
        #    self.root.recalculateNode(self.root)
        #)
        
        #self.root_x = self.x_paint_zero + self.width // 2 - self.node_size // 2
        #self.root.setX(self.root_x)

        self.update()
    
    def create_node(self, parent: Node|None):
        if parent is None:
            self.root = Node(1)
        else:
            child = Node(parent.getLevel() + 1, parent)
            parent.addChild(child)
        self.tree_height += 1
        #self.root.graphTraverse(
        #    self.root.recalculateNode(self.root, self.height, self.width, self.y_paint_zero, self.x_paint_zero, self.node_size, self.tree_height)
        #)
    

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(QFont('Arial', self.letter_size))
        painter.setPen(QPen(QColor(Qt.black), 2))
        painter.setRenderHint(QPainter.Antialiasing, True)


        self.draw_tree(painter, self.root)
        #self.draw_node(
        #    painter,
        #    self.root
        #)

        painter.end()
  
    
    def draw_node(self, painter: QPainter, node: Node):
        painter.drawEllipse(*node.getPosition(), self.node_size, self.node_size)
        painter.drawText(
            node.getX() + self.x_letter_position,
            node.getY() + self.y_letter_position,
            'A' if node.getLevel() % 2 else 'B'
        )

    def draw_tree(self, painter: QPainter, node: Node):
        self.draw_node(painter, node)
        for child in node.getChildren():
            self.connect_nodes(painter, node, child)
            self.draw_tree(painter, child)

    def connect_nodes(self, painter: QPainter, from_node: Node, to_node: Node):
        from_x, from_y = from_node.getPosition()
        to_x, to_y = to_node.getPosition()
        painter.drawLine(
            from_x + self.node_size // 2,
            from_y + self.node_size,
            to_x + self.node_size // 2,
            to_y
        )

    def mousePressEvent(self, event):
        if event.button() == 2:  # Правая кнопка мыши
            window_pos = self.mapToGlobal(QPoint(0, 0))
            dialog = CustomDialog(event.x() - window_pos.x(), event.y() - window_pos.y())
            dialog.exec_()

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
        self.update()

    def startSolution(self):
        pass

    def set_task_number(self, num: int):
        self.task_number = num

    def redraw(self):
        self.update()
