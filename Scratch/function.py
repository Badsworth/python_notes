# Unit 2: 4. Functions, Exercise 5
def foo(x, y=5):  # 2 x = 3, y =5
    def bar(x):
        print("return x + 1 within bar")
        return x + 1  # 4 Final returned value y * 2 + 1 ; note: original value of x is totaly ignored
    print("return bar(Y * 2) within foo")
    return bar(y * 2)  # 3 call bar with a value of 10


print(foo(3))  # 1. calls foo


def foo(x, y=5):
    def bar(x):  # the value of y * 2
        return x + 1
    return bar(y * 2)


# ditto as above exmaple. The value of x is ignored because of scope.
#  foo's x value = 20, bar's x value = 5 * 2 + 1 i.e. always 1
print(foo(20, 0))


def foo(x):
    def bar(z, x=0):  # x only gets set to a default of 0 if no value is supplied
        return z + x
    return bar(3, x)


print(foo(2))


def foo(x):
    def bar(z, x=0):
        return z + x
    return bar(3)


print(foo(5))
