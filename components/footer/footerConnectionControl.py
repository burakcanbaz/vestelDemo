from PySide6.QtWidgets import QGridLayout, QLabel, QLineEdit, QSizePolicy, QPushButton
from components.general import spechtButton
from components.general.formElement import Element
from components.general.form import Form
from components.footer import serverInfoWidget

class FoooterConnectionPanel(QGridLayout):
    def __init__(self):
        line1 = QLineEdit()
        line2 = QLineEdit()
        
        super().__init__()
        btnSizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        a = QLabel("test")
        b = QLabel("test2")
        a.setStyleSheet("background-color: white;")
        b.setStyleSheet("background-color: white;")
        self.addWidget(QLabel("T1"), 0, 0)
        self.addWidget(a, 0, 1)
        self.addWidget(QLabel("T2"), 1, 0)
        self.addWidget(b, 1, 1)
        self.addWidget(spechtButton.SegmentedButton(["DISCONNECT"], '#f51105', '#bd1108', ), 0, 2, 2, 2)