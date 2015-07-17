m = totalPaid = interest = 0
mir = annualInterestRate/12.0
rem = balance
lp = 10
m = 1
while True:
    if rem <= 0:
        break
    if m == 13:
        m = 1
        lp += 10
        rem = balance
    rem -= lp
    interest = mir * rem
    rem += interest
    m += 1
print 'Lowest Payment: ' + str(lp)