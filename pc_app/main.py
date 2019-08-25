import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from app_logic.View import View
from app_logic.Model import Model
from app_logic.Controller import Controller
from app_logic.Enums import Key

from qt_ui.app import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.controller, self.ui)
        self.model.add_view(self.view)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

