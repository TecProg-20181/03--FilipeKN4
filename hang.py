import random
import string

wordlistFileName = 'palavras.txt'
logFileName = 'log.txt'

def verifyVariable(variable, variableType):
    assert variable != None, "This variable can't be None."
    if variableType == "list":
        assert isinstance(variable, list), "This variable need to be a list."
    elif variableType == "string":
        assert isinstance(variable, str), "This variable need to be a string."
    elif variableType == "int":
        assert isinstance(variable, int), "This variable need to be an int."
    elif variableType == "boolean":
        assert isinstance(variable, bool), "This variable need to be a boolean."
    elif variableType == "Letter":
        assert isinstance(variable, Letter), "This variable need to be a Letter."
    elif variableType == "Word":
        assert isinstance(variable, Word), "This variable need to be a Word."

def updateLogFile(logFileName, message):
    logFile = open(logFileName, 'a')
    logFile.write(message)
    logFile.close()

class Word(object):

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print ("Loading word list from file...")
        inFile = open(wordlistFileName, 'r')
        line = inFile.readline()
        wordList = str.split(line)
        print ("  ", len(wordList), "words loaded.")

        return wordList

    def getRandomWord(self, wordList, letterObject):
        verifyVariable(wordList, "list")
        verifyVariable(letterObject, "Letter")

        randomWord = random.choice(wordList)
        while letterObject.getNumberOfDifferentLetters(randomWord) > 8:
            randomWord = random.choice(wordList).lower()

        return randomWord

    def isWordGuessed(self, secretWord, lettersGuessed):
        verifyVariable(secretWord, "string")
        verifyVariable(lettersGuessed, "list")

        for letter in secretWord:
            if letter in lettersGuessed:
                wordWasGuessed = True
            else:
                return False

        return wordWasGuessed

    def getGuessedWord(self, secretWord, lettersGuessed, letter):
        verifyVariable(secretWord, "string")
        verifyVariable(lettersGuessed, "list")
        verifyVariable(letter, "string")

        lettersGuessed.append(letter)
        guessed = ''

        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '

        return guessed


class Letter(object):

    def inputLetter(self):
        letter = ''
        isValidInput = False
        while isValidInput == False:
            letter = input('Please guess a letter: ')
            inputSize = len(letter)
            if inputSize == 0 or inputSize > 1:
                print("Please, input just one letter.")
            elif inputSize == 1:
                isNotUpperCase = letter < 'A' or letter > 'Z'
                isNotLowerCase = letter < 'a' or letter > 'z'
                if isNotUpperCase and isNotLowerCase:
                    print("Please, input only letters.")
                else:
                    isValidInput = True

        return letter

    def getNumberOfDifferentLetters(self, secretWord):
        verifyVariable(secretWord, "string")

        letters = []
        lettersNumber = 0

        for letter in secretWord:
            if letter in letters:
                pass
            else:
                letters += letter
                lettersNumber+=1

        return lettersNumber

    def getAvailableLetters(self, lettersGuessed):
        verifyVariable(lettersGuessed, "list")

        availableLetters = string.ascii_lowercase
        for letter in availableLetters:
            if letter in lettersGuessed:
                availableLetters = availableLetters.replace(letter, '')

        return availableLetters

def endGame(word, secretWord, lettersGuessed):
    verifyVariable(word, "Word")
    verifyVariable(secretWord, "string")
    verifyVariable(lettersGuessed, "list")

    gameWon = word.isWordGuessed(secretWord, lettersGuessed) == True
    if gameWon:
        print ('Congratulations, you won!')
    else:
        print ('Sorry, you ran out of guesses. The word was ', secretWord, '.')

def hangman():
    word = Word()
    letterObject = Letter()
    guesses = 8
    lettersGuessed = []
    updateLogFile(logFileName, 'Begin\n')

    wordList = word.loadWords()
    verifyVariable(wordList, "list")
    updateLogFile(logFileName, 'Load the list of words\n')

    secretWord = word.getRandomWord(wordList, letterObject)
    verifyVariable(secretWord, "string")
    updateLogFile(logFileName, 'Choose the secret word\n')

    lettersNumber = letterObject.getNumberOfDifferentLetters(secretWord)
    verifyVariable(lettersNumber, "int")
    updateLogFile(logFileName, 'Get the number of different letters\n')

    wordLenght = len(secretWord)
    verifyVariable(wordLenght, "int")
    updateLogFile(logFileName, 'Get the Lenght of the secret word\n')

    print ('Welcome to the game, Hangmam!')
    print ('I am thinking of a word that is', wordLenght, ' letters long.')
    print ('The number of different letters in the word is', lettersNumber)
    print ('-------------')

    while word.isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        wordWasGuessed = word.isWordGuessed(secretWord, lettersGuessed)
        verifyVariable(wordWasGuessed, "boolean")
        updateLogFile(logFileName, 'Check if the secret word was guessed\n')
        print ('You have ', guesses, 'guesses left.')

        availableLetters = letterObject.getAvailableLetters(lettersGuessed)
        verifyVariable(availableLetters, "string")
        updateLogFile(logFileName, 'Get the available letters\n')
        print ('Available letters', availableLetters)

        letter = letterObject.inputLetter()
        verifyVariable(letter, "string")
        updateLogFile(logFileName, 'Input of letter\n')
        if letter in lettersGuessed:
            print ('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            guessed = word.getGuessedWord(secretWord, lettersGuessed, letter)
            verifyVariable(guessed, "string")
            updateLogFile(logFileName, 'Update the guessed letters\n')
            print ('Good Guess: ', guessed)
        else:
            guesses -=1
            guessed = word.getGuessedWord(secretWord, lettersGuessed, letter)
            verifyVariable(guessed, "string")
            updateLogFile(logFileName, 'Update the tried letters\n')
            print ('Oops! That letter is not in my word: ',  guessed)
        print ('------------')
    else:
        endGame(word, secretWord, lettersGuessed)
        updateLogFile(logFileName, 'End the game\n\n')

if __name__ == '__main__':
    hangman()
