import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем объекты QLabel и задаем им текст и координаты
        self.labels = [
            {'text': 'Label 1', 'x': 100, 'y': 100},
            {'text': 'Label 2', 'x': 200, 'y': 200},
            {'text': 'Label 3', 'x': 300, 'y': 300},
            {'text': 'Label 4', 'x': 400, 'y': 400}
        ]

        self.set_labels()

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Labels')
        self.show()

    def set_labels(self):
        for label_data in self.labels:
            label = QLabel(self)
            label.setText(label_data['text'])
            label.move(label_data['x'], label_data['y'])
            label.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
