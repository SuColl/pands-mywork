# Write a program that will read in a student’s name, then keeps reading in their modules and grades (until the user enters a blank module name), You can break this up into two parts:
# a. Just read in the module names until the user enters blank,
# b. Then read in the grade as well
# This program can read in multiple students (and their module details).

# Author: Susan Collins


# Create a list to hold multiple students' information. (Another version might use a dict with the students' student numbers as the keys and the students' information as the values)
student_database = []


# Get first student's name, if it is non-blank, continue
student_name = str(input("Please enter student name (blank to finish): "))


while len(student_name)>0: 

    # create data structure to hold this student's info
    student_info = {"name":student_name}

    # create module list within main dict
    student_info.update({"modules":[]})

    # Part 1: get name of each module
    # Get name of first module
    module_name = input("Please enter a module name (blank to finish): ")

    while len(module_name)>0:

        # make a blank dict for this module's info, and add this module's name to it
        module_info = {"module_name":module_name}

        # append this module's info the the module list within main dict
        student_info["modules"].append(module_info)

        # get name of next module
        module_name = input("Please enter a module name (blank to finish): ")


    # Part 2: get grades for each module
    for module in student_info["modules"]:
        module_grade = input(f"Please enter the grade for module {module["module_name"]}: ")

        module.update({"grade":module_grade})

    # Append this student's information to the main list
    student_database.append(student_info)

    # Get next student's name
    student_name = str(input("\nNext student. Please enter student name (blank to finish): "))


##########################################################
# Part 3: print out student info

for student in student_database:
        
    print(f"\nStudent Name: {student['name']}")

    for module in student["modules"]:
        print(f"\t{module["module_name"]}: \t{module["grade"]}")








