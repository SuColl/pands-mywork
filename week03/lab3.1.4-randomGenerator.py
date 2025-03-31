# lab3.1.4-randomGenerator.py
# This program prints out a random number between limits input by the user.
# author: Susan Collins

import random

print("This program will return a random integer between an upper and lower limit supplied by the user.")

# Get user-supplied limits
lower=int(input("Enter lower limit (integer): "))
upper=int(input("Enter upper limit (integer): "))

# Calculate the random numbr between the limits
number = random.randint(lower,upper)

# Print output
print(f"here is the random integer: {number}")
