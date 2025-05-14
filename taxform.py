'''
Program: taxform.py
Author: Owen Baker

Compute a person's income tax
1. Significant constants:
    -tax rate
    -standard deduction
    -deduction per dependent
2. The inputs are:
    -gross income
    -number of dependents
3. Computations:
    -taxable income = gross income - standard deduction - a deduction for each dependent
    -income tax = a fixed percentage of taxable income
4. The outputs are:
    -income tax
'''

# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 1000.0

# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents

incomeTax = taxableIncome * TAX_RATE

# Display the income tax
print('The income tax is: $' + str(incomeTax))
