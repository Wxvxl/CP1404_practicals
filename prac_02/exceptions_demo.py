try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# ValueError will occur when numerator and denominator are not number values such as when the user enters a string instead of a number.
# When will a ZeroDivisionError occur?
# Wheen the denominator is entered as a 0 then Zero Division Error occurs.
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes changed code below, This should prevent both ZeroDivisionError AND ValueError.

is_finished = 0 
while is_finished != 1:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Finished.")
        is_finished = 1