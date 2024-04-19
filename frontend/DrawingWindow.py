from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QLabel

from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QEvent

from .HelpWindow import HelpWindow
from .ModeWindow import ModeWindow
from .AddDialog import AddDialog
from .SetDialog import SetDialog

from backend.Node import Node
from backend.TaskParser import TaskParser

from typing import Tuple
from math import cos, sin, atan2, pi

def log(*args):
    print('=' * 20)
    print(*args, sep=' ')
    print('=' * 20)


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

        self.settingCostsAction = QAction("&Задать выигрыши", self)
        self.settingCostsAction.setText("Задать выигрыши")
        self.settingCostsAction.triggered.connect(self.settingCostsMode)

        self.menubar = self.menuBar()
        self.menubar.addAction(helpAction)
        self.menubar.addAction(modeAction)
        self.menubar.addAction(clearFieldAction)
        self.menubar.addAction(self.settingCostsAction)

        ########################
        # === VARIABLES ===
        ########################
        self.task_number = -1
        self.node_size = 40
        self.letter_size = 16
        self.x_letter_position = int(self.node_size * 0.3)
        self.y_letter_position = int(self.node_size * 0.7)
        self.x_paint_zero = 0
        self.y_paint_zero = 40
        self.setting_costs_mode = False

        self.root_x = self.x_paint_zero + self.width // 2 - self.node_size
        self.root_y = self.y_paint_zero

        self.add_dialog_opened = False
        self.dialog = None

        ##############################
        # === TREE INITIALIZATION ===
        ##############################
        self.tree_height = 1
        self.root = Node(1, None, self.root_x, self.root_y)

    
    def resizeEvent(self, event):
        new_size = event.size()
        self.width, self.height = new_size.width(), new_size.height()
        self.root.graphTraverse(
            lambda node: node.recalculateNode(
                self.root, self.height, self.width,
                self.y_paint_zero, self.x_paint_zero,
                self.node_size, self.tree_height
            )
        )
        self.update()
        if self.add_dialog_opened:
            self.dialog.close()
    
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
    
    def create_cost_label(self, node: Node):
        node_costs = node.getCosts()
        if node_costs:
            text = "(" + str(node_costs[0]) + ";" + str(node_costs[1]) + ")"
            label = QLabel(text, self)
            label.setFont(QFont("Arial", 10))
            if node.getEndNode():
                label.move(node.getX(), node.getY() + self.node_size // 2)
            else:
                label.move(node.getX() + int(self.node_size * 0.75), node.getY() - self.node_size // 2)
            label.show()
    
    def paintEvent(self, event):
        for label in self.findChildren(QLabel):
            if self.dialog and label not in self.dialog.findChildren(QLabel):
                label.deleteLater()

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
        self.create_cost_label(node)

    def draw_tree(self, painter: QPainter):
        self.root.graphTraverse(
            lambda node: self.draw_node(painter, node)
        )
        self.root.graphTraverse(
            lambda node: self.connect_nodes(painter, node.getParent(), node)
        )
        self.root.graphTraverse(
            lambda node: self.create_cost_label(node)
        )

    def connect_nodes(self, painter: QPainter, from_node: Node, to_node: Node):
        if not from_node:
            return
        from_x, from_y = from_node.getPosition()
        to_x, to_y = to_node.getPosition()
        painter.drawLine(
            from_x + self.node_size // 2,
            from_y + self.node_size,
            to_x + self.node_size // 2,
            to_y
        )

    def set_node_cost(self, node: Node, costs: Tuple[int]):
        node.setCosts(costs)
        for label in self.findChildren(QLabel):
            if (label.x() == node.getX() + self.node_size // 2
                and label.y() == node.getY() - self.node_size // 2):
                label.deleteLater()
                break
        self.create_cost_label(node)

    def draw_arrow(self, painter: QPainter, from_node: Node, to_node: Node):
        if not from_node:
            return
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(Qt.black)
        x1, y1 = from_node.getPosition()
        x2, y2 = to_node.getPosition()
        dx = x2 - x1
        dy = y2 - y1
        angle = atan2(dy, dx)
        #headAngle = 15 * pi / 180  # Угол наклона стрелки
        headAngle = 30 * pi / 180
        arrowSize = 20
        # Черчение треугольника
        x3 = x2 - arrowSize * cos(angle + headAngle)
        y3 = y2 - arrowSize * sin(angle + headAngle)
        x4 = x2 - arrowSize * cos(angle - headAngle)
        y4 = y2 - arrowSize * sin(angle - headAngle)

        x1 = int(x1 + self.node_size // 2)
        y1 = int(y1 + self.node_size)
        x2 = int(x2 + self.node_size // 2)
        y2 = int(y2)

        x3 = int(x3 + self.node_size // 2)
        x4 = int(x4 + self.node_size // 2)
        y3 = int(y3)
        y4 = int(y4)

        painter.drawLine(x1, y1, x2, y2)
        painter.drawLine(x2, y2, x3, y3)
        painter.drawLine(x2, y2, x4, y4)
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if self.add_dialog_opened and not self.dialog.geometry().contains(event.globalPos()):
                self.dialog.close()
                self.add_dialog_opened = False
        return super().eventFilter(obj, event)
    
    def calibrate_dialog_window_pos(self, dialog, node):
        dialog_x, dialog_y = 0, 0
        if node.getX() + self.node_size + dialog.width() > self.width:
            dialog_x = node.getX() - dialog.width()
        else:
            dialog_x = node.getX() + self.node_size
        if node.getY() + self.node_size // 2 + dialog.height() > self.height:
            dialog_y = node.getY() + self.node_size // 2 - dialog.height()
        else:
            dialog_y = node.getY() + self.node_size // 2
        return dialog_x, dialog_y
    
    def create_dialog(self, type: str, current_node: Node):
        if type == "add":
            self.dialog = AddDialog(self, current_node)
        elif type == "set":
            self.dialog = SetDialog(self, current_node)
        else:
            return
        dialog_x, dialog_y = self.calibrate_dialog_window_pos(self.dialog, current_node)
        self.dialog.set_position(dialog_x, dialog_y)
        self.add_dialog_opened = True
        self.dialog.show()
    
    def mousePressEvent(self, event):
        if event.button() == 2:  # Правая кнопка мыши
            click_pos = [event.x(), event.y()]
            clicked_node = self.root.graphTraverse(
                lambda node: node.findNode(click_pos, self.node_size)
            )
            if clicked_node:
                if self.setting_costs_mode:
                    if clicked_node.getEndNode() or clicked_node.checkChildrenCosts():
                        self.create_dialog('set', clicked_node)
                else:
                    if not clicked_node.getEndNode():
                        self.create_dialog('add', clicked_node)

    def get_task_tree(self):
        parser = TaskParser(self.task_number)
        parser.createSchema(self.root)
        self.tree_height = self.root.updateTreeHeight(self.tree_height)
        self.root.graphTraverse(
            lambda node: node.recalculateNode(
                self.root, self.height, self.width,
                self.y_paint_zero, self.x_paint_zero,
                self.node_size, self.tree_height
            )
        )
        parser.setCosts(self.root)
        self.update()

        
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
        for label in self.findChildren(QLabel):
            if self.dialog and label in self.dialog.findChildren(QLabel):
                continue
            label.deleteLater()
        self.update()

    def settingCostsMode(self):
        self.setting_costs_mode = not self.setting_costs_mode

        current_text = self.settingCostsAction.text()
        if current_text == "Задать выигрыши":
            self.settingCostsAction.setText("Построить схему")
        else:
            self.settingCostsAction.setText("Задать выигрыши")
        self.settingCostsAction.changed.emit()

    def set_task_number(self, num: int):
        self.task_number = num

    def redraw(self):
        self.update()
