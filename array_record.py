# {"name":"sdfas", "mark1" = 60, ....}  json
# Going to store one record in json/dic object
# array object
#from student import *
#students = []  # mutiple records list object
#student = {}  # single entity dic
#from student import *
# 
'''for loop in range(2): # execute this loop for 2 time
    # reading student information dic Key/Value pair
    student = {} # new object every time
    student["name"] = input("Name ")
    student["mark1"] = int(input("Mark1 "))
    student["mark2"] = int(input("Mark2 "))
    student["mark3"] = int(input("Mark3 "))
    student["mark4"] = int(input("Mark4 "))
    student["mark5"] = int(input("Mark5 "))

    students.append(student) # adding into list
'''

#print("All student from List ", students) # all the object of student
students = [
    {"name": "Ram","mark1": 90, "mark2": 89, "mark3": 90, "mark4": 67, "mark5": 50},
    {"name": "Raj","mark1": 70, "mark2": 89, "mark3": 50, "mark4": 40, "mark5": 50},
    {"name": "K7","mark1": 50, "mark2": 89, "mark3": 60, "mark4": 67, "mark5": 50},
    {"name": "Murali","mark1": 80, "mark2": 79, "mark3": 80, "mark4": 67, "mark5": 50},
    ]

for student in students: # Students is list object, 
    #print("One Studenta from List ", student) # display only one student
    #print(student["name"], student["mark1"], student["mark2"], 
    #      student["mark3"], student["mark4"], student["mark5"])
    mark1G = student["mark1"]/10
    mark2G = student["mark2"]/10
    mark3G = student["mark3"]/10
    mark4G = student["mark4"]/10
    mark5G = student["mark5"]/10
    if(mark1G >= 5 and mark2G >= 5 and mark3G >= 5 and
        mark4G >= 5 and mark5G >= 5):
        print(student["name"], " Pass")  # this scenrio
    else:
        print(student["name"], " Fail")  # happy pathR

#print(students)