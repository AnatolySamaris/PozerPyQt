import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from frontend.SetDialog import SetDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        self.setDialog = SetDialog(self, 100)
        self.setDialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())