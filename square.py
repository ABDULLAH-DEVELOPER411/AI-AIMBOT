import sys

import json

from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen

class config:
    with open("lib/config/configuration.json") as f:
        config = json.load(f)

fovsquare = config.config["fovsquare"]
fovsize = config.config["fovsize"]

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("FOV Square")
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint 
        )

        # Make the background transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        screen_rect = QtWidgets.qApp.desktop().availableGeometry()

        screen_rect.setHeight(screen_rect.height() + 40)

        self.setGeometry(

            QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
            QtCore.QSize(fovsize, fovsize),
            screen_rect)
        )

    def paintEvent(self, event):
        # Create a QPainter object for drawing
        painter = QPainter(self)
        
        # Set the pen color and thickness for the window frame
        pen = QPen(QColor("white"), 4)
        painter.setPen(pen)
        
        # Draw the window frame
        painter.drawRect(self.rect())


if fovsquare == 1:
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    app.exec_()