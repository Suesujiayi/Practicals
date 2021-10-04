import random

THE_NUMBER_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    quick_pick_numbers = int(input("How many 'quick picks' you wish to generate?"))
    for i in range(quick_pick_numbers):
        numbers_list = []
        for j in range(THE_NUMBER_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            if number in numbers_list:
                number = random.randint(MINIMUM, MAXIMUM)
                numbers_list.append(number)
            else:
                numbers_list.append(number)
        numbers_list.sort()
        print(numbers_list)


main()
