# Test Cases, comment out before submitting for grading
# Test Case 1
balance = 320000
annualInterestRate = 0.2

# Test Case 2
# balance = 999999
# annualInterestRate = 0.18

# Calculate monthly interest rate, lower and upper payments
monthlyInterestRate = (annualInterestRate / 12.0)
paymentLower = (balance / 12)
paymentUpper = (balance * ((1 + monthlyInterestRate) ** 12)) / 12.0
epsilon = 0.01

origBalance = balance

while abs(balance) >= epsilon:
    ans = (paymentLower + paymentUpper) / 2
    balance = origBalance
    for i in range(0, 12):
        balance = ((balance - ans) * (1 + monthlyInterestRate))
    if balance > 0:
        paymentLower = ans
    else:
        paymentUpper = ans
print("Lowest Payment: " + str(round(ans, 2)))
