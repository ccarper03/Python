__author__ = 'Charles Carper'
__date__ = '9/15/14'

#initialize variables
hourly_rate = 0.0
reg_hours_worked = 0
ot_hours_worked = 0
weekly_pay = 0.0
monthly_pay = 0.0
yearly_pay = 0.0
OT_RATE = 1.5

#Input
#collect users first name and last name
fname = input('What is your first name? ')
lName = input('What is your last name? ')

# collect hourly rate, reg. hours, ot hours
hourly_rate = int(input('What is your hourly rate? '))
reg_hours_worked = float(input('What is your regular hours a week(up to 40)? '))
ot_hours_worked = float(input('What is your overtime hours in a week? '))

#Process
# Calculate Weekly pay
weekly_pay = reg_hours_worked * hourly_rate + ot_hours_worked * OT_RATE
# Calculate Monthly
monthly_pay = weekly_pay * 4
# Calculate Yearly
yearly_pay = monthly_pay * 12

#Output
# Display output to the user
print('Salary Summary for ' + lName + ", " +fname)
print()
print("Total Hours Worked ", end=' ')
print("Hourly Rate ", end=' ')
print("Overtime Rate ", end=' ')
print("Weekly Salary ", end=' ')
print("Monthly Salary ", end=' ')
print("Yearly Salary ", end=' ')
print()
print(format(reg_hours_worked, '2.0f'), end='                  $')
print(format(hourly_rate, '2.0f'), end='          $')
print(format(OT_RATE, '4.2f'), end='          $')
print(format(weekly_pay, '4.2f'), end='        $')
print(format(monthly_pay, '4.2f'), end='        $')
print(format(yearly_pay, '4.2f'))

