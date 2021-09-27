

def main():
    import random
    score = random.randint(0, 100)
    print(score_kinds(score))


def score_kinds(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score <= 50:
        return "Bad"
    elif score <= 90:
        return "Passable"
    else:
        return "Excellent"


main()