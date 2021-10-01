import random
CONSTANTS = random.randint(1, 45)
quick_pick_numbers = int(input("How many 'quick picks' you wish to generate?"))
numbers=[]
for j in range(0, quick_pick_numbers):
    for i in range(0, quick_pick_numbers):
        numbers.append(CONSTANTS)
        print(numbers)




