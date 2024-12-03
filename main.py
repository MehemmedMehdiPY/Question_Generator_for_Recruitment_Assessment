from PyQt5.QtWidgets import QApplication
from scripts import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()