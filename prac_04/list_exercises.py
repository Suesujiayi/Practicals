

def main():
    numbers = []
    for number in range(1, 6):
        number = int(input("Numbers: "))
        numbers.append(number)
    print(numbers)
    first_number = numbers[0]
    print("The first number is ", first_number)
    last_number = numbers[-1]
    print("The last number is ", last_number)


main()
