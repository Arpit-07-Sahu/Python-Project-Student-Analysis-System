from Task1 import students
from Task2 import new_AugmentData
from Task3 import branches

# Task 4 — Toppers & Ranking
print("\n" + "="*70)
print("TASK 4 — TOPPERS & RANKING")
print("="*70)

# Identify overall topper of the institute. (Hints: Find the student with the highest percentage.)
Highest_index = 0
for i in range(1, len(new_AugmentData)):
    if new_AugmentData[i]['percentage'] > new_AugmentData[Highest_index]['percentage']:
        Highest_index = i
print(f"\nOverall Topper: {students[Highest_index]['name']} with Percentage: {new_AugmentData[Highest_index]['percentage']:.2f}%")

# Identify branch-wise topper of the institute. (Hints: For each branch (CSE, ECE, EEE, ME), find the student who has the highest percentage in that branch.)
highest_per_branch = {}
for branch in branches:
    highest_index = 0
    for i in range(len(students)):
        if students[i]['branch'] == branch:
            if highest_index == 0 or new_AugmentData[i]['percentage'] > new_AugmentData[highest_index]['percentage']:
                highest_index = i
    highest_per_branch[branch] = (students[highest_index]['name'], new_AugmentData[highest_index]['percentage'])
print("\nBranch-wise toppers:", highest_per_branch)

# Create a manually sorted list (bubble/selection sort) of names of the top 10 students of the institute by
# percentage in descending order. (N.B.: Do not use any built-in sort function.
sorted_students = students.copy() # done bcz we dont want to modify the original list
sorted_augmented = new_AugmentData.copy() # Also copy the augmented data
for i in range(len(sorted_students)):
    for j in range(0, len(sorted_students)-i-1):
        if sorted_augmented[j]['percentage'] < sorted_augmented[j+1]['percentage']:
            # this is used to swap the student names based on percentage
            sorted_students[j], sorted_students[j+1] = sorted_students[j+1], sorted_students[j]
            # this is imp because we are sorting based on percentage in descending order
            sorted_augmented[j], sorted_augmented[j+1] = sorted_augmented[j+1], sorted_augmented[j]
top_10_students = sorted_students[:10] # getting top 10 students data to a new list
print("\nTop 10 students by percentage:")
for i in range(len(top_10_students)):
    print(f"{i+1}. {top_10_students[i]['name']} - {sorted_augmented[i]['percentage']:.2f}%")

# Take roll number as input and display complete student details. If the roll number doesn't exist, print "Not Found".
Roll = int(input("\nEnter roll number to get details: "))
for i in range(len(students)):
    if students[i]['roll'] == Roll:
        print(f"\nDetails of Roll Number {Roll} --> ")
        print(f"Name: {students[i]['name']}")
        print(f"Branch: {students[i]['branch']}")
        print(f"Marks: {students[i]['marks']}")
        print(f"Total Marks: {new_AugmentData[i]['total_marks']}")
        print(f"Percentage: {new_AugmentData[i]['percentage']:.2f}%")
        print(f"Grade: {new_AugmentData[i]['grade']}")
        break
else:
    print("No Details Found")
