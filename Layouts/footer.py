from PySide6.QtWidgets import QGridLayout, QPushButton
from components.footer import footerConnectionControl
class Footer(QGridLayout):
    def __init__(self):
        super().__init__()
        btn1 = footerConnectionControl.FoooterConnectionPanel()
        self.addLayout(btn1, 0, 0)