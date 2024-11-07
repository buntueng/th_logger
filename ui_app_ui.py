# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_app.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1361, 903)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.temperature_groupBox = QGroupBox(self.centralwidget)
        self.temperature_groupBox.setObjectName(u"temperature_groupBox")
        self.temperature_groupBox.setMinimumSize(QSize(520, 750))
        self.verticalLayout_2 = QVBoxLayout(self.temperature_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TCH1_label = QLabel(self.temperature_groupBox)
        self.TCH1_label.setObjectName(u"TCH1_label")

        self.verticalLayout_2.addWidget(self.TCH1_label)

        self.TCH1_widget = QWidget(self.temperature_groupBox)
        self.TCH1_widget.setObjectName(u"TCH1_widget")
        self.TCH1_widget.setMinimumSize(QSize(0, 100))

        self.verticalLayout_2.addWidget(self.TCH1_widget)

        self.TCH2_label = QLabel(self.temperature_groupBox)
        self.TCH2_label.setObjectName(u"TCH2_label")

        self.verticalLayout_2.addWidget(self.TCH2_label)

        self.TCH2_widget = QWidget(self.temperature_groupBox)
        self.TCH2_widget.setObjectName(u"TCH2_widget")
        self.TCH2_widget.setMinimumSize(QSize(0, 80))

        self.verticalLayout_2.addWidget(self.TCH2_widget)

        self.TCH3_label = QLabel(self.temperature_groupBox)
        self.TCH3_label.setObjectName(u"TCH3_label")

        self.verticalLayout_2.addWidget(self.TCH3_label)

        self.TCH3_widget = QWidget(self.temperature_groupBox)
        self.TCH3_widget.setObjectName(u"TCH3_widget")
        self.TCH3_widget.setMinimumSize(QSize(0, 80))

        self.verticalLayout_2.addWidget(self.TCH3_widget)

        self.TCH4_label = QLabel(self.temperature_groupBox)
        self.TCH4_label.setObjectName(u"TCH4_label")

        self.verticalLayout_2.addWidget(self.TCH4_label)

        self.TCH4_widget = QWidget(self.temperature_groupBox)
        self.TCH4_widget.setObjectName(u"TCH4_widget")
        self.TCH4_widget.setMinimumSize(QSize(0, 80))

        self.verticalLayout_2.addWidget(self.TCH4_widget)

        self.TCH5_label = QLabel(self.temperature_groupBox)
        self.TCH5_label.setObjectName(u"TCH5_label")

        self.verticalLayout_2.addWidget(self.TCH5_label)

        self.TCH5_widget = QWidget(self.temperature_groupBox)
        self.TCH5_widget.setObjectName(u"TCH5_widget")
        self.TCH5_widget.setMinimumSize(QSize(0, 80))

        self.verticalLayout_2.addWidget(self.TCH5_widget)

        self.TCH6_label = QLabel(self.temperature_groupBox)
        self.TCH6_label.setObjectName(u"TCH6_label")

        self.verticalLayout_2.addWidget(self.TCH6_label)

        self.TCH6_widget = QWidget(self.temperature_groupBox)
        self.TCH6_widget.setObjectName(u"TCH6_widget")
        self.TCH6_widget.setMinimumSize(QSize(0, 70))

        self.verticalLayout_2.addWidget(self.TCH6_widget)


        self.horizontalLayout.addWidget(self.temperature_groupBox)

        self.humidity_groupBox = QGroupBox(self.centralwidget)
        self.humidity_groupBox.setObjectName(u"humidity_groupBox")
        self.humidity_groupBox.setMinimumSize(QSize(520, 750))
        self.verticalLayout_3 = QVBoxLayout(self.humidity_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.HCH1_label = QLabel(self.humidity_groupBox)
        self.HCH1_label.setObjectName(u"HCH1_label")

        self.verticalLayout_3.addWidget(self.HCH1_label)

        self.HCH1_widget = QWidget(self.humidity_groupBox)
        self.HCH1_widget.setObjectName(u"HCH1_widget")

        self.verticalLayout_3.addWidget(self.HCH1_widget)

        self.HCH2_label = QLabel(self.humidity_groupBox)
        self.HCH2_label.setObjectName(u"HCH2_label")

        self.verticalLayout_3.addWidget(self.HCH2_label)

        self.HCH2_widget = QWidget(self.humidity_groupBox)
        self.HCH2_widget.setObjectName(u"HCH2_widget")

        self.verticalLayout_3.addWidget(self.HCH2_widget)

        self.HCH3_label = QLabel(self.humidity_groupBox)
        self.HCH3_label.setObjectName(u"HCH3_label")

        self.verticalLayout_3.addWidget(self.HCH3_label)

        self.HCH3_widget = QWidget(self.humidity_groupBox)
        self.HCH3_widget.setObjectName(u"HCH3_widget")

        self.verticalLayout_3.addWidget(self.HCH3_widget)

        self.HCH4_label = QLabel(self.humidity_groupBox)
        self.HCH4_label.setObjectName(u"HCH4_label")

        self.verticalLayout_3.addWidget(self.HCH4_label)

        self.HCH4_widget = QWidget(self.humidity_groupBox)
        self.HCH4_widget.setObjectName(u"HCH4_widget")

        self.verticalLayout_3.addWidget(self.HCH4_widget)

        self.HCH5_label = QLabel(self.humidity_groupBox)
        self.HCH5_label.setObjectName(u"HCH5_label")

        self.verticalLayout_3.addWidget(self.HCH5_label)

        self.HCH5_widget = QWidget(self.humidity_groupBox)
        self.HCH5_widget.setObjectName(u"HCH5_widget")

        self.verticalLayout_3.addWidget(self.HCH5_widget)

        self.HCH6_label = QLabel(self.humidity_groupBox)
        self.HCH6_label.setObjectName(u"HCH6_label")

        self.verticalLayout_3.addWidget(self.HCH6_label)

        self.HCH6_widget = QWidget(self.humidity_groupBox)
        self.HCH6_widget.setObjectName(u"HCH6_widget")

        self.verticalLayout_3.addWidget(self.HCH6_widget)


        self.horizontalLayout.addWidget(self.humidity_groupBox)

        self.status_groupBox = QGroupBox(self.centralwidget)
        self.status_groupBox.setObjectName(u"status_groupBox")
        self.status_groupBox.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.status_groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.status_plainTextEdit = QPlainTextEdit(self.status_groupBox)
        self.status_plainTextEdit.setObjectName(u"status_plainTextEdit")
        self.status_plainTextEdit.setMinimumSize(QSize(200, 500))
        self.status_plainTextEdit.setMaximumSize(QSize(280, 99999))
        self.status_plainTextEdit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.status_plainTextEdit)


        self.horizontalLayout.addWidget(self.status_groupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Temperature and Humidity monitor", None))
        self.temperature_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.TCH1_label.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.TCH2_label.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.TCH3_label.setText(QCoreApplication.translate("MainWindow", u"CH3", None))
        self.TCH4_label.setText(QCoreApplication.translate("MainWindow", u"CH4", None))
        self.TCH5_label.setText(QCoreApplication.translate("MainWindow", u"CH5", None))
        self.TCH6_label.setText(QCoreApplication.translate("MainWindow", u"CH6", None))
        self.humidity_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Humidityg", None))
        self.HCH1_label.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.HCH2_label.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.HCH3_label.setText(QCoreApplication.translate("MainWindow", u"CH3", None))
        self.HCH4_label.setText(QCoreApplication.translate("MainWindow", u"CH4", None))
        self.HCH5_label.setText(QCoreApplication.translate("MainWindow", u"CH5", None))
        self.HCH6_label.setText(QCoreApplication.translate("MainWindow", u"CH6", None))
        self.status_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"System status", None))
    # retranslateUi

