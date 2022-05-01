def get_name(email):
    name = email.split("@")[0]
    name = name.split(".")
    name = " ".join(name)
    return name


def check_name(name):
    user_input = input(f"Is your name {name}? (Y/N) ")
    if user_input.upper() == "Y":
        return name
    else:
        name = input("Name: ")
        return name


def main():
    emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email).title()
        name = check_name(name)
        emails[email] = name
        email = input("Email: ")
    for email in emails:
        print(f"{emails[email]} ({email})")

main()
