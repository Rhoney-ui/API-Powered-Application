# EXERCISE 1: VARIABLES AND TYPES.

name = "Rhoney"
age = 28
city = "Manama"

print ("=== INTRODUCTION ===")
print (f"My name is {name}, I am {age} years old, from {city}.")

# EXERCISE 2: CONDITIONALS
# Write a program that takes a score and prints a grade
# 90+ = A, 75+ = B, 60+ = C, below 60 = F
score = 78

print ("=== EXERCISE 2 ===")
if score >= 90:
    print ("Grade: A")
elif score >= 75:
    print ("Grade: B")

# EXERCISE 3: LOOPS
# Print the first 10 even numbers using a loop

print ("=== EXERCISE 3 ===")
for i in range (1,21): 
    if i % 2 == 0:
        print (i)