from PySide6.QtWidgets import QHBoxLayout, QPushButton

class Dashboard(QHBoxLayout):
    def __init__(self):
        super().__init__()
        btn1 = QPushButton("Dashboard")
        self.addWidget(btn1)

        