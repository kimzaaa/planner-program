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
        fontboldmed = QFont("Roboto Mono Medium", 11)
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
        self.sidetabbar.setGeometry(0, 200, 210, 800)
        self.sidetabbar.setStyleSheet("background-color : #404040 ")

        self.settitlename = QLineEdit("School work", self)
        self.settitlename.setGeometry(15, 270, 125, 20)
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
        self.settitlebtn.setGeometry(145, 270, 20, 20)
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
        self.unsettitlebtn.setGeometry(170, 270, 20, 20)
        self.unsettitlebtn.clicked.connect(self.unsettitle)
        self.unsettitlebtn.setStyleSheet(
            "QPushButton"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.settitleheader = QLabel("Set Planner Name", self)
        self.settitleheader.setGeometry(35, 250, 200, 10)
        self.settitleheader.setStyleSheet("color:white")
        self.settitleheader.setFont(fontboldsmall)

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
        # checklist
        self.checklistheader = QLabel("Add Checklist", self)
        self.checklistheader.setStyleSheet("color: white")
        self.checklistheader.setGeometry(50, 300, 200, 10)
        self.checklistheader.setFont(fontboldsmall)

        self.checklistwidget = QListWidget(self)
        self.checklistwidget.setStyleSheet(
            "QListWidget"
            "{"
            "background : #272727;"
            "border : #272727;"
            "color : white;"
            "}"
        )
        self.checklistwidget.setGeometry(800, 350, 350, 400)
        self.checklistwidget.setFont(fontboldmed)
        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet(
            "QScrollBar"
            "{"
            "border: none;"
            "background-color: rgb(59,59,90);"
            "border-radius: 0px;"
            "width: 14px;"
            "margin: 15px 0 15px 0"
            "}"
            "QScrollBar::handle"
            "{"
            "background-color: rgb(80,80,122);"
            "border-radius: 7px;"
            "min-height: 30px;"
            "}"
            "QScrollBar::handle::pressed"
            "{"
            "background-color: rgb(185,0,92);"
            "}"
            "QScrollBar::handle::hover"
            "{"
            "background-color: rgb(255,0,127);"
            "}"
            "QScrollBar::sub-line"
            "{"
            "border: none;"
            "background-color: rbg(59,59,90);"
            "border-top-left-radius: 7px;"
            "border-top-right-radius: 7px;"
            "subcontrol-position: top;"
            "subcontrol-origin: margin;"
            "height: 15px;"
            "}"
            "QScrollBar::sub-line::pressed"
            "{"
            "background-color: rgb(185,0,92);"
            "}"
            "QScrollBar::sub-line::hover"
            "{"
            "background-color: rgb(255,0,127);"
            "}"
            "QScrollBar::add-line"
            "{"
            "border: none;"
            "background-color: rgb(59,59,90);"
            "height: 15px;"
            "border-bottom-left-radius: 7px;"
            "border-bottom-right-radius: 7px;"
            "subcontrol-position: bottom;"
            "subcontrol-origin: margin;"
            "}"
            "QScrollBar::add-line::pressed"
            "{"
            "background-color: rgb(185,0,92);"
            "}"
            "QScrollBar::add-line::hover"
            "{"
            "background-color: rgb(255,0,127);"
            "}"
            "QScrollBar::add-page, QScrollBar::sub-page"
            "{"
            "background: none;"
            "}"
        )
        self.checklistwidget.setVerticalScrollBar(scroll_bar)

        self.checklisttext = QLabel("Checklist", self)
        self.checklisttext.setStyleSheet("color:white")
        self.checklisttext.setGeometry(935, 310, 150, 20)
        self.checklisttext.setFont(fontboldmed)

        self.setchecklistname = QLineEdit("example 1", self)
        self.setchecklistname.setStyleSheet(
            "QLineEdit"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.setchecklistname.setGeometry(0, 320, 125, 20)
        self.setchecklistname.setFont(fontboldsmall)

        self.setchecklistbtn = QPushButton("✔", self)
        self.setchecklistbtn.setGeometry(130, 320, 20, 20)
        self.setchecklistbtn.clicked.connect(self.setchecklist)
        self.setchecklistbtn.setStyleSheet(
            "QPushButton"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.unsetchecklistbtn = QPushButton("X", self)
        self.unsetchecklistbtn.setGeometry(155, 320, 20, 20)
        self.unsetchecklistbtn.clicked.connect(self.unsetchecklist)
        self.unsetchecklistbtn.setStyleSheet(
            "QPushButton"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.clearchecklistbtn = QPushButton("🗑", self)
        self.clearchecklistbtn.setGeometry(180, 320, 20, 20)
        self.clearchecklistbtn.clicked.connect(self.clearchecklist)
        self.clearchecklistbtn.setStyleSheet(
            "QPushButton"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )

        self.setting = QPushButton("⚙", self)
        self.setting.setGeometry(5, 205, 20, 20)
        self.setting.clicked.connect(self.settings)
        self.setting.setStyleSheet(
            "QPushButton"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )

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

    def setchecklist(self):
        checklistitem = self.setchecklistname.text()
        self.checklistwidget.addItem(checklistitem)

    def unsetchecklist(self):
        listclicked = self.checklistwidget.currentRow()
        self.checklistwidget.takeItem(listclicked)

    def clearchecklist(self):
        self.checklistwidget.clear()

    def settings(self):
        # themes tab
        pass


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
