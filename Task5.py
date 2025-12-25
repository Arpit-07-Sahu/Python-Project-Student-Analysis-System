from Task1 import students
from Task2 import new_AugmentData
from Task3 import branches

# Task 5 — Data Correction
print("\n" + "="*70)
print("TASK 5 — DATA CORRECTION")
print("="*70)

# Given a dictionary of roll numbers and their corrected marks for each subject, update the original dataset accordingly.
correction_marks = {104: (70, 75, 80), 106: (92, 97, 97)}

print("\nApplying corrections...")
# ONLY do data correction if the roll number exists in the original dataset.
for roll_no, marks in correction_marks.items():
    for i in range(len(students)):
        if students[i]['roll'] == roll_no:
            old_marks = students[i]['marks']
            students[i]['marks'] = marks
            print(f"Roll {roll_no}: Marks changed from {old_marks} to {marks}")
            
            # After correction, recalculate the total marks, percentage and grades for the affected students.
            # UPDATE the existing new_AgumentData instead of creating new list
            total_marks = sum(students[i]['marks'])
            percentage = (total_marks / 300) * 100
            
            if percentage >= 90:
                grade = 'O'
            elif percentage >= 80:
                grade = 'A'
            elif percentage >= 70:
                grade = 'B'
            elif percentage >= 60:
                grade = 'C'
            elif percentage >= 50:
                grade = 'P'
            else:
                grade = 'F'
            
            # Update the existing new_AgumentData
            new_AugmentData[i]['total_marks'] = total_marks
            new_AugmentData[i]['percentage'] = percentage
            new_AugmentData[i]['grade'] = grade
            
            print(f"Updated - Total: {total_marks}, Percentage: {percentage:.2f}%, Grade: {grade}")

# Check whether the ranking list changes after changes in marks of the students in correction marks dictionary.
print("\n" + "-"*70)
print("UPDATED RANKINGS AFTER DATA CORRECTION")
print("-"*70)

# Create a combined list for sorting
combined_data = []
for i in range(len(students)):
    combined_data.append({
        'roll': students[i]['roll'],
        'name': students[i]['name'],
        'branch': students[i]['branch'],
        'percentage': new_AugmentData[i]['percentage'],
        'total_marks': new_AugmentData[i]['total_marks'],
        'grade': new_AugmentData[i]['grade']
})

# Bubble sort in descending order by percentage
# Use sorted function to sort by percentage in descending order
new_Ranks = sorted(combined_data, key=lambda x: x['percentage'], reverse=True)
# Print updated rankings
print("\nUpdated Top 10 Rankings:")
for i in range(min(10, len(new_Ranks))):
    print(f"{i+1}. {new_Ranks[i]['name']} (Roll: {new_Ranks[i]['roll']}) - {new_Ranks[i]['percentage']:.2f}%")
