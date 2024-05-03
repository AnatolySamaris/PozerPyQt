from PyQt5.QtWidgets import QApplication
import sys


sys.path.append('./backend')
sys.path.append('./frontend')


from frontend.DrawingWindow import DrawingWindow


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = DrawingWindow()
    window.show()
    sys.exit(App.exec())
