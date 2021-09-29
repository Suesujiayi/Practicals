"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
MIN_LENGTH = 6


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH)
    password = input("> ")
    is_valid_password(password)


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH:
        return False
    else:
        n = int(len(password))
        for i in range(n):
            print('*', end="")
    return True


main()
