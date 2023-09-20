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

        scroll_bar_vertical = QScrollBar(self)
        scroll_bar_vertical.setStyleSheet(
            "QScrollBar"
            "{"
            "border: none;"
            "background-color: #343434;"
            "border-radius: 0px;"
            "width: 14px;"
            "margin: 15px 0 15px 0"
            "}"
            "QScrollBar::handle"
            "{"
            "background-color: #404040;"
            "border-radius: 7px;"
            "min-height: 30px;"
            "}"
            "QScrollBar::handle::pressed"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::handle::hover"
            "{"
            "background-color: #373737;"
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
            "background-color: #373737;"
            "}"
            "QScrollBar::sub-line::hover"
            "{"
            "background-color: #373737;"
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
            "background-color: #373737;"
            "}"
            "QScrollBar::add-line::hover:vertical"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page"
            "{"
            "background: none;"
            "}"
        )
        self.checklistwidget.setVerticalScrollBar(scroll_bar_vertical)

        scroll_bar_horizontal = QScrollBar(self)
        scroll_bar_horizontal.setStyleSheet(
            "QScrollBar"
            "{"
            "border: none;"
            "background-color: #343434;"
            "border-radius: 0px;"
            "height: 14px;"
            "margin: 0 15px 0 15px"
            "}"
            "QScrollBar::handle"
            "{"
            "background-color: #404040;"
            "border-radius: 7px;"
            "min-height: 30px;"
            "}"
            "QScrollBar::handle::pressed"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::handle::hover"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::sub-line"
            "{"
            "border: none;"
            "background-color: rbg(59,59,90);"
            "border-top-left-radius: 7px;"
            "border-top-right-radius: 7px;"
            "subcontrol-position: left;"
            "subcontrol-origin: margin;"
            "width: 15px;"
            "}"
            "QScrollBar::sub-line::pressed"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::sub-line::hover"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::add-line"
            "{"
            "border: none;"
            "background-color: rgb(59,59,90);"
            "width: 15px;"
            "border-bottom-left-radius: 7px;"
            "border-bottom-right-radius: 7px;"
            "subcontrol-position: right;"
            "subcontrol-origin: margin;"
            "}"
            "QScrollBar::add-line::pressed"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::add-line::hover:vertical"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::add-page, QScrollBar::sub-page"
            "{"
            "background: none;"
            "}"
        )

        self.checklistwidget.setHorizontalScrollBar(scroll_bar_horizontal)

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

        self.save = QPushButton("💾", self)
        self.save.setGeometry(30, 205, 20, 20)
        self.save.clicked.connect(self.savee)
        self.save.setStyleSheet(
            "QPushButton"
            "{"
            "background : #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )

        self.toggleheaders = QLabel("Toggle Widgets", self)
        self.toggleheaders.setGeometry(45, 350, 100, 20)
        self.toggleheaders.setFont(fontboldsmall)
        self.toggleheaders.setStyleSheet("QLabel" "{" "color : white;" "}")

        self.togglenotes = QPushButton("📚", self)
        self.togglenotes.setGeometry(5, 385, 20, 20)
        self.togglenotes.setCheckable(True)
        self.togglenotes.clicked.connect(self.togglenotess)
        self.togglenotes.setStyleSheet(
            "QPushButton" "{" "background : #545454;" "border : #545454;" "}"
        )

        self.togglechecklist = QPushButton("📝", self)
        self.togglechecklist.setGeometry(30, 385, 20, 20)
        self.togglechecklist.setCheckable(True)
        self.togglechecklist.clicked.connect(self.togglechecklists)
        self.togglechecklist.setStyleSheet(
            "QPushButton" "{" "background : #545454;" "border : #545454;" "}"
        )

        self.togglecalendar = QPushButton("📅", self)
        self.togglecalendar.setGeometry(55, 385, 20, 20)
        self.togglecalendar.setCheckable(True)
        self.togglecalendar.clicked.connect(self.togglecalendarr)
        self.togglecalendar.setStyleSheet(
            "QPushButton" "{" "background : #545454;" "border : #545454;" "}"
        )

        self.togglesaving = QPushButton("💰", self)
        self.togglesaving.setGeometry(80, 385, 20, 20)
        self.togglesaving.setCheckable(True)
        self.togglesaving.clicked.connect(self.togglesavingss)
        self.togglesaving.setStyleSheet(
            "QPushButton" "{" "background : #545454;" "border : #545454;" "}"
        )

        self.togglepaints = QPushButton("🖌️", self)
        self.togglepaints.setGeometry(105, 385, 20, 20)
        self.togglepaints.setCheckable(True)
        self.togglepaints.clicked.connect(self.togglecanvas)
        self.togglepaints.setStyleSheet(
            "QPushButton" "{" "background : #545454;" "border : #545454;" "}"
        )

        self.notesbg = QLabel(self)
        self.notesbg.setStyleSheet(
            "QLabel"
            "{"
            "background : #272727;"
            "border : #272727;"
            "color : white;"
            "}"
        )
        self.notesbg.setGeometry(250, 350, 450, 100)

        self.notesheader = QLabel("Notes", self)
        self.notesheader.setStyleSheet("color: white")
        self.notesheader.setGeometry(435, 320, 200, 20)
        self.notesheader.setFont(fontboldmed)

        self.notes = QPlainTextEdit(self)
        self.notes.setStyleSheet(
            "QPlainTextEdit"
            "{"
            "background : #272727;"
            "border : #272727;"
            "color : white;"
            "}"
        )
        self.notes.setGeometry(260, 360, 430, 80)
        self.notes.setFont(fontboldmed)
        scroll_bar_vertical_note = QScrollBar(self)
        scroll_bar_vertical_note.setStyleSheet(
            "QScrollBar"
            "{"
            "border: none;"
            "background-color: #343434;"
            "border-radius: 0px;"
            "width: 14px;"
            "margin: 15px 0 15px 0"
            "}"
            "QScrollBar::handle"
            "{"
            "background-color: #404040;"
            "border-radius: 7px;"
            "min-height: 30px;"
            "}"
            "QScrollBar::handle::pressed"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::handle::hover"
            "{"
            "background-color: #373737;"
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
            "background-color: #373737;"
            "}"
            "QScrollBar::sub-line::hover"
            "{"
            "background-color: #373737;"
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
            "background-color: #373737;"
            "}"
            "QScrollBar::add-line::hover:vertical"
            "{"
            "background-color: #373737;"
            "}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page"
            "{"
            "background: none;"
            "}"
        )
        self.notes.setVerticalScrollBar(scroll_bar_vertical_note)

        now = QDate.currentDate()
        self.date = QLabel(now.toString("dd-MM-yyyy"), self)
        self.date.setGeometry(1050, 230, 1000, 100)
        self.date.setFont(fontboldsmall)
        self.date.setStyleSheet("color:white")

        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(260, 500, 430, 250)
        self.calendar.setFont(fontboldsmall)
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setStyleSheet(
            "QCalendarWidget QWidget"
            "{"
            "alternate-background-color : #272727;"
            "background-color : #272727;"
            "color:white;"
            "selection-background-color: #4D4D4D;"
            "selection-color: white;"
            "}"
            "QCalendarWidget QToolButton"
            "{"
            "background-color:#272727;"
            "border: 2px solid #272727;"
            "border-bottom: 0px;"
            "border-top-left-radius: 5px;"
            "color:white;"
            "icon-size:0px"
            "}"
            "QCalendarWidget QAbstractItemView"
            "{"
            "color: white;"
            "}"
        )

        self.calendartitle = QLabel("Calendar", self)
        self.calendartitle.setStyleSheet("color:white")
        self.calendartitle.setGeometry(435, 470, 200, 20)
        self.calendartitle.setFont(fontboldmed)

        self.savingsbg = QLabel("", self)
        self.savingsbg.setStyleSheet("background-color: #272727")
        self.savingsbg.setGeometry(250, 320, 900, 450)

        self.savingstabbar = QLabel("", self)
        self.savingstabbar.setStyleSheet("background-color: #363636")
        self.savingstabbar.setGeometry(13, 450, 175, 200)

        self.savingstabbarheader = QLabel("Your income", self)
        self.savingstabbarheader.setStyleSheet("color: white")
        self.savingstabbarheader.setFont(fontboldsmall)
        self.savingstabbarheader.setGeometry(60, 470, 200, 20)

        self.savingstabbarbtn = QPushButton("✔", self)
        self.savingstabbarbtn.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.savingstabbarbtn.setFont(fontboldsmall)
        self.savingstabbarbtn.setGeometry(156, 500, 20, 20)

        self.amountmoney = QLineEdit("", self)
        self.amountmoney.setGeometry(26, 500, 125, 20)
        self.amountmoney.setStyleSheet(
            "QLineEdit"
            "{"
            "background : #585858;"
            "border : #585858;"
            "color : white;"
            "}"
        )
        self.amountmoney.setFont(fontboldsmall)

        self.piggybank = QLabel(" ", self)
        self.pixmap1 = QPixmap("pictures\piggybank.png")
        self.piggybank.setPixmap(self.pixmap1)
        self.piggybank.setGeometry(270, 300, 500, 500)

        self.totalmoney = QLabel("test", self)
        self.totalmoney.setStyleSheet("color:white")
        self.totalmoney.setGeometry(400, 550, 200, 20)
        self.totalmoney.setFont(fontbold)

        self.savingsbg.setVisible(False)
        self.savingstabbar.setVisible(False)
        self.savingstabbarheader.setVisible(False)
        self.piggybank.setVisible(False)
        self.amountmoney.setVisible(False)
        self.totalmoney.setVisible(False)
        self.savingstabbarbtn.setVisible(False)

        self.setGeometry(0, 0, 1200, 800)
        self.show()

        # work in progress

    """
        self.calendar.selectionChanged.connect(self.grab_date)  
        self.Datething = QTextEdit("fgs",self)
        self.Datething.setGeometry(435,750,200,20)
        #self.Datething.setStyleSheet("color:white")
        self.Datething.setFont(fontboldmed)
        self.Datething.setVisible(False)       

    def grab_date(self):
        dateselected = self.calendar.selectedDate()
        self.Datething.setText(str(dateselected.toString()))
        self.Datething.setVisible(True)
    """

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

    def savee(self):
        pass

    # save in .json file thing

    def togglenotess(self):
        if self.togglenotes.isChecked():
            self.notes.setVisible(False)
            self.notesbg.setVisible(False)
            self.notesheader.setVisible(False)
        else:
            self.notes.setVisible(True)
            self.notesbg.setVisible(True)
            self.notesheader.setVisible(True)

    def togglechecklists(self):
        if self.togglechecklist.isChecked():
            self.checklistwidget.setVisible(False)
            self.checklisttext.setVisible(False)
        else:
            self.checklistwidget.setVisible(True)
            self.checklisttext.setVisible(True)

    def togglecalendarr(self):
        if self.togglecalendar.isChecked():
            self.calendar.setVisible(False)
            self.calendartitle.setVisible(False)
        else:
            self.calendar.setVisible(True)
            self.calendartitle.setVisible(True)

    def togglesavingss(self):
        if self.togglesaving.isChecked():
            self.notes.setVisible(False)
            self.notesbg.setVisible(False)
            self.notesheader.setVisible(False)
            self.calendar.setVisible(False)
            self.calendartitle.setVisible(False)
            self.checklistwidget.setVisible(False)
            self.checklisttext.setVisible(False)
            # savings
            self.savingsbg.setVisible(True)
            self.savingstabbar.setVisible(True)
            self.savingstabbarheader.setVisible(True)
            self.piggybank.setVisible(True)
            self.amountmoney.setVisible(True)
            self.totalmoney.setVisible(True)
            self.savingstabbarbtn.setVisible(True)
        else:
            self.notes.setVisible(True)
            self.notesbg.setVisible(True)
            self.notesheader.setVisible(True)
            self.calendar.setVisible(True)
            self.calendartitle.setVisible(True)
            self.checklistwidget.setVisible(True)
            self.checklisttext.setVisible(True)
            # savings
            self.savingsbg.setVisible(False)
            self.savingstabbar.setVisible(False)
            self.savingstabbarheader.setVisible(False)
            self.piggybank.setVisible(False)
            self.amountmoney.setVisible(False)
            self.totalmoney.setVisible(False)
            self.savingstabbarbtn.setVisible(False)

    def togglecanvas(self):
        if self.togglepaints.isChecked():
            self.notes.setVisible(False)
            self.notesbg.setVisible(False)
            self.notesheader.setVisible(False)
            self.calendar.setVisible(False)
            self.calendartitle.setVisible(False)
            self.checklistwidget.setVisible(False)
            self.checklisttext.setVisible(False)

        else:
            self.notes.setVisible(True)
            self.notesbg.setVisible(True)
            self.notesheader.setVisible(True)
            self.calendar.setVisible(True)
            self.calendartitle.setVisible(True)
            self.checklistwidget.setVisible(True)
            self.checklisttext.setVisible(True)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

# project notes, calendar will be on full screen with the ability to write on each pannel and set the month and the title name.
# fix notes scrollbar
