# Basic list operations
# Create the file list_exercises.py
# Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
# The program should then output various interesting things, as in the output below.
# Note that you can use the functions min, max, sum and len, and you can use the append method to add a number to a list.

def get_numbers(numbers):
    for x in range(0, 5):
        number = float(input("Number: "))
        numbers.append(number)


def basic_list_operation():
    numbers = []
    get_numbers(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    numbers_sum = sum(numbers)
    print(f"The average of the numbers is {numbers_sum/len(numbers)}")


basic_list_operation()

# Woefully inadequate security checker
# (Still in the same file)
# Copy the following list of usernames:
# usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
# Ask the user for their username. If the username is in the above list of authorised users, print "Access granted", otherwise print "Access denied".


def inadequate_security_checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter Username: ")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


inadequate_security_checker()
