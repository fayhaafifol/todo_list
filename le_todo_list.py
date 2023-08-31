import PyQt5.QtWidgets as qtw

from todolist import Ui_MainWindow

class MainWindow(qtw.QMainWindow,Ui_MainWindow):

   def __init__(self):

      super().__init__()

      self.setupUi(self)


app = qtw.QApplication([])

win = MainWindow()

win.show()

app.exec()

