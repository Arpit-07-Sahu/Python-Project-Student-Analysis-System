# Task 3 — Branch Analysis Using Sets
from Task1 import students

# Task 3 — Branch Analysis Using Sets
print("\n" + "="*70)
print("TASK 3 — BRANCH ANALYSIS USING SETS")
print("="*70)

# Create a set of all unique branches. (Hints: Extract branch values and store them in a set so that duplicates get removed.)
branches = set(students[i]['branch'] for i in range(len(students)))
print("\nUnique branches in the dataset:", branches)

# For each unique branch, count how many students belong to that branch.
for branch in branches:
    count = 0
    for i in range(len(students)):
        if students[i]['branch'] == branch:
            count += 1
    print(f"Number of students in branch {branch}: {count}")

# Display branch-wise student data using a dictionary of sets. Display a dictionary where:
# • Key = branch name
# • Value = set of roll numbers belonging to that branch
branch_wise = {}
for branch in branches:
    roll_num = {students[i]['roll'] for i in range(len(students)) if students[i]['branch'] == branch}
    branch_wise[branch] = roll_num        
print("\nBranch-wise data:", branch_wise)
