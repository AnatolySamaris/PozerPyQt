from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QTabWidget, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class HelpWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Справка")
        self.setFixedSize(800, 500)
        self.center()

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        self.text_general = QTextEdit("""
            Программа позволяет пользователю составить и проверить решение позиционной игры двух игроков.<br><br>
            При запуске программы пользователь может выбрать один из двух режимов работы:<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- ввод из файла;<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- ручной ввод.<br> 
            Режим ручного ввода задан по умолчанию, при необходимости его можно изменить с помощью кнопки "Режим работы". Для переключения между режимами можно использовать стрелки вниз-вверх<br><br> 

            При решении задачи пользователь может работать в двух режимах:<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- построение схемы;<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- задание выигрышей.<br>
            В режиме построения схемы в меню показывается кнопка "Задать выигрыши", в режиме задания выигрышей - кнопка "Построить схему".
        """)

        self.text_load = QTextEdit("""
            Пользователь может использовать один из 100 готовых вариантов. 
            Для этого необходимо кликнуть по кнопке "Режим работы", выбрать опцию "Вариант", затем указать номер нужного варианта от 1 до 100. Для сохранения результата необходимо нажать кнопку "ОК" или кнопку Enter на клавиатуре. <br><br>
                                   
            При некорректном вводе номера варианта поле ввода станет красным и будет показано информационное сообщение.
        """)

        self.text_schema = QTextEdit("""
            Пользователь находится в режиме построения схемы, если в меню отображается кнопка "Задать выигрыши".<br><br>
                                      
            Для того, чтобы добавить дочернюю вершину к какой-либо вершине, необходимо кликнуть по родительской вершине правой кнопкой мыши.<br> 
            Появится всплывающее окно с 3 вариантами действий:<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- Добавить потомка;<br> 
                &nbsp;&nbsp;&nbsp;&nbsp;- Добавить исход;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- Удалить вершину.<br>
            При этом потомок - обычная вершина; исход - конечная вершина, которая не будет иметь потомков.<br> 
            После выбора необходимого вида потомка он добавится к родительской вершине.<br> 
            Чтобы закрыть окно добавления потомка, достаточно кликнуть за его пределами.<br><br>
                                     
            ОГРАНИЧЕНИЕ: к исходам нельзя добавлять потомков.
        """)

        self.text_costs = QTextEdit("""
            Пользователь находится в режиме задания выигрышей, если в меню отображается кнопка "Построить схему".<br><br>
 
            Для того, чтобы задать выигрыши какой-либо вершине, необходимо кликнуть по ней правой кнопкой мыши.<br> 
            Появится всплывающее окно, в котором можно будет ввести выигрыш игрока A и выигрыш игрока B.<br> 
            Для перехода между полями ввода можно воспользоваться стрелками: стрелка вверх - переход в поле ввода выигрыша B, стрелка вниз - переход в поле ввода A. <br>
            Для проверки и сохранения результата необходимо нажать кнопку "ОК" либо кнопку Enter на клавиатуре. <br><br>
            Если выигрыши введены правильно, они появятся на схеме, а также автоматически будет нарисована стрелка к правильному потомку.<br>
            Если выигрыши заданы неверно, поля ввода станут красными.<br><br>
            ОГРАНИЧЕНИЕ: нельзя задавать выигрыши тем вершинам, которые имеют хотя бы одного потомка без выигрышей.
        """)

        self.text_about = QTextEdit("""
            Решение позиционных игр.<br>
            &#169; ЛГТУ, 2024 г <br>
            Седых О.М., Целищев А.Е.
        """)

        self.text_general.setFont(font)
        self.text_load.setFont(font)
        self.text_schema.setFont(font)
        self.text_costs.setFont(font)
        self.text_about.setFont(font)

        # Создаем виджет для отображения инструкций
        self.tab_widget = QTabWidget(self)
        self.tab_widget.addTab((self.text_general), "Общие сведения")
        self.tab_widget.addTab((self.text_load), "Загрузка из файла")
        self.tab_widget.addTab((self.text_schema), "Построение схемы")
        self.tab_widget.addTab((self.text_costs), "Задание выигрышей")
        self.tab_widget.addTab((self.text_about), "О программе")

        # Запрещаем редактирование текста в каждом QTextEdit
        for index in range(self.tab_widget.count()):
            self.text_edit = self.tab_widget.widget(index)
            self.text_edit.setReadOnly(True)
            self.text_edit.setTabChangesFocus(True)
            self.text_edit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.setCentralWidget(self.tab_widget)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
