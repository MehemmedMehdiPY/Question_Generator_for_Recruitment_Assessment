from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QVBoxLayout, QWidget, QTextEdit, QListWidget, QListWidgetItem, QAbstractItemView
import sys

class MainWindow(QMainWindow):
    instruction_selected = False

    def __init__(self):
        super().__init__()

        self.setWindowTitle("App")
        self.setGeometry(100, 100, 200, 300)

        label = QLabel("Choose the number of questions")
        selection = QListWidget()
        selection.setSelectionMode(QAbstractItemView.NoSelection)
        selection.setGeometry(100, 100, 200, 300)
        self.__upload_items(selection)
        selection.currentRowChanged.connect(lambda : self.selection_triggered(selection))
        
        button = QPushButton("Button")
        button.clicked.connect(lambda : self.button_triggered(selection))
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(selection)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def button_triggered(self, selection):

        if not self.instruction_selected:
            msg = "Please, choose the number of questions"        
        else:
            n_questions = self.items[selection.currentRow()].text()
            msg = "Model started processing on {} questions".format(n_questions)
            self.run_model()
            self.instruction_selected = False
            selection.setCurrentRow(-1)

        message = QMessageBox()
        message.setText(msg)
        message.setGeometry(700, 700, 500, 500)
        message.exec_()

    def __upload_items(self, selection):
        item_0 = QListWidgetItem("10")
        item_1 = QListWidgetItem("20")
        selection.addItem(item_0)
        selection.addItem(item_1)
        self.items = [item_0, item_1]
    
    def selection_triggered(self, selection):
        if selection.currentRow() != -1:
            self.instruction_selected = True

    def run_model(self):
        print("There you go")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()