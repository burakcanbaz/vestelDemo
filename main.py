import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication
from main_window import VestelMainWindow
from mainWindow import  MainWindow
from utils.utils import *


if __name__ == "__main__":
    app = QApplication()
    # resolution = getScreenGeometry()
    window = MainWindow()
    # window.setGeometry(resolution)
    window.show()
    sys.exit(app.exec())