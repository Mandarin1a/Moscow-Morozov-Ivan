from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.flag = True
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radius = randint(1, 100)
        qp.drawEllipse(100, 50, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())