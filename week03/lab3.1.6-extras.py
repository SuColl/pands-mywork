# lab3.1.6-extras.py
# This program answers the extra questions in lab3.1.
# author: Susan Collins

'''
6. Why does this expression cause an error? How can you fix it?
message = 'I have eaten ' + 99 + ' burritos.'
print (message)

Answer: this expression tries to append an integer to a string. Can be fixed by casting the integer as a string.
'''
message = 'I have eaten ' + str(99) + ' burritos.'
print (message)

'''
7. Why is eggs a valid variable name while 100 is invalid?
Answer: Variable names must begin with a letter or the underscore character (but may contain digits.)
'''

'''
8. What three functions can be used to get the integer, floating-point number, or
string version of a value?
'''


int_version = int(2.8)
print(f"Variable int_version is of type:{type(int_version)} and is of value:{int_version}")

float_version = float(300)
print(f"Variable float_version is of type:{type(float_version)} and is of value:{float_version}")

string_version = str(29)
print(f"Variable str_version is of type:{type(string_version)} and is of value:{string_version}")


