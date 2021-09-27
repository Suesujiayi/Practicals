"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":

    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahernheit()
        print("Result: {:.2f} F".format(fahrenheit))

    elif choice == "F":
        fahrenheit = float(input("Fahernheit: "))
        celsius = fahernheit_to_celsius()
        print("Result: {:.2f} C".format(celsius))

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

def celsius_to_fahernheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahernheit_to_celsius(fahernheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius
