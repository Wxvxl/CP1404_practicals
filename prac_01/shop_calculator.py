
def check_user_input(input_text,number_floor):
    user_input = float(input(input_text))
    while user_input <= number_floor:
        print("Invalid Input")
        user_input = float(input(input_text))
    return user_input

def main():
    number_of_items = int(check_user_input("Enter the number of items: ",0,))
    cost_total = 0
    for x in range (number_of_items):
        cost = float(check_user_input("Enter the price of item: ",0))
        cost_total += cost
    if cost_total > 100:
        cost_total = cost_total - (cost_total*10/100)
    print(f"Total price for {number_of_items} items is ${cost_total:.2f}")

main()