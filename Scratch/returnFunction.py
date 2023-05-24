# function returning a function
def func01(x):
    print(f"func01, x: {x}")

    def func02(y):
        print(f"func02, y: {y}")
    return func02


func01(2)(3)
