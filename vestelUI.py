# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vestelLastUIUpdate2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
from imageGraphicWidget import graphOnImage
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1339, 923)
        MainWindow.setStyleSheet(u"font-size: 22px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = graphOnImage()
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: #f7f4f3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_50 = QLabel(self.widget)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font: 22px; font-weight: bold; ")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_50)

        self.label_45 = QLabel(self.widget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 200))
        self.label_45.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"font-size: 40px;\n"
"border-radius: 5px;\n"
"")
        self.label_45.setFrameShadow(QFrame.Plain)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_45)

        self.label_53 = QLabel(self.widget)
        self.label_53.setObjectName(u"label_53")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy)
        self.label_53.setLayoutDirection(Qt.LeftToRight)
        self.label_53.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"font-size: 22px;\n"
"border-radius: 5px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_53)

        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 12)
        self.verticalLayout_6.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setStyleSheet(u"font: 12px; border-bottom-width: 1px; border-bottom-style: solid")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 16px; font-weight:bold; ")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setStyleSheet(u"font: 12px; border-bottom-width: 1px; border-bottom-style: solid")
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size: 22px; font-weight: bold;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 2)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(70, 0))
        self.label_9.setMaximumSize(QSize(70, 70))
        self.label_9.setStyleSheet(u"font: 16px; font-weight:bold; ")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_9, 1, 0, 1, 1)

        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 1)
        self.gridLayout_6.setRowStretch(2, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 150))
        self.label.setStyleSheet(u"image: url(:/spechtLab Logo/logo-main.png);")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(100, 150))
        self.label_2.setMaximumSize(QSize(123123, 123213))
        self.label_2.setStyleSheet(u"image: url(:/vestel/vestel_logo.png);")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(2, 2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout_2.addWidget(self.widget, 0, 1, 2, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: #f7f4f3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_42 = QLabel(self.widget_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(250, 0))
        self.label_42.setMaximumSize(QSize(100, 16777215))
        self.label_42.setStyleSheet(u"font: 12px; ")
        self.label_42.setFrameShadow(QFrame.Plain)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_42, 0, 1, 1, 1)

        self.label_40 = QLabel(self.widget_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(100, 16777215))
        self.label_40.setStyleSheet(u"font: 12px; font-weight:bold; ")
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_40, 1, 0, 1, 1)

        self.label_41 = QLabel(self.widget_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(250, 0))
        self.label_41.setStyleSheet(u"font: 12px; ")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_41, 1, 1, 1, 1)

        self.label_43 = QLabel(self.widget_2)
        self.label_43.setObjectName(u"label_43")
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        self.label_43.setMinimumSize(QSize(0, 0))
        self.label_43.setMaximumSize(QSize(100, 16777215))
        self.label_43.setStyleSheet(u"font: 12px; font-weight:bold; ")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_43, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(16777215, 55))
        self.pushButton_5.setStyleSheet(u"background-color: #55a630;\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(16777215, 55))
        self.pushButton_6.setStyleSheet(u"background-color: #bb010b;")

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 2, 2, 1)

        self.gridLayout_8.setColumnStretch(0, 5)

        self.horizontalLayout_2.addLayout(self.gridLayout_8)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 10)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setColumnStretch(0, 8)
        self.gridLayout_2.setColumnStretch(1, 2)

        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1339, 36))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"spechtLab Profile Measurement", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u" FPS:", None))
        self.label_7.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"STEP:", None))
        self.label_6.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"INFORMATIONS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"GAP:", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_42.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"SERVER PORT :", None))
        self.label_41.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"SERVER IP :", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"DISCONNECT", None))
    # retranslateUi

