# https://www.youtube.com/watch?v=6oDQaB2one8&feature=youtu.be
def countDown(n):
    for i in range(n):
        print(i + 1)
    print("Hooray")


def countDownRecursive(n):
    # The firt thing we need to do is write a cluase that breaks us
    # out of the recursive funtion.
    if n <= 0:
        # This is the end of the recursive functionm
        print("Hooray")
        return
    print(n)
    countDownRecursive(n - 1)  # count down 'n'

# countDownRecursive(3)
#   countDownRecursive(2)
#     countDownRecursive(1)
#       countDownRecursive(0)
#       return
#     return
#   return
# return


def sumRange(n):
    total = 0
    for i in range(n):
        total += i + 1
    return total


def sumRangeRecursive(n, total=0):
    if n <= 0:
        return
    print(f"return: {n -1} , {total + n}")
    return sumRangeRecursive(n - 1, total + n)


sumRangeRecursive(4)


'''
Step 1: total + sumRangeRecursive(3, 4) <--------------
  |                                                   | Step 8: return * , *
  |                                                   |
Step 2: total + sumRangeRecursive(2, 3) <----------  --
  |                                               |  Step 7: return * , *
  |                                               |
Step 3: total + sumRangeRecursive(1, 2) <------  --
help(dictionary)
  |                                           |  Step 6: return * , *
  |                                           |                            
Step 4: 0                    1       ------  --
     |                                    |  Step 5: return 0 , 0 + 4 -> 4
     |                                    |
     --------------------------------------
'''

# Tower of Hanoi


# Factorial of a number using recursion
'''
The factorial of a number is the product of all the integers from 1 to that number.

factorial(n) = n * factorial(n - 1) or factorial(n) = n∗factorial(n−1)

For example, the factorial of 4 is 1*2*3*4 = 24. Factorial is not defined for
negative numbers and the factorial of zero is one, 0! = 1.
'''


def fact(n):
    if n == 1:
        return 1
    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print(str(n*(n-1)))
        return n * fact(n-1)


n = int(input("Input a number to compute the factiorial : "))
print(str(fact(n)))

'''
LIFO Stack

Step 5: fact(1) # is n == 1 -> yes, return 1             Step 6: fact(1) value 1 popped off stack, return 1
step 4: fact(2) # is n == 1 -> no,  return 2 * fact(1)   Step 7: waiting on fact(1): fact(2) value 2 popped off stack, return 2 * 1 -> 2
step 3: fact(3) # is n == 1 -> no,  return 3 * fact(2)   Step 8: waiting on fact(2): fact(3) value 6 popped off stack, return 3 * 2 -> 6
step 2: fact(4) # is n == 1 -> no,  return 4 * fact(3)   Step 9: waiting on fact(3): fact(4) value 24 popped off stack, return 4 * 6 -> 24
step 1: print()                                               24

factorial(0) = 1;
factorial(n) = n * factorial(n-1)
'''
