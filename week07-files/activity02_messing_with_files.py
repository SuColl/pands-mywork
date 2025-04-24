#  a program that counts how many times it was run.

# Author: Susan Collins


import os.path

# Filename to hold the persistent count
FILENAME = "count.txt"

file_exists = os.path.isfile(FILENAME)

# Function to read in a number from a file that already exists
def read_number(): 
    with open (FILENAME, "rt") as f:
        # want to return an int
        return(int(f.read()))


# Function to takes in a number and overwrites a file with that number
def write_number(number): 
    with open (FILENAME, "wt") as f:
        f.write(str(number))


# testing the function

# if the file does not yet exist, create it
if not(file_exists):
    write_number(0)

# read in the stored number
count = read_number()
# increment
count += 1
# print to terminal
print (count)
# store in file
write_number(count)
