s = 'zyxwvutsrqponmlkjihgfedcbajkl'
tmpString = longestString = s[0:1]
# retrieve positon index and corresponding value in sequence
for i, char in enumerate(s):
    # use slicing to avoid IndexError: string index out of range
    if char <= s[i + 1:i + 2]:
        tmpString += s[i+1:i + 2]
        if len(longestString) < len(tmpString):
            longestString = tmpString
    else:
        tmpString = longeString = s[i+1:i + 2]
print("Longest substring in alphabetical order is:", longestString)
