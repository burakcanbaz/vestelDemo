import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QVBoxLayout, QFrame, QGraphicsTextItem
from PySide6.QtGui import QPixmap, QPen, QColor
from PySide6.QtCore import Qt

class graphOnImage(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("PhotoAndGraphFrame")

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        layout = QVBoxLayout(self)
        layout.addWidget(self.view)

        self.setStyleSheet("#PhotoAndGraphFrame { background-color: white; }")  # Arka plan rengini beyaza ayarla

        # Fotoğrafı yükle
        photo = QPixmap("C:\\Users\\Burak\\Desktop\\kurutma_wireFrame.jpg")
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
        pen = QPen(Qt.black)
        pen.setWidth(1)
        for i in range(1, 31):
            x_position = self.graph_left + i * (self.graph_width / 31)
            tick_line = self.scene.addLine(x_position, self.graph_top - 5, x_position, self.graph_top + 5, pen)

            # Dikey tireler
            if i < 10:
                tick_line = self.scene.addLine(x_position, self.graph_top - 2, x_position, self.graph_top + 2, pen)

            # Sayılar
            text_item = QGraphicsTextItem(str(i))
            fnt = self.view.font()
            fnt.setPointSize(fnt.pointSize() + 3)
            text_item.setFont(fnt)
            text_item.setPos(x_position - text_item.boundingRect().width() / 2, self.graph_top - 30)  # Sayıları biraz daha yukarı kaydır

            # Tek sayıları kırmızı, çift sayıları yeşil renkte yap
            if i % 2 == 0:
                text_item.setDefaultTextColor(Qt.green)
            else:
                text_item.setDefaultTextColor(Qt.red)

            self.scene.addItem(text_item)