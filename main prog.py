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
        fontboldverysmall = QFont("Roboto Mono Medium", 6)
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

        """
        SAVINGS ##########################################################################################################################
        """

        self.savingsbg = QLabel("", self)
        self.savingsbg.setStyleSheet("background-color: #272727")
        self.savingsbg.setGeometry(250, 320, 900, 450)

        self.savingstabbar = QLabel("", self)
        self.savingstabbar.setStyleSheet("background-color: #363636")
        self.savingstabbar.setGeometry(13, 450, 175, 300)

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
        self.savingstabbarbtn.clicked.connect(self.addmoney)

        self.savingstabbarheaderd = QLabel("Details", self)
        self.savingstabbarheaderd.setStyleSheet("color: white")
        self.savingstabbarheaderd.setFont(fontboldsmall)
        self.savingstabbarheaderd.setGeometry(70, 525, 200, 20)

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

        self.detailss = QLineEdit("", self)
        self.detailss.setGeometry(26, 550, 125, 20)
        self.detailss.setStyleSheet(
            "QLineEdit"
            "{"
            "background : #585858;"
            "border : #585858;"
            "color : white;"
            "}"
        )
        self.detailss.setFont(fontboldsmall)

        self.expensemoeny = QLineEdit("", self)
        self.expensemoeny.setGeometry(26, 600, 125, 20)
        self.expensemoeny.setStyleSheet(
            "QLineEdit"
            "{"
            "background : #585858;"
            "border : #585858;"
            "color : white;"
            "}"
        )
        self.expensemoeny.setFont(fontboldsmall)
        self.expensemoeny.setVisible(False)

        self.expensemoenytabbarbtn = QPushButton("✔", self)
        self.expensemoenytabbarbtn.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.expensemoenytabbarbtn.setFont(fontboldsmall)
        self.expensemoenytabbarbtn.setGeometry(156, 600, 20, 20)
        self.expensemoenytabbarbtn.clicked.connect(self.delmoney)

        self.expensetabbarheader = QLabel("Your expense", self)
        self.expensetabbarheader.setStyleSheet("color: white")
        self.expensetabbarheader.setFont(fontboldsmall)
        self.expensetabbarheader.setGeometry(60, 580, 200, 20)

        self.expensedetails = QLabel("Expense details", self)
        self.expensedetails.setStyleSheet("color: white")
        self.expensedetails.setFont(fontboldsmall)
        self.expensedetails.setGeometry(40, 625, 200, 20)

        self.expensedetailss = QLineEdit("", self)
        self.expensedetailss.setGeometry(26, 650, 150, 20)
        self.expensedetailss.setStyleSheet(
            "QLineEdit"
            "{"
            "background : #585858;"
            "border : #585858;"
            "color : white;"
            "}"
        )
        self.expensedetailss.setFont(fontboldsmall)

        self.clearmoney = QPushButton("🗑", self)
        self.clearmoney.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.clearmoney.setGeometry(80, 680, 20, 20)
        self.clearmoney.clicked.connect(self.clearmon)

        self.deletesavings = QPushButton("X", self)
        self.deletesavings.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.deletesavings.setGeometry(110, 680, 20, 20)
        self.deletesavings.clicked.connect(self.delmon)

        self.deletesavings2 = QPushButton("X", self)
        self.deletesavings2.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: #545454;"
            "border : #545454;"
            "color : white;"
            "}"
        )
        self.deletesavings2.setGeometry(155, 550, 20, 20)
        self.deletesavings2.clicked.connect(self.delmonad)

        self.yourbalance = QLabel("Your balance", self)
        self.yourbalance.setStyleSheet("color:white")
        self.yourbalance.setFont(fontboldmed)
        self.yourbalance.setGeometry(395, 500, 200, 20)

        self.totalmoney = QLabel("0", self)
        self.totalmoney.setStyleSheet("color:white")
        self.totalmoney.setFont(fontboldmed)
        self.totalmoney.setGeometry(450, 530, 200, 20)

        self.savingswarning = QLabel(
            "*Note* if you do remove your list from the savings list, please add the deleted money in the expense list and delete the list bar",
            self,
        )
        self.savingswarning.setStyleSheet("color:white")
        self.savingswarning.setFont(fontboldverysmall)
        self.savingswarning.setGeometry(250, 780, 2000, 20)

        self.Expenseheader = QLabel("Expense list", self)
        self.Expenseheader.setStyleSheet("color: white")
        self.Expenseheader.setGeometry(930, 300, 200, 30)
        self.Expenseheader.setFont(fontboldmed)

        self.expensechecklistwidget = QListWidget(self)
        self.expensechecklistwidget.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.expensechecklistwidget.setGeometry(900, 350, 200, 400)
        self.expensechecklistwidget.setFont(fontboldmed)

        self.checklistwidget.setGeometry(800, 350, 350, 400)
        self.checklistwidget.setFont(fontboldmed)

        scroll_bar_verticalsa = QScrollBar(self)
        scroll_bar_verticalsa.setStyleSheet(
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
            "QScrollBar::sub-line"
            "{"
            "border: none;"
            "background-color: rbg(59,59,90);"
            "subcontrol-position: top;"
            "subcontrol-origin: margin;"
            "height: 15px;"
            "}"
            "QScrollBar::add-line"
            "{"
            "border: none;"
            "background-color: rgb(59,59,90);"
            "height: 15px;"
            "subcontrol-position: bottom;"
            "subcontrol-origin: margin;"
            "}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page"
            "{"
            "background: none;"
            "}"
        )

        self.expensechecklistwidget.setVerticalScrollBar(scroll_bar_verticalsa)

        scroll_bar_horizontalsa = QScrollBar(self)
        scroll_bar_horizontalsa.setStyleSheet(
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
            "QScrollBar::sub-line"
            "{"
            "border: none;"
            "background-color: rbg(59,59,90);"
            "subcontrol-position: left;"
            "subcontrol-origin: margin;"
            "width: 15px;"
            "}"
            "QScrollBar::add-line"
            "{"
            "border: none;"
            "background-color: rgb(59,59,90);"
            "width: 15px;"
            "subcontrol-position: right;"
            "subcontrol-origin: margin;"
            "}"
            "QScrollBar::add-page, QScrollBar::sub-page"
            "{"
            "background: none;"
            "}"
        )

        self.expensechecklistwidget.setHorizontalScrollBar(scroll_bar_horizontalsa)

        self.savingsheader = QLabel("Savings list", self)
        self.savingsheader.setStyleSheet("color: white")
        self.savingsheader.setGeometry(690, 300, 200, 30)
        self.savingsheader.setFont(fontboldmed)

        self.savingschecklistwidget = QListWidget(self)
        self.savingschecklistwidget.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.savingschecklistwidget.setGeometry(650, 350, 200, 400)
        self.savingschecklistwidget.setFont(fontboldmed)

        scroll_bar_verticalsaa = QScrollBar(self)
        scroll_bar_verticalsaa.setStyleSheet(
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
            "QScrollBar::sub-line"
            "{"
            "border: none;"
            "background-color: rbg(59,59,90);"
            "subcontrol-position: top;"
            "subcontrol-origin: margin;"
            "height: 15px;"
            "}"
            "QScrollBar::add-line"
            "{"
            "border: none;"
            "background-color: rgb(59,59,90);"
            "height: 15px;"
            "subcontrol-position: bottom;"
            "subcontrol-origin: margin;"
            "}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page"
            "{"
            "background: none;"
            "}"
        )

        self.savingschecklistwidget.setVerticalScrollBar(scroll_bar_verticalsaa)

        scroll_bar_horizontalsaa = QScrollBar(self)
        scroll_bar_horizontalsaa.setStyleSheet(
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
            "QScrollBar::sub-line"
            "{"
            "border: none;"
            "background-color: rbg(59,59,90);"
            "subcontrol-position: left;"
            "subcontrol-origin: margin;"
            "width: 15px;"
            "}"
            "QScrollBar::add-line"
            "{"
            "border: none;"
            "background-color: rgb(59,59,90);"
            "width: 15px;"
            "subcontrol-position: right;"
            "subcontrol-origin: margin;"
            "}"
            "QScrollBar::add-page, QScrollBar::sub-page"
            "{"
            "background: none;"
            "}"
        )

        self.savingschecklistwidget.setHorizontalScrollBar(scroll_bar_horizontalsaa)

        self.savingsbg.setVisible(False)
        self.savingstabbar.setVisible(False)
        self.savingstabbarheader.setVisible(False)
        self.amountmoney.setVisible(False)
        self.savingstabbarbtn.setVisible(False)
        self.expensemoenytabbarbtn.setVisible(False)
        self.expensetabbarheader.setVisible(False)
        self.totalmoney.setVisible(False)
        self.clearmoney.setVisible(False)
        self.Expenseheader.setVisible(False)
        self.expensechecklistwidget.setVisible(False)
        self.savingsheader.setVisible(False)
        self.savingschecklistwidget.setVisible(False)
        self.savingstabbarheaderd.setVisible(False)
        self.detailss.setVisible(False)
        self.expensedetails.setVisible(False)
        self.expensedetailss.setVisible(False)
        self.yourbalance.setVisible(False)
        self.deletesavings.setVisible(False)
        self.deletesavings2.setVisible(False)
        self.savingswarning.setVisible(False)

        """
        SAVINGS END ##########################################################################################################################
        """

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

    def addmoney(self):
        try:
            moneyadd = self.amountmoney.text()
            moneyaddnum = float(moneyadd)
            ttlmoney = self.totalmoney.text()
            ttlmoneynum = float(ttlmoney)
            newmoney = moneyaddnum + ttlmoneynum
            newmoneystr = str(newmoney)
            self.totalmoney.setText(newmoneystr)
            self.amountmoney.clear()
            detailsss = self.detailss.text()
            self.detailss.clear()

            self.savingschecklistwidget.addItem(moneyadd + " : " + detailsss)

        except:
            pass

    def delmoney(self):
        try:
            moneydel = self.expensemoeny.text()
            moneydelnum = float(moneydel)
            ttlmoney = self.totalmoney.text()
            ttlmoneynum = float(ttlmoney)
            moneyleft = ttlmoneynum - moneydelnum
            moneyleft = str(moneyleft)
            self.totalmoney.setText(moneyleft)
            self.expensemoeny.clear()
            detailssss = self.expensedetailss.text()
            self.expensedetailss.clear()

            self.expensechecklistwidget.addItem(moneydel + " : " + detailssss)

        except:
            pass

    def clearmon(self):
        self.amountmoney.clear()
        self.expensemoeny.clear()
        self.totalmoney.setText("0")
        self.expensechecklistwidget.clear()
        self.savingschecklistwidget.clear()

    def delmon(self):
        clickeds = self.expensechecklistwidget.currentRow()
        self.expensechecklistwidget.takeItem(clickeds)

    def delmonad(self):
        clickedss = self.savingschecklistwidget.currentRow()
        self.savingschecklistwidget.takeItem(clickedss)

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
            self.amountmoney.setVisible(True)
            self.savingstabbarbtn.setVisible(True)
            self.expensemoeny.setVisible(True)
            self.expensemoenytabbarbtn.setVisible(True)
            self.expensetabbarheader.setVisible(True)
            self.totalmoney.setVisible(True)
            self.clearmoney.setVisible(True)
            self.Expenseheader.setVisible(True)
            self.expensechecklistwidget.setVisible(True)
            self.savingsheader.setVisible(True)
            self.savingschecklistwidget.setVisible(True)
            self.savingstabbarheaderd.setVisible(True)
            self.detailss.setVisible(True)
            self.expensedetails.setVisible(True)
            self.expensedetailss.setVisible(True)
            self.yourbalance.setVisible(True)
            self.deletesavings.setVisible(True)
            self.deletesavings2.setVisible(True)
            self.savingswarning.setVisible(True)
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
            self.amountmoney.setVisible(False)
            self.savingstabbarbtn.setVisible(False)
            self.expensemoeny.setVisible(False)
            self.expensemoenytabbarbtn.setVisible(False)
            self.expensetabbarheader.setVisible(False)
            self.totalmoney.setVisible(False)
            self.clearmoney.setVisible(False)
            self.Expenseheader.setVisible(False)
            self.expensechecklistwidget.setVisible(False)
            self.savingsheader.setVisible(False)
            self.savingschecklistwidget.setVisible(False)
            self.savingstabbarheaderd.setVisible(False)
            self.detailss.setVisible(False)
            self.expensedetails.setVisible(False)
            self.expensedetailss.setVisible(False)
            self.yourbalance.setVisible(False)
            self.deletesavings.setVisible(False)
            self.deletesavings2.setVisible(False)
            self.savingswarning.setVisible(False)

    def togglecanvas(self):
        if self.togglepaints.isChecked():
            self.notes.setVisible(False)
            self.notesbg.setVisible(False)
            self.notesheader.setVisible(False)
            self.calendar.setVisible(False)
            self.calendartitle.setVisible(False)
            self.checklistwidget.setVisible(False)
            self.checklisttext.setVisible(False)
            self.savingsbg.setVisible(False)
            self.savingstabbar.setVisible(False)
            self.savingstabbarheader.setVisible(False)
            self.amountmoney.setVisible(False)
            self.savingstabbarbtn.setVisible(False)
            self.expensemoeny.setVisible(False)
            self.expensemoenytabbarbtn.setVisible(False)
            self.expensetabbarheader.setVisible(False)
            self.totalmoney.setVisible(False)
            self.clearmoney.setVisible(False)
            self.Expenseheader.setVisible(False)
            self.expensechecklistwidget.setVisible(False)
            self.savingsheader.setVisible(False)
            self.savingschecklistwidget.setVisible(False)
            self.savingstabbarheaderd.setVisible(False)
            self.detailss.setVisible(False)
            self.expensedetails.setVisible(False)
            self.expensedetailss.setVisible(False)
            self.yourbalance.setVisible(False)
            self.deletesavings.setVisible(False)
            self.deletesavings2.setVisible(False)
            self.savingswarning.setVisible(False)

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
