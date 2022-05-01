"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def get_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = float(input("Enter score: "))
    return score


def check_grades(score):
    if score < 0 or score > 100:
        grade = "Invalid Score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


def main():
    score = get_score()
    grade = check_grades(score)
    print(f"Your grade is {grade}")
    random_score = random.randint(0,100)
    print(f"The random score is {random_score}")
    print(f"Your grade is {check_grades(random_score)}")


main()

