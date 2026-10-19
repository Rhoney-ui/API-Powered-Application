# WEEK 4 ASSIGNMENTS: FILES, JSON, and CSV

# EXERCISE 1: FILE WRITING
# Write a program that saves your name and city to a text file
# then reads it back and prints it

print()
print("--- EXERCISE 1 ---")
print()
import tempfile, os
path = tempfile.mktemp(suffix='.txt')
with open(path, 'w') as f:
    f.write("Name: Rhoney\nCity: Manama\n") 
with open(path) as f:
    print(f.read())

# EXERCISE 2: ERROR HANDLING
# Wrap a division operation in try/except
# Handle ZeroDivisionError and ValueError separately

print()
print("--- EXERCISE 2 ---")
print()
def safe_divide(a, b):
    try:
        return a / b 
    except ZeroDivisionError: 
        return "Cannot divide by zero"
    except ValueError as e:
        return f"Invalid input: {e}"

print(safe_divide(10, 2))
print(safe_divide(10, 2))

# EXERCISE 3: JSON

import json
# Create a python dictionary and convert it to JSON
# Then parse it back and access a value
data = {"name": "Rhoney", "age": 28, "city": "Manama"}
json_str = json.dumps(data,indent=2)
print(json_str)
parsed = json.loads(json_str)
print(f"Name: {parsed['name']}")