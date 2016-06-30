__author__ = 'ccarp_000'
# 10. Monthly Sales Tax
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected. The state sales tax rate is 4 percent
# and the county sales tax rate is 2 percent. Write a program that asks the user to enter the
# total sales for the month. From this figure, the application should calculate and display the
# following:
# • The amount of county sales tax
# • The amount of state sales tax
# • The total sales tax (county plus state)


# Input
# declare variables
STATE_TAX_RATE = .04
COUNTY_TAX_RATE = .02
monthlySales = 0.0
countyTax = 0.0
stateTax = 0.0

# Get amount of sales from the user
monthlySales = float(input('Enter amount of purchase: '))

#Processing
#calculate taxes
stateTax = monthlySales * STATE_TAX_RATE
countyTax = monthlySales * COUNTY_TAX_RATE
totSalesTax = stateTax + countyTax

# Display Tax results
print('The Amount of County Sales tax $', format(countyTax, '.2f'))
print('The Amount of State Sales tax $', format(stateTax, '.2f'))
print('The total amount Sales tax(county plus state) $', format(totSalesTax, '.2f'))