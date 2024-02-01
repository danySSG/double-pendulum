from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QMenuBar,
    QStatusBar,
    QApplication,
    QMainWindow,
)
from PyQt5.QtCore import QThread, QRect, Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon

from threading import *
from styles import general_style, anime_button
from os import system


def running_window1():
    system("python window1.py")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setStyleSheet(general_style)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(380, 220)  # Запрет изменения размера окна
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.window1_button = QPushButton(self.centralwidget)
        self.window1_button.setStyleSheet(anime_button)
        self.window1_button.setGeometry(QRect(15, 20, 350, 60))
        self.window1_button.setObjectName("window1_button")

        self.window2_button = QPushButton(self.centralwidget)
        self.window2_button.setStyleSheet(anime_button)
        self.window2_button.setGeometry(QRect(15, 80, 350, 60))
        self.window2_button.setObjectName("window2_button")

        self.window3_button = QPushButton(self.centralwidget)
        self.window3_button.setStyleSheet(anime_button)
        self.window3_button.setGeometry(QRect(15, 140, 350, 60))
        self.window3_button.setObjectName("window3_button")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 380, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Комплекс"))
        MainWindow.setWindowIcon(QIcon("icon.ico"))
        self.window1_button.setText(_translate("MainWindow", "Автономный маятник"))
        self.window2_button.setText(
            _translate("MainWindow", "Маятник с периодическим возмущением")
        )
        self.window3_button.setText(_translate("MainWindow", "Двойной маятник"))

    def add_functions(self):
        self.window1_button.clicked.connect(self.open_window1)
        self.window2_button.clicked.connect(self.open_window2)
        self.window3_button.clicked.connect(self.open_window3)

    def open_window1(self):
        t1 = Thread(target=running_window1)
        t1.start()

    def open_window2(self):
        pass

    def open_window3(self):
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
