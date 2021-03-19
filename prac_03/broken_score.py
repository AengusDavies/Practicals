"""
CP1404/CP5632 - Practical
Program that determines score status
"""


def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = determine_score(score)
    print(result)


def determine_score(score):
    """Determine a result based on given score"""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


determine_score()
main()
