import queue
import game
import re

class guess:
    """
        Class guess is the main class including logic for
        storing multiple games in a single session
        one must pass player's name while creating instance of this class
        it includes method named 'play' must be called to start the game.
    """
    def __init__(self, nameOfPlayer):
        self.playerName = nameOfPlayer
        print("WELCOME ", nameOfPlayer, "Lets play!")
        self.regEx = re.compile("[a-zA-Z]")
        self.g1 = game.game()
        self.noOfGames = 0
        self.listOfGames = [] #list of games
        self.startNewGame()


    def play(self):
        """
            This mehtod is beggining of game;
            one must call to start the game
        """
        self.startNewGame()


    def startNewGame(self):
            """
                This method will start a new game and will
                store the new game instance into session list
            """
            temp= input('Wanna Start a new game.... Y|N:' )
            if self.validateInput(temp)==2:
                self.g1 = game.game()
                print(self.g1.word)
            else: 
                exit()
                
            self.playGame()
            # self.g1.numberOfTries += 1
            # self.getUserInput() 
        # if self.g1.numberOfTries==0:
        #     temp = input("")
        # elif self.g1.numberOfTries==9:
        #     exit()
        

    def playGame(self):
        while self.g1.noOfBadGuess<3 or self.g1.numberOfTries==9:
            inChar=self.getUserInput()
            self.validateInput(inChar)
            print(self.g1.noOfBadGuess)
            print(self.g1.listOfCorrectGuesses)
        self.checkForMatches()
    
    def getUserInput(self):
        """
            getUserInput is the main interface between user and system;
            It also validate the input
        """
        while True:
            try:
                inChar = int(input("Type in a number between 1 and 16   "))
            except ValueError:
                print('Sorry, your input is not a number')
                continue
            else:
                 break
        return inChar

    def getSessionSummery(self):
        """
            getSessionSummery will print the statistics of all the games
            played in perticular session.
            This statistics includes Words,Status(0-giveUp | 1-Success),
            # of Bad Guess and Score for individual words.

            This function will be called at the end of session
            OR whenever user wants to quit.
        """
        pass


    def validateInput(self, inChar):
        if inChar=='y' or inChar=='Y':
            return 2                        
        elif str(inChar).isdigit() and int(inChar)>0 and int(inChar)<17:
            if (any(self.g1.word[int(inChar) - 1] in s for s in self.g1.dictOfWords.values())) and (self.g1.word[int(inChar) - 1] not in self.g1.listOfCorrectGuesses):
                self.g1.appendCorrectGuess(self.g1.word[int(inChar) - 1])
            else:
                self.g1.increaseBadGuess()
            return True      
        else:
            print("Please enter a number between 1 and 16 ")
            return False


    def checkForMatches(self):
        print('The game ended.')
        if set(self.g1.dictOfWords[5]).issubset(set(self.g1.listOfCorrectGuesses)):
            print('We have a match. COUNCILWOMAN in the building...')
        if set(self.g1.dictOfWords[4]).issubset(set(self.g1.listOfCorrectGuesses)):
            print('We have a match. BARRISTER in the building...')
        if set(self.g1.dictOfWords[3]).issubset(set(self.g1.listOfCorrectGuesses)):
            print('We have a match. SHERIFF in the building...')
        if set(self.g1.dictOfWords[1]).issubset(set(self.g1.listOfCorrectGuesses)):
            print('We have a match. HANGMAN in the building...')
        elif set(self.g1.dictOfWords[1]).issubset(set(self.g1.listOfCorrectGuesses)):
            print('We have a match. ROPE in the building...')
        elif set(self.g1.dictOfWords[0]).issubset(set(self.g1.listOfCorrectGuesses)):
            print('We have a match. MAN in the building...')

        else:
            print('No matches. You lose.')
            exit()

gue1 = guess("Milos")
gue1.play()