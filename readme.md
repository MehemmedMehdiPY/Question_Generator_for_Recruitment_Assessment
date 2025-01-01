# Introduction 

The repository contains the application to generate questions for interviews powered by [OpenAI GPT-2](https://huggingface.co/openai-community/gpt2). GPT-2 is a transformers model pretrained on a very large corpus of English data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely, it was trained to guess the next word in sentences.

# Prerequisites 
From software part, it is mandatory to have Python. Since a Language Model is used, it is advised to have 1GB GPU from hardware part.

## Installation
The repo is 100% Python-integrated. Make sure you have [Python](https://www.python.org/) programming installed in your local machine/computer. To install external packages for Python, you may also need [Pip](https://pypi.org/project/pip/) to be built-in. 

External packages are listed in [requirements.txt](https://github.com/MehemmedMehdiPY/Question_Generator_for_Recruitment_Assessment/blob/main/requirements.txt). The below command must be run via a terminal.
~~~
pip install -r requirements.txt
~~~

# Usage
To launch the application, [main.py](https://github.com/MehemmedMehdiPY/Question_Generator_for_Recruitment_Assessment/blob/main/main.py) should be run via Python interpreter. 

The file contains the following code to be executed. .
~~~
from PyQt5.QtWidgets import QApplication
from scripts import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow(max_tokens=1000)
window.show()
app.exec()
~~~

MainWindow is a class to handle user interface and expects the maximum number of tokens as a limitation for the output of the model. The user interfaces takes the input of easily customizable parameters, such as the number of questions, difficulty level, topic, and question format. These parameters are further used to create a prompt in a rule-based way. The prompt supervises the model to generate sample interview questions based on the user-requested parameters.

The generated output by the model is saved as ./output/output.pdf - output.pdf file in a folder named as output. The folder is automatically created when the application starts and output.pdf is saved when the model output is available. Make sure generated files are saved safely in different filenames/folders so that they would not be overwritten by the next output of the model. 

During the initial running, [HuggingFace](https://huggingface.co/) will automatically download the required Language Model - OpenAI GPT-2. When everything is well-set-up, the application can easily be used

Please, note that the model requires GPU usage. Thus, the speed of the application fairly depends on the local machine performance.
