# EXERCISE 1: WRITE FUNCTIONS

# Write a function called greet that takes a name
# and returns a greeting string

def greet (name):
    return f"Hello {name}. Welcome to the program."

print ()
print ("--- EXERCISE 1 ---")
print (greet ("Rhoney"))

# EXERCISE 2: DEFAULT PARAMETERS
# Write a function called power(base, exp=2)
# that returns base raised to exp

def power (base, exp=2):
    return base ** exp

print ()
print ("--- EXERCISE 2 ---")
print(power (3))    # 9
print(power(2, 10)) # 1024