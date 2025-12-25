students = [{'roll' : 101 , 'name' : "Ameet " , 'branch' : "CSE" , 'marks' : (78, 67, 89)} ,
{'roll' : 102 , 'name' : "Riyaa " , 'branch' : "CSE" , 'marks' : (88, 91, 76)} ,
{'roll' : 103 , 'name' : "Suman " , 'branch' : "ECE" , 'marks' : (92, 81, 74)} ,
{'roll' : 104 , 'name' : "Priya " , 'branch' : "EEE" , 'marks' : (65, 69, 72)} ,
{'roll' : 105 , 'name' : "Kunal " , 'branch' : "CSE" , 'marks' : (91, 73, 84)} ,
{'roll' : 106 , 'name' : "Meera " , 'branch' : "ME" , 'marks' : (58, 82, 55)} ,
{'roll' : 107 , 'name' : "Ameet " , 'branch' : "CSE" , 'marks' : (78, 67, 89)} ,
{'roll' : 108 , 'name' : "Diyaa " , 'branch' : "EEE" , 'marks' : (85, 81, 76)} ,
{'roll' : 109 , 'name' : "Rohan " , 'branch' : "ECE" , 'marks' : (37, 87, 70)} ,
{'roll' : 110 , 'name' : "Sriya " , 'branch' : "EEE" , 'marks' : (65, 66, 72)} ,
{'roll' : 111 , 'name' : "Kusal " , 'branch' : "ME" , 'marks' : (88, 73, 84)} ,
{'roll' : 112 , 'name' : "Manoj " , 'branch' : "ME" , 'marks' : (78, 73, 65)} ,]

# Task 1 — Basic Display 
# Count how many student records are present in the given list by using list functions or basic iteration.
print("Total number of student records:", len(students))
#  Create a list that contains only the names of all students (Hints: extract the name value from each dictionary)
print("List of student names:")
# List comprehension to extract names using key 'name'
Student_names = [x['name'] for x in students]   
print(Student_names)
# Collect all roll numbers from the dataset and store them inside a tuple. Then print the tuple.
roll_num = tuple([x['roll'] for x in students])
print("Tuple of roll numbers:", roll_num)
