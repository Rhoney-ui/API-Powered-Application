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

print ()
print ("=== TRIAL WITH A NEW FUNCTION ===")
def get_status (steps):
    if steps >= 10000:
        print (steps, "steps - Goal exceeded")
    elif steps >= 8000:
        print (steps, "steps - Hit")
    else:
        print (steps, "steps - Missed")

# Call with different values
get_status (10000)
get_status (8000)
get_status (7500)

# A Function That Works With Dictionaries

def print_client (client):
    print (f"Name : {client['name']}")
    print (f"Goal : {client['goal']}")
    print (f"Bench : {client['bench_press_kg']}kg")
    print (f"Sessions : {client['weekly_sessions']}per week")
    print ()

clients = [
    {"name": "James", "goal": "fat loss", "bench_press_kg": 80, "weekly_sessions": 4},
    {"name": "Sandra", "goal": "endurance", "bench_press_kg": 50, "weekly_sessions": 3},
    {"name": "Mwangi", "goal": "muscle gain", "bench_press_kg": 100, "weekly_sessions": 5},
]

for client in clients:
    print_client (client)