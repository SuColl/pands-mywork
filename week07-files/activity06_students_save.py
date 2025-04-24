# This program takes the student records program made in week06 lab, and add JSON file storage functionality to it. 
# author: Susan Collins

import json

def command_menu ():
    print("\nMENU: What would you like to do?") 
    print("\t(a) Add new student info")
    print("\t(v) View student info")
    print("\t(s) Save student info to TXT file")
    print("\t(l) Load student info from TXT file")
    print("\t(q) Quit")

    menu_choice_valid = False
    
    while menu_choice_valid == False:
        menu_choice = input ("Type one letter (a/v/q):").strip()

        if menu_choice == "a" or menu_choice == "v" or menu_choice == "q" or menu_choice == "s" or menu_choice == "l":
            menu_choice_valid = True

        else:
            print("Sorry, I didn't understand that choice.\n")

    return(menu_choice)


# this function recalled from lab week 06 activity 04 - adds student records to memory
def do_add(student_list):
    student_name = str(input("Please enter student name: "))

    # create dict to hold this student's info
    student_info = {"name":student_name}

    # add student module information to this dict
    student_info["modules"] = get_modules()

    # add student info dict to list of all students to be added
    student_list.append(student_info)


# this function recalled from lab week 05 activity 04 - views student records stored in memory
def do_view(list):
    for entry in list:
        print (f"Student Name: {entry["name"]}")
        for module in entry["modules"]:
            print(f"\t{module["module_name"]}: {module["grade"]}")

# function to store dict to file
def store_dict (some_dict):
    with open (FILENAME, "wt") as f:
        json.dump(some_dict, f)

# function to read dict from file
def read_dict ():
    with open (FILENAME, "rt") as f:
        return json.load(f)

# stores student records to text file
def do_save(list):
    store_dict(list)
    print("students saved")

# loads student records from text file
def do_load ():
    print("students loading from file")
    return read_dict ()

# from activity05_get_modules.py
def get_modules():
    # start list to hold module information
    module_list = []

    # Get name of first module
    module_name = input("Please enter the first module name (blank to finish): ")

    while len(module_name)>0:

        # make a dict for this module's info, and add this module's name to it
        module_info = {"module_name":module_name}

        # add this module's grade to the dict
        module_grade = input(f"Please enter the grade for module {module_name}: ")
        module_info["grade"] = module_grade

        # append this module's info the the module list within main dict
        module_list.append(module_info)

        # get name of next module
        module_name = input("Please enter the next module name (blank to finish): ")

    return(module_list)        # will return a list of modules





###### Main Code #######

# empty list to store student info
students_added = []

# txt file to store student records
FILENAME = "storage.json"

menu_choice="start_value"

while menu_choice != "q":
    menu_choice = command_menu()

    if menu_choice == "a":
        do_add(students_added)

    elif menu_choice == "v":
        do_view(students_added)

    elif menu_choice == "s":
        do_save(students_added)

    elif menu_choice == "l":
        students_added = do_load()

    else:
        print (f"You chose Quit. Goodbye")