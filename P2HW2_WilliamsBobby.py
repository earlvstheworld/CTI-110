# Bobby Williams
# 09/25/2026    
# P2HW2
# Create a grading scale for Modules

print("Enter grade for Module 1:")
grade1 = float(input())
print("Enter grade for Module 2:")
grade2 = float(input())
print("Enter grade for Module 3:")
grade3 = float(input())
print("Enter grade for Module 4:")
grade4 = float(input())
print("Enter grade for Module 5:")
grade5 = float(input())
print("Enter grade for Module 6:")
grade6 = float(input())

print("------------Results------------")
print(f"Lowest Grade: {min(grade1, grade2, grade3, grade4, grade5, grade6)}")
print(f"Highest Grade: {max(grade1, grade2, grade3, grade4, grade5, grade6)}")
print(f"Sum of Grades: {sum([grade1, grade2, grade3, grade4, grade5, grade6])}")
print(f"Average: {sum([grade1, grade2, grade3, grade4, grade5, grade6]) / 6:.2f}")
print("--------------------------------")