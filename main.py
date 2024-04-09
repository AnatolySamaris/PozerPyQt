from PyQt5.QtWidgets import QApplication
from frontend.DrawingWindow import DrawingWindow
import sys


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = DrawingWindow()
    window.show()
    sys.exit(App.exec())