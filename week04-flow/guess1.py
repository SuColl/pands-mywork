# guess1.py
# This program prompts the user to guess a number, the program rogram prompts the user to guess the number until the user gets the right one
# author: Susan Collins

#hard-coded answer
answer = 37 

#get first guess
guess = int(input("Please guess the number: "))

while guess != answer:
    print("wrong...")
    guess = int(input("Please guess again: "))

# if the guess is correct, congratulate the player and end the program
print("well guessed! the answer was", guess)


