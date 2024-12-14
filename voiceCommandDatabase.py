# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voiceCommandDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from voiceRecorderDialog import Ui_voiceRecorderDialog


class Ui_MainWindow(object):
    def open_record_page(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_voiceRecorderDialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 480)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 1px solid darkgray;*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/qss_icons/DarkOrange/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 1px solid darkgray;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/qss_icons/DarkOrange/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/qss_icons/DarkOrange/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid darkgray;\n"
"\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameFilter = QtWidgets.QFrame(self.centralwidget)
        self.frameFilter.setGeometry(QtCore.QRect(30, 20, 432, 311))
        self.frameFilter.setStyleSheet("background-color:#ffa850;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: #556B2F;\n"
"border-radius: 5px;")
        self.frameFilter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFilter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFilter.setObjectName("frameFilter")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameFilter)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetFilterLanguage = QtWidgets.QWidget(self.frameFilter)
        self.widgetFilterLanguage.setStyleSheet("border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ffe5d8;")
        self.widgetFilterLanguage.setObjectName("widgetFilterLanguage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widgetFilterLanguage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.labelFilterLanguage = QtWidgets.QLabel(self.widgetFilterLanguage)
        self.labelFilterLanguage.setStyleSheet("background-color: #ff9b0f;\n"
"color: black;\n"
"border-color: #4d4018;")
        self.labelFilterLanguage.setObjectName("labelFilterLanguage")
        self.horizontalLayout_22.addWidget(self.labelFilterLanguage)
        spacerItem = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem)
        self.radioButtonFilterLanguageTurkish = QtWidgets.QRadioButton(self.widgetFilterLanguage)
        self.radioButtonFilterLanguageTurkish.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonFilterLanguageTurkish.setStyleSheet("QRadioButton{\n"
"    background-color: #ff6d49;\n"
"    color: black;;\n"
"    border-color: #4d4018;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"    background-color: red;\n"
"}\n"
"")
        self.radioButtonFilterLanguageTurkish.setChecked(True)
        self.radioButtonFilterLanguageTurkish.setAutoExclusive(False)
        self.radioButtonFilterLanguageTurkish.setObjectName("radioButtonFilterLanguageTurkish")
        self.horizontalLayout_22.addWidget(self.radioButtonFilterLanguageTurkish)
        spacerItem1 = QtWidgets.QSpacerItem(88, 77, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem1)
        self.radioButtonFilterLanguageEnglish = QtWidgets.QRadioButton(self.widgetFilterLanguage)
        self.radioButtonFilterLanguageEnglish.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonFilterLanguageEnglish.setStyleSheet("QRadioButton{\n"
"    background-color: #ff6d49;\n"
"    color: black;;\n"
"    border-color: #4d4018;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"    background-color: red;\n"
"}\n"
"")
        self.radioButtonFilterLanguageEnglish.setChecked(True)
        self.radioButtonFilterLanguageEnglish.setAutoExclusive(False)
        self.radioButtonFilterLanguageEnglish.setObjectName("radioButtonFilterLanguageEnglish")
        self.horizontalLayout_22.addWidget(self.radioButtonFilterLanguageEnglish)
        self.gridLayout_5.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widgetFilterLanguage)
        self.widgetFilterGender = QtWidgets.QWidget(self.frameFilter)
        self.widgetFilterGender.setStyleSheet("border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ffe5d8;")
        self.widgetFilterGender.setObjectName("widgetFilterGender")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widgetFilterGender)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelFilterGender = QtWidgets.QLabel(self.widgetFilterGender)
        self.labelFilterGender.setStyleSheet("background-color: #ff9b0f;\n"
"color: black;\n"
"border-color: #4d4018;")
        self.labelFilterGender.setObjectName("labelFilterGender")
        self.gridLayout_4.addWidget(self.labelFilterGender, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 1, 1, 1)
        self.radioButtonFilterGenderMale = QtWidgets.QRadioButton(self.widgetFilterGender)
        self.radioButtonFilterGenderMale.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonFilterGenderMale.setStyleSheet("QRadioButton{\n"
"    background-color: #ff6d49;\n"
"    color: black;;\n"
"    border-color: #4d4018;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"    background-color: red;\n"
"}\n"
"")
        self.radioButtonFilterGenderMale.setChecked(True)
        self.radioButtonFilterGenderMale.setAutoExclusive(False)
        self.radioButtonFilterGenderMale.setObjectName("radioButtonFilterGenderMale")
        self.gridLayout_4.addWidget(self.radioButtonFilterGenderMale, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 3, 1, 1)
        self.radioButtonFilterGenderFemale = QtWidgets.QRadioButton(self.widgetFilterGender)
        self.radioButtonFilterGenderFemale.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonFilterGenderFemale.setStyleSheet("QRadioButton{\n"
"    background-color: #ff6d49;\n"
"    color: black;;\n"
"    border-color: #4d4018;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"    background-color: red;\n"
"}\n"
"")
        self.radioButtonFilterGenderFemale.setChecked(True)
        self.radioButtonFilterGenderFemale.setAutoExclusive(False)
        self.radioButtonFilterGenderFemale.setObjectName("radioButtonFilterGenderFemale")
        self.gridLayout_4.addWidget(self.radioButtonFilterGenderFemale, 0, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.widgetFilterGender)
        self.widgetFilterName = QtWidgets.QWidget(self.frameFilter)
        self.widgetFilterName.setStyleSheet("border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ffe5d8;")
        self.widgetFilterName.setObjectName("widgetFilterName")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widgetFilterName)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.labelFilterName = QtWidgets.QLabel(self.widgetFilterName)
        self.labelFilterName.setStyleSheet("background-color: #ff9b0f;\n"
"color: black;\n"
"border-color: #4d4018;")
        self.labelFilterName.setObjectName("labelFilterName")
        self.horizontalLayout_21.addWidget(self.labelFilterName)
        self.gridLayout_3.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.comboBoxFilterName = QtWidgets.QComboBox(self.widgetFilterName)
        self.comboBoxFilterName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxFilterName.setStyleSheet("QComboBox{\n"
"    background-color: #ff6d49;\n"
"    color: black;;\n"
"    border-color: #4d4018;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    background-color: red;\n"
"}\n"
"")
        self.comboBoxFilterName.setObjectName("comboBoxFilterName")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.comboBoxFilterName.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxFilterName, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widgetFilterName)
        self.widgetFilterCommend = QtWidgets.QWidget(self.frameFilter)
        self.widgetFilterCommend.setStyleSheet("border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ffe5d8;")
        self.widgetFilterCommend.setObjectName("widgetFilterCommend")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widgetFilterCommend)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.labelFilterCommend = QtWidgets.QLabel(self.widgetFilterCommend)
        self.labelFilterCommend.setStyleSheet("background-color: #ff9b0f;\n"
"color: black;\n"
"border-color: #4d4018;")
        self.labelFilterCommend.setObjectName("labelFilterCommend")
        self.horizontalLayout_27.addWidget(self.labelFilterCommend)
        self.gridLayout_10.addLayout(self.horizontalLayout_27, 0, 0, 1, 1)
        self.comboBoxFilterCommend = QtWidgets.QComboBox(self.widgetFilterCommend)
        self.comboBoxFilterCommend.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxFilterCommend.setStyleSheet("QComboBox{\n"
"    background-color: #ff6d49;\n"
"    color: black;;\n"
"    border-color: #4d4018;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    background-color: red;\n"
"}\n"
"")
        self.comboBoxFilterCommend.setObjectName("comboBoxFilterCommend")
        self.comboBoxFilterCommend.addItem("")
        self.comboBoxFilterCommend.addItem("")
        self.comboBoxFilterCommend.addItem("")
        self.gridLayout_10.addWidget(self.comboBoxFilterCommend, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widgetFilterCommend)
        self.frameList = QtWidgets.QFrame(self.centralwidget)
        self.frameList.setGeometry(QtCore.QRect(500, 20, 521, 311))
        self.frameList.setStyleSheet("background-color:#ffa850;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: #556B2F;\n"
"border-radius: 5px;")
        self.frameList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameList.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameList.setObjectName("frameList")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frameList)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollAreaList = QtWidgets.QScrollArea(self.frameList)
        self.scrollAreaList.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"background-color: #ffe5d8;")
        self.scrollAreaList.setWidgetResizable(True)
        self.scrollAreaList.setObjectName("scrollAreaList")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 485, 275))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollAreaList.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.addWidget(self.scrollAreaList, 1, 0, 1, 1)
        self.frameButtons = QtWidgets.QFrame(self.centralwidget)
        self.frameButtons.setGeometry(QtCore.QRect(30, 360, 521, 61))
        self.frameButtons.setStyleSheet("background-color:#ffa850;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: #556B2F;\n"
"border-radius: 5px;")
        self.frameButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButtons.setObjectName("frameButtons")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frameButtons)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButtonButtonsFilterData = QtWidgets.QPushButton(self.frameButtons)
        self.pushButtonButtonsFilterData.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonButtonsFilterData.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ff6d49;\n"
