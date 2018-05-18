import random
import string

wordlistFilename = 'palavras.txt'

class Word(object):

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print ("Loading word list from file...")
        # infFile = File
        inFile = open(wordlistFilename, 'r')
        line = inFile.readline()
        wordList = str.split(line)
        print ("  ", len(wordList), "words loaded.")

        return wordList

    def getRandomWord(self, wordList, letter):
        randomWord = random.choice(wordList)
        while letter.getNumberOfDifferentLetters(randomWord) > 8:
            randomWord = random.choice(wordList).lower()

        return randomWord

    def isWordGuessed(self, secretWord, lettersGuessed):
        for letter in secretWord:
            if letter in lettersGuessed:
                wordWasGuessed = True
            else:
                return False

        return wordWasGuessed

    def getGuessedWord(self, secretWord, lettersGuessed, letter):
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
                isNotUppercase = letter < 'A' or letter > 'Z'
                isNotLowercase = letter < 'a' or letter > 'z'
                if isNotUppercase and isNotLowercase:
                    print("Please, input only letters.")
                else:
                    isValidInput = True

        return letter

    def getNumberOfDifferentLetters(self, secretWord):
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
        availableLetters = string.ascii_lowercase

        for letter in availableLetters:
            if letter in lettersGuessed:
                availableLetters = availableLetters.replace(letter, '')

        return availableLetters

def endGame(word, secretWord, lettersGuessed):
    gameWon = word.isWordGuessed(secretWord, lettersGuessed) == True
    if gameWon:
        print ('Congratulations, you won!')
    else:
        print ('Sorry, you ran out of guesses. The word was ', secretWord, '.')

def verifyVariable(variable, variableType):
    assert variable != None, "This variable can't be None."
    if variableType == "list":
        assert isinstance(variable, list), "This argument need to be a list."
    elif variableType == "string":
        assert isinstance(variable, str), "This argument need to be a string."

def hangman():
    word = Word()
    letterObject = Letter()
    wordList = word.loadWords()
    verifyVariable(wordList, "list")
    secretWord = word.getRandomWord(wordList, letterObject)
    verifyVariable(secretWord, "string")
    guesses = 8
    lettersGuessed = []
    lettersNumber = letterObject.getNumberOfDifferentLetters(secretWord)
    wordLenght = len(secretWord)
    print ('Welcome to the game, Hangam!')
    print ('I am thinking of a word that is', wordLenght, ' letters long.')
    print ('The number of different letters in the word is', lettersNumber)
    print ('-------------')

    while word.isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print ('You have ', guesses, 'guesses left.')
        availableLetters = letterObject.getAvailableLetters(lettersGuessed)

        print ('Available letters', availableLetters)
        #letter = letterObject.inputLetter()
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:
            print ('Oops! You have already guessed that letter: ', guessed)

        elif letter in secretWord:
            guessed = word.getGuessedWord(secretWord, lettersGuessed, letter)
            print ('Good Guess: ', guessed)

        else:
            guesses -=1
            guessed = word.getGuessedWord(secretWord, lettersGuessed, letter)
            print ('Oops! That letter is not in my word: ',  guessed)
        print ('------------')

    else:
        endGame(word, secretWord, lettersGuessed)

#call function hangman
hangman()
