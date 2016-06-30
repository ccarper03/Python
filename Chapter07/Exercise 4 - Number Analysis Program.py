__author__ = 'Charles Carper'


def main():

    num = []
    counter = 1

    while counter <= 20:
        value = int(input('Enter a number.'))
        num.insert(0, value)
        counter += 1
    # end of while loop

    print()
    print(num)
    print('The lowest number in the list', min(num))
    print('The highest number in the list', max(num))
    print('The total of the numbers in the list', sum(num))
    print('The average of the numbers in the list', sum(num) / len(num))
    print()
    print('end of program')
# Call the main function.
main()