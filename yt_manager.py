import sys, os, pytube
from PyQt5.QtWidgets import QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QApplication, QFileDialog, qApp, QAction, QMainWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.url_lbl = QLabel('Video URL')
        self.url_le = QLineEdit()
        self.btn_dwn = QPushButton('Download')

        url_layout = QHBoxLayout()
        url_layout.addStretch()
        url_layout.addWidget(self.url_lbl)
        url_layout.addWidget(self.url_le)
        url_layout.addStretch()

        layout = QVBoxLayout()
        layout.addLayout(url_layout)
        layout.addWidget(self.btn_dwn)

        self.setLayout(layout)

        self.show()


app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec_())




