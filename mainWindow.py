import os
import queue
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QStackedLayout, QFormLayout, QHBoxLayout, QVBoxLayout, QGridLayout, QTreeView, QSizePolicy, QLineEdit, QLabel
from PySide6.QtCore import Signal
from vestelUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self, parent=None) -> None:
		super().__init__(parent)
		self.setupUi(self)
		self.setMinimumSize(1440, 900)
		
		

	