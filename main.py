import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel, QApplication, QSlider, QWidget
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen, QColor
from math import pi, cos, sin
from PyQt5 import uic
from PyQt5 import QtCore, QtMultimedia


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.player = QtMultimedia.QMediaPlayer()
        self.btnA.clicked.connect(self.run)
        self.btnA.clicked.connect(self.player.play)
        self.btnB.clicked.connect(self.run)
        self.btnB.clicked.connect(self.player.play)
        self.btnC.clicked.connect(self.run)
        self.btnC.clicked.connect(self.player.play)
        self.btnD.clicked.connect(self.run)
        self.btnD.clicked.connect(self.player.play)
        self.btnE.clicked.connect(self.run)
        self.btnE.clicked.connect(self.player.play)
        self.btnF.clicked.connect(self.run)
        self.btnF.clicked.connect(self.player.play)
        self.btnG.clicked.connect(self.run)
        self.btnG.clicked.connect(self.player.play)

    def run(self):
        if self.sender().text() == 'до':
            self.load_mp3('A.mp3')

        elif self.sender().text() == 'ре':
            self.load_mp3('B.mp3')
        elif self.sender().text() == 'ми':
            self.load_mp3('C.mp3')
        elif self.sender().text() == 'фа':
            self.load_mp3('D.mp3')
        elif self.sender().text() == 'соль':
            self.load_mp3('E.mp3')
        elif self.sender().text() == 'ля':
            self.load_mp3('F.mp3')
        elif self.sender().text() == 'си':
            self.load_mp3('G.mp3')

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player.setMedia(content)

    def keyPressEvent(self, event):
        if event.key() == 81:
            self.load_mp3('A.mp3')
            self.player.play()
        if event.key() == 87:
            self.load_mp3('B.mp3')
            self.player.play()
        if event.key() == 69:
            self.load_mp3('C.mp3')
            self.player.play()
        if event.key() == 82:
            self.load_mp3('D.mp3')
            self.player.play()
        if event.key() == 84:
            self.load_mp3('E.mp3')
            self.player.play()
        if event.key() == 89:
            self.load_mp3('F.mp3')
            self.player.play()
        if event.key() == 85:
            self.load_mp3('G.mp3')
            self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
