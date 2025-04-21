# Create a program that puts 10 random numbers into a queue(list), the program should then output all the values in the queue, then take the numbers from the queue one at a time, print it and the current numbers still in the queue. (the command pop(0) takes the first element out of a list)
# author: Susan Collins


import random

listsize = 10
random_list = []
random_range = 100

while len(random_list) < listsize:
    random_list.append(random.randint(1,random_range))

print(f"The queue is: {random_list}")

# Method 01 - use a variable to iterate through the list - the list itself does not change
current = 0

while current < listsize:
    print(f"Currently serving number {random_list[current]}, remaining numbers are {random_list[current+1:]}")
    current += 1
print("The queue is now empty.\n")


# Method 02 - remove the first item from the list each iteration - more accurate to the idea of a queue
while len(random_list)>0:
    print(f"Currently serving number {random_list[0]}, remaining numbers are {random_list[1:]}")
    random_list.pop(0)

print("The queue is now empty.")
