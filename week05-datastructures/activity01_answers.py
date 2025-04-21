# lists types of different datastructures - checking my answers for lab 05 activity 01
# author: Susan Collins

'''
My answers:
a. numberOfQuestions        <- int
b. averageAge                      <- float
c. debugMode                       <- bool
d. name                                 <- str
e. ages                         <- list, length 0
f. months                     <- tuple, length 3
g. months[1]           <- str
h. book                     <- dict, length 0
i. stuff                     <- list, length 4
j. stuff[2]                     <- bool
k. someone                     <- dict, length 1
l. someone["firstname"]           <- str 
m. me                               <- dict, length 2
n. me["teaching"]           <- list
o. me["teaching"][0]["semester"]           <-  int
p is a trick question look at it carefully 
p. me["teaching"][0]["coursename"]      <- Error
'''


#My answers
answer_a = "int"
answer_b = "float"
answer_c = "bool"
answer_d = "str"
answer_e = "list, length 0"
answer_f = "tuple, length 3"
answer_g = "str"
answer_h = "dict, length 0"
answer_i = "list, length 4"
answer_j = "bool"
answer_k = "dict, length 1"
answer_l = "str"
answer_m = "dict, length 2"
answer_n = "list"
answer_o = "int"
answer_p = "Error"


# Code from question:
numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
    "firstName" : "Andrew",
    "teaching"  : [{
        "courseName" : "programming",
        "semester" : 1
    },{
        "courseName" : "Data Representation",
        "semester" : 2
    }
] }


#Printing answers:
print(f"The data type of numberOfQuestions is {type(numberOfQuestions)}: you answered {answer_a}")
print(f"The data type of averageAge is {type(averageAge)}: you answered {answer_b}")
print(f"The data type of debugMode is {type(debugMode)}: you answered {answer_c}")
print(f"The data type of name is {type(name)}: you answered {answer_d}")
print(f"The data type of ages is {type(ages)}, length {len(ages)}: you answered {answer_e}")
print(f"The data type of months is {type(months)}, length {len(months)}: you answered {answer_f}")
print(f"The data type of months[1] is {type(months[1])}: you answered {answer_g}")
print(f"The data type of book is {type(book)}, length {len(book)}: you answered {answer_h}")
print(f"The data type of stuff is {type(stuff)}, length {len(stuff)}: you answered {answer_i}")
print(f"The data type of stuff[2] is {type(stuff[2])}: you answered {answer_j}")
print(f"The data type of someone is {type(someone)}, length {len(someone)}: you answered {answer_k}")
print(f"The data type of firstname is {type(someone["firstname"])}: you answered {answer_l}")
print(f"The data type of me is {type(me)}, length {len(me)}: you answered {answer_m}")
print(f"The data type of teaching is {type(me["teaching"] )}: you answered {answer_n}")
print(f"The data type of me[\"teaching\"][0][\"semester\"] is {type(me["teaching"][0]["semester"])}: you answered {answer_o}")
print(f"The data type of me[\"teaching\"][0][\"courseware\"] is {type(me["teaching"][0].get("coursename"))}: you answered {answer_p}")
