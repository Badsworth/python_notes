# Write a program to calculate the credit card balance after one year if a person only pays the minimum
# monthly payment required by the credit card company each month.

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 0
totalPay = 0
monthlyInterestRate = annualInterestRate / 12.0
while month < 12:
    minPay = monthlyPaymentRate * balance
    unpayBal = balance - minPay
    totalPay += minPay
    balance = unpayBal + (monthlyInterestRate * unpayBal)
    month += 1
#    print('Month ' + str(month) + ' Remaining balance: ' + str(round(balance, 2)))
print('Remaining balance: ' + str(round(balance, 2)))
