# average.py
# This program reads numbers until the user enters a 0, appending each of number into a list. The program then prints out each of the numbers entered and the average of them.
# author: Susan Collins


# Create an empty list
numbers = []

# Get input from the user
input_number = int(input("Please enter a number (0 to finish): "))

while input_number != 0:
    # Append each input nunber to the list
    numbers.append(input_number)

    # Get another input number
    input_number = int(input("Please enter a number (0 to finish): "))


# create variables to sum and count the list elements
sum_numbers = 0
count_numbers = len(numbers)

# print out the 
for number in numbers:
    # print out each number
    print(number)
       
    # add each number to the sum
    sum_numbers += number


# calcualate the average of the numbers and print it out
average_numbers = sum_numbers / count_numbers
print(f"The average of these {count_numbers} numbers is {average_numbers:.2f}")

