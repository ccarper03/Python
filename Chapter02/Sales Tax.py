__author__ = 'Charles Carper'


# Input
# declare variables
STATE_TAX_RATE = .04
COUNTY_TAX_RATE = .02
stateTax = 0.0
countyTax = 0.0
amount = 0.0
totSalesTax = 0.0
grandTotOfSale = 0.0

# Get amount of purchase from the user
amount = float(input('Enter amount of purchase: '))

#Processing
#calculate taxes
stateTax = amount * STATE_TAX_RATE
countyTax = amount * COUNTY_TAX_RATE
totSalesTax = stateTax + countyTax
grandTotOfSale = amount + totSalesTax

#Display Results
print('Your purchase amount is $', format(amount, ',.2f'))
print('Your State Tax is $', format(stateTax, ',.2f'))
print('Your County Tax is $', format(countyTax, ',.2f'))
print('Your Total Taxes are $', format(totSalesTax, ',.2f'))
print('Your Grand total is $',format(grandTotOfSale, ',.2f'))