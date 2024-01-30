from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets as qtw
from grafica import *
from Custom_Widgets.Widgets import *
import sys

class gui_interface(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################        
        

        self.show()

if __name__ == "__main__":
    app = qtw.QApplication([])

    ventana = gui_interface()
    ventana.show()
    app.exec_()