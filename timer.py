import sys
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox,
    QPushButton, QScrollArea, QFrame, QSizePolicy
)
from PyQt5.QtGui import QFont

class TimerWorker(QThread):
    update_time = pyqtSignal(int, int)
    timer_finished = pyqtSignal(int)

    def __init__(self, duration, timer_id):
        super().__init__()
        self.duration = duration
        self.timer_id = timer_id

    def run(self):
        for i in range(self.duration, 0, -1):
            self.update_time.emit(self.timer_id, i)
            self.sleep(1)
        self.timer_finished.emit(self.timer_id)

class MultiTimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.timer_widgets = []
        self.timer_workers = []

    def init_ui(self):
        self.setWindowTitle("Multi-Timer App")
        self.setGeometry(100, 100, 600, 500)

        self.num_timers_input = QSpinBox()
        self.num_timers_input.setRange(1, 10)
        self.num_timers_input.setValue(3)

        self.set_timers_button = QPushButton("Set Timer")
        self.set_timers_button.clicked.connect(self.setup_timers)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Jumlah Timer:"))
        input_layout.addWidget(self.num_timers_input)
        input_layout.addWidget(self.set_timers_button)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #F9F9F9;
            }
            QScrollBar:vertical {
                background: #E0E0E0;
                width: 10px;
            }
            QScrollBar::handle:vertical {
                background: black;
                border-radius: 5px;
            }
        """)

        self.scroll_content = QWidget()
        self.timer_layout = QVBoxLayout(self.scroll_content)
        self.timer_layout.setSpacing(15)
        self.timer_layout.setContentsMargins(15, 15, 15, 15)
        self.scroll_area.setWidget(self.scroll_content)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

    def setup_timers(self):
        for i in reversed(range(self.timer_layout.count())):
            widget = self.timer_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        self.timer_widgets.clear()
        self.timer_workers.clear()

        num_timers = self.num_timers_input.value()
        for i in range(1, num_timers + 1):
            timer_widget = TimerWidget(i, self)
            self.timer_layout.addWidget(timer_widget)
            self.timer_widgets.append(timer_widget)

    def start_timer(self, timer_id, duration):
        timer_worker = TimerWorker(duration, timer_id)
        timer_worker.update_time.connect(self.update_timer)
        timer_worker.timer_finished.connect(self.timer_done)
        timer_worker.start()
        self.timer_workers.append(timer_worker)

    def update_timer(self, timer_id, time_left):
        if 0 < timer_id <= len(self.timer_widgets):
            self.timer_widgets[timer_id - 1].update_timer_label(time_left)

    def timer_done(self, timer_id):
        if 0 < timer_id <= len(self.timer_widgets):
            self.timer_widgets[timer_id - 1].timer_done()

class TimerWidget(QFrame):
    def __init__(self, timer_id, parent=None):
        super().__init__(parent)
        self.timer_id = timer_id
        self.parent_app = parent
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #E0E0E0;
                border-radius: 10px;
                padding: 10px;
                color: black;
            }
        """)

        self.setFixedHeight(150)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.duration_input = QSpinBox()
        self.duration_input.setRange(1, 3600)
        self.duration_input.setValue(10)

        self.start_button = QPushButton(f"Mulai Timer {self.timer_id}")
        self.start_button.setFont(QFont("Arial", 12))
        self.start_button.setStyleSheet("color: #333;")
        self.start_button.clicked.connect(self.start_timer)

        self.timer_label = QLabel(f"Timer {self.timer_id}: Belum dimulai")
        self.timer_label.setFont(QFont("Arial", 12))
        self.timer_label.setStyleSheet("color: #333;")

        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        top_layout.addWidget(QLabel(f"Timer {self.timer_id}:"))
        top_layout.addWidget(self.duration_input)
        top_layout.addWidget(self.start_button)

        layout.addLayout(top_layout)
        layout.addWidget(self.timer_label)
        self.setLayout(layout)

    def start_timer(self):
        duration = self.duration_input.value()
        self.start_button.setDisabled(True)
        self.parent_app.start_timer(self.timer_id, duration)

    def update_timer_label(self, time_left):
        self.timer_label.setText(f"Timer {self.timer_id}: {time_left} detik tersisa")

    def timer_done(self):
        self.timer_label.setText(f"Timer {self.timer_id}: Waktu habis!")
        self.start_button.setDisabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    multi_timer_app = MultiTimerApp()
    multi_timer_app.show()
    sys.exit(app.exec_())