from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QLabel, QApplication

from PyQt5.QtGui import QPaintEvent, QPainter, QBrush, QPen, QColor, QFont, QResizeEvent
from PyQt5.QtCore import Qt

from .HelpWindow import HelpWindow
from .ModeWindow import ModeWindow

from backend.Node import Node


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
        self.root = Node(1, None, self.root_x, self.root_y)

        node1 = Node(2, self.root, 100, 100)
        node2 = Node(2, self.root, 500, 100)
        self.root.addChild(node1)
        self.root.addChild(node2)


    def resizeEvent(self, event):
        new_size = event.size()
        self.width, self.height = new_size.width(), new_size.height()

        # Update coordinates of all the nodes
        self.root_x = self.x_paint_zero + self.width // 2 - self.node_size // 2
        self.root.setX(self.root_x)

        self.update()
    
    def add_child(self, parent: Node):
        child = Node(parent.getLevel() + 1, parent)
        parent.addChild(child)
        # Необходимо пересчитать координаты всего дерева сразу
    

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(QFont('Arial', self.letter_size))
        painter.setPen(QPen(QColor(Qt.black), 2))
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.draw_node(
            painter,
            self.root
        )

        painter.end()
        
    
    def draw_node(self, painter: QPainter, node: Node):
        painter.drawEllipse(*node.getPosition(), self.node_size, self.node_size)
        painter.drawText(
            node.getX() + self.x_letter_position,
            node.getY() + self.y_letter_position,
            'A' if node.getLevel() % 2 else 'B'
        )

    def connect_nodes(self, node1, node2):
        pass

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
        pass

    def startSolution(self):
        pass

    def set_task_number(self, num: int):
        self.task_number = num

    def redraw(self):
        self.update()
