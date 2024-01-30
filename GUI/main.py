########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################
from functions import AppFunctions
########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################



########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        # loadJsonStyle(self, self.ui, jsonFiles = {
        #     "mystyle.json", "style.json"
        #     }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        QAppSettings.updateAppSettings(self)
        # settings = QSettings()

        # settings.setValue("THEME", "Default-Dark")
        # QAppSettings.updateAppSettings(self)

        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__),'Database/prueba_DB.db'))
        AppFunctions.main(dbFolder)

        AppFunctions.displayUsers(self,AppFunctions.getAllUsers(dbFolder))

        self.ui.addUserBtn.clicked.connect(lambda: AppFunctions.addUser(self,dbFolder))



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication([])
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    app.exec_()
########################################################################
## END===>
########################################################################  
