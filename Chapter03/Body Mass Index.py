__author__ = 'Charles Carper'
# 6. Body Mass Index
# Write a program that calculates and displays a person’s body mass index (BMI). The
# BMI is often used to determine whether a person is overweight or underweight for his
# or her height. A person’s BMI is calculated with the following formula:
# BMI  weight  703 / height2
# where weight is measured in pounds and height is measured in inches.


# Get height and weight from user
weight = float(input('Enter your weight: '))
height = float(input('Enter your height in inches: '))
BMI = int

# Calculate BMI
BMI = weight * 703 / height**2

# Display output to the user
print("Your BMI is: " + format(BMI, '3.1f'))
