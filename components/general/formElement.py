from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

class Element(QWidget):
    def __init__(self, elem1: QWidget | str, elem2: QWidget | str):
        super().__init__()
        self.firstElement = elem1
        self.secondElement = elem2