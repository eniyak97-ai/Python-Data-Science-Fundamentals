# Day 3 - File Handling
# Python & Data Science Fundamentals - Module 1

# Create and write to a file
with open("student.txt", "w") as file:
    file.write("Name: Eniya\n")
    file.write("Course: B.Sc Computer Science with Data Science\n")
    file.write("Year: 2\n")
    file.write("Module: Python & Data Science Fundamentals\n")

print("File created successfully.")

# Read the file
with open("student.txt", "r") as file:
    content = file.read()

print("\n--- File Contents ---")
print(content)

# Append new information
with open("student.txt", "a") as file:
    file.write("Status: Module 1 Completed\n")

print("New information appended successfully.")

# Read updated file
with open("student.txt", "r") as file:
    updated_content = file.read()

print("\n--- Updated File ---")
print(updated_content)
