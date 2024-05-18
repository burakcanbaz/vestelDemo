from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Signal, QObject


class SegmentedButton(QWidget):
    indexChanged = Signal(int)

    def __init__(self, labels, startColor = None, endColor = None, parent: QObject = None):
        super().__init__(parent)
        self.buttons = []
        self.selected_index = -1
        self.startColor = startColor
        self.endColor = endColor

        self.setStyleSheet('''
            QPushButton#segmentedButton {
                color: black;
                border-radius: 0px;
                font: 63 12pt "Yu Gothic UI Semibold\";
                font-weight: 500;
                border: 1px solid;
                background-color: ''' + self.startColor  + ''';
            }
            
            QPushButton#segmentedButton[selected="true"] {
                background-color: ''' + self.endColor + ''';
                color: white;
            }
            
            QPushButton#segmentedButton[first="true"] {
                border-top-left-radius: 2px;
                border-bottom-left-radius: 2px;
            }

            QPushButton#segmentedButton[last="true"] {
                border-top-right-radius: 2px;
                border-bottom-right-radius: 2px;
            }

            QPushButton#segmentedButton[first="false"] {
                border-left: 0px;
            }
        ''')

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        for i, label in enumerate(labels):
            button = QPushButton(label)
            button.setObjectName("segmentedButton")
            button.clicked.connect(lambda _, index=i: self.setSelectedIndex(index))

            layout.addWidget(button)
            self.buttons.append(button)

        self.setLayout(layout)
        self.setButtonStyles()

    def setButtonStyles(self):
        for i, button in enumerate(self.buttons):
            button.setProperty("first", i == 0)
            button.setProperty("last", i == (len(self.buttons)-1))
            button.setProperty("selected", i == self.selected_index)
            button.style().unpolish(button)
            button.style().polish(button)
            button.update()

    def setSelectedIndex(self, index):
        if 0 <= index < len(self.buttons) and index != self.selected_index:
            self.selected_index = index
            self.setButtonStyles()
            self.indexChanged.emit(index)