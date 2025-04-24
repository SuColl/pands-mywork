#  a program that stores / reads a simple dict to /from a file as JSON

# Author: Susan Collins


import json

mydict = {"tree":"aspen","fish":"trout","stone":"basalt"}
# mydict = dict(tree = 'pine', fish = 'carp', stone = ['pumice', 'granite'])


FILENAME = "storage.json"

# function to store dict to file
def store_dict (some_dict):
    with open (FILENAME, "wt") as f:
        json.dump(some_dict, f)

# function to read dict from file
def read_dict ():
    with open (FILENAME, "rt") as f:
        return json.load(f)
    
    

# testing
store_dict(mydict)

dict_out = read_dict()

print (dict_out)