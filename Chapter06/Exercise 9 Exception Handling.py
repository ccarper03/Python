__author__ = 'Charles Carper'

import sys


def main():

    try:
        infile = open('numbers.txt', 'r')

    except IOError as err:
        print(err)
        print('D\'oh!,(Facepalm) Seems as if we have a problem... sucks to be you! Now scram!')
        sys.exit(1)  # quit Python

    try:
        # Read three numbers from the file.
        num1 = int(infile.readline())
        num2 = int(infile.readline())
        num3 = int(infile.readline())

    except ValueError as err:
        print(err)
        print('D\'oh!,(Facepalm) Seems as if we have a problem... sucks to be you! Now scram!')
        sys.exit(1)  # quit Python# Open a file for reading.

    # Close the file.
    infile.close()

    # find the average of the three numbers.
    total = (num1 + num2 + num3)/3

    # Display the numbers and their total.
    print('The Average of:', num1, num2, num3)
    print('is:', total)

# Call the main function.
main()
