# lab3.2.4-convert.py
# This program takes in a float amount of dollars and returns that absolute amount in cent
# author: Susan Collins

import math

# get input float. I assume that the input value is a valid number.
input_dollars = float(input ("Please enter an amount: "))

# get absolute value of input 
absolute_dollars = abs(input_dollars)

# get value of the input dollar amount in cent, floored to whole cent. Assuming that the bank is not interested in fractional cents, and wants the cent value as an integer for accuracy.
cent_value = absolute_dollars * 100
whole_cent = math.floor(cent_value)

# print result
print(f"That amount in cent is: {whole_cent}")