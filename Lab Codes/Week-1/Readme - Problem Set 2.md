##Problem Set 2  

PAYING THE MINIMUM  (10/10 points):  
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment  
required by the credit card company each month.

The following variables contain values as described below:  

balance - the outstanding balance on the credit card  
annualInterestRate - annual interest rate as a decimal  
monthlyPaymentRate - minimum monthly payment rate as a decimal  

For each month, calculate statements on the monthly payment and remaining balance,  
and print to screen something of the format:  

Month: 1  
Minimum monthly payment: 96.0  
Remaining balance: 4784.0  

Be sure to print out no more than two decimal digits of accuracy - so print:  

Remaining balance: 813.41  
instead of  
Remaining balance: 813.4141998135  

Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:  

Total paid: 96.0  
Remaining balance: 4784.0  


A summary of the required math is found below:  

Monthly interest rate= (Annual interest rate) / 12.0  
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)  
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)  
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)   

------------------------------------------------------------------------------------------------------------------------

PAYING DEBT OFF IN A YEAR  (15/15 points):  

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance  
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead  
is a constant amount that will be paid each month.  

In this problem, we will not be dealing with a minimum monthly payment rate.  

The following variables contain values as described below:  

balance - the outstanding balance on the credit card  
annualInterestRate - annual interest rate as a decimal  

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year,  
for example:  

Lowest Payment: 180  

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment  
for that  month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that  
it is possible for  the balance to become negative using this payment scheme, which is okay.  

A summary of the required math is found below:  

Monthly interest rate = (Annual interest rate) / 12.0  
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)  
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)  

------------------------------------------------------------------------------------------------------------------------

