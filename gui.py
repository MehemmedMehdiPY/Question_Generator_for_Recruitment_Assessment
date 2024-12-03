from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, QListWidget, QListWidgetItem, QAbstractItemView
import sys

class NumberOfQuestions:
    choices = [5, 10, 15, 20]

class DifficultyLevel:
    choices = ["easy", "medium", "hard"]

class Category:
    choices = ["numerical reasoning", "verbal reasoning", "situational judgment"]

class Format:
    choices = ["multiple-choice", "fill-in-the-blank", "true/false"]

class Customization:
    features = [NumberOfQuestions, DifficultyLevel, Category, Format]

class MainWindow(QMainWindow, Customization):
    number_of_questions_selected = False
    difficulty_level_selected = False
    category_selected = False
    format_selected = False

    def __init__(self):
        super().__init__()

        self.setWindowTitle("App")
        self.setGeometry(700, 200, 400, 600)

        questions_label = QLabel("Choose the number of questions")
        difficulty_label = QLabel("Choose a difficulty level")
        category_label = QLabel("Choose a category")
        format_label = QLabel("Choose a format")

        number_of_questions = self.__create_selection(0)
        number_of_questions.currentRowChanged.connect(lambda : self.number_of_questions_triggered(number_of_questions))
        
        difficulty_level = self.__create_selection(1)
        difficulty_level.currentRowChanged.connect(lambda : self.difficulty_level_triggered(difficulty_level))

        category = self.__create_selection(2)
        category.currentRowChanged.connect(lambda : self.category_triggered(category))
        
        format = self.__create_selection(3)
        format.currentRowChanged.connect(lambda x: self.format_triggered(format))

        button = QPushButton("Button")
        button.clicked.connect(lambda : self.button_triggered(number_of_questions, difficulty_level, category, format))
        
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()
        layout_top = QHBoxLayout()
        layout_bottom = QHBoxLayout()
        layout_final = QVBoxLayout()
        
        layout_left.addWidget(questions_label)
        layout_left.addWidget(number_of_questions)
        layout_left.addWidget(difficulty_label)
        layout_left.addWidget(difficulty_level)
        layout_right.addWidget(category_label)
        layout_right.addWidget(category)
        layout_right.addWidget(format_label)
        layout_right.addWidget(format)
        layout_bottom.addWidget(button)

        layout_top.addLayout(layout_left)
        layout_top.addLayout(layout_right)
        layout_final.addLayout(layout_top)
        layout_final.addLayout(layout_bottom)

        widget = QWidget()
        widget.setLayout(layout_final)
        self.setCentralWidget(widget)
    
    def button_triggered(self, number_of_questions, difficulty_level, category, format):
        self.run = True
        message = ""
        if not self.number_of_questions_selected:
            sentence = "Please, choose the number of questions\n"
            message = message + sentence
            self.run = False

        if not self.difficulty_level_selected:
            sentence = "Please, choose a difficulty level\n"
            message = message + sentence
            self.run = False
        
        if not self.category_selected:
            sentence = "Please, choose a category\n"
            message = message + sentence
            self.run = False

        if not self.format_selected:
            sentence = "Please, choose a format\n"
            message = message + sentence
            self.run = False

        if self.run:
            choices = self.features[0].choices
            n_questions_value = choices[number_of_questions.currentRow()]

            choices = self.features[1].choices
            difficulty_value = choices[difficulty_level.currentRow()]

            choices = self.features[2].choices
            category_value = choices[category.currentRow()]

            choices = self.features[3].choices
            format_value = choices[format.currentRow()]

            message = "Model started processing on {} questions, {} difficulty level, {} category, and {} format".format(
                n_questions_value, 
                difficulty_value, 
                category_value,
                format_value)
            
            number_of_questions.setCurrentRow(-1)
            difficulty_level.setCurrentRow(-1)
            category.setCurrentRow(-1)
            format.setCurrentRow(-1)

        message_box = QMessageBox()
        message_box.setText(message)
        message_box.setGeometry(800, 500, 500, 500)
        message_box.exec_()

        if self.run:
            self.run_model()
            self.number_of_questions_selected = False
            self.difficulty_level_selected = False
            self.category_selected = False
            self.format_selected = False

    def __upload_items(self, selection, idx):
        for choice in self.features[idx].choices:
            item = QListWidgetItem(str(choice))
            selection.addItem(item)

    def __create_selection(self, idx):
        selection = QListWidget()
        selection.setSelectionMode(QAbstractItemView.NoSelection)
        selection.setGeometry(700, 900, 100, 200)
        self.__upload_items(selection, idx)
        return selection
    
    def number_of_questions_triggered(self, selection):
        if selection.currentRow() != -1:
            self.number_of_questions_selected = True

    def difficulty_level_triggered(self, selection):
        if selection.currentRow() != -1:
            self.difficulty_level_selected = True

    def category_triggered(self, selection):
        if selection.currentRow() != -1:
            self.category_selected = True
    
    def format_triggered(self, selection):
        if selection.currentRow() != -1:
            self.format_selected = True

    def run_model(self):
        print("There you go")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()