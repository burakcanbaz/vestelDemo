from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QStackedLayout, QFormLayout, QHBoxLayout, QVBoxLayout, QGridLayout, QTreeView, QSizePolicy, QLineEdit, QLabel
from components.general.form import Form
from components.general.formElement import Element
from Layouts import dashboard, footer, sidebar

class VestelMainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self._setMainLayout(widget)
        self._outlineLayoutDesign(widget) # taslak(genel) layout dizaynı

    def _setMainLayout(self, wd):
        self.mainLayout = QGridLayout()
        wd.setLayout(self.mainLayout)

    def _outlineLayoutDesign(self, mainWidget):
        self.imageHbox = dashboard.Dashboard()
        self.toolsVbox = sidebar.Side()
        self.footerHbox = footer.Footer()

        self.mainLayout.addLayout(self.imageHbox, 0, 0)
        self.mainLayout.addLayout(self.toolsVbox, 0, 5)
        self.mainLayout.addLayout(self.footerHbox, 1, 0)

        self.mainLayout.setRowStretch(0, 5)
        # self.mainLayout.setColumnStretch(0, 5)
        # self.mainLayout.setColumnStretch(5, 3)
        self.mainLayout.setRowStretch(1, 2)