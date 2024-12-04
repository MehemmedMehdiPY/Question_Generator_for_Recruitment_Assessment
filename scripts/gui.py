from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget, QListWidget, QListWidgetItem, QAbstractItemView
from .constants import Customization
from .prompt_processing import ModelProcessor, prompt_generator

class MainWindow(QMainWindow, Customization):
    questions_selected = False
    difficulty_level_selected = False
    category_selected = False
    format_selected = False

    def __init__(self, max_tokenizer: int = 128):
        super().__init__()

        # Initalizing processor object to execute Llama model
        self.__initialize_model(max_tokenizer=max_tokenizer)

        self.setWindowTitle("BUILT WITH META LLAMA 3")
        self.setGeometry(700, 200, 400, 600)

        questions_label = QLabel("Choose the number of questions")
        difficulty_label = QLabel("Choose a difficulty level")
        category_label = QLabel("Choose a category")
        format_label = QLabel("Choose a format")

        questions = self.__create_selection(0)
        questions.currentRowChanged.connect(lambda : self.questions_triggered(questions))
        
        difficulty_level = self.__create_selection(1)
        difficulty_level.currentRowChanged.connect(lambda : self.difficulty_triggered(difficulty_level))

        category = self.__create_selection(2)
        category.currentRowChanged.connect(lambda : self.category_triggered(category))
        
        format = self.__create_selection(3)
        format.currentRowChanged.connect(lambda x: self.format_triggered(format))

        button = QPushButton("Button")
        button.clicked.connect(lambda : self.button_triggered(questions, difficulty_level, category, format))
        
        layout_right = self.__construct_right_layout(category_label, category, format_label, format)
        layout_left = self.__construct_left_layout(questions_label, questions, difficulty_label, difficulty_level)
        layout_top = self.__construct_top_layout(layout_left, layout_right)
        layout_bottom = self.__construct_bottom_layout(button)

        layout_final = QVBoxLayout()
        layout_final.addLayout(layout_top)
        layout_final.addLayout(layout_bottom)

        widget = QWidget()
        widget.setLayout(layout_final)
        self.setCentralWidget(widget)
    
    def __construct_right_layout(self, category_label, category, format_label, format):
        layout_right = QVBoxLayout()
        layout_right.addWidget(category_label)
        layout_right.addWidget(category)
        layout_right.addWidget(format_label)
        layout_right.addWidget(format)
        return layout_right

    def __construct_left_layout(self, questions_label, questions, difficulty_label, difficulty_level):
        layout_left = QVBoxLayout()
        layout_left.addWidget(questions_label)
        layout_left.addWidget(questions)
        layout_left.addWidget(difficulty_label)
        layout_left.addWidget(difficulty_level)
        return layout_left
    
    def __construct_top_layout(self, layout_left, layout_right):
        layout_top = QHBoxLayout()
        layout_top.addLayout(layout_left)
        layout_top.addLayout(layout_right)
        return layout_top

    def __construct_bottom_layout(self, button):
        layout_bottom = QHBoxLayout()
        layout_bottom.addWidget(button)
        return layout_bottom
    
    def __initialize_model(self, max_tokenizer: int = 128):
        self.processor = ModelProcessor(max_tokenizer=max_tokenizer)

    def button_triggered(self, questions, difficulty_level, category, format):
        self.run = True
        message = ""
        if not self.questions_selected:
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
            questions_value = choices[questions.currentRow()]

            choices = self.features[1].choices
            difficulty_value = choices[difficulty_level.currentRow()]

            choices = self.features[2].choices
            category_value = choices[category.currentRow()]

            choices = self.features[3].choices
            format_value = choices[format.currentRow()]

            message = "Model started processing on {} questions, {} difficulty level, {} category, and {} format".format(
                questions_value, 
                difficulty_value, 
                category_value,
                format_value)
            print(message)
            
            questions.setCurrentRow(-1)
            difficulty_level.setCurrentRow(-1)
            category.setCurrentRow(-1)
            format.setCurrentRow(-1)
            
            message = ""
        
        if message:
            message_box = QMessageBox()
            message_box.setText(message)
            message_box.setGeometry(800, 500, 500, 500)
            message_box.exec_()

        if self.run:
            response = self.run_model(questions_value, difficulty_value, category_value, format_value)
            self.questions_selected = False
            self.difficulty_level_selected = False
            self.category_selected = False
            self.format_selected = False

            message_box = QMessageBox()
            message_box.setText(response[0]['generated_text'])
            message_box.setGeometry(800, 500, 500, 500)
            message_box.exec_()

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
    
    def questions_triggered(self, selection):
        if selection.currentRow() != -1:
            self.questions_selected = True

    def difficulty_triggered(self, selection):
        if selection.currentRow() != -1:
            self.difficulty_level_selected = True

    def category_triggered(self, selection):
        if selection.currentRow() != -1:
            self.category_selected = True
    
    def format_triggered(self, selection):
        if selection.currentRow() != -1:
            self.format_selected = True

    def run_model(self, questions_value, difficulty_value, category_value, format_value):
        prompt = prompt_generator(
            questions=questions_value, 
            difficulty=difficulty_value, 
            category=category_value, 
            format=format_value)
        response = self.processor.run(prompt)
        return response