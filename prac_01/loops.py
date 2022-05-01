for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for x in range(0, 101, 10):
    print(x, end=' ')
print()

#b
for z in range(20, 0, -1):
    print(z, end=' ')
print()

#c
number_of_stars = int(input("Enter the number of stars: "))
for x in range(1, number_of_stars+1):
    print("*", end="")

#d
number_of_increasing_stars = int(input("Enter the number of stars: "))
for z in range(1,number_of_increasing_stars+1):
    for b in range(z):
        print("*", end="")
    print()

