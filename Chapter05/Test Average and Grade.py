__author__ = 'ccarp_000'


def main():
    total = 0
    def cal_average(total):
        print('Average of all scores ', total / 5)
        return

    def Determin_Grade(score):
        if score == (90,91,92,93,94,95,96,97,98,99,100):
            print('A')
        elif score == (80,81,82,83,84,85,86,87,88,89):
            print('B')
        elif score == (70,71,72,73,74,75,76,77,78,79):
            print('C')
        elif score == (60,61,62,63,64,65,66,67,68,69):
            print('D')
        elif score <= 59:
            print('F')
        else:
            print('Not a Valid Answer')

    for score in range(1, 6):
        print('Enter score.')
        score = int(input())
        Determin_Grade(score)
        total += score

main()
