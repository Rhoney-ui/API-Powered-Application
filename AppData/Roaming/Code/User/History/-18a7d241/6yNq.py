# DEFAULT PARAMETERS AND SCOPE

# Default Parameters

def check_steps (steps, goal=8000):
    if steps >= goal:
        print (f"{steps} steps - Goal of {goal} hit.")
    else: 
        print (f"{steps} steps - Goal of {goal} missed.")

# Uses the default goal of 8000
check_steps (9200)
check_steps (7500)

# Override the default goal
check_steps (9200, goal=10000)
check_steps (11500, goal=10000)