#Charles Carper

def main():
    # Open a file for reading.
    infile = open('numbers.txt', 'r')

    # Read three numbers from the file.
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Close the file.
    infile.close()

    # find the average of the three numbers.
    total = (num1 + num2 + num3)/3

    # Display the numbers and their total.
    print('The Average of:', num1, num2, num3)
    print('is:', total)

# Call the main function.
main()
