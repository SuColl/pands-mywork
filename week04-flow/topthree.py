# topthree.py
# This program generates 10 random numbers (0-100), prints them out then prints out the top three.
# author: Susan Collins

# Create an empty list
numbers = []

# append 10 random numbers to the list
import random

while len(numbers) <10:
    numbers.append(random.randint(1,100))

# Sort the list elements and print them
numbers.sort()
print(f"The 10 random numbers are: {numbers}")

# copy the last three numnbers to a new list
top_three = numbers[7:10]
# sort the new top three list in reverse order
top_three.sort( reverse = True )

# print the top three list
print(f"The top three numbers are {top_three}")

