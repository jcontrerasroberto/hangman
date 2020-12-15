import read_words as reader
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtGui, QtTest
from Hangman import HangMan
import random

class HangManApplication(QDialog):

    word = ""
    mistakes = 0
    correct = 0
    display_string = ""
    definition = ""
    words = reader.read_json()
    buttons = []
    correct_chars = []
    words_taken = []
    hangman_imgs = [
        "img/Hangman-0.png",
        "img/Hangman-1.png",
        "img/Hangman-2.png",
        "img/Hangman-3.png",
        "img/Hangman-4.png",
        "img/Hangman-5.png",
        "img/Hangman-6.png"
    ]

    def __init__(self):
        super().__init__()
        self.ui = HangMan()
        self.ui.setupUi(self)
        self.buttons.append(self.ui.btnA)
        self.buttons.append(self.ui.btnB)
        self.buttons.append(self.ui.btnC)
        self.buttons.append(self.ui.btnD)
        self.buttons.append(self.ui.btnE)
        self.buttons.append(self.ui.btnF)
        self.buttons.append(self.ui.btnG)
        self.buttons.append(self.ui.btnH)
        self.buttons.append(self.ui.btnI)
        self.buttons.append(self.ui.btnJ)
        self.buttons.append(self.ui.btnK)
        self.buttons.append(self.ui.btnL)
        self.buttons.append(self.ui.btnM)
        self.buttons.append(self.ui.btnN)
        self.buttons.append(self.ui.btnNe)
        self.buttons.append(self.ui.btnO)
        self.buttons.append(self.ui.btnP)
        self.buttons.append(self.ui.btnQ)
        self.buttons.append(self.ui.btnR)
        self.buttons.append(self.ui.btnS)
        self.buttons.append(self.ui.btnT)
        self.buttons.append(self.ui.btnU)
        self.buttons.append(self.ui.btnV)
        self.buttons.append(self.ui.btnW)
        self.buttons.append(self.ui.btnX)
        self.buttons.append(self.ui.btnY)
        self.buttons.append(self.ui.btnZ)
        for button in self.buttons:
            button.clicked.connect(self.check_char)
        self.change_word()
        self.show()

    def change_word(self):
        string = ""
        value = random.randint(0, len(self.words)-1)
        while value in self.words_taken:
            value = random.randint(0, len(self.words) - 1)
        self.words_taken.append(value)
        self.word = self.words[value].word
        self.definition = self.words[value].meaning
        for char in self.word:
            string += "_ "
        self.display_string = string
        self.ui.txt_word.setText('<html><head/><body><p align="center"><span style=" font-size:36pt; font-weight:600; color: white;">' + self.display_string + '</span></p></body></html>')
        self.ui.txt_word.setStyleSheet('font-size:36pt; font-weight:600; color: white;')
        self.ui.txt_definition.setText('<html><head/><body><p align="center"><span style=" font-size:20pt; color:#ffffff;">'+ self.definition +'</span></p></body></html>')
        self.ui.txt_definition.setWordWrap(True)

    def check_char(self):
        self.sender().setEnabled(False)
        self.sender().setStyleSheet(
            'background-color: rgb(156, 155, 155); font: 75 20pt "Roboto"; color: rgb(0, 0, 0);')
        self.check_coincidence(self.sender().text())


    def reset(self):
        if len(self.words) == len(self.words_taken):
            print("No more words")
            exit(0)
        QtTest.QTest.qWait(1000)
        self.correct = 0
        self.mistakes = 0
        self.display_string = ""
        self.ui.hangman_img.setPixmap(QtGui.QPixmap(self.hangman_imgs[self.mistakes]))
        for button in self.buttons:
            button.setStyleSheet('background-color: rgb(0, 170, 127); font: 75 20pt "Roboto"; color: rgb(0, 0, 0);')
            button.setEnabled(True)
        self.correct_chars = []
        print(self.correct_chars)
        print(self.correct)
        print(self.mistakes)
        self.change_word()

    def check_coincidence(self, char):
        accents = {
            "A": "Á",
            "E": "É",
            "I": "Í",
            "O": "Ó",
            "U": "Ú"
        }
        string = ""
        self.correct = 0
        len_word = len(self.word)
        if self.mistakes<6 :
            if char.upper() in "AEIOU":
                if (char.upper() in self.word) or (accents.get(char.upper()) in self.word):
                    self.correct_chars.append(char.upper())
                    self.correct_chars.append(accents.get(char.upper()))
                else:
                    self.mistakes += 1
                    self.ui.hangman_img.setPixmap(QtGui.QPixmap(self.hangman_imgs[self.mistakes]))
                    if self.mistakes==6:
                        self.wrong_answer()
                        return
            else:
                if char.upper() in self.word:
                    self.correct_chars.append(char.upper())
                else:
                    self.mistakes += 1
                    self.ui.hangman_img.setPixmap(QtGui.QPixmap(self.hangman_imgs[self.mistakes]))
                    if self.mistakes == 6:
                        self.wrong_answer()
                        return

            for char in self.word:
                if char in self.correct_chars:
                    string += char+" "
                    self.correct += 1
                else:
                    string += "_ "
            self.display_string = string
            self.ui.txt_word.setText(
                '<html><head/><body><p align="center"><span style=" font-size:36pt; font-weight:600;">' + self.display_string + '</span></p></body></html>')
            print(self.correct)
            print(len(self.word))
            if self.correct == len(self.word):
                self.ui.txt_word.setStyleSheet("font-size:36pt; font-weight:600; color: green")
                self.reset()
                return


    def wrong_answer(self):
        self.ui.txt_word.setText(
            '<html><head/><body><p align="center"><span style=" font-size:36pt; font-weight:600;">' + self.word + '</span></p></body></html>')
        self.ui.txt_word.setStyleSheet("font-size:36pt; font-weight:600; color:red")
        self.reset()


def main():
    app = QApplication(sys.argv)
    window = HangManApplication()
    app.exec_()


if __name__ == '__main__':
    main()
