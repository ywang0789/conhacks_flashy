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
        self.file_name =''
        self.flash_cards = []
        self.index = 0
        
        # initiate bot
        # self.bot = gpt.gpt(keys.gpt_api_key)

        # button clicked events
        self.home_button.clicked.connect(self.showHome)
        self.content_button.clicked.connect(self.showContent)
        self.settings_button.clicked.connect(self.showSettings)

        # get file location
        self.home_file_button.clicked.connect(self.getFileName)

        # show flash card 
        self.show_answer_button.clicked.connect(self.showFlashCardAnswer)

    # get file location from file_location_textedit
    def getFileName(self):
        self.file_name = self.file_location_lineedit.text().strip()
        self.getFlashCards()
        print(self.file_name)
        print(self.flash_cards)
    
    def getFlashCards(self):
        self.flash_cards = gpt.PDFtoFlashcards.convertToNote(self.file_name)

    def showFlashCardQuestion(self):
        # show flash card question
        #print(self.flash_cards)
        self.flash_card_textedit.append(self.flash_card[self.index].question)
    
    def showFlashCardAnswer(self, flash_card):
        # show flash card answer
        self.flash_card_textedit.append(flash_card.answer)
    
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
    ui.showHome()
    
    ui.show()
    app.exec_()

