# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Planner program")

        QFontDatabase.addApplicationFont("RobotoMono.ttf")

        self.UiComponents()

    def UiComponents(self):
        fontbold = QFont("Roboto Mono Medium", 15)
        fontboldsmall = QFont("Roboto Mono Medium", 8)
        font = QFont("Roboto Mono", 15)
        fontthin = QFont("Roboto Mono Thin", 15)

        self.blur_effect = QGraphicsBlurEffect()
        self.bgimgplaceholder = QLabel("text", self)
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.7)
        self.pixmap = QPixmap("pictures\cafe.png")
        self.bgimgplaceholder.setPixmap(self.pixmap)
        self.bgimgplaceholder.setGeometry(0, 0, 1200, 200)
        self.bgimgplaceholder.setGraphicsEffect(self.blur_effect)
        self.bgimgplaceholder.setGraphicsEffect(self.opacity_effect)

        self.sidetabbar = QLabel(" ", self)
        self.sidetabbar.setGeometry(0, 200, 200, 800)
        self.sidetabbar.setStyleSheet("background-color : #404040 ")

        self.settitlename = QLineEdit("School work", self)
        self.settitlename.setGeometry(15, 240, 125, 20)
        self.settitlename.setStyleSheet(
            "QLineEdit"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.settitlename.setFont(fontboldsmall)

        self.settitlebtn = QPushButton("✔", self)
        self.settitlebtn.setGeometry(145, 240, 20, 20)
        self.settitlebtn.clicked.connect(self.settitle)
        self.settitlebtn.setStyleSheet(
            "QPushButton"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.unsettitlebtn = QPushButton("X", self)
        self.unsettitlebtn.setGeometry(170, 240, 20, 20)
        self.unsettitlebtn.clicked.connect(self.unsettitle)
        self.unsettitlebtn.setStyleSheet(
            "QPushButton"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )

        self.main = QLabel(" ", self)
        self.main.setGeometry(200, 200, 1000, 800)
        self.main.setStyleSheet("background-color : #2E2E2E")

        self.title = QLabel("Your Planner Title Here", self)
        self.title.setStyleSheet("color : white")
        self.title.setGeometry(300, 200, 1000, 100)
        self.title.setFont(fontbold)

        self.clock = QLabel("", self)
        self.clock.setStyleSheet("color : white")
        self.clock.setGeometry(1030, 200, 1000, 100)
        self.clock.setFont(fontbold)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

        self.setGeometry(0, 0, 1200, 800)
        self.show()

    def showTime(self):
        self.current_time = QTime.currentTime()
        self.label_time = self.current_time.toString("hh:mm:ss")
        self.clock.setText(self.label_time)

    def settitle(self):
        self.title.setText(self.settitlename.text())

    def unsettitle(self):
        self.title.setText("Your Planner Title Here")
        self.settitlename.clear()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
