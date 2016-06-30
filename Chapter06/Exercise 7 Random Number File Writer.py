__author__ = 'Charles Carper'
import random
import sys


def main():
    print('Let\'s create a new text file!\n')
    name = input(str('Enter name of the text file:')) + '.txt'

    try:
        file = open(name, 'w')
        file.close()

    except ValueError:
        print('D\'oh!,(Facepalm) Seems as if we have a problem... sucks to be you! Now scram!')
        sys.exit(1)  # quit Python

    choice = int(input('How many random numbers would you like to see in a file?: \n'))
    for count in range(0, choice, 1):
        print(random.randint(1, 500))
    print(name, 'has been created and random numbers has been stored! buh bye now!')
# Call the main function.
main()