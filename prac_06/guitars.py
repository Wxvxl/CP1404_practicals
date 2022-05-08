from prac_06.guitar import Guitar
print("My guitars!")
guitars = []

name = input("Name: ")
while name != "":
    year = input("Year: ")
    cost = input("$")
    guitars.append(Guitar("name, year, cost"))
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        print(f"Guitar {i + 1}: {guitar.name} ({guitar.year}), worth $ {guitar.cost:,.2f} (vintage)")
    else:
        print(f"Guitar {i+1}: {guitar.name} ({guitar.year}), worth $ {guitar.cost:,.2f}")