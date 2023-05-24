count = 0
substring = "bob"
s = input("Enter a string: ")

for i in range(len(s)):
    if s[i:i + 3] == substring:
        count += 1
print("The number of times", substring,
      "appears in \"" + s + "\" = ", str(count))
