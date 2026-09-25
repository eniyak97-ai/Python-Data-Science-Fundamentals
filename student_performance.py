# Day 4 - Student Performance Analysis
# Python & Data Science Fundamentals - Module 1

students = [
    {"name": "Anu", "marks": 85},
    {"name": "Priya", "marks": 72},
    {"name": "Divya", "marks": 91},
    {"name": "Meena", "marks": 65},
    {"name": "Kavi", "marks": 78}
]

# Extract marks
marks = [student["marks"] for student in students]

# Average
average = sum(marks) / len(marks)

print("--- Student Performance Analysis ---")
print("Number of Students:", len(students))
print("Average Marks:", round(average, 2))

# Highest mark
highest = max(students, key=lambda x: x["marks"])
print("\nTop Student:", highest["name"])
print("Highest Mark:", highest["marks"])

# Lowest mark
lowest = min(students, key=lambda x: x["marks"])
print("\nLowest Student:", lowest["name"])
print("Lowest Mark:", lowest["marks"])

# Grade calculation
print("\n--- Grades ---")

for student in students:
    marks = student["marks"]

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    print(f"{student['name']} - {marks} - Grade {grade}")

print("\nAnalysis completed successfully.")
