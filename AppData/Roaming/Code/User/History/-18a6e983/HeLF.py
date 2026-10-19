# LIST COMPREHENSIONS AND LAMBDA

# List Comprehension

# The Problem: Building Lists with Loops

# STANDARD LOOP APPROACH

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = []
for steps in weekly_steps:
    if steps >= 8000:
        goal_days.append(steps)
        
print(goal_days)

# LIST COMPREHENSION APPROACH

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = [steps for steps in weekly_steps if steps >= 8000]

print()
print ("=== LIST COMPREHENSION APPROACH ===")
print(goal_days)

# Breaking Down the Syntax
# Transforming Items

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

print ()
print ("=== TRANSFORMING ITEMS ===")
# Convert each step count to km 
km_walked = [round(s * 1.3 / 1000, 2) for s in weekly_steps]
print("Steps:", weekly_steps)
print ("km :", km_walked)

# Filtering a List of Dictionaries

clients = [
    {"name": "James", "goal": "fat loss", "sessions": 4},
    {"name": "Sandra", "goal": "endurance", "sessions": 3},
    {"name": "Patrick", "goal": "fat loss", "sessions": 4},
    {"name": "Grace", "goal": "fat loss", "sessions": 3}]

print ()
print ("=== FILTERING A LIST OF DICTIONARIES ===")
# Get names of all fat loss clients
fat_loss_names = [c["name"] for c in clients if c["goal"] == "fat loss"]
print ("Fat loss clients:", fat_loss_names)

# Get all clients with 4 or more sessions per week
active_clients = [c for c in clients if c["sessions"] >= 4]
print ("Active clients:", [c["name"] for c in active_clients])
