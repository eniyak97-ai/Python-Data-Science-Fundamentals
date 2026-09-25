# Day 1 - Python Basics
# Python & Data Science Fundamentals - Module 1

import sys

print("Python Version:", sys.version)

# Variables and data types
name = "Eniya"
age = 19
height = 163.4
student = True

print("\n--- Student Information ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", student)

print("\n--- Data Types ---")
print(type(name))
print(type(age))
print(type(height))
print(type(student))

# Arithmetic operations
a = 20
b = 10

print("\n--- Arithmetic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# User input
user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))

print("Hello,", user_name)
print("Your age is", user_age)
