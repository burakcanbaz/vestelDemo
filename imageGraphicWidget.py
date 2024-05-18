import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QVBoxLayout, QFrame, QGraphicsTextItem
from PySide6.QtGui import QPixmap, QPen, QColor, QPainter
from PySide6.QtCore import Qt


class CustomGraphicsView(QGraphicsView):
    def __init__(self, *args):
        super().__init__(*args)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.scale_factor = 1.2

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.scale(self.scale_factor, self.scale_factor)
        else:
            self.scale(1 / self.scale_factor, 1 / self.scale_factor)

class graphOnImage(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("PhotoAndGraphFrame")

        self.scene = QGraphicsScene()
        self.view = CustomGraphicsView(self.scene)

        layout = QVBoxLayout(self)
        layout.addWidget(self.view)

        # self.setStyleSheet("background-color: white;")  # Arka plan rengini beyaza ayarla

        # Fotoğrafı yükle
        photo = QPixmap("C:\\Users\\Burak\\Desktop\\kurutma.jpg")
        photo_height = 800
        photo_width = int(photo.width() * (photo_height / photo.height())) + 100
        self.photo = QGraphicsPixmapItem(photo.scaled(photo_width, photo_height))
        self.scene.addItem(self.photo)

        # Fotoğrafı arayüzün tam ortasına yerleştir
        self.photo.setPos((self.view.width() - photo_width) / 2, (self.view.height() - photo_height) / 2)

        # Grafik fotoğrafın genişliğine eşitlenecek
        self.graph_width = photo_width
        self.graph_height = 50  # Grafik yüksekliği
        self.graph_left = (self.view.width() - self.graph_width) / 2
        self.graph_top = (self.view.height() + photo_height) / 2 - 188 # Fotoğrafın altından başlayacak

        # Grafik çizimi için yatay çizgi oluştur
        self.draw_horizontal_line()

        # Grafik üzerinde 1'den 10'a kadar olan sayılar
        self.draw_ticks()

    def draw_horizontal_line(self):
        pen = QPen(Qt.black)
        pen.setWidth(2)
        line = self.scene.addLine(self.graph_left, self.graph_top, self.graph_left + self.graph_width, self.graph_top, pen)

    def draw_ticks(self):
        partsOfImage = [10, 20, 30, 40, 50, 60]
        pen = QPen(Qt.black)
        pen.setWidth(1)
        for i in range(1, 30):
            x_position = self.graph_left + i * (self.graph_width / 30)
            tick_line = self.scene.addLine(x_position, self.graph_top - 5, x_position, self.graph_top + 5, pen)

            # Dikey tireler
            if i % 5 == 0:
                tick_line = self.scene.addLine(x_position, self.graph_top - 30, x_position, self.graph_top + 50, pen)
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
                rect_item = self.scene.addRect(
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