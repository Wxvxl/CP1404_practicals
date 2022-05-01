# #Write a program that asks the user how many "quick picks" they wish to generate.
# The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
# These values should be stored as CONSTANTS.
# Each line (quick pick) should not contain any repeated number.
# Each line of numbers should be displayed in sorted (ascending) order.
import random


def verify_quick_picks(random_number, numbers):
    """Verify the quick pick number validity"""
    while True:
        if random_number in numbers:
            random_number = random.randint(1, 45)
        else:
            return random_number


def quick_picks():
    numbers = []
    for x in range(1, 7):
        random_number = random.randint(1, 45)
        random_number = verify_quick_picks(random_number, numbers)
        numbers.append(random_number)
    return numbers

def main():
    number_of_quick_picks = int(input("How many quick picks?: "))
    for x in range (0,number_of_quick_picks):
        numbers = quick_picks()
        numbers.sort()
        for x in range(0,len(numbers)):
            print(numbers[x], end=" ")
        print()
main()
