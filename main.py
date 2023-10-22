import sys

# main window
from PyQt5.QtWidgets import QMainWindow, QApplication

# load ui file
from PyQt5.uic import loadUi

# my api keys :)
import api_keys as keys

# gpt 
import gpt


# class for app
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # load ui file
        loadUi("gui.ui", self)
        
        # initiate bot
        # self.bot = gpt.gpt(keys.gpt_api_key)

        # button clicked events
        self.home_button.clicked.connect(self.showHome)
        self.content_button.clicked.connect(self.showContent)
        self.settings_button.clicked.connect(self.showSettings)

        # get file location
        self.home_file_button.clicked.connect(self.getFileLocation)

    # get file location from file_location_textedit
    def getFileName(self):
        file_name = self.file_location_lineedit.text().strip()
        return file_name
    
    def getFlashCards(self, file_location):
        pass

    





    # functions for home button
    def showHome(self):
        self.stackedWidget.setCurrentIndex(0)

    # functions for chat button
    def showContent(self):
        self.stackedWidget.setCurrentIndex(1)
    
    # functions for settings button
    def showSettings(self):
        self.stackedWidget.setCurrentIndex(2)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    app.exec_()

