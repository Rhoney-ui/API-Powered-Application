# Defining and Calling a Function

def show_daily_goal (): 
    print ("Step goal: 8,000 steps")
    print ("Water goal: 8 glasses")
    print ("Cold shower: yes")

# Call the function
show_daily_goal ()
print ("---")
show_daily_goal () # Call it again

# Parameters: Passing Information In

print()
print ("=== PARAMETERS ===")
def check_steps (steps):
    if steps >= 10000:
        print (steps, "steps - Goal exceeded")
    elif steps >= 8000:
        print (steps, "steps - Goal hit")
    else:
        print (steps, "steps - Below goal")

# Call with different values
check_steps (9200)
check_steps (7500)
check_steps (11000)

# Several Parameters

print ()
print ("=== SEVERAL PARAMETERS ===")
def log_day (day, steps, protocol):
    print (f"{day}: {steps} steps | Protocol: {protocol}")

log_day ("Monday", 9200, "OMAD")
log_day ("Tuesday", 10500, "2MAD")
log_day ("Wednesday", 8800, "Autophagy Marathon")

# RETURN: Getting a Value Back

print ()
print ("=== RETURN: Getting a Value Back ===")
def calculate_average_steps (steps_list):
    total = sum (steps_list)
    average = total / len (steps_list)
    return average 

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
avg = calculate_average_steps (weekly_steps)
print ("Average steps this week:", avg)

def check_steps (steps):
    if steps >= 10000:
        print (steps, "steps - Goal exceeded")
    elif steps >= 8000:
        print (steps, "steps - Goal hit")
    else:
        print (steps, "steps - Below goal")

# Call with different values
check_steps (10000)
check_steps (8000)
check_steps (10000)