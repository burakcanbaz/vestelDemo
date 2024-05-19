import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QVBoxLayout, QFrame, QGraphicsTextItem
from PySide6.QtGui import QPixmap, QPen, QColor, QPainter, QWheelEvent, QTransform
from PySide6.QtCore import Qt


class CustomGraphicsView(QGraphicsView):
    def __init__(self, *args):
        super().__init__(*args)
        # self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse) # scaling according to under of current mouse position
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.min_zoom = 1.0
        self.max_zoom = 3.0

    def wheelEvent(self, event: QWheelEvent):
        # Mevcut zoom seviyesini al
        current_zoom = self.transform().m22()

        # Fare tekerleği olayından kaydırma değerini al
        delta = event.angleDelta().y() / 120

        # Yeni zoom seviyesini hesapla
        new_zoom = current_zoom + delta * 0.1

        # Yeni zoom seviyesini minimum ve maksimum zoom seviyeleri arasında sınırla
        new_zoom = min(max(new_zoom, self.min_zoom), self.max_zoom)

        # Yeni zoom seviyesini ayarla
        self.setTransform(QTransform().scale(new_zoom, new_zoom))

class graphOnImage(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("PhotoAndGraphFrame")

        self.scene = QGraphicsScene()
        self.view = CustomGraphicsView(self.scene)

        layout = QVBoxLayout(self)
        layout.addWidget(self.view)

        self.setStyleSheet("QFrame { border: none; background: transparent; }")
 
        self._addPhotoToScene()
        self._setPositionOfPhoto()

    def _addPhotoToScene(self):
        photo = QPixmap("C:\\Users\\Burak\\Desktop\\kurutma.jpg")
        self.photo_height = 800
        self.photo_width = int(photo.width() * (self.photo_height / photo.height())) + 100
        self.photo = QGraphicsPixmapItem(photo.scaled(self.photo_width, self.photo_height))  # can be manipulate this image as a another graphic item on QGraphicScene. 
        self.scene.addItem(self.photo)

    def _setPositionOfPhoto(self):
        # set photo to center of the QFrame
        self.photo.setPos((self.view.width() - self.photo_width) / 2, (self.view.height() - self.photo_height) / 2) # 11, 160
        # graphic width setted the equal size of photo
        self.graph_width = self.photo_width
        self.graph_height = 50  # height of graphic
        self.graph_left = (self.view.width() - self.graph_width) / 2
        self.graph_top = (self.view.height() + self.photo_height) / 2 - 188 # Fotoğrafın altından başlayacak

        # create one-axis graphic line 
        self.draw_horizontal_line()

        # draw ticks on to one-axis graphic line
        self.draw_ticks()

    def draw_horizontal_line(self):
        pen = QPen(Qt.black)
        pen.setWidth(2)
        line = self.scene.addLine(self.graph_left, self.graph_top, self.graph_left + self.graph_width, self.graph_top, pen)

    def draw_ticks(self):
        pen = QPen(Qt.black)
        pen.setWidth(1)
        for i in range(0, 31):
            x_position = self.graph_left + i * (self.graph_width / 30)
            self.scene.addLine(x_position, self.graph_top - 5, x_position, self.graph_top + 5, pen)

            # Dikey tireler
            if i % 5 == 0:
                self.scene.addLine(x_position, self.graph_top - 30, x_position, self.graph_top + 50, pen)
                text_item = QGraphicsTextItem(str(i * 2) + 'cm')
                text_item.setDefaultTextColor(Qt.white)
                fnt = self.view.font()
                fnt.setPointSize(fnt.pointSize() + 5)
                fnt.setBold(True)
                text_item.setFont(fnt)
                text_item.setPos(x_position - text_item.boundingRect().width() / 2, self.graph_top - 35)  # Sayıları biraz daha yukarı kaydır
                self.scene.addItem(text_item)

            # Sayılar
            text_item1 = QGraphicsTextItem(str(i * 2))
            fnt1 = self.view.font()
            fnt1.setBold(True)
            fnt1.setPointSize(fnt1.pointSize() + 3)
            text_item1.setFont(fnt1)
            text_item1.setPos(x_position - text_item1.boundingRect().width() / 2, self.graph_top + 10)
            
            if (i * 2) % 8 == 0:
                text_item1.setDefaultTextColor(Qt.red)
                self.scene.addRect(
                    x_position - (self.graph_width / 60) - (self.graph_width / 60),  # Center the rectangle on the tick
                    self.graph_top - 29,  # Adjust as necessary to fit the region
                    2 * (self.graph_width / 30),  # Width of the rectangle
                    80,  # Height of the rectangle
                    pen,
                    QColor(255, 0, 0, 50)  # Red color with some transparency
                )
            else:
                text_item1.setDefaultTextColor(Qt.green)

            self.scene.addItem(text_item1)