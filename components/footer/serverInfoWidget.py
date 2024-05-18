from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel


class ServerInfoWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Form layout oluştur
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        # Server IP satırı
        self.label_ip = QLabel("Server IP:")
        self.line_edit_ip = QLineEdit()
        form_layout.addRow(self.label_ip, self.line_edit_ip)

        # Server Port satırı
        self.label_port = QLabel("Server Port:")
        self.line_edit_port = QLineEdit()
        form_layout.addRow(self.label_port, self.line_edit_port)

    def get_server_info(self):
        ip = self.line_edit_ip.text()
        port = self.line_edit_port.text()
        return ip, port
