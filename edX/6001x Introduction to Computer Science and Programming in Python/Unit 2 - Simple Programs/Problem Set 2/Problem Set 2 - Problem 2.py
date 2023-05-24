# Now write a program that calculates the minimum fixed monthly payment needed in order
# pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a
# single number which does not change each month, but instead is a constant amount that
# will be paid each month.

# The following variables contain values as described below:
#   1. balance - the outstanding balance on the credit card
#   2. annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will pay off all
# debt in under 1 year.

annualInterestRate = 0.2
balance = 3926
monthlyInterestRate = annualInterestRate / 12.0
month = 0
minPayment = 10


def calculate(month, balance, minPayment, monthlyInterestRate):
    while month < 12:
        monthlyUnpaidBalance = balance - minPayment
        balance = monthlyUnpaidBalance + \
            (monthlyInterestRate * monthlyUnpaidBalance)
        month += 1
    return balance


while calculate(month, balance, minPayment, monthlyInterestRate) > 0:
    minPayment += 10
    month = 0
print('Lowest Payment: ' + str(minPayment))
