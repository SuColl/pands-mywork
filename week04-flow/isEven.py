# isEven.py
# This program asks the user to enter in a number, and the program will tell the user if the number is even or odd.
# author: Susan Collins

# get input integer
number = input("Enter an integer: ")

# check input is an integer, if not, request new input
while not number.isdigit():
    print("That's not an integer.")
    number = input("Please enter an INTEGER: ")

# Even if the input is an integer, the input function will have recorded it as a string; so, cast it to an int for working.
number = int(number)

# check whether number is odd or even and print result
if (number % 2) == 0:
    print (f"{number} is an even number")

else:
    print(f"{number} is an odd number")