from PySide6.QtWidgets import QFormLayout, QWidget, QApplication, QPushButton
from components.general.formElement import Element
from typing import List

class Form(QFormLayout):
    def __init__(self) -> None:
        super().__init__()

    def addRows(self, *args: List[Element]):
        for i in args:
            self.addRow(i.firstElement, i.secondElement)
    