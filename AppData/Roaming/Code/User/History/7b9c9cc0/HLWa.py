# ERROR HANDLING: TRY AND EXCEPT

# An unhandled error
# See the error

# This will crash

# TRY AND EXCEPT
steps_data = ["9200", "7500", "ten thousand", "8800", "6900"]

for item in steps_data:
    try:
        steps = int(item)
        if steps >= 8000:
            print(steps, "- Goal hit") 
        else: 
            print(steps, "- Below goal")
    except ValueError:
        print(f"'{item}' is not a valid number. Skipping.")

# CATCHING SPECIFIC ERROR TYPES

# TRY IT: MULTIPLE EXCEPT BLOCKS

print ()
print("--- MULTIPLE EXCEPT BLOCKS ---")
print ()
def calculate_average(steps_list):
    try:
        total = sum(steps_list)
        avg = total / len(steps_list)
        return round(avg)
    except ZeroDivisionError: 
        print("Error: List is empty. Cannot calculate average.")
        return 0
    except TypeError:
        print("Error: List contains non-numeric values.")
        return 0

print("Average:", calculate_average([9200, 10500, 8800, 11000]))
print("Average:", calculate_average([]))
print("Average:", calculate_average([9200, "eight thousand", 10500]))

# ELSE AND FINALLY

print ()
print ("--- ELSE AND FINALLY ---")
print ()
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"{a} / {b} = {result}")
    finally:
        print("(Calculation attempted)")
        print()

safe_divide(100, 4)
safe_divide(100, 0)
safe_divide(9200, 7)

# RAISING YOUR OWN ERRORS

print()
print("--- RAISING YOUR OWN ERRORS ---")
print ()

def log_steps(steps):
    if not isinstance(steps, int): 
        raise TypeError("Steps must be an integer.")
    if steps < 0:
        raise ValueError("Steps cannot be negative.")
    print(f"Steps logged: {steps}")  

try:
    log_steps(9200)
    log_steps("nine thousand")
except ValueError as e: 
    print("ValueError:", e)
except TypeError as e: 
    print("TypeError:", e)

# ERROR HANDLING WITH DATA PROCESSING

print()
print ("--- ERROR HANDLING WITH DATA PROCESSING ---")
print ()
daily_logs = [
    {"day": "Monday", "steps": "9200"},
    {"day": "Tuesday", "steps": "not recorded"},
    {"day": "Wednesday", "steps": "10500"},
    {"day": "Thursday", "steps": None},
    {"day": "Friday", "steps": "8800"},
]

valid_steps = []
for log in daily_logs:
    try:
        steps = int(log["steps"])
        
        valid_steps.append(steps) 
    print(f"{log['day']}: {steps} steps") 
    except (ValueError, TypeError):
            print(f"{log['day']}: invalid data - skipped")

if valid_steps:
    avg = sum(valid_steps) / len(valid_steps)
    print(f"\nAverage from valid days: {round(avg)} steps")
