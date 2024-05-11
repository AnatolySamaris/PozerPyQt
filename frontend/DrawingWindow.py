from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QDialog, QAction, QMessageBox, QMenu

from PyQt5.QtGui import QPainter, QPen, QColor, QFont, QIcon
from PyQt5.QtCore import Qt, QEvent

from .HelpWindow import HelpWindow
from .ModeWindow import ModeWindow
from .AddDialog import AddDialog
from .SetDialog import SetDialog

from backend.Node import Node
from backend.TaskParser import TaskParser

from typing import Tuple, List
from math import sqrt


class DrawingWindow(QMainWindow):
    """
    Главное окно приложения, на котором рисуется дерево игры.
    Параметры рисования задаются в методе __init__, в секции VARIABLES.
    """
    def __init__(self):
        super().__init__()

        #######################
        # === WINDOW CONFIG ===
        #######################
        self.title = "Позиционные игры"
        self.width = 1800
        self.height = 900

        self.setWindowTitle(self.title)
        self.setGeometry(150, 150, self.width, self.height)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setWindowIcon(QIcon('../PosGames.ico'))
        self.center()

        self.installEventFilter(self)

        ##################
        # === MENU BAR ===
        ##################
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

        self.arrowAction = self.qmenu.addAction("Выделение пути")
        self.arrowAction.triggered.connect(self.selectingArrows)

        self.menubar.addMenu(self.qmenu)

        ###################
        # === VARIABLES ===
        ###################
        self.task_number = -1
        self.node_size = 40
        self.arrow_range = 15
        self.letter_size = 16
        self.x_letter_position = int(self.node_size * 0.3)
        self.y_letter_position = int(self.node_size * 0.7)
        self.x_paint_zero = 0
        self.y_paint_zero = 50
        self.mode = 'schema'
        self.arrow_size = 30
        self.error_counter = 0
        self.correct_arrows = set()
        self.selected_arrows = set()
        self.root_x = self.x_paint_zero + self.width // 2 - self.node_size
        self.root_y = self.y_paint_zero
        self.add_dialog_opened = False
        self.dialog = None

        #############################
        # === TREE INITIALIZATION ===
        #############################
        self.tree_height = 1
        self.root = Node(1, None, self.root_x, self.root_y)

    #######################
    # === WINDOW EVENTS ===
    #######################

    def paintEvent(self, event) -> None:
        """
        Обработчик отрисовки окна. Срабатывает каждый раз, когда меняется состояние окна.
        """
        painter = QPainter(self)
        painter.setFont(QFont('Arial', self.letter_size))
        painter.setPen(QPen(QColor(Qt.black), 2))
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.draw_tree(painter)
        painter.end()
    
    def resizeEvent(self, event) -> None:
        """
        Обработчик изменения размера окна. При изменении размера окна пересчитывает
        положение вершин и перерисовывает дерево, а также закрывает открытые диалоги.
        """
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

    def eventFilter(self, obj, event):
        """
        Обработчик нажатия за пределами диалогового окна.
        """
        if event.type() == QEvent.MouseButtonPress:
            if self.dialog and not self.dialog.geometry().contains(event.globalPos()):
                self.dialog.close()
                self.dialog = None
                self.add_dialog_opened = False
        return super().eventFilter(obj, event)
    
    def mousePressEvent(self, event) -> None:
        """
        Обработчик нажатия на кнопку мыши. При клике правой кнопкой по вершине
        открывает диалоговое окно в зависимости от текущего режима работы.
        При клике левой кнопкой по стрелке (в режиме выбора пути) выделяет стрелку.
        Если все стрелки выделены правильно, задача решена.
        """

        click_pos = [event.x(), event.y()]

        # Левая кнопка мыши
        if event.button() == 1:
            if self.mode == 'arrow':
                answer = self.root.graphTraverse(
                    lambda node: self.find_arrow(node, click_pos[0], click_pos[1])
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
                            self.selected_arrows.remove((parent, child))
                            child.setBoldArrow(False)
                        else:
                            self.error_counter += 1
                            self.selected_arrows.add((parent, child))
                            child.setBoldArrow(True)
                    self.update()
                if self.selected_arrows == self.correct_arrows:
                    self.show_end_window()

        # Правая кнопка мыши
        elif event.button() == 2:
            clicked_node = self.root.graphTraverse(
                lambda node: node.findNode(click_pos, self.node_size)
            )
            if clicked_node:
                if self.mode == 'costs':
                    if clicked_node.getEndNode() or clicked_node.checkChildrenCosts():
                        self.create_dialog('set', clicked_node)
                elif self.mode == 'schema':
                    self.create_dialog('add', clicked_node)

    #############################
    # === OBJECTS CALIBRATION ===
    #############################
    
    def calibrate_cost_label(self, node: Node, text: str) -> Tuple[int]:
        """
        Расчитывает положение лейбла с выигрышами в зависимости от
        типа вершины и её положения среди потомков родителя.
        """
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
    
    def calibrate_dialog_window_pos(self, dialog: QDialog, node: Node) -> Tuple[int]:
        """
        Расчитывает положение диалогового окна в зависимости от
        положения выбранной вершины и размеров главного окна.
        """
        dialog_x, dialog_y = 0, 0
        if node.getX() + self.node_size + dialog.width() > self.width:
            dialog_x = node.getX() - dialog.width()
        else:
            dialog_x = node.getX() + self.node_size
        if node.getY() + self.node_size // 2 - dialog.height() < 0:
            dialog_y = node.getY() + self.node_size // 2
        else:
            dialog_y = node.getY() + self.node_size // 2 - dialog.height()
        if node.getEndNode():
            dialog_x -= self.node_size // 4
            dialog_y -= self.node_size // 4
        return dialog_x, dialog_y
    
    #########################
    # === DRAWING OBJECTS ===
    #########################

    def draw_tree(self, painter: QPainter) -> None:
        """
        С помощью нескольких рекурсивных обходов рисует дерево решения.
        """
        self.root.graphTraverse(
            lambda node: self.draw_node(painter, node)
        )
        self.root.graphTraverse(
            lambda node: self.draw_line(painter, node.getParent(), node)
        )
        self.root.graphTraverse(
            lambda node: self.draw_arrow(node.getParent(), node)
        )
        if self.root.getCosts() and len(self.correct_arrows) == 0:
            self.get_completed_task(self.root)

    def draw_cost_label(self, painter: QPainter, node: Node) -> None:
        """
        Рисует лейбл выигрышей рядом с вершиной.
        """
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

    def draw_node(self, painter: QPainter, node: Node) -> None:
        """
        Рисует вершину дерева.
        """
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
        self.draw_cost_label(painter, node)

    def draw_line(self, painter: QPainter, from_node: Node, to_node: Node) -> None:
        """
        Рисует соединительную линию от вершины from_node к вершине to_node.
        """
        if not from_node:
            return
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

    def draw_arrow(self, from_node: Node, to_node: Node, task_completed=False) -> None:
        """
        На основе соединяющей линии рисует стрелку от вершины from_node к вершине to_node.
        """
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
            w, h = 5, 12

            x3 = int(x2 - h * l[0] + w * n[0])
            y3 = int(y2 - h * l[1] + w * n[1])
            x4 = int(x2 - h * l[0] - w * n[0])
            y4 = int(y2 - h * l[1] - w * n[1])

            painter.drawLine(x2, y2, x3, y3)
            painter.drawLine(x2, y2, x4, y4)
            painter.end()

    ##########################
    # === CREATING OBJECTS ===
    ##########################

    def create_node(self, parent, leaf=False) -> None:
        """
        Создает вершину дерева. Если родитель не передан - создается корень дерева.
        """
        if parent is None:
            self.root = Node(1)
        else:
            child = Node(parent.getLevel() + 1, parent)
            if leaf:
                child.setEndNode(True)
            parent.addChild(child)
        self.tree_height = self.root.updateTreeHeight(self.tree_height)
        self.root.graphTraverse(
            lambda node: node.recalculateNode(
                self.root, self.height, self.width,
                self.y_paint_zero, self.x_paint_zero,
                self.node_size, self.tree_height
            )
        )

    def create_dialog(self, type: str, current_node: Node) -> None:
        """
        Создает и показывает диалоговое окно рядом с выбранной вершиной.
        """
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

    ###########################
    # === UTILITY FUNCTIONS ===
    ###########################
    
    def show_end_window(self) -> None:
        """
        Создает и показывает информационное окно об окончании решения,
        выводя также количество совершенных ошибок.
        """
        msg = QMessageBox()
        msg.setWindowTitle("Решение завершено")
        msg.setText("Задача решена верно!\nКоличество ошибок: " + str(self.error_counter))
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def get_completed_task(self, node: Node) -> None:
        """
        Заполняет множество стрелок, соответствующих правильному решению.
        """
        node_costs = node.getCosts()
        for child in node.getChildren():
            if child.getCosts() == node_costs:
                self.correct_arrows.add((node, child))
                self.get_completed_task(child)
                break

    def calculate_distance(self, child: Node, x: int, y: int) -> float:
        """
        Рассчитывает расстояние от клика до линии. Для учета конечной длины стрелки
        проверяет, находится ли точка клика между перпендикулярными прямыми, проходящими
        через начальную и конечную точки линии. Иначе возвращает большое значение расстояния.
        """
        parent = child.getParent()
        x1, y1 = parent.getX() + self.node_size // 2, parent.getY() + self.node_size
        x2, y2 = child.getX() + self.node_size // 2, child.getY()
        A, B, C = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
        n1 = B * x - A * y + (A * y1 - B * x1)
        n2 = B * x - A * y + (A * y2 - B * x2)
        if n1 * n2 <= 0:
            d = abs(A * x + B * y + C) / sqrt(A ** 2 + B ** 2)
        else:
            d = 10000.0
        return d

    def find_arrow(self, node: Node, x: int, y: int):
        """
        Проверяет, выбрана ли стрелка. Если да - возвращает потомка и родителя.
        Иначе возвращает None.
        """
        if node.checkArrow(self.root):
            (child, parent) = node.checkArrow(self.root)
            parent = child.getParent()
            if self.calculate_distance(child, x, y) <= self.arrow_range:
                return (child, parent)
            else:
                return None
            
    def center(self) -> None:
        """
        Устанавливает окно по центру экрана.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    ######################
    # === PARSING TASK ===
    ######################

    def get_task_tree(self) -> None:
        """
        Запускает парсер для считывания варианта задания.
        Генерирует задание по варианту и автоматически рисует его.
        """
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

    ########################
    # === WINDOW BUTTONS ===
    ########################

    def buildSchema(self):
        self.mode = 'schema'
        self.qmenu.setTitle('Построение схемы')

    def settingCosts(self):
        self.mode = 'costs'
        self.qmenu.setTitle('Задание выигрышей')

    def selectingArrows(self):
        if self.root.checkAllCosts():
            self.mode = 'arrow'
            self.qmenu.setTitle('Выделение пути')
            self.schemaAction.setEnabled(False)
            self.costsAction.setEnabled(False)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Сообщение об ошибке")
            msg.setText("Заданы не все выигрыши!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def showHelpMenu(self):
        help_window = HelpWindow(self)
        help_window.show()

    def showModeActionMenu(self):
        mode_window = ModeWindow(self)
        mode_window.show()

    def clearField(self):
        self.error_counter = 0
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

    #########################
    # === OUTER FUNCTIONS ===
    #########################
        
    def get_root(self):
        return self.root

    def set_task_number(self, num: int):
        self.task_number = num

    def set_node_cost(self, node: Node, costs: Tuple[int]):
        node.setCosts(costs)
    
    def increment_counter(self, counter):
        self.error_counter += counter

    def update_nodes_pos(self):
        self.root.graphTraverse(
            lambda node: node.recalculateNode(
                self.root, self.height, self.width,
                self.y_paint_zero, self.x_paint_zero,
                self.node_size, self.tree_height
            )
        )
