MINIMUM_LENGTH = 10


def get_password():
    password = input("Please enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password does not meet minimum length requirement")
        password = input("Please enter you password: ")
    else:
        return password


def print_asterisk(password):
    for x in range(0, len(password)):
        print("*", end="")


def main():
    password = get_password()
    print_asterisk(password)


main()
