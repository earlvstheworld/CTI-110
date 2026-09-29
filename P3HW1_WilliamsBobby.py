# Bobby Williams
# 09/29/2026    
# P3HW1
# Branching to determine letter grade based on the average

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

# Create a list to hold the test grade
module_test_grade = [grade1, grade2, grade3, grade4, grade5, grade6]

total_grade = sum(module_test_grade)

average = sum(module_test_grade) / len(module_test_grade)

print("------------Results------------")
print(f"Lowest Grade: {min(grade1, grade2, grade3, grade4, grade5, grade6)}")
print(f"Highest Grade: {max(grade1, grade2, grade3, grade4, grade5, grade6)}")
print(f"Sum of Grades: {sum([grade1, grade2, grade3, grade4, grade5, grade6])}")
print(f"Average: {sum([average]):.2f}")
print("--------------------------------")

# Branching to determine letter grade based on the average
if average >=90: 
    grade_report = "A"
elif average >=80:
    grade_report = "B"
elif average >=70:
    grade_report = "C"
elif average >=60:
    grade_report = "D"
else:
    grade_report = "F"
    
print()
print(f"Your average is {average:.2f}, so your letter grade {grade_report}")