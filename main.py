from PyQt5.QtWidgets import QApplication
from scripts import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow(max_tokens=1000)
window.show()
app.exec()