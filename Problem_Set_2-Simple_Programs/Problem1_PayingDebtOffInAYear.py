'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
The following variables contain values as described below:
    1.balance - the outstanding balance on the credit card
    2.annualInterestRate - annual interest rate as a decimal
    3.monthlyPaymentRate - minimum monthly payment rate as a decimal
For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print 
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 
# Test Case 1:
          balance = 42
          annualInterestRate = 0.2
          monthlyPaymentRate = 0.04
          
          # Result Your Code Should Generate Below:
          Remaining balance: 31.38
'''

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0
updatedBalanceEachMonth = balance

for x in range(0, 12):
    minimumMonthlyPayment = monthlyPaymentRate * updatedBalanceEachMonth
    monthlyUnpaidBalance = updatedBalanceEachMonth - minimumMonthlyPayment
    updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

print('Remaining balance: {}'.format(round(updatedBalanceEachMonth, 2)))
