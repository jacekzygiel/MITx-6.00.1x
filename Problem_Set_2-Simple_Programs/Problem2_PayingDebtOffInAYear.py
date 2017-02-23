balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
updatedBalanceEachMonth = balance
multiplier = 0

while updatedBalanceEachMonth > 0:
    multiplier += 1
    updatedBalanceEachMonth = balance
    for x in range(0, 12):        
        minimumFixedMonthlyPayment = 10 * multiplier
        monthlyUnpaidBalance = updatedBalanceEachMonth - minimumFixedMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)    
    
print('Lowest Payment: {}'.format(int(minimumFixedMonthlyPayment)))
