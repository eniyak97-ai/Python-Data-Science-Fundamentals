# Day 2 - Lists, Dictionaries, Loops and Functions
# Python & Data Science Fundamentals - Module 1

# List
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("--- List ---")
print("Fruits:", fruits)
print("First fruit:", fruits[0])

fruits.append("Grapes")
print("Updated list:", fruits)

# Dictionary
student = {
    "name": "Eniya",
    "age": 19,
    "course": "B.Sc Computer Science with Data Science",
    "year": 2
}

print("\n--- Dictionary ---")
print(student)
print("Name:", student["name"])
print("Course:", student["course"])

# For loop
print("\n--- For Loop ---")
for i in range(1, 11):
    print(i)

# While loop
print("\n--- While Loop ---")
i = 1
while i <= 5:
    print(i)
    i += 1

# Function
def calculate_sum(a, b):
    return a + b

print("\n--- Function ---")
result = calculate_sum(25, 15)
print("Sum:", result)

# Even or odd
number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
