import sys, os, pytube
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QApplication, QFileDialog, qApp, QAction, QMainWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

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

        self.url_le.selectAll()
        self.url_le.setFocus()

        self.btn_dwn.clicked.connect(lambda:self.get_video(self.url_le.text()))

        self.setLayout(layout)

        self.show()

    def get_video(self, url):
        try:
            video = pytube.YouTube(url, on_progress_callback=self.progress).streams.first().download()
        except pytube.exceptions.VideoUnavailable:
            print('Not available')

    def progress(self, stream, chunk, file_handle, bytes_remaining):
        size = stream.filesize
        print(str(100 - (100 * bytes_remaining / size)) + '%')


class ErrorWindow(QWidget):
    def __init__(self, error):
        super().__init__()
        self.msg_error = error

        self.init_ui()

    def init_ui(self):
        pass

class YouTubeManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window = MainWindow()
        self.setCentralWidget(self.main_window)

        self.init_ui()

    def init_ui(self):
        self.show()

#print(yt.streams.all())
app = QApplication(sys.argv)
yt_manager = YouTubeManager()
sys.exit(app.exec_())




