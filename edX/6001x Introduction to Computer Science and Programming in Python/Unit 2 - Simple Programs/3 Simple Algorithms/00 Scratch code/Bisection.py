low = 0
high = 100
ans = ""
print('Please think of a number between 0 and 100!')
while ans != "c":
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + ' ?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == 'c':
        print('Game over. Your secret number was:', str(guess))
    elif ans == 'l':
        low = guess
    elif ans == 'h':
        high = guess
    else:
        print('Sorry, I did not understand your input.')
