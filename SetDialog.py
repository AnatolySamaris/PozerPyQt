from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem
from PyQt5 import QtCore, QtWidgets

class SetDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Set Dialog")
        self.setMinimumSize(230, 150)
        self.setMaximumSize(230, 150)
        self.setStyleSheet("QDialog { background-color: #e5e5e5; border: 1px solid black; }")

        layout = QVBoxLayout(self)

        label = QLabel("Enter your winnings:", self)
        layout.addWidget(label)

        hlayout = QHBoxLayout()
        layout.addLayout(hlayout)

        label_2 = QLabel("(", self)
        hlayout.addWidget(label_2)

        self.lineEdit = QLineEdit(self)
        hlayout.addWidget(self.lineEdit)

        label_3 = QLabel(";", self)
        hlayout.addWidget(label_3)

        self.lineEdit_2 = QLineEdit(self)
        hlayout.addWidget(self.lineEdit_2)

        label_4 = QLabel(")", self)
        hlayout.addWidget(label_4)

        hlayout_2 = QHBoxLayout()
        layout.addLayout(hlayout_2)

        spacerItem = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        hlayout_2.addItem(spacerItem)

        self.pushButton = QPushButton("OK", self)
        hlayout_2.addWidget(self.pushButton)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        label.show()
        label_2.show()
        label_3.show()
        label_4.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = SetDialog()
    dialog.show()
    sys.exit(app.exec())