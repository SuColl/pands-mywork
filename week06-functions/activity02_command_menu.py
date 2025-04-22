# a function that prints out a menu of commands we can perform, ie add, view and quit. The function should return what the user chose.

# author: Susan Collins

def command_menu ():
    print("What would you like to do?") 
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

# Testing the above function
menu_choice = command_menu()
print (f"You chose {menu_choice}")