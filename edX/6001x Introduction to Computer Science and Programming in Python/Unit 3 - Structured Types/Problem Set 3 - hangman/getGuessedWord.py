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

    #print(getGuessedWord(secretWord, lettersGuessed))
