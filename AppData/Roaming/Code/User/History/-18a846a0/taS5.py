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

def log_day (day, steps, protocol):
    print (f"{day}: {steps} steps | Protocol: {protocol}")

log_day ("Monday", 9200, "OMAD")
log_day ("Tuesday", 10500, "2MAD")
log_day ("Wednesday", 8800, "Autophagy Marathon")