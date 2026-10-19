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