"border-color: #4d4018;\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: red;\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: orange;\n"
"    \n"
"}")
        self.pushButtonButtonsFilterData.setObjectName("pushButtonButtonsFilterData")
        self.gridLayout_8.addWidget(self.pushButtonButtonsFilterData, 0, 0, 1, 1)
        self.pushButtonButtonsShowAllData = QtWidgets.QPushButton(self.frameButtons)
        self.pushButtonButtonsShowAllData.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonButtonsShowAllData.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ff6d49;\n"
"border-color: #4d4018;\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: red;\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: orange;\n"
"    \n"
"}")
        self.pushButtonButtonsShowAllData.setObjectName("pushButtonButtonsShowAllData")
        self.gridLayout_8.addWidget(self.pushButtonButtonsShowAllData, 0, 1, 1, 1)
        self.pushButtonButtonsDownloadData = QtWidgets.QPushButton(self.frameButtons)
        self.pushButtonButtonsDownloadData.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonButtonsDownloadData.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ff6d49;\n"
"border-color: #4d4018;\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: red;\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: orange;\n"
"    \n"
"}")
        self.pushButtonButtonsDownloadData.setObjectName("pushButtonButtonsDownloadData")
        self.gridLayout_8.addWidget(self.pushButtonButtonsDownloadData, 0, 2, 1, 1)
        self.pushButtonButtonsClearData = QtWidgets.QPushButton(self.frameButtons)
        self.pushButtonButtonsClearData.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonButtonsClearData.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ff6d49;\n"
