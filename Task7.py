from Task1 import students
from Task2 import new_AugmentData
from Task3 import branches


# Task 7 — Display the below Structures
print("\n" + "="*70)
print("TASK 7 — DISPLAY REQUIRED STRUCTURES")
print("="*70)

# Create the following Python data structures from the processed dataset:
# 1. List of tuples → (roll, name, total, percentage)
list_of_tuples = [(students[i]['roll'], students[i]['name'], 
                   new_AugmentData[i]['total_marks'], new_AugmentData[i]['percentage']) 
                   for i in range(len(students))]
print("\n1. List of tuples (roll, name, total, percentage):")
for tup in list_of_tuples:
    print(f"   {tup}")

# 2. Create a dictionary mapping roll numbers to percentage. Dictionary → { roll : percentage } Example: {101: 78.2, 102: 85.6, ...}
roll_to_percentage = {students[i]['roll']: new_AugmentData[i]['percentage'] for i in range(len(students))}
print("\n2. Dictionary {roll: percentage}:")
print(f"   {roll_to_percentage}")

# 3. Set of all students scoring ≥ 75%. Add the names (or roll numbers) of students who have percentage >= 75.
students_above_75 = set(students[i]['name'] for i in range(len(students)) if new_AugmentData[i]['percentage'] >= 75)
print("\n3. Set of students scoring >= 75%:")
print(f"   {students_above_75}")

print("\n" + "="*70)
print(" "*15 + "ANALYSIS COMPLETED SUCCESSFULLY!")
print("="*70)
