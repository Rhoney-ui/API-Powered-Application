# LIST OPERATIONS
# Create a list of 5 fruits
# Sort it, reverse it, then add one more item

print ()
print ("=== LIST OPERATIONS ASSIGNMENT ===")
print ()
fruits = ["mango", "banana", "apple", "orange", "grape"]
fruits.sort ()
print (fruits) 
fruits.reverse ()
print (fruits)
fruits.append ("pawpaw")
print (fruits)

# EXERCISE 2: DICTIONARY WORK
# Create a dictionary for a student with name, age, and grade
# Print each value using the key 

print ()
print ("=== DICTIONARY WORK ASSIGNMENT ===")
print ()
student = {"name": "Eric", "age": 25, "grade": "A"}
for key, value in student.items (): 
    print (f" {key}: {value}")

# EXERCISE 3: NESTED DATA
# Create a list of 3 student dictionaries
# Loop through and print each student's name and grade

print ()
print ("=== NESTED DATA ASSIGNMENT ===")
print ()
students = [
    {"name": "Eric", "grade": "A"}, 
    {"name": "James", "grade": "B"},
    {"name": "Amina", "grade": "A"}]
for s in students:
    print (f" {s['name']}: {s['grade']}")

# EXERCISE 4: CHALLENGE
# Build a simple phonebook
# Store 3 contacts as a dictionary of name: number
# Print a formatted contact list

phonebook = {"Eric": "0712345678", "James": "0798765432", "Amina": "0756123456"}
print ("--- Contacts ---")
for name, number in phonebook.items ():
    print (f"{name}: {number}")