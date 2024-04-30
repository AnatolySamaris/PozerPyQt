from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QLabel, QMessageBox, QMenu

from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QEvent, QPoint

from .HelpWindow import HelpWindow
from .ModeWindow import ModeWindow
from .AddDialog import AddDialog
from .SetDialog import SetDialog

from backend.Node import Node
from backend.TaskParser import TaskParser

from typing import Tuple
from math import sqrt, pi

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
        self.width = 1800
        self.height = 900

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
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

        self.menubar = self.menuBar()
        self.menubar.addAction(helpAction)
        self.menubar.addAction(modeAction)
        self.menubar.addAction(clearFieldAction)

        self.qmenu = QMenu("Построение схемы", self)

        self.schemaAction = self.qmenu.addAction("Построение схемы")
        self.schemaAction.triggered.connect(self.buildSchema)

        self.costsAction = self.qmenu.addAction("Задание выигрышей")
        self.costsAction.triggered.connect(self.settingCosts)

        self.arrowAction = self.qmenu.addAction("Выбор стрелок")
        self.arrowAction.triggered.connect(self.selectingArrows)

        self.menubar.addMenu(self.qmenu)

        ########################
        # === VARIABLES ===
        ########################
        self.task_number = -1
        self.node_size = 40
        self.letter_size = 16
        self.x_letter_position = int(self.node_size * 0.3)
        self.y_letter_position = int(self.node_size * 0.7)
        self.x_paint_zero = 0
        self.y_paint_zero = 50
        # self.setting_costs_mode = False
        self.mode = 'schema'
        self.arrow_size = 30
        self.counter = 0
        self.correct_arrows = set()
        self.selected_arrows = set()

        self.root_x = self.x_paint_zero + self.width // 2 - self.node_size
        self.root_y = self.y_paint_zero

        self.add_dialog_opened = False
        self.dialog = None

        ##############################
        # === TREE INITIALIZATION ===
        ##############################
        self.tree_height = 1
        self.root = Node(1, None, self.root_x, self.root_y)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 50, 50)

    
    def set_counter(self, counter):
            self.counter += counter
    
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
        if self.dialog:
            self.dialog.close()
            self.dialog = None
        self.update()
    
    def update_nodes_pos(self):
        self.root.graphTraverse(
            lambda node: node.recalculateNode(
                self.root, self.height, self.width,
                self.y_paint_zero, self.x_paint_zero,
                self.node_size, self.tree_height
            )
        )
    
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

    def calibrate_cost_label(self, node: Node, text: str):
        x_label, y_label = node.getX(), node.getY()
        if node.getEndNode():
            y_label += self.node_size
        elif node == self.root:
            x_label += int(self.node_size * 0.75)
        else:
            siblings = node.getParent().getChildren()
            if siblings.index(node) >= len(siblings) // 2:
                x_label += int(self.node_size * 0.75)
            else:
                x_label -= len(text) * (5 + max(len(text) - 5, 0) // 3)
        return x_label, y_label
    
    def create_cost_label(self, painter, node: Node):
        node_costs = node.getCosts()
        if node_costs:
            text = "(" + str(node_costs[0]) + ";" + str(node_costs[1]) + ")"
            painter.setFont(QFont('Arial', 10))
            label_pos = self.calibrate_cost_label(node, text)
            if node.getEndNode():
                painter.drawText(*label_pos, text)
            else:
                painter.drawText(*label_pos, text)
            painter.setFont(QFont('Arial', self.letter_size))
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(QFont('Arial', self.letter_size))
        painter.setPen(QPen(QColor(Qt.black), 2))
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.draw_tree(painter)
        
        self.label.setText(str(self.counter))
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
        self.create_cost_label(painter, node)

    def draw_tree(self, painter: QPainter):
        self.root.graphTraverse(
            lambda node: self.draw_node(painter, node)
        )
        self.root.graphTraverse(
            lambda node: self.connect_nodes(painter, node.getParent(), node)
        )
        self.root.graphTraverse(
            lambda node: self.draw_arrow(node.getParent(), node)
        )
        if self.root.getCosts() and len(self.correct_arrows) == 0:
            self.get_completed_task(self.root)

    def connect_nodes(self, painter: QPainter, from_node: Node, to_node: Node):
        if not from_node:
            return
        
        # проверяем, надо ли рисовать эту линию жирным
        if to_node.getBoldArrow():
            painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
        else:
            painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.setBrush(Qt.black)

        from_x, from_y = from_node.getPosition()
        to_x, to_y = to_node.getPosition()
        painter.drawLine(
            from_x + self.node_size // 2,
            from_y + self.node_size,
            to_x + self.node_size // 2,
            to_y
        )

    def draw_completed_task(self, node: Node):
        node_costs = node.getCosts()
        for child in node.getChildren():
            if child.getCosts() == node_costs:
                self.draw_arrow(node, child, task_completed=True)
                self.draw_completed_task(child)
                break

    def get_completed_task(self, node: Node):
        node_costs = node.getCosts()
        for child in node.getChildren():
            if child.getCosts() == node_costs:
                self.correct_arrows.add((node, child))
                self.get_completed_task(child)
                break

    def draw_arrow(self, from_node: Node, to_node: Node, task_completed=False):
        if not from_node:
            return
        from_costs = from_node.getCosts()
        to_costs = to_node.getCosts()
        if from_costs and to_costs and from_costs == to_costs:
            count_costs = {}
            for child in from_node.getChildren():
                count_costs[child.getCosts()] = [child] + count_costs.get(child.getCosts(), [])
            if len(count_costs[to_costs]) > 1:
                to_node = count_costs[to_costs][-1]
            
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing, True)
            if task_completed or to_node.getBoldArrow():
                painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
            else:
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
            painter.setBrush(Qt.black)

            x1, y1 = from_node.getPosition()
            x2, y2 = to_node.getPosition()

            x1 = int(x1 + self.node_size // 2)
            y1 = int(y1 + self.node_size)
            x2 = int(x2 + self.node_size // 2)
            y2 = int(y2)

            dx, dy = x2 - x1, y2 - y1

            l = (dx / sqrt(dx**2 + dy**2), dy / sqrt(dx**2 + dy**2))
            n = (-l[1], l[0])

            w = 5
            h = 12

            x3 = int(x2 - h * l[0] + w * n[0])
            y3 = int(y2 - h * l[1] + w * n[1])
            x4 = int(x2 - h * l[0] - w * n[0])
            y4 = int(y2 - h * l[1] - w * n[1])

            #painter.drawLine(x1, y1, x2, y2)
            painter.drawLine(x2, y2, x3, y3)
            painter.drawLine(x2, y2, x4, y4)
            painter.end()
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if self.dialog and not self.dialog.geometry().contains(event.globalPos()):
                self.dialog.close()
                self.dialog = None
                self.add_dialog_opened = False
        return super().eventFilter(obj, event)
    
    def calibrate_dialog_window_pos(self, dialog, node):
        dialog_x, dialog_y = 0, 0

        # Калибруем по границам главного окна
        if node.getX() + self.node_size + dialog.width() > self.width:
            dialog_x = node.getX() - dialog.width()
        else:
            dialog_x = node.getX() + self.node_size
        if node.getY() + self.node_size // 2 - dialog.height() < 0:
            dialog_y = node.getY() + self.node_size // 2
        else:
            dialog_y = node.getY() + self.node_size // 2 - dialog.height()

        # Калибруем по типу ноды
        if node.getEndNode():
            dialog_x -= self.node_size // 4
            dialog_y -= self.node_size // 4

        return dialog_x, dialog_y
    
    def create_dialog(self, type: str, current_node: Node):
        if self.dialog:
            return
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
        click_pos = [event.x(), event.y()]
        if event.button() == 2:  # Правая кнопка мыши
            clicked_node = self.root.graphTraverse(
                lambda node: node.findNode(click_pos, self.node_size)
            )
            if clicked_node:
                # if self.setting_costs_mode:
                if self.mode == 'costs':
                    if clicked_node.getEndNode() or clicked_node.checkChildrenCosts():
                        self.create_dialog('set', clicked_node)
                        # print(self.counter)
                elif self.mode == 'schema':
                    self.create_dialog('add', clicked_node)

        elif event.button() == 1:
            if self.mode == 'arrow':
                # проходим по всем нодам и находим те ноды, между которыми есть стрелка
                limit = 35
                answer = self.root.graphTraverse(
                    lambda node: self.find_arrow(node, limit, click_pos[0], click_pos[1])
                )
                if answer:
                    child, parent = answer
                    if (parent, child) in self.correct_arrows:
                        if child.getBoldArrow():
                            self.selected_arrows.remove((parent, child))
                            child.setBoldArrow(False)
                        else:
                            self.selected_arrows.add((parent, child))
                            child.setBoldArrow(True)
                    else:
                        if child.getBoldArrow():
                            # counter
                            self.selected_arrows.remove((parent, child))
                            child.setBoldArrow(False)
                        else:
                            # counter
                            self.counter += 1
                            self.selected_arrows.add((parent, child))
                            child.setBoldArrow(True)
                    self.update()

                if self.selected_arrows == self.correct_arrows:
                    self.checkingTask()
                '''
                if answer: 
                    (child, parent) = answer
                    if child.getBoldArrow():
                        child.setBoldArrow(False) 
                        self.counter -= 1
                    else:
                        child.setBoldArrow(True)
                    print(self.root.checkTask())
                    if self.root.checkTask(): 
                        self.checkingTask()'''

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
        self.setWindowTitle(self.title + f" - Вариант {self.task_number}")
        self.update()

    # вычисляет расстояние от клика до стрелки
    def calculate_distance(self, child: 'Node', x, y):
        parent = child.getParent()

        if child.getX() == parent.getX(): 
            if y >= parent.getY() and y <= child.getY():
                d = abs(x - child.getX())
            else:
                d = 1000
        else:
            if y <= child.getY() and y >= parent.getY() and ((x <= child.getX() and x >= parent.getX()) or (x >= child.getX() and x <= parent.getX())):
                A = parent.getY() - child.getY()
                B = child.getX() - parent.getX()
                C = child.getY() * parent.getX() - child.getX() * parent.getY()

                d = abs(A * x + B * y + C) / sqrt(A**2 + B**2)
            else:
                d = 1000
        return d

    # вычисляем расстояние до всех стрелок (в данном случае до одной из стрелок)
    def find_arrow(self, node: 'Node', limit, x, y):
        if node.checkArrow(self.root):
            (child, parent) = node.checkArrow(self.root)
            parent = child.getParent()
            if self.calculate_distance(child, x, y) != -1 and self.calculate_distance(child, x, y) <= limit:
                #if not node.checkBoldArrow(): self.counter += 1
                return (child, parent)
            else:
                return None


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
        self.counter = 0
        self.correct_arrows = set()
        self.selected_arrows = set()
        self.root.deleteChildren()
        self.root.setCosts(())
        self.tree_height = 1
        self.setWindowTitle(self.title)
        self.qmenu.setTitle("Построение схемы")
        self.mode = 'schema'
        self.schemaAction.setEnabled(True)
        self.costsAction.setEnabled(True)
        self.update()

    def buildSchema(self):
        self.mode = 'schema'
        self.qmenu.setTitle('Построение схемы')

    def settingCosts(self):
        self.mode = 'costs'
        self.qmenu.setTitle('Задание выигрышей')

    def selectingArrows(self):
        if self.root.checkAllCosts():
            self.mode = 'arrow'
            self.qmenu.setTitle('Выбор стрелок')
            self.schemaAction.setEnabled(False)
            self.costsAction.setEnabled(False)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Сообщение об ошибке")
            msg.setText("Заданы не все выигрыши!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        
    def get_root(self):
        return self.root

    def set_task_number(self, num: int):
        self.task_number = num

    def set_node_cost(self, node: Node, costs: Tuple[int]):
        node.setCosts(costs)

    def checkingTask(self):
        msg = QMessageBox()
        msg.setWindowTitle("Решение завершено")
        msg.setText("Задача решена верно!\nКоличество ошибок: " + str(self.counter))
        msg.setIcon(QMessageBox.Information)
        msg.exec_()