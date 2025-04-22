# program that defines and tests a function to read in student data and add it to a list
# author: Susan Collins

# empty list to store student info
students_added = []

# function to be defined later
def get_modules():
    return[]        # will return a list of modules

# main function
def do_add(student_list):
    student_name = str(input("Please enter student name: "))

    # create dict to hold this student's info
    student_info = {"name":student_name}

    # add student module information to this dict
    student_info["modules"] = get_modules()

    # add student info dict to list of all students to be added
    student_list.append(student_info)


# test the main function
print(f"students added: {students_added}")
do_add(students_added)
print(f"students added: {students_added}")
