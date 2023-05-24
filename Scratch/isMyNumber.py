def isMyNumber(guess):
    secretNumber = 999999999999999999999999999999999
    if guess < secretNumber:
        return -1
    if guess == secretNumber:
        return 0
    if guess > secretNumber:
        return 1


def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number

    guess = 1
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == 0:
            return guess
        if sign == -1:
            guess += 1
        else:
            guess -= 1
    '''

    guess = 1

    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if isMyNumber(guess) == 0:
            return guess
        if sign == -1:
            guess += 1
        else:
            guess -= 1


print(jumpAndBackpedal(isMyNumber))
