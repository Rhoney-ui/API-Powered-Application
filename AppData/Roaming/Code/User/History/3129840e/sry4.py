# EXERCISE 1: WRITE FUNCTIONS

# Write a function called greet that takes a name
# and returns a greeting string

def greet (name):
    return f"Hello {name}. Welcome to the program."

print ()
print ("--- EXERCISE 1: WRITE FUNCTIONS ---")
print (greet ("Rhoney"))

# EXERCISE 2: DEFAULT PARAMETERS
# Write a function called power(base, exp=2)
# that returns base raised to exp

def power (base, exp=2):
    return base ** exp

print ()
print ("--- EXERCISE 2: DEFAULT PARAMETERS ---")
print(power (3))    # 9
print(power(2, 10)) # 1024

# EXERCISE 3: LIST COMPREHENSIONS
# Use a list comprehension to get all even numbers from 1 to 30

print ()
print ("--- EXERCISE 3: LIST COMPREHENSIONS ---")
evens = [n for n in range(1, 31) if n % 2 == 0]
print (evens)

# Now get the squares of those even numbers 

squares = [n**2 for n in evens]
print (squares)