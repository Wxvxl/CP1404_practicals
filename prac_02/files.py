# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
out_file = open("name.txt", "w")
name = input("What is your name?: ")
print(name, file=out_file)
out_file.close()

# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
read_file = open("name.txt", "r")
read_name = read_file.readline()
print(f"Your name is {read_name} ")

# Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.
read_file = open("numbers.txt","r")
number_sum = 0
for x in range(0,2):
    number_sum += int(read_file.readline())
print(number_sum)
read_file.close()

# Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.

read_file = open("numbers.txt", "r")
number_sum = 0
for lines in read_file:
    number_sum += int(lines)
print (number_sum)