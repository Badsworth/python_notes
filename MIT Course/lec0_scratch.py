# Print() function - type
#print("aaa", type(5))
#c = True
#print("c=", type(c))
# print(3.0-1)


# Branching
#x = float(input("Enter a number for x: "))
#y = float(input("Enter a number for y: "))
# if x == y:
#    if y != 0:
#        print("x / y is", x/y)
# elif x < y:
#    print("x is smaller")
# else:
#    print("y is smaller")


# while LOOPS - Lecture 2
# while <condition>:
#     <expression>
#     <expression>
#     ...
#
# <condition> evaluates to a Boolean
# if <condition> is True, do all the steps inside the while code block
# check <condition> again
# repeat until <condition> is False


# CONTROL FLOW: while and for loops
# iterate through numbers in sequence
#
#n = 0
# while n < 5:
#    print(n)
#    n = n+1
#
# shortcut with for loop
# for n in range(5):
#    print(n)


# for LOOPS, using range - Lecture 2
# for loops have a loop variable that iterates over a set of values
#
# range(start, stop, step)
# default values are start = 0 and step =1 and optional
# loop until value is stop -1 ******* -1 remember
#
# for var in range(4):   # var iterates over values 0,1,2,3
#     <expression>       # expressions inside loop executed with each value for var
#
# for var in range(4,6): # var iterates over values 4,5
#     <expression>
#
# Note: range is a way to iterate over numbers, but a for loop variable can iterate over and set
#       of values, not just numbers!


# String Manipulation - Lecture 3
# STRINGS
# s = "abc"
# index: s[0] evaluates to "a" <- indexing always starts at 0
# index: s[3] trying to index out of bounds, error
# index: s[-3] evaluates to "a"  <- last element always at index -1
#
# can slice strings using [start:stop:step]
# if give two numbers, [start:stop], step=1 by default
#
# you can also omit numbers and leave just colons
# s = "abcdefgh"
# s[3:6] -> evaluates to "def", same as s[3:6:1]
# s[3:6:2]  evaluates to "df"
# s[::]     evaluates to "abcdefgh", same as s[0:len(s):1]
# s[::-1]   evaluates to "hgfedbca", same as s[-1:-(len(s)+1):-1] # Reverse charaters in string
# s[4:1:-2] evaluates to "ec"

#s = "6.00 is 6.0001 and 6.0002"
#print("s=", type(s))
#new_str = ""
#new_str += s[-1]
#new_str += s[0]
#new_str += s[5::30]
#new_str += s[13:10:-1]
# print(new_str)
