# guess2.py
# This program prompts the user to guess a number, the program rogram prompts the user to guess the number until the user gets the right one. The program tells the user if their guess is too high or too low.
# author: Susan Collins

#hard-coded answer
answer = 37

#get first guess
guess = int(input("Please guess the number: "))

# if the guess is wrong, give feedback and ask for another guess
while guess != answer:
    if guess < answer:
        print("Your guess was too low")
    else:
        print("Your guess was too high")

    guess = int(input("Please guess again: "))

# if the guess is correct, congratulate the player and end the program
print("well guessed! the answer was", guess)


