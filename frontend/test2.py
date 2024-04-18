from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        # Рисуем закрашенный черный кружок
        qp.setBrush(QColor(0, 0, 0))  # Черный цвет
        qp.setPen(Qt.NoPen)  # Убираем обводку
        qp.drawEllipse(50, 50, 100, 100)

        # Рисуем незакрашенный кружок
        qp.setBrush(Qt.NoBrush)  # Убираем закрашивание
        qp.setPen(QColor(0, 0, 0))  # Черный цвет обводки
        qp.drawEllipse(200, 50, 100, 100)

        qp.end()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec_()
