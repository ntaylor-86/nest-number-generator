import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import main

"""
|--------------------------------------------------------------------------
| Class: MainWindow
|--------------------------------------------------------------------------
|
"""
class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


"""
|--------------------------------------------------------------------------
| Class: Controller
|--------------------------------------------------------------------------
|
"""
class Controller:
    def __init__(self):
        pass
    
    def show_main_window(self):
        self.main_window = MainWindow()

        ###########################################################################
        ## Connecting the "Generate GEO's" button to the generate_geo() function ##
        ###########################################################################
        self.main_window.generateButton.clicked.connect( self.generate_geo )

        self.main_window.show()

    
    ################################################
    ####  Main Window -> Generate GEO's Button  ####
    ################################################
    def generate_geo(self):
        job_name = self.get_jobInput()
        if job_name == False:
            return False
        
        geo_size = self.get_comboBox_value()
        if geo_size == False:
            return False
        
        print(job_name)
        print(geo_size)
    
    ##############################################
    #### Getting the Job Name from the Input  ####
    ##############################################
    def get_jobInput(self):
        if self.main_window.jobInput.text() == "":
            QtWidgets.QMessageBox.warning(
                self.main_window,
                "[ rookie ]",
                "errrr...\n\n You need to enter a job name bro. \n"
            )
            self.main_window.jobInput.setFocus()
            return False
        else:
            return self.main_window.jobInput.text()
    
    ##################################################
    ####  Getting the Combo Box (GEO size) value  ####
    ##################################################
    def get_comboBox_value(self):
        value = self.main_window.comboBox.currentText()
        if value == "Choose a GEO size...":
            QtWidgets.QMessageBox.warning(
                self.main_window,
                "[ n00b ]",
                "Please select a GEO size."
            )
            return False
        else:
            return value


"""
|--------------------------------------------------------------------------
| Function: run_app()
|--------------------------------------------------------------------------
|
"""
def run_app():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main_window()
    sys.exit(app.exec())


"""
|--------------------------------------------------------------------------
| if __name__ == '__main__':
|--------------------------------------------------------------------------
|
"""
if __name__ == '__main__':
    run_app()
