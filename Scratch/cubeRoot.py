x = int(input("Enter an integer: "))
ans = 0
while ans ** 3 < abs(x):
    ans = ans + 1
#    print(f"ans: {ans} ; abs(x): {abs(x)} ; ans**3: {ans**3}")
if ans**3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of", x, "is", ans)
