# Prime numbers
string = ""
for number in range(1, 101):
    for i in range(2, number):
        if (number % i) == 0:
            break
    else:
        string += str(number) + " "
print(string)
