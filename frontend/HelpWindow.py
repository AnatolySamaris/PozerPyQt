# from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QAction, QTabWidget, QVBoxLayout, QLabel, QTextEdit
# from PyQt5.QtGui import QPalette, QColor


# class HelpWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Справка")
#         self.setGeometry(300, 300, 800, 700)
#         self.center()

#         # Создаем горизонтальное меню
#         self.menu = self.menuBar()

#         # Создаем пункты меню
#         # self.general_info_action = QAction("Общие сведения", self)
#         # self.file_load_action = QAction("Загрузка из файла", self)
#         # self.scheme_building_action = QAction("Построение схемы", self)
#         # self.wins_assignment_action = QAction("Задание выигрышей", self)

#         self.tab_widget = QTabWidget(self)
#         self.tab_widget.addTab(QLabel("Инструкции по общим сведениям"), "Общие сведения")
#         self.tab_widget.addTab(QLabel("Инструкции по загрузке из файла"), "Загрузка из файла")
#         self.tab_widget.addTab(QLabel("Инструкции по построению схемы"), "Построение схемы")
#         self.tab_widget.addTab(QLabel("Инструкции по заданию выигрышей"), "Задание выигрышей")

#         # Добавляем пункты в меню
#         self.menu.addAction(self.general_info_action)
#         self.menu.addAction(self.file_load_action)
#         self.menu.addAction(self.scheme_building_action)
#         self.menu.addAction(self.wins_assignment_action)

#         # Подключаем сигналы от пунктов меню к слотам
#         self.general_info_action.triggered.connect(self.showGeneralInfo)
#         self.file_load_action.triggered.connect(self.showFileLoad)
#         self.scheme_building_action.triggered.connect(self.showSchemeBuilding)
#         self.wins_assignment_action.triggered.connect(self.showWinsAssignment)

#         # # Создаем виджет для отображения инструкций
#         # self.text_edit = QTextEdit(self)
#         # # Запрещаем редактирование текста
#         # self.text_edit.setReadOnly(True)
#         # self.setCentralWidget(self.text_edit)
#         # self.show()

#         # Создаем виджет для отображения инструкций
#         # self.tab_widget = QTabWidget(self)
#         # self.tab_widget.addTab(QLabel("Инструкции по общим сведениям"), "Общие сведения")
#         # self.tab_widget.addTab(QLabel("Инструкции по загрузке из файла"), "Загрузка из файла")
#         # self.tab_widget.addTab(QLabel("Инструкции по построению схемы"), "Построение схемы")
#         # self.tab_widget.addTab(QLabel("Инструкции по заданию выигрышей"), "Задание выигрышей")
#         # self.tab_widget.setCurrentIndex(0)  # Устанавливаем индекс вкладки "Общие сведения"

#         self.setCentralWidget(self.tab_widget)
#         self.show()

#     def showGeneralInfo(self):
#         # self.text_edit.setText("Инструкции по общим сведениям")
#         self.tab_widget.setCurrentIndex(0)
#         self.setButtonSelected()

#     def showFileLoad(self):
#         # self.text_edit.setText("Инструкции по загрузке из файла")
#         self.tab_widget.setCurrentIndex(1)
#         self.setButtonSelected()

#     def showSchemeBuilding(self):
#         # self.text_edit.setText("Инструкции по построению схемы")
#         self.tab_widget.setCurrentIndex(2)
#         self.setButtonSelected()

#     def showWinsAssignment(self):
#         # self.text_edit.setText("Инструкции по заданию выигрышей")
#         self.tab_widget.setCurrentIndex(3)
#         self.setButtonSelected()
    
#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())

#     def show_content(self, title):
#         # Создание вкладки с текстом инструкции
#         tab = QVBoxLayout()
#         tab.addWidget(QLabel(f'Инструкция для "{title}"'))
#         self.tab_widget.clear()
#         self.tab_widget.addTab(tab, title)

#     def setButtonSelected(self):
#         # Применяем стиль для выделения выбранной кнопки
#         style = f"""
#             QAction:checked {{
#                 background-color: rgb(192, 192, 192);
#             }}
#         """
#         self.setStyleSheet(style)


from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QAction, QTabWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextOption, QFont

class HelpWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Справка")
        self.setGeometry(300, 300, 800, 700)
        self.center()

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        # self.label_2.setFont(font)

        self.text_general = QTextEdit("""
            При запуске программы пользователь может выбрать один из двух режимов работы:<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- ввод из файла<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- ручной ввод<br> 
            Режим ручного ввода задан по умолчанию, при необходимости его можно изменить с помощью кнопки "режим работы"<br> <br> 

            При решении задачи пользователь может работать в двух режимах:<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- построение схемы<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- задание выигрышей<br> 
            Режим решения переключается правой кнопкой меню: в режиме построения схемы она имеет название "задать выигрыши", в режиме задания выигрышей - "построить схему".<br> 
        """)

        self.text_load = QTextEdit("""
            Пользователь может использовать один из 100 готовых вариантов.<br> 
            Для этого необходимо кликнуть по кнопке "режим работы" и выбрать режим работы "ввод из файла", а затем указать номер нужного варианта - от 1 до 100.
        """)

        self.text_schema = QTextEdit("""
            Пользователь находится в режиме построения схемы, если самая правая кнопка меню имеет название "задать выигрыши". <br> 
            Для того чтобы добавить дочернюю вершину к какой-либо вершине, необходимо кликнуть по родительской вершине правой кнопкой мыши.<br> 
            Появится всплывающее окошко с 2 вариантами действий: <br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- добавить потомка <br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- добавить лист <br> 
            При этом потомок - обычная вершина; лист - конечная вершина, которая не будет иметь потомков.<br> 
            После выбора необходимого вида потомка, он добавится к родительской вершине.<br> 
            Чтобы закрыть окно добавления потомка, достаточно кликнуть за его пределами.<br> 
            ОГРАНИЧЕНИЕ: к листам нельзя добавлять потомков.
        """)

        self.text_costs = QTextEdit("""
            Для переключения в режим задания выигрышей пользователю необходимо нажать кнопку "задать выигрыши".<br> 
            (Для обратного переключания в режим построения схемы - нажать кнопку "построить схему").<br> 
            Для того, чтобы задать выигрыши какой-лидо вершине, необходимо кликнуть по ней правой кнопкой мыши.<br> 
            Появится всплывающее окошко, в котором можно будет ввести выигрыш игрока A и выигрыш игрока B. <br> 
            Для проверки и сохранения результата необходимо нажать кнопку "ОК".<br> 
            В случае если какой-либо из выигрышей задан неверно, поле ввода неправильного выигрыша окрасится в красный цвет.<br> 
            Если выигрыши введены правильно, они появятся на схеме, а также автооматически будет нарисована стрелка в соответствии с введенными выигрышами.<br> 
            ОГРАНИЧЕНИЕ: нельзя задавать выигрыши тем вершинам, которые имеют хотя бы одного потомка без выигрышей.
        """)

        self.text_general.setFont(font)
        self.text_load.setFont(font)
        self.text_schema.setFont(font)
        self.text_costs.setFont(font)

        # Создаем виджет для отображения инструкций
        self.tab_widget = QTabWidget(self)
        self.tab_widget.addTab((self.text_general), "Общие сведения")
        self.tab_widget.addTab((self.text_load), "Загрузка из файла")
        self.tab_widget.addTab((self.text_schema), "Построение схемы")
        self.tab_widget.addTab((self.text_costs), "Задание выигрышей")

        # Запрещаем редактирование текста в каждом QTextEdit
        for index in range(self.tab_widget.count()):
            self.text_edit = self.tab_widget.widget(index)
            self.text_edit.setReadOnly(True)
            self.text_edit.setTabChangesFocus(True)
            self.text_edit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.setCentralWidget(self.tab_widget)
        self.show()

    def showGeneralInfo(self):
        self.tab_widget.setCurrentIndex(0)

    def showFileLoad(self):
        self.tab_widget.setCurrentIndex(1)

    def showSchemeBuilding(self):
        self.tab_widget.setCurrentIndex(2)

    def showWinsAssignment(self):
        self.tab_widget.setCurrentIndex(3)
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_content(self, title):
        # Создание вкладки с текстом инструкции
        tab = QVBoxLayout()
        tab.addWidget(QLabel(f'Инструкция для "{title}"'))
        self.tab_widget.clear()
        self.tab_widget.addTab(tab, title)

if __name__ == '__main__':
    app = QApplication([])
    ex = HelpWindow()
    app.exec_()
