from Task1 import students
from Task2 import new_AugmentData
from Task3 import branches
from Task5 import combined_data,new_Ranks

# Task 6 — Dictionary-Based Report
print("\n" + "="*70)
print("TASK 6 — DICTIONARY-BASED REPORT")
print("="*70)

# Find overall topper from updated data
overall_topper_name = new_Ranks[0]['name']

# Find branch-wise toppers from updated data
branch_topper_names = {}
for branch in branches:
    highest_percentage = -1
    topper_name = ""
    for i in range(len(students)):
        if students[i]['branch'] == branch:
            if new_AugmentData[i]['percentage'] > highest_percentage:
                highest_percentage = new_AugmentData[i]['percentage']
                topper_name = students[i]['name']
    branch_topper_names[branch] = topper_name

# Create the report dictionary
report = {
    "total_students": len(students),
    "branches": list(branches),
    "toppers": {
        "overall": overall_topper_name,
        "CSE": branch_topper_names.get("CSE", "N/A"),
        "ECE": branch_topper_names.get("ECE", "N/A"),
        "EEE": branch_topper_names.get("EEE", "N/A"),
        "ME": branch_topper_names.get("ME", "N/A")
    }
}

# Display the report in clean format
print("\n" + "="*70)
print(" "*22 + "COLLEGE REPORT")
print("="*70)
print(f"\nTotal Students: {report['total_students']}")
print(f"Branches: {', '.join(report['branches'])}")
print("\n" + "-"*70)
print(" "*25 + "TOPPERS")
print("-"*70)
print(f"\nOverall Topper: {report['toppers']['overall']}")
print("\nBranch-wise Toppers:")
print(f"  CSE: {report['toppers']['CSE']}")
print(f"  ECE: {report['toppers']['ECE']}")
print(f"  EEE: {report['toppers']['EEE']}")
print(f"  ME:  {report['toppers']['ME']}")
print("\n" + "="*70)
