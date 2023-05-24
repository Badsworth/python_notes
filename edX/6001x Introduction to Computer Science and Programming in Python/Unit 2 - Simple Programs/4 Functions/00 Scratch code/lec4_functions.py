def a(x):
    '''
    x: int or float.
    '''
    return x + 1


def b(x):
    '''
    x: int or float.
    '''
    return x + 1.0


def c(x, y):
    '''
    x: int or float. 
    y: int or float.
    '''
    return x + y


def d(x, y):
    '''
    x: Can be of any type.
    y: Can be of any type.
    '''
    return x > y


def e(x, y, z):
    '''
    x: Can be of any type.
    y: Can be of any type.
    z: Can be of any type.
    '''
    return x >= y and x <= z


def f(x, y):
    '''
    x: int or float.
    y: int or float
    '''
    x + y - 2


def square(x):
    return x ** 2


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return ((a * x ** 2) + (b * x + c))


def a(x, y, z):
    if x:
        return y
    else:
        return z


def b(q, r):
    return a(q > r, q, r)


def foo(x, y=5):
    def bar(x):
        return x + 1
    return bar(y * 2)


foo(3)  # 11


def foo(x, y=5):
    def bar(x):
        return x + 1
    return bar(y * 2)


foo(3, 0)  # 1


def foo(x):
    def bar(z, x=0):
        return z + x
    return bar(3, x)


foo(2)  # 5


def foo(x):
    def bar(z, x=0):
        return z + x
    return bar(3)


foo(5)  # 3()


def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    def square(x):
        '''
        x: int or float.
        '''
        x = x * x
        return x
    return square(square(x))


def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x % 2 != 0


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    lowestValue = a if a < b else b
    for testValue in range(lowestValue, 0, -1):
        if a % testValue == 0 and b % testValue == 0:
            return testValue


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # https://en.wikipedia.org/wiki/Euclidean_algorithm
    # Euclid of Alexandria - Born Mid 4th centuary BC - often referred to as the "founder of geometry"
    if b == 0:
        return a

    return gcdRecur(b, a % b)
