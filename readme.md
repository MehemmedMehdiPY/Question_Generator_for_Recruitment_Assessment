# Introduction 

The repository contains the application to generate questions for interviews powered by [MobileLLaMA-1.4B-Chat](https://huggingface.co/mtgv/MobileLLaMA-1.4B-Chat). The model is originally fine-tuned from [MobileLLaMA-1.4B-Base](https://huggingface.co/mtgv/MobileLLaMA-1.4B-Base) with supervised instruction fine-tuning on [ShareGPT dataset](https://huggingface.co/datasets/Aeala/ShareGPT_Vicuna_unfiltered). It was first introduced in [paper](https://arxiv.org/abs/2312.16886). 

Please, note that the author of this repository does not have any correspondence with the paper mentioned above.

# Prerequisites 
From software part, it is mandatory to have Python. Since a Language Model is used, it is advised to have 4GB GPU from hardware part.

## Installation
The repo is 100% Python-integrated. Make sure you have [Python](https://www.python.org/) programming installed in your local machine/computer. To install external packages for Python, you may also need [Pip](https://pypi.org/project/pip/) to be built-in. 

External packages are listed in [requirements.txt](https://github.com/MehemmedMehdiPY/Question_Generator_for_Recruitment_Assessment/blob/main/requirements.txt). The below command must be run via a terminal.
~~~
pip install -r requirements.txt
~~~

# Usage
To launch the application, [main.py](https://github.com/MehemmedMehdiPY/Question_Generator_for_Recruitment_Assessment/blob/main/main.py) should be run via Python interpreter. 

The file contains the following code to be executed.
~~~
from PyQt5.QtWidgets import QApplication
from scripts import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
~~~

During the initial running, [HuggingFace](https://huggingface.co/) will automatically download the required Language Model. When everything is well-set-up, the application can easily be used.

Please, note that the model requires GPU usage. Thus, the speed of the application fairly depends on the local machine performance.
