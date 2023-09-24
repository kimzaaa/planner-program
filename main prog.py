# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wip")

        QFontDatabase.addApplicationFont("RobotoMono.ttf")

        self.UiComponents()

    def UiComponents(self):
        fontbold = QFont("Roboto Mono Medium", 15)
        fontboldsmall = QFont("Roboto Mono Medium", 8)
        fontboldverysmall = QFont("Roboto Mono Medium", 6)
        fontboldmed = QFont("Roboto Mono Medium", 11)
        fontboldformood = QFont("Roboto Mono Medium", 13)
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
        self.setting.setCheckable(True)
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

        """
        MOOD TRACKER
        """
        self.moodtrackertriggerbtn = QPushButton("🙂", self)
        self.moodtrackertriggerbtn.setGeometry(130, 385, 20, 20)
        self.moodtrackertriggerbtn.setCheckable(True)
        self.moodtrackertriggerbtn.clicked.connect(self.togglemood)
        self.moodtrackertriggerbtn.setStyleSheet(
            "QPushButton" "{" "background : #545454;" "border : #545454;" "}"
        )

        self.moodbg = QLabel("", self)
        self.moodbg.setStyleSheet("background-color: #272727")
        self.moodbg.setGeometry(210, 320, 1000, 470)

        self.moodtitle = QLabel("Mood Tracker", self)
        self.moodtitle.setStyleSheet("color:white")
        self.moodtitle.setGeometry(230, 340, 200, 20)
        self.moodtitle.setFont(fontboldformood)

        self.month1 = QListWidget(self)
        self.month1.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month1.setGeometry(250, 730, 980, 30)
        self.month1.setFont(fontboldmed)

        self.month2 = QListWidget(self)
        self.month2.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month2.setGeometry(250, 700, 980, 30)
        self.month2.setFont(fontboldmed)

        self.month3 = QListWidget(self)
        self.month3.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month3.setGeometry(250, 670, 980, 30)
        self.month3.setFont(fontboldmed)

        self.month4 = QListWidget(self)
        self.month4.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month4.setGeometry(250, 640, 980, 30)
        self.month4.setFont(fontboldmed)

        self.month5 = QListWidget(self)
        self.month5.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month5.setGeometry(250, 610, 980, 30)
        self.month5.setFont(fontboldmed)

        self.month6 = QListWidget(self)
        self.month6.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month6.setGeometry(250, 580, 980, 30)
        self.month6.setFont(fontboldmed)

        self.month7 = QListWidget(self)
        self.month7.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month7.setGeometry(250, 550, 980, 30)
        self.month7.setFont(fontboldmed)

        self.month8 = QListWidget(self)
        self.month8.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month8.setGeometry(250, 520, 980, 30)
        self.month8.setFont(fontboldmed)

        self.month9 = QListWidget(self)
        self.month9.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month9.setGeometry(250, 490, 980, 30)
        self.month9.setFont(fontboldmed)

        self.month10 = QListWidget(self)
        self.month10.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month10.setGeometry(250, 460, 980, 30)
        self.month10.setFont(fontboldmed)

        self.month11 = QListWidget(self)
        self.month11.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month11.setGeometry(250, 430, 980, 30)
        self.month11.setFont(fontboldmed)

        self.month12 = QListWidget(self)
        self.month12.setStyleSheet(
            "QListWidget"
            "{"
            "background : #202020;"
            "border : #202020;"
            "color : white;"
            "}"
        )
        self.month12.setGeometry(250, 400, 980, 30)
        self.month12.setFont(fontboldmed)

        self.monthnumside = QLabel(
            "12 \n11 \n10 \n9 \n8 \n7 \n6 \n5 \n4 \n3 \n2 \n1", self
        )
        self.monthnumside.setGeometry(215, 80, 200, 1000)
        self.monthnumside.setStyleSheet("color:white")
        self.monthnumside.setFont(fontboldformood)

        self.monthtitle = QLabel("Month", self)
        self.monthtitle.setStyleSheet("color:white")
        self.monthtitle.setFont(fontboldsmall)
        self.monthtitle.setGeometry(205, 0, 200, 780)

        self.daynumshor = QLabel("Days 1 - 31", self)
        self.daynumshor.setGeometry(600, 770, 1000, 30)
        self.daynumshor.setStyleSheet("color:white")
        self.daynumshor.setFont(fontboldformood)

        self.moodoptions = QLabel("", self)
        self.moodoptions.setGeometry(15, 450, 170, 260)
        self.moodoptions.setStyleSheet("background-color:#363636")

        self.selectmonth = QLineEdit(self)
        self.selectmonth.setGeometry(25, 500, 125, 20)
        self.selectmonth.setStyleSheet(
            "QLineEdit"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.selectmonth.setFont(fontboldsmall)

        self.selectmonthtitle = QLabel("Select Month 1 - 12", self)
        self.selectmonthtitle.setGeometry(24, 465, 200, 30)
        self.selectmonthtitle.setStyleSheet("color:white")
        self.selectmonthtitle.setFont(fontboldsmall)

        self.confirmselectmonth = QPushButton("✔", self)
        self.confirmselectmonth.setGeometry(155, 500, 20, 20)
        self.confirmselectmonth.setStyleSheet(
            "QPushButton"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.confirmselectmonth.clicked.connect(self.setmonth)

        self.btnred = QPushButton("🟥", self)
        self.btnred.setGeometry(20 + 20, 535, 20, 20)
        self.btnred.setStyleSheet(
            "QPushButton"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.btnred.clicked.connect(self.setred)

        self.btnorange = QPushButton("🟧", self)
        self.btnorange.setGeometry(45 + 20, 535, 20, 20)
        self.btnorange.setStyleSheet(
            "QPushButton"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.btnorange.clicked.connect(self.setorange)

        self.btnyellow = QPushButton("🟨", self)
        self.btnyellow.setGeometry(70 + 20, 535, 20, 20)
        self.btnyellow.setStyleSheet(
            "QPushButton"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.btnyellow.clicked.connect(self.setyellow)

        self.btngreen = QPushButton("🟩", self)
        self.btngreen.setGeometry(95 + 20, 535, 20, 20)
        self.btngreen.setStyleSheet(
            "QPushButton"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.btngreen.clicked.connect(self.setgreen)

        self.btnblue = QPushButton("🟦", self)
        self.btnblue.setGeometry(120 + 20, 535, 20, 20)
        self.btnblue.setStyleSheet(
            "QPushButton"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.btnblue.clicked.connect(self.setblue)

        self.selectcolor = QLineEdit(self)
        self.selectcolor.setGeometry(25, 570, 125, 20)
        self.selectcolor.setStyleSheet(
            "QLineEdit"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.selectcolor.setFont(fontboldsmall)

        self.moodnotes = QLabel("🟥: Very bad mood \n🟧: bad mood \n🟨: Normal mood \n🟩 Good mood \n🟦 Very good mood    ",self)
        self.moodnotes.setGeometry(20, 560, 200, 100)
        self.moodnotes.setStyleSheet("color:white")
        self.moodnotes.setFont(fontboldsmall)

        self.deletemood = QPushButton("🗑", self)
        self.deletemood.setGeometry(90, 675, 20, 20)
        self.deletemood.setStyleSheet(
            "QPushButton"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.deletemood.clicked.connect(self.delmood)

        self.month1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.month12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.month1.setFlow(QListView.LeftToRight)
        self.month2.setFlow(QListView.LeftToRight)
        self.month3.setFlow(QListView.LeftToRight)
        self.month4.setFlow(QListView.LeftToRight)
        self.month5.setFlow(QListView.LeftToRight)
        self.month6.setFlow(QListView.LeftToRight)
        self.month7.setFlow(QListView.LeftToRight)
        self.month8.setFlow(QListView.LeftToRight)
        self.month9.setFlow(QListView.LeftToRight)
        self.month10.setFlow(QListView.LeftToRight)
        self.month11.setFlow(QListView.LeftToRight)
        self.month12.setFlow(QListView.LeftToRight)

        self.moodbg.setVisible(False)
        self.moodtitle.setVisible(False)
        self.month1.setVisible(False)
        self.month2.setVisible(False)
        self.month3.setVisible(False)
        self.month4.setVisible(False)
        self.month5.setVisible(False)
        self.month6.setVisible(False)
        self.month7.setVisible(False)
        self.month8.setVisible(False)
        self.month9.setVisible(False)
        self.month10.setVisible(False)
        self.month11.setVisible(False)
        self.month12.setVisible(False)
        self.monthnumside.setVisible(False)
        self.daynumshor.setVisible(False)
        self.monthtitle.setVisible(False)
        self.selectcolor.setVisible(False)
        self.moodoptions.setVisible(False)
        self.moodnotes.setVisible(False)
        self.btnred.setVisible(False)
        self.btnorange.setVisible(False)
        self.btnyellow.setVisible(False)
        self.btngreen.setVisible(False)
        self.btnblue.setVisible(False)
        self.confirmselectmonth.setVisible(False)
        self.selectmonth.setVisible(False)
        self.selectmonthtitle.setVisible(False)
        self.deletemood.setVisible(False)

        """
        SETTINGS ########################################################################################################################
        """

        self.settingsbg = QLabel("",self)
        self.settingsbg.setStyleSheet("background-color: #272727")
        self.settingsbg.setGeometry(0,0,1200,800)

        self.settingbackbtn = QPushButton("<",self)
        self.settingbackbtn.setGeometry(90, 675, 20, 20)
        self.settingbackbtn.setStyleSheet(
            "QPushButton"
            "{"
            "background : #484848;"
            "border: #484848;"
            "color:white;"
            "}"
        )
        self.settingbackbtn.clicked.connect(self.backtonorm)

        self.logo = QLabel("WIP",self)
        self.logo.setGeometry(30, 30, 150, 50)
        self.logo.setStyleSheet("color:white")
        self.logo.setFont(fontbold)

        self.settingsbg.setVisible(False)
        self.settingbackbtn.setVisible(False)

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
        if self.setting.isChecked():
            self.settingsbg.setVisible(True)
            self.settingbackbtn.setVisible(True)
        else:
            self.settingsbg.setVisible(False)
            self.settingbackbtn.setVisible(False)
    
    def backtonorm(self):
        self.settingsbg.setVisible(False)
        self.settingbackbtn.setVisible(False)

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

    def setmonth(self):
        if self.selectmonth.text() == "1":
            self.month1.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "2":
            self.month2.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "3":
            self.month3.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "4":
            self.month4.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "5":
            self.month5.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "6":
            self.month6.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "7":
            self.month7.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "8":
            self.month8.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "9":
            self.month9.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "10":
            self.month10.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "11":
            self.month11.addItem(self.selectcolor.text())
        if self.selectmonth.text() == "12":
            self.month12.addItem(self.selectcolor.text())

    def setred(self):
        self.selectcolor.setText("🟥")

    def setorange(self):
        self.selectcolor.setText("🟧")

    def setyellow(self):
        self.selectcolor.setText("🟨")

    def setgreen(self):
        self.selectcolor.setText("🟩")

    def setblue(self):
        self.selectcolor.setText("🟦")

    def delmood(self):
        self.month1.clear()
        self.month2.clear()
        self.month3.clear()
        self.month4.clear()
        self.month5.clear()
        self.month6.clear()
        self.month7.clear()
        self.month8.clear()
        self.month9.clear()
        self.month10.clear()
        self.month11.clear()
        self.month12.clear()

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
            self.moodbg.setVisible(False)
            self.moodtitle.setVisible(False)
            self.month1.setVisible(False)
            self.month2.setVisible(False)
            self.month3.setVisible(False)
            self.month4.setVisible(False)
            self.month5.setVisible(False)
            self.month6.setVisible(False)
            self.month7.setVisible(False)
            self.month8.setVisible(False)
            self.month9.setVisible(False)
            self.month10.setVisible(False)
            self.month11.setVisible(False)
            self.month12.setVisible(False)
            self.monthnumside.setVisible(False)
            self.daynumshor.setVisible(False)
            self.monthtitle.setVisible(False)
            self.selectcolor.setVisible(False)
            self.moodoptions.setVisible(False)
            self.moodnotes.setVisible(False)
            self.btnred.setVisible(False)
            self.btnorange.setVisible(False)
            self.btnyellow.setVisible(False)
            self.btngreen.setVisible(False)
            self.btnblue.setVisible(False)
            self.confirmselectmonth.setVisible(False)
            self.selectmonth.setVisible(False)
            self.selectmonthtitle.setVisible(False)
            self.deletemood.setVisible(False)
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
            self.moodbg.setVisible(False)
            self.moodtitle.setVisible(False)
            self.month1.setVisible(False)
            self.month2.setVisible(False)
            self.month3.setVisible(False)
            self.month4.setVisible(False)
            self.month5.setVisible(False)
            self.month6.setVisible(False)
            self.month7.setVisible(False)
            self.month8.setVisible(False)
            self.month9.setVisible(False)
            self.month10.setVisible(False)
            self.month11.setVisible(False)
            self.month12.setVisible(False)
            self.monthnumside.setVisible(False)
            self.daynumshor.setVisible(False)
            self.monthtitle.setVisible(False)
            self.selectcolor.setVisible(False)
            self.moodoptions.setVisible(False)
            self.moodnotes.setVisible(False)
            self.btnred.setVisible(False)
            self.btnorange.setVisible(False)
            self.btnyellow.setVisible(False)
            self.btngreen.setVisible(False)
            self.btnblue.setVisible(False)
            self.confirmselectmonth.setVisible(False)
            self.selectmonth.setVisible(False)
            self.selectmonthtitle.setVisible(False)
            self.deletemood.setVisible(False)

        else:
            self.notes.setVisible(True)
            self.notesbg.setVisible(True)
            self.notesheader.setVisible(True)
            self.calendar.setVisible(True)
            self.calendartitle.setVisible(True)
            self.checklistwidget.setVisible(True)
            self.checklisttext.setVisible(True)

    def togglemood(self):
        if self.moodtrackertriggerbtn.isChecked():
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
            # mood
            self.moodbg.setVisible(True)
            self.moodtitle.setVisible(True)
            self.month1.setVisible(True)
            self.month2.setVisible(True)
            self.month3.setVisible(True)
            self.month4.setVisible(True)
            self.month5.setVisible(True)
            self.month6.setVisible(True)
            self.month7.setVisible(True)
            self.month8.setVisible(True)
            self.month9.setVisible(True)
            self.month10.setVisible(True)
            self.month11.setVisible(True)
            self.month12.setVisible(True)
            self.monthnumside.setVisible(True)
            self.daynumshor.setVisible(True)
            self.monthtitle.setVisible(True)
            self.btnred.setVisible(True)
            self.btnorange.setVisible(True)
            self.btnyellow.setVisible(True)
            self.btngreen.setVisible(True)
            self.btnblue.setVisible(True)
            self.confirmselectmonth.setVisible(True)
            self.selectmonth.setVisible(True)
            self.selectmonthtitle.setVisible(True)
            self.moodoptions.setVisible(True)
            self.moodnotes.setVisible(True)
            self.deletemood.setVisible(True)
        else:
            self.notes.setVisible(True)
            self.notesbg.setVisible(True)
            self.notesheader.setVisible(True)
            self.calendar.setVisible(True)
            self.calendartitle.setVisible(True)
            self.checklistwidget.setVisible(True)
            self.checklisttext.setVisible(True)
            # mood
            self.moodbg.setVisible(False)
            self.moodtitle.setVisible(False)
            self.month1.setVisible(False)
            self.month2.setVisible(False)
            self.month3.setVisible(False)
            self.month4.setVisible(False)
            self.month5.setVisible(False)
            self.month6.setVisible(False)
            self.month7.setVisible(False)
            self.month8.setVisible(False)
            self.month9.setVisible(False)
            self.month10.setVisible(False)
            self.month11.setVisible(False)
            self.month12.setVisible(False)
            self.monthnumside.setVisible(False)
            self.daynumshor.setVisible(False)
            self.monthtitle.setVisible(False)
            self.btnred.setVisible(False)
            self.btnorange.setVisible(False)
            self.btnyellow.setVisible(False)
            self.btngreen.setVisible(False)
            self.btnblue.setVisible(False)
            self.confirmselectmonth.setVisible(False)
            self.selectmonth.setVisible(False)
            self.selectmonthtitle.setVisible(False)
            self.moodoptions.setVisible(False)
            self.moodnotes.setVisible(False)
            self.deletemood.setVisible(False)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
