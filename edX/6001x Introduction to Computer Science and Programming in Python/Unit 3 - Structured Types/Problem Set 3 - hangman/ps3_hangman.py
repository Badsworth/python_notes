# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

import string

# print(string.ascii_lowercase)

WORDLIST_FILENAME = "d:/OneDrive/Pyhton Notes/edX/6001x/Unit 3 - Structured Types/hangman/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedSofar = ""
    for char in secretWord:
        if char not in lettersGuessed:
            guessedSofar += "_ "
        else:
            guessedSofar += char
    return guessedSofar


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableLetters = ""
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            availableLetters += char
    return availableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = ""
    guesses = 8
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secretWord)) + ' letters long')
    print("-----------")

    # In Python 2 (and Python 3)

    # Formatting output using String modulo operator(%) :
    # The % operator can also be used for string formatting. It interprets the left
    # argument much like a printf()-style format as in C language string to be applied
    # to the right argument.

    # The general syntax for a format placeholder is:
    # %[flags][width][.precision]type
    # print("You have %02d guesses left." % (guesses))

    # The format() method was added in Python(2.6).
    # print('You have {0:02d} guesses left.'.format(guesses))

    # the above formatting can also be done by using f-Strings
    # Although, this features work only with python 3.6 or above.
    # print(f'You have {guesses:02d} guesses left.')

    # print("You have " + str(guesses) + " guesses left.")

    while guesses > 0:
        print('You have ' + str(guesses) + ' guesses left')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        guess = guess.lowear()

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ",
                  getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            #print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
        elif guess not in secretWord:
            lettersGuessed += guess
            print("Oops! That letter is not in my word: ",
                  getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            #print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}")
            guesses -= 1
        else:
            lettersGuessed += guess
            #print(f"Good guess {getGuessedWord(secretWord, lettersGuessed)}")
            print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            if isWordGuessed(secretWord, lettersGuessed):
                print("Congratulations, you won!")
                return
    print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
