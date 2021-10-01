# Basic list operations
def main():
    numbers = []
    for number in range(1, 6):
        number = int(input("Numbers: "))
        numbers.append(number)
    first_number = numbers[0]
    print("The first number is ", first_number)
    last_number = numbers[-1]
    print("The last number is ", last_number)
    print("The smallest number is ", min(numbers))
    print("The largest number is ", max(numbers))
    average_of_the_numbers = sum(numbers)/len(numbers)
    print("The average of the numbers is ", average_of_the_numbers)

# Woefully inadequate security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup',
                 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']
    name = input(" What's your name? ")
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
