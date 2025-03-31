# lab3.1.5-randomFruit.py
# This program prints out a random fruit.
# author: Susan Collins

import random

fruits = ["strawberry","kiwi","apricot","pomegranate","lime"]

# select random number between 0 and length-1
index = random.randint(0,len(fruits)-1)

print(f"A Random Fruit: {fruits[index]}")