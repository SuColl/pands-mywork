# grade_extra3.py
# This program reads in a student’s percentage mark and prints out corresponding the grade. The program checks that the percentage is valid. This program rounds grades - ie 69.5 gets rounded to 70 so is equal to a Distinction.
# author: Susan Collins


grade = float(input("Enter grade percentage (0-100): "))


# Method 1 - change the selection limits to account for the rounding
if grade > 100 or grade < 0:
    print("Invalid grade percentage.")
elif grade < 39.5:
    print("Fail")
elif grade < 49.5:
    print("Pass")
elif grade < 59.5:
    print("Merit 2")
elif grade < 69.5:
    print("Merit 1")
else:
    print("Distinction")


# Method 2 - round the grade to the nearest integer, then compare it to the original grade bands.
rounded_grade = round(grade)

if rounded_grade > 100 or grade < 0:
    print("Invalid grade percentage.")
elif rounded_grade < 40:
    print("Fail")
elif rounded_grade < 50:
    print("Pass")
elif rounded_grade < 60:
    print("Merit 2")
elif rounded_grade < 70:
    print("Merit 1")
else:
    print("Distinction")

    