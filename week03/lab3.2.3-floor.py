# lab3.2.3-floor.py
# This program takes in a float and outputs the nearest lower integer (i.e rounds down.)
# author: Susan Collins

import math

# get input float
input_float = float(input ("Enter a float number: "))

# get value of input rounded down to nearest integer
input_floored = math.floor(input_float)

# print result
print(f"{input_float} floored is {input_floored}")