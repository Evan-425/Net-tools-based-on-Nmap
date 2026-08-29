# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1158, 661)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 20, 81, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 71, 21))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 80, 591, 23))
        self.progressBar.setValue(24)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 50, 61, 16))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 50, 81, 21))
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(630, 0, 211, 161))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(770, 371, 371, 201))
        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(390, 370, 371, 201))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(40, 130, 71, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 110, 41, 16))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(40, 190, 301, 22))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 160, 221, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(780, 350, 71, 16))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(220, 40, 101, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 20, 81, 16))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(40, 310, 301, 22))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(40, 250, 71, 31))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 230, 41, 16))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 280, 221, 20))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 350, 71, 16))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(40, 340, 301, 31))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(40, 370, 301, 31))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(40, 580, 301, 31))
        self.listWidget_3 = QListWidget(self.centralwidget)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setGeometry(QRect(40, 440, 301, 141))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(410, 40, 101, 16))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(40, 420, 301, 20))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 400, 151, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1158, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5bfb\u627e\u7ec4\u4ef6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u672a\u627e\u5230\u7ec4\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u5f85\u521d\u59cb\u5316", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u5316", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8Nmap", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nmap1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nmap1\u8f93\u51fa\uff1a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u547d\u4ee4\u63d0\u793a\u7b26", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u63d0\u793a\u7b26", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8Nmap", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nmap2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nmap2\u8f93\u51fa\uff1a", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8Zenmap", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"---\u5206\u6790\u5f53\u524d\u7f51\u7edc---", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u5206\u6790\u7ed3\u679c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u4efd\u9a8c\u8bc1\u672a\u901a\u8fc7", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165ip\u6bb5,\u4f8b\u5982192.168.0.1/24", None))
    # retranslateUi

