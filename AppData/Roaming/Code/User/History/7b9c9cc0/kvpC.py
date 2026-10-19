# ERROR HANDLING: TRY AND EXCEPT

# An unhandled error
# See the error

# This will crash

# TRY AND EXCEPT



# RAISING YOUR OWN ERRORS

print()
print("--- RAISING YOUR OWN ERRORS ---")
print ()

def log_steps(steps):
    if not isinstance(steps, int):
        raise
    TypeError("Steps must be an integer.")
    if steps < 0:
        raise
    ValueError("Steps cannot be negative.")
        print(f"Steps logged: {steps}")

try:
    log_steps(9200)
    log_steps(-500)
except ValueError as e:
    print("ValueError:", e)
except TypeError as e:
    print("TypeError:", e)
