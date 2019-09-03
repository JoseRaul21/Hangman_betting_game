import math
import random
import string

class game:

    def __init__(self):
        self.word = ''.join(random.choices(string.ascii_uppercase, k=16))
        self.status = 0 #0 for giveup and 1 for success
        self.noOfBadGuess = 0
        self.numberOfTries=0
        self.dictOfWords={0 : 'MAN', 1 : 'ROPE', 2 : 'HANGMAN', 3: 'SHERIFF', 4 : 'BARRISTER', 5: 'PHILOSOPHER' , 6 : 'COUNCILWOMAN'}
        self.listOfCorrectGuesses=[]
        self.score = 0


    def increaseBadGuess(self):
        self.noOfBadGuess += 1

    def appendCorrectGuess(self,a):
        self.listOfCorrectGuesses.append(a)

    def isCorrectGuess(self, tempChar):
        """
            This method returns true
                if the character entered by user is correct guess
            (means, part of current word)
            It also add or deduct the score accordingly
        """
        pass


