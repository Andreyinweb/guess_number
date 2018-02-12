# python3 guess_number.py

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QMainWindow,
                             QGridLayout, QApplication)
from PyQt5.QtCore import Qt                             

from PyQt5.QtGui import QIcon

from guess_number_help import CheckingNumbers
from config_guess_number import LEN_NUMBER, NUMBER_OF_ATTEMPTS, LANGUAGE, WORDS



class GuessNumber(QWidget):

    def __init__(self):
        super().__init__()

        self.guess_number()
        self.initUI()

    def guess_number(self):
        
        self.input_number = ''
        self.user = CheckingNumbers(LEN_NUMBER)
        self.word = WORDS[LANGUAGE] 
        # Print line and attempt
        # Строка печати и попытка
        self.line = 0   

    def initUI(self):
        # Restart the game
        # Перезапуск игры
        self.exit_game = False
        
        # List of text fields
        # Список текстовых полей
        self.listlbl = []
        for i in range(NUMBER_OF_ATTEMPTS * 3):
            self.listlbl.append(QLabel(self))


        self.message = QLabel((self.word[1] + str(LEN_NUMBER) + self.word[2]), self)
        # Number input field
        # Поле ввода цифр
        self.qle = QLineEdit('',self)
        self.qle.textChanged[str].connect(self.writetext) 
        # Button
        # Кнопка
        btn1 = QPushButton(self.word[1], self)
        btn1.setShortcut('Return')
        btn1.clicked.connect(self.buttonClicked)
        # Creating a grid
        # Создание сетки
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        positions = [(i,j) for i in range(int(NUMBER_OF_ATTEMPTS)) for j in range(3)]
        for position, lbls in zip(positions, self.listlbl):
            if lbls == '':
                continue
            lbls.setText('')
            self.grid.addWidget(lbls, *position)
        endline = NUMBER_OF_ATTEMPTS
        self.grid.addWidget(self.message, endline+1 , 0,1,3)
        self.grid.addWidget(self.qle, endline+2 , 0,1,2)
        self.grid.addWidget(btn1, endline+2 , 1)

        # Set the window size
        # Установка размеров окна 
        self.setWindowIcon(QIcon('icon.png'))  
        self.setGeometry(300, 300, 300, NUMBER_OF_ATTEMPTS*30)
        self.setWindowTitle(self.word[0])
        self.show()
    

    def onmessage(self, text):
        """
        Message
        Сообщение
        """
        self.message.setText(text)
        self.message.adjustSize()
    
    def writetext(self, text):
        """
        Save Text
        Сохранить текст
        """
        self.input_number = text
    
    def keyPressEvent(self, e):
        """
        Side Inter
        Боковой интер
        """
        if e.key() == Qt.Key_Enter:
            self.buttonClicked()

    def buttonClicked(self):
        """
        Button press
        Нажатие кнопки
        """
        check = self.user.check_number(self.input_number)
        # Check that the entered text is numbers.
        # Проверка, что  введенный текст это цифры. 
        if check == False:
            self.onmessage(self.word[3] + self.word[1] + str(LEN_NUMBER) + self.word[2] )
            self.input_number = ''
            self.qle.setText('')
            self.qle.setFocus()
        # Actions in cases of victory
        # Действия в случаи победы
        elif check == True :
            self.printline()
            self.onmessage(self.word[4]) 
            self.close_game(self.word[4])
            self.qle.setText('')
            self.qle.setFocus()
        # Actions in cases where attempts are ended    
        # Действия в случаи если попытки закончились
        elif self.line >= NUMBER_OF_ATTEMPTS - 1:
            self.onmessage( self.word[6] + '  ' + self.word[7] )
            self.qle.setText('')
            self.close_game(self.word[6] + '  ' + self.word[7] )
        # Standard Actions
        # Стандартные действия   
        else:  
            self.onmessage( self.word[1] + str(LEN_NUMBER) + self.word[2] )
            self.printline()
            self.qle.setText('')
            self.qle.setFocus()
            self.line +=1
    
    def printline(self):
        """
        Print data
        Печать данных
        """
        self.listlbl[(self.line*3)].setText(str(self.line + 1) + self.word[5])
        self.listlbl[(self.line*3 + 1)].setText(self.input_number)
        self.listlbl[(self.line*3 + 2)].setText('[' + str(self.user.guessed) + ':' + str(self.user.place) + ']') 
    
    def close_game(self,text_message):
        """
        Closing the game
        Закрытие игры
        """
    
        reply = QMessageBox.question(self, text_message,
            (text_message + ' \n ' + self.word[8] ), QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            self.exit_game = True
            self.close()
        if reply == QMessageBox.No:
            self.exit_game = False
            self.close()

if __name__ == '__main__':
    app = QApplication([]) 
    x = True
    while x:
        

        ex = GuessNumber()
        app.exec_()
        x = ex.exit_game
        app.exit()
        
        
        
      
  