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