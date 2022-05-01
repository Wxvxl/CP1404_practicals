import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# a random number between 5 - 20. Smallest possible is 5 and the largest possible is 20

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
#a random number between 3, 10  Could line 2 have produced a 4? Smallestnumber would 3 and the highest is 9. and line 2 cannot produce a 4 since it's on interval of 2 between 3 - 10 so 4 is not part of the possible numbers.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# A random float number between 2.5 and 5.5. Smallest number is 5.5 and the largest is 5.5 On line 3 

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))