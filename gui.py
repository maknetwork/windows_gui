import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Task'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 440
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        l1 = QLabel(self)
        l2 = QLabel(self)
        l3 = QLabel(self)
        l4 = QLabel(self)

        l1.setText("Location of the work")
        l1.resize(300,40)

        l1.move(20, 0)

        l2.resize(300,40)

        l2.setText("Who will do the Work?")

        l2.move(20, 80)

        l3.resize(300,40)

        l3.setText("Task")

        l3.move(20, 150)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 30)
        self.textbox.resize(280,40)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 110)
        self.textbox2.resize(280,40)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(20, 180)
        self.textbox3.resize(280,40)

        # Create a button in the window
        self.button = QPushButton('Save', self)
        self.button.move(20,240)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox2.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
