from prac_06.guitar import Guitar

Gibson = Guitar("Gibson L-5", 1922, 16035.4)
GuitarAlt = Guitar("Another Guitar", 2013, 350)

print(f"Gibson L-5 CES get_age() - Expected 100. got {Gibson.get_age()}")
print(f"Another Guitar get_age() - Expected 9. got {GuitarAlt.get_age()}")

print(f"Gibson L-5 CES is_vintage() - Expected True. got {Gibson.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. got {GuitarAlt.is_vintage()}")