# This program builds on the function created in activity02.py. This program keeps displaying the menu until the user picks q. if the user chooses a then call a function called doAdd(), if the user chooses v then call a function called doView(). These functions are not yet defined. 
# author: Susan Collins

def command_menu ():
    print("MENU: What would you like to do?") 
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")

    menu_choice_valid = False
    
    while menu_choice_valid == False:
        menu_choice = input ("Type one letter (a/v/q):").strip()

        if menu_choice == "a" or menu_choice == "v" or menu_choice == "q":
            menu_choice_valid = True

        else:
            print("Sorry, I didn't understand that choice.\n")

    return(menu_choice)

# to be added later
def do_add():
    print (f"You chose Append.\n") 

# to be added later
def do_view():
    print (f"You chose View.\n")

menu_choice="start_value"

while menu_choice != "q":
    menu_choice = command_menu()

    if menu_choice == "a":
        do_add()

    elif menu_choice == "v":
        do_view()

    else:
        print (f"You chose Quit. Goodbye")