# addOne.py
# This program asks for a number and then prints out that number plus 1.
# author: Susan Collins

number = int(input('please enter a number:')) 
newNumber = number + 1

# version 1
print (f'{number} plus one is {newNumber}')

# version 2  - increment in the print statement, without intermediate variable.
print (f'{number} plus one is {number+1}')