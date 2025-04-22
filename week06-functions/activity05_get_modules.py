# developing get_modules() function that reads in student module data and adds it to a list. Most of this function's code was developed in lab week05.
# author: Susan Collins


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



# test the above function
module_list = get_modules()
print(f"Module List: {module_list}")
