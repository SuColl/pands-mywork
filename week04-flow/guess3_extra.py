# guess3_extra.py
# This program prompts the user to guess a random number, the program prompts the user to guess the number until the user gets the right one. The program tells the user if their guess is too high or too low.
# author: Susan Collins

# generate an answer that is a random integer between 1 and 100.
import random
answer = random.randint(1,100) 

#get first guess
guess = int(input("Please guess the number: "))
# start counting guesses
num_guesses = 1

# if the guess is wrong, give feedback and ask for another guess, increment the guess counter
while guess != answer:
    if guess < answer:
        print("Your guess was too low")
    else:
        print("Your guess was too high")

    guess = int(input("Please guess again: "))
    num_guesses += 1

# if the guess is correct, congratulate the player and end the program
print("well guessed! the answer was", guess)
print(f"You used {num_guesses} guesses.")


