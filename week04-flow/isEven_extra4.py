# isEven_extra4.py
# This program asks the user to enter in a number, and the program will tell the user if the number is even or odd. The program keeps prompting the user for a number until the user enters -1.
# author: Susan Collins

# give an initial value for the variable that will mirror the input number
loop_flag = 1

# create loop to run until the input number is -1
while (loop_flag != -1):

    # get input integer
    number = input("\nEnter an integer: ")

    # check input is an integer, if not, request new input

    if len(number) == 0:        # if input string is empty
        print(f"That's not an integer, you entered nothing.")

    # if input string is not a positive or negative integer
    elif not (number.isdigit() or (number[0]=="-" and number[1:].isdigit())):    
        print(f"That's not an integer, it is {type(number)}")

    else:
        # Even if the input is an integer, the input function will have recorded it as a string; so, cast it to an int for working. The program has no further use for this value so I change the original variable
        number = int(number)

        # check whether number is odd or even and print result
        if (number % 2) == 0:
            print (f"{number} is an even number")

        else:
            print(f"{number} is an odd number")

        # set value of the loop flag to see if the program continues
        loop_flag = number

print("That's my signal to finish. Goodbye")