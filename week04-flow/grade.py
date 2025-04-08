# grade.py
# This program reads in a student’s percentage mark and prints out corresponding the grade. The program checks that the percentage is valid.
# author: Susan Collins


grade = float(input("Enter grade percentage (0-100): "))

if grade > 100 or grade < 0:
    print("Invalid grade percentage.")
elif grade < 40:
    print("Fail")
elif grade < 50:
    print("Pass")
elif grade < 60:
    print("Merit 2")
elif grade < 70:
    print("Merit 1")
else:
    print("Distinction")

