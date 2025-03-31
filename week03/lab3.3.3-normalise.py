# lab3.3.2-simple_string.py
# This program reads in a string and strips any leading or trailing spaces, then converts the string to lower case. The program also outputs the length of the input and output strings.
# author: Susan Collins

# get input string
input_string = str(input("Please enter a string: "))

# strip leading and trailing spaces, and convert to lower case, in one statement.
output_string = input_string.strip().lower()

# get string lengths
length_input_string = len(input_string)
length_output_string = len(output_string)

# print results
print(f"That string normalised is '{output_string}'.")
print(f"We reduced the input string from {length_input_string} to {length_output_string} characters.")
