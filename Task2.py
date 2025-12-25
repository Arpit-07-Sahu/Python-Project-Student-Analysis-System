
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

# Task 2: Augment Dataset Using Grades
print("\n" + "="*70)
print("TASK 2 — AUGMENT DATASET USING GRADES")
print("="*70)

new_AugmentData = []  # Copying the original list to avoid modifying it directly
# For each student, calculate total and percentage using list/tuple only.
for str in students:
    total_marks = sum(str['marks'])  # Sum of marks from the tuple
    percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100
    
    # Augment the input data set by including an additional item (feature), Grade, for each student using their percentage
    match percentage:
        case percentage if percentage >= 90:
            grade = 'O'
        case percentage if percentage >= 80:
            grade = 'A'
        case percentage if percentage >= 70:
            grade = 'B'
        case percentage if percentage >= 60:
            grade = 'C'
        case percentage if percentage >= 50:
            grade = 'P'
        case _:
            grade = 'F'
    new_AugmentData.append({'total_marks': total_marks, 'percentage': percentage, 'grade': grade})
    print(f"Total Marks: {total_marks} of {str['name']}, Percentage: {percentage:.2f}%, Grade: {grade}")

# Given a roll number as input, write code to display that student's grade
roll_input = int(input("\nEnter the roll number: "))
for i in range(len(new_AugmentData)):
    if students[i]['roll'] == roll_input:
        print(f"Student Roll Number: {roll_input}, Grade: {new_AugmentData[i]['grade']}")
        break
else:
    print("Roll number not found.")

# Print all the students having a particular grade, inputted by user. (Hints: Ask the user for a grade
# (O/A/B/C/P/F) and print all students matching that grade.)
input_grade = input("\nEnter the grade to filter students (O/A/B/C/P/F): ").upper()
found = False
for i in range(len(new_AugmentData)):
    if new_AugmentData[i]['grade'] == input_grade:
        print(f"Student Name: {students[i]['name']}")
        found = True
if not found:
    print("No students with the specified grade.")