__author__ = 'Charles Carper'
#input
miles = 0.0
gallons = 0.0
mpg = 0.0
#collect miles and gallons from user
miles = float(input('Enter amount of miles: '))
gallons = float(input('Enter amount of gallons: '))

#calculation
mpg = miles / gallons

#output
print(format(mpg, '7.2f'))