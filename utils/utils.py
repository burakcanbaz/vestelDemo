from PySide6.QtGui import QGuiApplication


def getScreenGeometry():
    return QGuiApplication.primaryScreen().availableGeometry()