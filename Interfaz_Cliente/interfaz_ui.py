# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 460)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{	\n"
"	border:none;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #01070A;\n"
"	\n"
"}\n"
"#side_menu{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	\n"
"}\n"
"QPushButton{\n"
"	padding: 5px;\n"
"	background-color: #01070A;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"#main_body{\n"
"	background-color: #17202A;\n"
"	border-radius: 10px;\n"
"\n"
"\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, -1, -1)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setStyleSheet(u"QFrame {\n"
"border: 1px solid #151515;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"pushButton {\n"
"border: 1px solid #ffffff;\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.homeBtn = QPushButton(self.frame)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy)
        self.homeBtn.setMinimumSize(QSize(132, 40))
        self.homeBtn.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Sitka Display"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.homeBtn.setFont(font)
        self.homeBtn.setFocusPolicy(Qt.NoFocus)
        self.homeBtn.setAcceptDrops(False)
        self.homeBtn.setToolTipDuration(0)
        self.homeBtn.setLayoutDirection(Qt.LeftToRight)
        self.homeBtn.setStyleSheet(u"QPushButton {\n"
"	\n"
"	border: 0.5px solid #000000;\n"
"	\n"
"	font: 75 16pt \"Sitka Display\";\n"
"	background-color: rgb(0, 0, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/bluehousehousehome_azulcasa_cas_6791.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.homeBtn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"QLabel {\n"
"	border: 1px solid #ffffff;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"	")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"QFrame {\n"
"border: 0px solid #000000;\n"
"\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QCustomSlideMenu(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setLayoutDirection(Qt.LeftToRight)
        self.side_menu.setStyleSheet(u"border-radius: 10px;")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(80, 0))
        self.pushButton_2.setMaximumSize(QSize(80, 80))
        font2 = QFont()
        font2.setPointSize(20)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #ffffff;\n"
"border-radius: 40px;	\n"
"color: rgb(255, 255, 255);\n"
"border-width: 3px;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #ffffff;\n"
"border-radius: 20px;	\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(80, 0))
        self.pushButton_4.setMaximumSize(QSize(80, 80))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #ffffff;\n"
"border-radius: 40px;	\n"
"color: rgb(255, 255, 255);\n"
"border-width: 3px;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #ffffff;\n"
"border-radius: 20px;	\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.side_menu, 0, Qt.AlignLeft)

        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy3)
        self.main_body.setStyleSheet(u"color: rgb(21, 21, 21);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.main_body)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.main_body)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
#if QT_CONFIG(shortcut)
        self.homeBtn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"MONITOREO", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"207", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"95%", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Unidades", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MAIN-BODY", None))
    # retranslateUi

