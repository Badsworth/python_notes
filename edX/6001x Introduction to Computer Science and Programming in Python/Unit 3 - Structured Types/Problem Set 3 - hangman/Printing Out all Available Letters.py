import string

# print(string.ascii_lowercase)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    NotGuessedSofar = ""
    for char in string.ascii_lowercase:
        :
        if char not in lettersGuessed:
            NotGuessedSofar += char
    return NotGuessedSofar
