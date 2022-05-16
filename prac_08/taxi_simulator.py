from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def print_menu():
    print("q)uit, c)hoose taxi, d)rive")


def main():
    bill = 0.00
    current_taxi = None
    valid_answers = ["q", "c", "d"]
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Lets Drive!")
    print_menu()
    answer = input(">>> ").lower()

    while answer != "q":
        if answer not in valid_answers:
            print("Invalid Option")
            print_menu()
            print(f"Bill to date: ${bill}")
            answer = input(">>> ").lower()

        if answer == "c":
            print("Taxis Available: ")
            for index, taxi in enumerate(taxis):
                print(f"{index} - {taxi}")
                final_index = index

            current_taxi = int(input("Choose Taxi: "))
            if current_taxi > final_index:
                print("Invalid Taxi Choice")
            print(f"Bill to date: ${bill}")
            answer = input(">>> ").lower()

        if answer == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${bill}")
                print_menu()
                answer = input(">>> ").lower()

            else:
                distance = int(input("Drive how far? "))
                taxis[current_taxi].drive(distance)
                trip_cost = taxis[current_taxi].get_fare()
                bill += trip_cost
                print(f"Your {taxis[current_taxi].name} trip cost you ${trip_cost}")
                print(f"Bill to date: ${bill}")
                print_menu()
                answer = input(">>> ").lower()

    print(f"Total trip cost: ${bill}")
    print("Taxis are now:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


main()