"border-color: #4d4018;\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: red;\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: orange;\n"
"    \n"
"}")
        self.pushButtonButtonsClearData.setObjectName("pushButtonButtonsClearData")
        self.gridLayout_8.addWidget(self.pushButtonButtonsClearData, 0, 3, 1, 1)
        self.widgetShowedData = QtWidgets.QWidget(self.centralwidget)
        self.widgetShowedData.setGeometry(QtCore.QRect(600, 360, 171, 61))
        self.widgetShowedData.setStyleSheet("border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ffe5d8;\n"
"border-color: #556B2F;")
        self.widgetShowedData.setObjectName("widgetShowedData")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widgetShowedData)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 1, 1, 1)
        self.labelShowedDataNumber = QtWidgets.QLabel(self.widgetShowedData)
        self.labelShowedDataNumber.setStyleSheet("background-color: #ff9b0f;\n"
"color: black;\n"
"border-color: #4d4018;\n"
"border-style: solid;\n"
"border-width: 3px;")
        self.labelShowedDataNumber.setObjectName("labelShowedDataNumber")
        self.gridLayout_6.addWidget(self.labelShowedDataNumber, 0, 3, 1, 1)
        self.labelShowedData = QtWidgets.QLabel(self.widgetShowedData)
        self.labelShowedData.setStyleSheet("background-color: #ff9b0f;\n"
"color: black;\n"
"border-color: #4d4018;")
        self.labelShowedData.setObjectName("labelShowedData")
        self.gridLayout_6.addWidget(self.labelShowedData, 0, 0, 1, 1)
        self.pushButtonRecordVoice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRecordVoice.setGeometry(QtCore.QRect(810, 360, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRecordVoice.setFont(font)


        self.pushButtonRecordVoice.clicked.connect(self.open_record_page)

        self.pushButtonRecordVoice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonRecordVoice.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"background-color: #ff6d49;\n"
"border-color: #4d4018;\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: red;\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: orange;\n"
"    \n"
"}")
        self.pushButtonRecordVoice.setObjectName("pushButtonRecordVoice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelFilterLanguage.setText(_translate("MainWindow", "Voice Language:"))
        self.radioButtonFilterLanguageTurkish.setText(_translate("MainWindow", "Turkish"))
        self.radioButtonFilterLanguageEnglish.setText(_translate("MainWindow", "English"))
        self.labelFilterGender.setText(_translate("MainWindow", "Voice Gender"))
        self.radioButtonFilterGenderMale.setText(_translate("MainWindow", "Male"))
        self.radioButtonFilterGenderFemale.setText(_translate("MainWindow", "Female"))
        self.labelFilterName.setText(_translate("MainWindow", "Name:"))
        self.comboBoxFilterName.setItemText(0, _translate("MainWindow", "All"))
        self.comboBoxFilterName.setItemText(1, _translate("MainWindow", "Yusuf"))
        self.comboBoxFilterName.setItemText(2, _translate("MainWindow", "Kaan"))
        self.comboBoxFilterName.setItemText(3, _translate("MainWindow", "Mehmet"))
        self.comboBoxFilterName.setItemText(4, _translate("MainWindow", "Dila"))
        self.comboBoxFilterName.setItemText(5, _translate("MainWindow", "Eylül"))
        self.comboBoxFilterName.setItemText(6, _translate("MainWindow", "Nursena"))
        self.comboBoxFilterName.setItemText(7, _translate("MainWindow", "Eren"))
        self.comboBoxFilterName.setItemText(8, _translate("MainWindow", "Barış"))
        self.comboBoxFilterName.setItemText(9, _translate("MainWindow", "Emre"))
        self.comboBoxFilterName.setItemText(10, _translate("MainWindow", "Emin"))
        self.labelFilterCommend.setText(_translate("MainWindow", "Commend:"))
        self.comboBoxFilterCommend.setItemText(0, _translate("MainWindow", "All"))
        self.comboBoxFilterCommend.setItemText(1, _translate("MainWindow", "test"))
        self.comboBoxFilterCommend.setItemText(2, _translate("MainWindow", "deneme"))
        self.pushButtonButtonsFilterData.setText(_translate("MainWindow", "Filter Data"))
        self.pushButtonButtonsShowAllData.setText(_translate("MainWindow", "Show All Data"))
        self.pushButtonButtonsDownloadData.setText(_translate("MainWindow", "Download Data"))
        self.pushButtonButtonsClearData.setText(_translate("MainWindow", "Clear Data"))
        self.labelShowedDataNumber.setText(_translate("MainWindow", "22"))
        self.labelShowedData.setText(_translate("MainWindow", "Showed Data:"))
        self.pushButtonRecordVoice.setText(_translate("MainWindow", "Record Voice"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())