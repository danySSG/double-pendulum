from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QSlider,
    QLabel,
    QMenuBar,
    QStatusBar,
    QApplication,
    QMainWindow,
)
from PyQt5.QtCore import QThread, QRect, Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon

from manim.utils.file_ops import open_file as open_media_file
from styles import general_style, anime_button, pdf_button
from animation3 import Phase_Space
from os import startfile, path
from shutil import rmtree


class AnimationThread(QThread):
    def __init__(self, scene):
        QThread.__init__(self)
        self.scene = scene

    def run(self):
        self.scene.render()
        open_media_file(self.scene.renderer.file_writer.movie_file_path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Проверить, существует ли директория
        if path.exists("media/videos"):
            # Если существует, то удалить
            rmtree("media/videos")

        MainWindow.setStyleSheet(general_style)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(580, 420)  # Запрет изменения размера окна
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_button = QPushButton(self.centralwidget)
        self.main_button.setStyleSheet(anime_button)
        self.main_button.setGeometry(QRect(15, 340, 210, 60))
        self.main_button.setObjectName("main_button")

        self.pdf_button = QPushButton(self.centralwidget)
        self.pdf_button.setStyleSheet(pdf_button)
        self.pdf_button.setGeometry(QRect(235, 340, 340, 60))
        self.pdf_button.setObjectName("pdf_button")

        self.angle1_slider = QSlider(self.centralwidget)
        self.angle1_slider.setGeometry(QRect(20, 20, 200, 20))
        self.angle1_slider.setMinimum(-314)
        self.angle1_slider.setMaximum(314)
        self.angle1_slider.setProperty("value", 271)
        self.angle1_slider.setOrientation(Qt.Horizontal)
        self.angle1_slider.setObjectName("angle1_slider")

        self.angle2_slider = QSlider(self.centralwidget)
        self.angle2_slider.setGeometry(QRect(20, 60, 200, 20))
        self.angle2_slider.setMinimum(-314)
        self.angle2_slider.setMaximum(314)
        self.angle2_slider.setProperty("value", 271)
        self.angle2_slider.setOrientation(Qt.Horizontal)
        self.angle2_slider.setObjectName("angle2_slider")

        self.gravity_slider = QSlider(self.centralwidget)
        self.gravity_slider.setGeometry(QRect(20, 100, 200, 20))
        self.gravity_slider.setMaximum(100)
        self.gravity_slider.setProperty("value", 20)
        self.gravity_slider.setOrientation(Qt.Horizontal)
        self.gravity_slider.setObjectName("gravity_slider")

        self.length1_slider = QSlider(self.centralwidget)
        self.length1_slider.setGeometry(QRect(20, 140, 200, 20))
        self.length1_slider.setMinimum(1)
        self.length1_slider.setMaximum(100)
        self.length1_slider.setSingleStep(1)
        self.length1_slider.setProperty("value", 10)
        self.length1_slider.setOrientation(Qt.Horizontal)
        self.length1_slider.setObjectName("length1_slider")

        self.length2_slider = QSlider(self.centralwidget)
        self.length2_slider.setGeometry(QRect(20, 180, 200, 20))
        self.length2_slider.setMinimum(1)
        self.length2_slider.setMaximum(100)
        self.length2_slider.setSingleStep(1)
        self.length2_slider.setProperty("value", 10)
        self.length2_slider.setOrientation(Qt.Horizontal)
        self.length2_slider.setObjectName("length2_slider")

        self.mass1_slider = QSlider(self.centralwidget)
        self.mass1_slider.setGeometry(QRect(20, 220, 200, 20))
        self.mass1_slider.setMinimum(1)
        self.mass1_slider.setMaximum(100)
        self.mass1_slider.setSingleStep(1)
        self.mass1_slider.setProperty("value", 50)
        self.mass1_slider.setOrientation(Qt.Horizontal)
        self.mass1_slider.setObjectName("mass1_slider")

        self.mass2_slider = QSlider(self.centralwidget)
        self.mass2_slider.setGeometry(QRect(20, 260, 200, 20))
        self.mass2_slider.setMinimum(1)
        self.mass2_slider.setMaximum(100)
        self.mass2_slider.setSingleStep(1)
        self.mass2_slider.setProperty("value", 50)
        self.mass2_slider.setOrientation(Qt.Horizontal)
        self.mass2_slider.setObjectName("mass2_slider")

        self.time_slider = QSlider(self.centralwidget)
        self.time_slider.setGeometry(QRect(20, 300, 200, 20))
        self.time_slider.setMinimum(1)
        self.time_slider.setMaximum(100)
        self.time_slider.setProperty("value", 30)
        self.time_slider.setOrientation(Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")

        self.angle1_label = QLabel(self.centralwidget)
        self.angle1_label.setGeometry(QRect(240, 20, 330, 20))
        self.angle1_label.setObjectName("angle1_label")

        self.angle2_label = QLabel(self.centralwidget)
        self.angle2_label.setGeometry(QRect(240, 60, 330, 20))
        self.angle2_label.setObjectName("angle2_label")

        self.gravity_label = QLabel(self.centralwidget)
        self.gravity_label.setGeometry(QRect(240, 100, 330, 20))
        self.gravity_label.setObjectName("gravity_label")

        self.length1_label = QLabel(self.centralwidget)
        self.length1_label.setGeometry(QRect(240, 140, 330, 20))
        self.length1_label.setObjectName("length1_label")

        self.length2_label = QLabel(self.centralwidget)
        self.length2_label.setGeometry(QRect(240, 180, 330, 20))
        self.length2_label.setObjectName("length2_label")

        self.mass1_label = QLabel(self.centralwidget)
        self.mass1_label.setGeometry(QRect(240, 220, 330, 20))
        self.mass1_label.setObjectName("mass1_label")

        self.mass2_label = QLabel(self.centralwidget)
        self.mass2_label.setGeometry(QRect(240, 260, 330, 20))
        self.mass2_label.setObjectName("mass2_label")

        self.time_label = QLabel(self.centralwidget)
        self.time_label.setGeometry(QRect(240, 300, 330, 20))
        self.time_label.setObjectName("time_label")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Двойной"))
        MainWindow.setWindowIcon(QIcon("icon.ico"))
        self.main_button.setText(_translate("MainWindow", "Анимировать"))
        self.pdf_button.setText(_translate("MainWindow", "Читать теорию"))
        self.angle1_label.setText(
            _translate(
                "MainWindow", f"Первый угол: {self.angle1_slider.value()/100} rad"
            )
        )
        self.angle2_label.setText(
            _translate(
                "MainWindow", f"Второй угол: {self.angle2_slider.value()/100} rad"
            )
        )
        self.gravity_label.setText(
            _translate(
                "MainWindow",
                f"Ускорение свободного падения: {self.gravity_slider.value()/10} м/с^2",
            )
        )
        self.length1_label.setText(
            _translate(
                "MainWindow",
                f"Длина первого стержня: {self.length1_slider.value()/10} м",
            )
        )
        self.length2_label.setText(
            _translate(
                "MainWindow",
                f"Длина второго стержня: {self.length2_slider.value()/10} м",
            )
        )
        self.mass1_label.setText(
            _translate(
                "MainWindow", f"Масса первого груза: {self.mass1_slider.value()/10} кг"
            )
        )
        self.mass2_label.setText(
            _translate(
                "MainWindow", f"Масса второго груза: {self.mass2_slider.value()/10} кг"
            )
        )
        self.time_label.setText(
            _translate(
                "MainWindow", f"Время симуляции: {self.time_slider.value()} секунд"
            )
        )

    def add_functions(self):
        self.main_button.clicked.connect(self.make_animation)

        self.pdf_button.clicked.connect(self.open_pdf)

        self.angle1_slider.valueChanged.connect(self.change_label_angle1)
        self.angle2_slider.valueChanged.connect(self.change_label_angle2)
        self.gravity_slider.valueChanged.connect(self.change_label_gravity)
        self.length1_slider.valueChanged.connect(self.change_label_length1)
        self.length2_slider.valueChanged.connect(self.change_label_length2)
        self.mass1_slider.valueChanged.connect(self.change_label_mass1)
        self.mass2_slider.valueChanged.connect(self.change_label_mass2)
        self.time_slider.valueChanged.connect(self.change_label_time)

    def open_pdf(self):
        startfile("theory.pdf")

    def make_animation(self):
        self.main_button.setEnabled(False)
        self.main_button.setText("Анимация готовится...")
        self.main_button.setStyleSheet("background-color: grey;")
        scene = Phase_Space(
            self.angle1_slider.value() / 100,
            self.angle2_slider.value() / 100,
            self.gravity_slider.value() / 10,
            self.length1_slider.value() / 10,
            self.length2_slider.value() / 10,
            self.mass1_slider.value() / 10,
            self.mass2_slider.value() / 10,
            self.time_slider.value(),
        )
        self.thread = AnimationThread(scene)
        self.thread.finished.connect(self.on_animation_finished)
        self.thread.start()

    def on_animation_finished(self):
        self.main_button.setEnabled(True)
        self.main_button.setText("Анимировать")
        self.main_button.setStyleSheet("background-color: #ff5a1f;")

    def change_label_angle1(self):
        self.angle1_label.setText(f"Первый угол: {self.angle1_slider.value()/100} rad")

    def change_label_angle2(self):
        self.angle2_label.setText(f"Второй угол: {self.angle2_slider.value()/100} rad")

    def change_label_gravity(self):
        self.gravity_label.setText(
            f"Ускорение свободного падения: {self.gravity_slider.value()/10} м/с^2"
        )

    def change_label_length1(self):
        self.length1_label.setText(
            f"Длина первого стержня: {self.length1_slider.value()/10} м"
        )

    def change_label_length2(self):
        self.length2_label.setText(
            f"Длина второго стержня: {self.length2_slider.value()/10} м"
        )

    def change_label_mass1(self):
        self.mass1_label.setText(
            f"Масса первого груза: {self.mass1_slider.value()/10} кг"
        )

    def change_label_mass2(self):
        self.mass2_label.setText(
            f"Масса второго груза: {self.mass2_slider.value()/10} кг"
        )

    def change_label_time(self):
        self.time_label.setText(f"Время симуляции: {self.time_slider.value()} секунд")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
