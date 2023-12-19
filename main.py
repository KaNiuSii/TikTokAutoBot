import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QFileDialog
from bot import run

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'File and Text Processor'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 500, 300)

        main_layout = QVBoxLayout()
        file_selection_layout = QHBoxLayout()
        text_input_layout = QVBoxLayout()

        self.file_path_label = QLabel("File Path:")
        self.file_path_entry = QLineEdit()
        self.select_file_button = QPushButton("Browse")
        self.select_file_button.clicked.connect(self.select_file)

        file_selection_layout.addWidget(self.file_path_label)
        file_selection_layout.addWidget(self.file_path_entry)
        file_selection_layout.addWidget(self.select_file_button)

        self.text_input_label = QLabel("Enter Caption:")
        self.text_input_box = QTextEdit()

        text_input_layout.addWidget(self.text_input_label)
        text_input_layout.addWidget(self.text_input_box)

        self.start_button = QPushButton("Run")
        self.start_button.clicked.connect(self.execute)

        main_layout.addLayout(file_selection_layout)
        main_layout.addLayout(text_input_layout)
        main_layout.addWidget(self.start_button)

        self.setLayout(main_layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        self.file_path_entry.setText(file_path)

    def execute(self):
        file_path = self.file_path_entry.text()
        text_input = self.text_input_box.toPlainText()
        
        with open('caption.txt', 'w') as f:
            f.write(text_input)
        run(file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
