

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


main()
