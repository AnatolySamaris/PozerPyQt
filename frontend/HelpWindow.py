from PyQt5.QtWidgets import QMainWindow, QDesktopWidget


class HelpWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Справка")
        self.setGeometry(300, 300, 400, 300)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())