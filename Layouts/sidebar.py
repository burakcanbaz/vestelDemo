from PySide6.QtWidgets import QVBoxLayout, QPushButton

class Side(QVBoxLayout):
    def __init__(self):
        super().__init__()
        btn1 = QPushButton("Side")
        self.addWidget(btn1)

        