m = totalPaid = interest = 0
mir = annualInterestRate/12.0
rem = balance
for m in range(1, 13):
    mmp = 0
    mmp = monthlyPaymentRate * rem
    rem -= mmp
    interest = mir * rem
    rem += interest
    totalPaid += mmp
    print 'Month: ' + str(m)
    print 'Minimum monthly payment: ' + str(round(mmp,2))
    print 'Remaining balance: ' + str(round(rem,2))
print 'Total paid: ' + str(round(totalPaid,2))
print 'Remaining balance: ' + str(round(rem,2))