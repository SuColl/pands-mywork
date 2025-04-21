# Write a program that will read in a student’s name, then keeps reading in their modules and grades (until the user enters a blank module name), You can break this up into two parts:
# a. Just read in the module names until the user enters blank,
# b. Then read in the grade as well
# This program can just read in one student (and their module details).

# Author: Susan Collins


# Get student name and create data structure to hold this student's info
student_name = str(input("Please enter student name: "))
student_info = {"name":student_name}

# create module list within main dict
student_info.update({"modules":[]})

# ©et name of first module
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


# Part 3: print out student info
print(f"\nStudent Name: {student_info['name']}")

for module in student_info["modules"]:
    print(f"\t{module["module_name"]}: \t{module["grade"]}")




