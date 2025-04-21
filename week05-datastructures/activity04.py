# a program that stores a student name and a list of her courses and grades in a dict, the program should then print out her data. The number of courses she has could change.
# author: Susan Collins

student_info= {"name":"Mary",
               "courses":[
                   {    "course_name":"Programming",
                        "grade":45
                    },
                    {   "course_name":"History",
                        "grade":99
                    }
                 ]
                          
}



print(f"Student Name: {student_info['name']}")

# get number of courses (do not assume 2)
num_courses = len(student_info["courses"])


'''
# iterate through courses and print course name and grade
for course in range(0,num_courses):
    print(f"\t{student_info["courses"][course][course_name]}: \t{student_info["courses"][course]["grade"]}")
'''


# ^^^ do not neet a range! can just iterate through the list of courses
for course in student_info["courses"]:
    print(f"\t{course["course_name"]}: \t{course["grade"]}")



