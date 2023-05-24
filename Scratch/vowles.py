numConsonants = 0
numVowles = 0

s = input("Enter a string: ")
for char in s:
    if char in "aeiou":
        numVowles += 1
    else:
        numConsonants += 1
print("Number of vowles in string ", s, "=", numVowles)
print("Number of consonants in string ", s, "=", numConsonants)
